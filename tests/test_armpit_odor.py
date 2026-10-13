# SPDX-License-Identifier: MIT
"""Synthetic-only decisions and exact consent snapshots; no external actions."""
import copy
import importlib.util
from pathlib import Path
import tempfile
import shutil
import unittest

ROOT = Path(__file__).resolve().parents[1] / 'skills' / 'armpit-odor'

def module(name):
    spec = importlib.util.spec_from_file_location('armpit_odor_' + name, ROOT / 'scripts' / (name + '.py'))
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result

policy = module('decision')
validator = module('validate')

class ProcedureFlow(unittest.TestCase):
    def test_every_use_needs_fresh_evidence(self):
        facts = dict(options_ready=True, choice_complete=True, details_current=True)
        self.assertEqual(policy.next_decision(facts), 'refresh_current_evidence')
        facts['sources_checked_this_run'] = True
        self.assertEqual(policy.next_decision(facts), 'prepare_future_consent_review')
        facts['details_current'] = False
        self.assertEqual(policy.next_decision(facts), 'verify_clinic_details')

    def test_decision_gates(self):
        self.assertEqual(policy.next_decision(dict(sources_checked_this_run=True)), 'research_shortlist')
        self.assertEqual(policy.next_decision(dict(sources_checked_this_run=True, options_ready=True)), 'person_choose')
        self.assertEqual(policy.next_decision(dict(sources_checked_this_run=True, diagnosis_needed=True)), 'diagnostic_consultation')
        self.assertEqual(policy.next_decision(dict(medical_question=True)), 'clinician_consultation')
        self.assertEqual(policy.next_decision(dict(urgent_concern=True)), 'medical_care')
        self.assertEqual(policy.next_decision(dict(private_records_offered=True)), 'minimize_private_data')
        with self.assertRaises(ValueError):
            policy.next_decision({'sources_checked_this_run': 'yes'})

    def test_unusable_communication_stops_booking_readiness(self):
        self.assertEqual(policy.next_decision(dict(
            sources_checked_this_run=True, options_ready=True, choice_complete=True,
            details_current=True, communication_unusable=True)),
            'resolve_communication_before_booking')

    def test_unknown_is_not_zero_or_total(self):
        summary = policy.cost_summary({'base': 100000, 'face': 20000, 'vio': 30000, 'shaving': 5 * 2000, 'anesthesia': None})
        self.assertEqual(summary['known_subtotal_jpy'], 160000)
        self.assertFalse(summary['complete'])
        self.assertEqual(summary['unknown_items'], ['anesthesia'])
        self.assertTrue(policy.cost_summary({'consultation': 3000})['complete'])
        for invalid in (-1, True, 1.5):
            with self.assertRaises(ValueError):
                policy.cost_summary({'base': invalid})

    def test_exact_separate_booking_and_transmission_approval(self):
        action = dict(kind='consultation_booking', destination='https://clinic.invalid/form',
                      branch='Synthetic A', procedure='consultation only', time='2030-01-10T10:00:00+09:00',
                      cost='synthetic JPY 3000', unknowns=[], cancellation='synthetic 24 hours',
                      fields=[{'field': 'contact', 'value': 'SYNTHETIC_PLACEHOLDER'}], purpose='consultation request')
        approval = dict(booking_confirmed=True, transmission_confirmed=True, action=copy.deepcopy(action))
        result = policy.future_handoff_ready(action, approval)
        self.assertEqual(result['status'], 'future_handoff_only')
        self.assertFalse(result['execute'])
        for key in action:
            changed = copy.deepcopy(action)
            changed[key] = [{'field': 'extra', 'value': 'SYNTHETIC'}] if key == 'fields' else ['changed'] if key == 'unknowns' else 'changed'
            self.assertIsNone(policy.future_handoff_ready(changed, approval), key)
        for flag in ('booking_confirmed', 'transmission_confirmed'):
            absent = copy.deepcopy(approval)
            absent[flag] = False
            self.assertIsNone(policy.future_handoff_ready(action, absent))
        action['fields'][0]['value'] = 'CHANGED_SYNTHETIC'
        self.assertNotEqual(result['snapshot']['fields'], action['fields'])
        self.assertIsNone(policy.future_handoff_ready({}, approval))

    def test_duplicate_metadata_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            portable = Path(directory) / 'skill'
            shutil.copytree(ROOT, portable)
            entry = portable / 'SKILL.md'
            original = entry.read_text()
            parts = original.split('---', 2)
            parts[1] += '  compatibility: duplicated value\n'
            entry.write_text('---'.join(parts))
            self.assertIn('SKILL.md: duplicate YAML key: compatibility', validator.validate_skill(portable))
            entry.write_text(original)
            concept = portable / 'references' / 'okf' / 'procedure.md'
            concept.write_text(concept.read_text().replace('"status": "draft",', '"status": "draft", "status": "stable",'))
            self.assertTrue(any('duplicate JSON key: status' in error for error in validator.validate_skill(portable)))
        self.assertEqual(validator.validate_entrypoint_frontmatter('---\nname: test\nmetadata:\n  name: nested\n---\n'), [])

    def test_portable_bundle_and_missing_dependency(self):
        self.assertEqual(validator.validate_skill(ROOT), [])
        with tempfile.TemporaryDirectory() as directory:
            portable = Path(directory) / 'skill'
            shutil.copytree(ROOT, portable)
            self.assertEqual(validator.validate_skill(portable), [])
            (portable / 'references' / 'handoff.md').unlink()
            self.assertTrue(validator.validate_skill(portable))

if __name__ == '__main__':
    unittest.main()
