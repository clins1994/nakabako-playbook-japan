# SPDX-License-Identifier: MIT
"""Synthetic administrative decision aid. No network, writes or clinical decisions.

These functions do not enforce host/agent behavior and never execute an action.
Live consent payloads must not be saved in the public repository.
"""
from copy import deepcopy


def cost_summary(items):
    """Sum already-extracted JPY charges; unknown required charges stay unknown."""
    if not isinstance(items, dict) or not items:
        raise ValueError('provide named charges')
    for amount in items.values():
        if amount is not None and (type(amount) is not int or amount < 0):
            raise ValueError('charges must be nonnegative integer JPY or unknown')
    return {'known_subtotal_jpy': sum(x for x in items.values() if x is not None),
            'unknown_items': [k for k, v in items.items() if v is None],
            'complete': all(x is not None for x in items.values())}


def next_decision(facts):
    """Return a checkpoint using caller-extracted flags, never a diagnosis."""
    if not isinstance(facts, dict) or any(type(v) is not bool for v in facts.values()):
        raise ValueError('flags must be booleans')
    if facts.get('urgent_concern'):
        return 'medical_care'
    if facts.get('private_records_offered'):
        return 'minimize_private_data'
    if facts.get('medical_question'):
        return 'clinician_consultation'
    if not facts.get('sources_checked_this_run'):
        return 'refresh_current_evidence'
    if facts.get('diagnosis_needed'):
        return 'diagnostic_consultation'
    if not facts.get('options_ready'):
        return 'research_shortlist'
    if not facts.get('choice_complete'):
        return 'person_choose'
    if not facts.get('details_current'):
        return 'verify_clinic_details'
    return 'prepare_future_consent_review'


def future_handoff_ready(action, approval):
    """Exact synthetic snapshot comparison, NOT authority to book or send.

    Caller must ensure actual human approval, freshness and one-time consumption.
    Return a copy so later mutation cannot alter the reviewed snapshot.
    """
    required = {'kind', 'destination', 'branch', 'procedure', 'time', 'cost',
                'unknowns', 'cancellation', 'fields', 'purpose'}
    if not isinstance(action, dict) or set(action) != required:
        return None
    if action['kind'] not in {'consultation_booking', 'treatment_booking'}:
        return None
    if any(not isinstance(action[k], str) or not action[k].strip()
           for k in required - {'unknowns', 'fields'}):
        return None
    if not isinstance(action['unknowns'], list) or not isinstance(action['fields'], list):
        return None
    if not isinstance(approval, dict) or approval.get('booking_confirmed') is not True:
        return None
    if approval.get('transmission_confirmed') is not True or approval.get('action') != action:
        return None
    return {'status': 'future_handoff_only', 'snapshot': deepcopy(action), 'execute': False}
