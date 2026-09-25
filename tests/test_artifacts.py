# SPDX-License-Identifier: MIT
import importlib.util
import json
from pathlib import Path
import shutil
import tempfile
import unittest
from test_policy import ROOT

CHECKER = ROOT / 'skills/health-checkup/scripts/validate.py'
SKILL = ROOT / 'skills/health-checkup'


def checker():
    spec = importlib.util.spec_from_file_location('validator', CHECKER)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class ArtifactTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        (ROOT / '.work').mkdir(exist_ok=True)

    def test_portable_skill_and_missing_dependency_detected(self):
        self.assertTrue(CHECKER.exists(), 'missing artifact checker')
        p = checker()
        self.assertEqual(p.validate_skill(SKILL), [])
        with tempfile.TemporaryDirectory(dir=ROOT / '.work') as temp:
            copy = Path(temp) / 'health-checkup'
            shutil.copytree(SKILL, copy, ignore=shutil.ignore_patterns('__pycache__'))
            self.assertEqual(p.validate_skill(copy), [])
            (copy/'references/okf/health/employment.md').unlink()
            self.assertTrue(p.validate_skill(copy))

    def test_private_schema_rejects_identifiers_and_free_text(self):
        self.assertTrue(CHECKER.exists(), 'missing case validator')
        p = checker()
        case = {'schema_version':'1','purpose':'employment','stage':'booking','next_action':'user_checkpoint'}
        self.assertEqual(p.validate_case(case), [])
        for key in ['name', 'insurance_number', 'medical_results', 'raw_document', 'appointment_date', 'notes']:
            self.assertTrue(p.validate_case({**case, key:'not permitted'}))
        self.assertTrue(p.validate_case({**case,'next_action':'My medical history is ...'}))
        self.assertTrue(p.validate_case({**case,'requirements_reviewed':'true'}))
        self.assertTrue(p.validate_case({'purpose':'employment'}))

    def test_bad_claim_attribution_detected(self):
        self.assertTrue(CHECKER.exists(), 'missing artifact checker')
        p = checker()
        with tempfile.TemporaryDirectory(dir=ROOT / '.work') as temp:
            copy = Path(temp) / 'health-checkup'
            shutil.copytree(SKILL, copy, ignore=shutil.ignore_patterns('__pycache__'))
            claim = copy/'references/okf/health/routes.md'
            claim.write_text(claim.read_text()+'\nUnsupported attributed claim.[^missing]\n')
            self.assertTrue(p.validate_skill(copy))

if __name__ == '__main__':
    unittest.main()
