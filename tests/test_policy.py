# SPDX-License-Identifier: MIT
import importlib.util
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / 'skills/health-checkup/scripts/policy.py'


def policy():
    spec = importlib.util.spec_from_file_location('policy', SCRIPT)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class IntakeTests(unittest.TestCase):
    def test_ambiguous_request_only_asks_next_material_question(self):
        self.assertTrue(SCRIPT.exists(), 'missing executable policy helper')
        result = policy().next_step({})
        self.assertEqual(result['action'], 'ask_purpose')
        self.assertEqual(result['questions'], ['purpose'])
        self.assertNotIn('address', result['questions'])


if __name__ == '__main__':
    unittest.main()
