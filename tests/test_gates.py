# SPDX-License-Identifier: MIT
from test_policy import policy
import unittest


class GateTests(unittest.TestCase):
    def test_booking_consent_binds_exact_review_not_blanket_yes(self):
        p = policy()
        self.assertTrue(hasattr(p, 'authorize'), 'missing consequential-action gate')
        action = {'kind': 'booking', 'destination': 'https://clinic.example/reserve', 'fields': ['name', 'dob'], 'summary': 'Branch A, employer package, 10:00 JST, 12000 JPY, cancellation terms shown'}
        self.assertFalse(p.authorize(action, None))
        approval = {'confirmed': True, 'action': action.copy()}
        self.assertTrue(p.authorize(action, approval))
        self.assertFalse(p.authorize({**action, 'destination': 'https://other.example'}, approval))
        self.assertFalse(p.authorize({**action, 'summary': 'different price'}, approval))
        self.assertFalse(p.authorize(action, {'confirmed': 'yes', 'action': action}))
        self.assertFalse(p.authorize({'kind': 'unknown'}, {'confirmed': True, 'action': {'kind': 'unknown'}}))

    def test_employer_japanese_document_extracted_items_match_package(self):
        p = policy()
        self.assertTrue(hasattr(p, 'compare_package'), 'missing package comparison')
        # Synthetic extraction, not an OCR test: 血圧, 尿糖・尿蛋白, 心電図.
        required = ['blood_pressure', 'urine_glucose', 'urine_protein', 'ecg']
        r = p.compare_package(required, ['blood_pressure', 'urine_glucose', 'urine_protein'], ['ecg'])
        self.assertFalse(r['suitable'])
        self.assertEqual(r['excluded'], ['ecg'])
        r = p.compare_package(required, ['blood_pressure'], [])
        self.assertEqual(r['unknown'], ['ecg', 'urine_glucose', 'urine_protein'])
        self.assertFalse(r['suitable'])
        self.assertTrue(p.compare_package(required, required, [])['suitable'])
        self.assertFalse(p.compare_package([], required, [])['suitable'])


if __name__ == '__main__':
    unittest.main()
