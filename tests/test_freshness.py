# SPDX-License-Identifier: MIT
from test_policy import policy
from datetime import datetime, timezone
import unittest

NOW = datetime(2026, 9, 25, tzinfo=timezone.utc)

class FreshnessTests(unittest.TestCase):
    def test_retrieved_is_not_verified(self):
        p = policy()
        self.assertTrue(hasattr(p, 'freshness'), 'missing freshness evaluator')
        self.assertEqual(p.freshness({'x_nakabako': {'last_verified_at': None}, 'retrieved_at': NOW.isoformat()}, NOW), 'unverified')

    def test_verified_event_and_boundary_and_edits(self):
        p = policy()
        self.assertTrue(hasattr(p, 'freshness'), 'missing freshness evaluator')
        meta = {'status':'stable', 'verified': {'by':'process:review','at':'2026-09-24T00:00:00Z'}, 'stale_after':'2026-09-26T00:00:00Z'}
        self.assertEqual(p.freshness(meta, NOW), 'runtime_check_required')
        self.assertEqual(p.freshness({**meta,'stale_after': NOW.isoformat()}, NOW), 'stale')
        self.assertEqual(p.freshness({**meta,'generated': {'at':'2026-09-25T00:00:00Z'}}, NOW), 'unverified')
        self.assertEqual(p.freshness({**meta,'status':'deprecated'}, NOW), 'deprecated')
        self.assertEqual(p.freshness({**meta,'x_nakabako':{'volatility':'highly-volatile'}}, NOW), 'fetch_live')

    def test_refresh_requires_revalidation_and_rediscovery(self):
        p = policy()
        self.assertTrue(hasattr(p, 'proposal_ready'), 'missing refresh proposal gate')
        proposal = {'statement_id':'jp.healthcheck.employment.baseline','proposed_text':'Scoped replacement claim', 'revalidation':{'url':'https://example.gov/old','retrieved_at':NOW.isoformat(),'outcome':'unchanged','evidence':'Relevant paragraph inspected'}, 'rediscovery':{'query':'site:example.gov revised checkup requirements','searched_at':NOW.isoformat(),'candidates':[{'url':'https://example.gov/new','assessment':'newer in-scope guidance supersedes old'}]}, 'scope':'Japan; actual examination date checked','effective_from':None,'superseded_by':'https://example.gov/new','privacy_reviewed':True}
        self.assertTrue(p.proposal_ready(proposal))
        self.assertFalse(p.proposal_ready({**proposal,'rediscovery':{}}))
        self.assertFalse(p.proposal_ready({**proposal,'revalidation':{'outcome':'HTTP 200'}}))
        self.assertFalse(p.proposal_ready({**proposal,'privacy_reviewed':False}))
        self.assertFalse(p.proposal_ready({**proposal,'rediscovery':{'query':'x','searched_at':NOW.isoformat(),'candidates':[]}}))

if __name__ == '__main__':
    unittest.main()
