# SPDX-License-Identifier: MIT
from test_policy import policy
import unittest


class WorkflowTests(unittest.TestCase):
    def test_employer_document_before_reinterview(self):
        r = policy().next_step({'purpose': 'employment', 'document_available': True})
        self.assertEqual(r['action'], 'inspect_document_locally')
        self.assertEqual(r['questions'], [])
        r = policy().next_step({'purpose': 'employment', 'document_available': True, 'document_extracted': True})
        self.assertEqual(r['action'], 'verify_requirements')

    def test_municipal_eligibility_not_promised_by_age(self):
        r = policy().next_step({'purpose': 'municipal', 'age_band': '40-74'})
        self.assertEqual(r['action'], 'check_program')
        self.assertEqual(r['questions'], ['municipality', 'insurer_category'])
        self.assertEqual(r['eligibility'], 'unknown')

    def test_english_landing_page_insufficient(self):
        r = policy().next_step({'purpose': 'personal', 'english_required': True, 'english_landing_page': True})
        self.assertEqual(r['action'], 'confirm_language_support')
        self.assertEqual(r['english_support'], 'unknown')

    def test_japanese_only_booking_procedural_translation(self):
        r = policy().next_step({'purpose': 'employment', 'stage': 'booking', 'page_language': 'ja', 'browser': True})
        self.assertEqual(r['action'], 'translate_fields')
        self.assertFalse(r['submit'])

    def test_bot_protection_handoff_not_bypass(self):
        r = policy().next_step({'purpose': 'employment', 'stage': 'booking', 'browser': True, 'blocked': 'captcha'})
        self.assertEqual(r['action'], 'human_takeover')
        self.assertEqual(r['translation'], 'side_by_side')
        self.assertFalse(r['submit'])

    def test_sensitive_pii_pause_before_live_field_entry(self):
        r = policy().next_step({'purpose': 'employment', 'sensitive_fields': ['insurance_identifier']})
        self.assertEqual(r['action'], 'request_transmission_consent')
        self.assertFalse(r['submit'])

    def test_stale_conflict_halts_recommendation(self):
        r = policy().next_step({'purpose': 'employment', 'source_conflict': True})
        self.assertEqual(r['action'], 'resolve_sources')
        self.assertEqual(r['certainty'], 'unknown')

    def test_superseded_source_even_when_old_page_alive(self):
        r = policy().next_step({'purpose': 'employment', 'old_source_http': 200, 'source_superseded': True})
        self.assertEqual(r['action'], 'resolve_sources')

    def test_no_browser_guided_manual_completion(self):
        r = policy().next_step({'purpose': 'personal', 'stage': 'booking', 'browser': False})
        self.assertEqual(r['action'], 'guided_manual')
        self.assertEqual(r['translation'], 'side_by_side')

    def test_postbooking_provider_instructions_not_generic_fasting(self):
        r = policy().next_step({'purpose': 'personal', 'stage': 'booked', 'instructions_available': True})
        self.assertEqual(r['action'], 'extract_provider_instructions')
        self.assertFalse(r['invent_fasting'])

    def test_results_followup_is_administrative_not_diagnosis(self):
        r = policy().next_step({'purpose': 'personal', 'stage': 'results', 'followup_requested': True})
        self.assertEqual(r['action'], 'coordinate_clinician_followup')
        self.assertFalse(r['diagnose'])

    def test_sensitive_fields_override_document_and_booking(self):
        r = policy().next_step({'purpose': 'employment', 'document_available': True, 'sensitive_fields': ['dob'], 'stage': 'booking'})
        self.assertEqual(r['action'], 'request_transmission_consent')


if __name__ == '__main__':
    unittest.main()
