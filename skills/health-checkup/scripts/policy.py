# SPDX-License-Identifier: MIT
"""Offline decision checks on already-extracted facts; not an agent or a medical tool."""

from datetime import datetime


def timestamp(value):
    """Require explicit timezone; never silently interpret local time as UTC."""
    result = datetime.fromisoformat(value.replace('Z', '+00:00'))
    if result.tzinfo is None:
        raise ValueError('timestamp needs UTC offset')
    return result


def freshness(meta, now):
    """Conservative document signal, never automatic runtime verification."""
    if now.tzinfo is None:
        raise ValueError('now needs UTC offset')
    if meta.get('status') == 'deprecated':
        return 'deprecated'
    if meta.get('x_nakabako', {}).get('volatility') == 'highly-volatile':
        return 'fetch_live'
    if meta.get('stale_after') and now >= timestamp(meta['stale_after']):
        return 'stale'
    events = meta.get('verified', [])
    if isinstance(events, dict):
        events = [events]
    if not events or meta.get('status') == 'draft':
        return 'unverified'
    latest = max(timestamp(event['at']) for event in events)
    if latest > now or (meta.get('generated', {}).get('at') and latest < timestamp(meta['generated']['at'])):
        return 'unverified'
    return 'runtime_check_required'


def proposal_ready(proposal):
    """Structural evidence gate only; does not assess truth or write any file."""
    if not isinstance(proposal, dict):
        return False
    revalidation = proposal.get('revalidation', {})
    discovery = proposal.get('rediscovery', {})
    if not isinstance(revalidation, dict) or not isinstance(discovery, dict):
        return False
    required = ('statement_id', 'proposed_text', 'scope')
    if not all(isinstance(proposal.get(k), str) and proposal[k].strip() for k in required):
        return False
    if proposal.get('privacy_reviewed') is not True:
        return False
    if not all(revalidation.get(k) for k in ('url', 'retrieved_at', 'outcome', 'evidence')):
        return False
    if not all(discovery.get(k) for k in ('query', 'searched_at', 'candidates')):
        return False
    try:
        timestamp(revalidation['retrieved_at'])
        timestamp(discovery['searched_at'])
    except (ValueError, TypeError, AttributeError):
        return False
    candidates = discovery['candidates']
    return isinstance(candidates, list) and all(isinstance(c, dict) and c.get('url') and c.get('assessment') for c in candidates)


def next_step(facts):
    """Return the next small administrative decision; never execute an action."""
    if facts.get('sensitive_fields'):
        return {'action': 'request_transmission_consent', 'submit': False}
    if facts.get('source_conflict') or facts.get('source_superseded'):
        return {'action': 'resolve_sources', 'certainty': 'unknown'}
    if facts.get('blocked'):
        return {'action': 'human_takeover', 'translation': 'side_by_side', 'submit': False}
    stage = facts.get('stage', 'intake')
    if stage == 'booked':
        return {'action': 'extract_provider_instructions' if facts.get('instructions_available') else 'request_provider_instructions', 'invent_fasting': False}
    if stage == 'results':
        return {'action': 'coordinate_clinician_followup' if facts.get('followup_requested') else 'check_submission_requirements', 'diagnose': False}
    if stage == 'booking':
        if not facts.get('browser'):
            return {'action': 'guided_manual', 'translation': 'side_by_side', 'submit': False}
        return {'action': 'translate_fields' if facts.get('page_language') == 'ja' else 'review_booking', 'submit': False}
    if not facts.get('purpose'):
        return {'action': 'ask_purpose', 'questions': ['purpose']}
    if facts.get('document_available') and not facts.get('document_extracted'):
        return {'action': 'inspect_document_locally', 'questions': []}
    if facts['purpose'] == 'municipal':
        return {'action': 'check_program', 'questions': [key for key in ('municipality', 'insurer_category') if not facts.get(key)], 'eligibility': 'unknown'}
    if facts.get('english_required') and not facts.get('english_support_confirmed'):
        return {'action': 'confirm_language_support', 'english_support': 'unknown'}
    return {'action': 'verify_requirements', 'questions': []}


def authorize(action, approval):
    """Compare an ephemeral consent snapshot. Caller must consume it once.

    This does not authenticate the user or enforce a browser sandbox.
    Never persist action values; actual field values must be reviewed by user.
    """
    kinds = {'booking', 'cancellation', 'payment', 'sensitive_transmission', 'employer_submission', 'government_submission', 'reminder'}
    required = {'kind', 'destination', 'fields', 'summary'}
    return bool(isinstance(action, dict) and required <= action.keys()
                and action['kind'] in kinds
                and isinstance(action['fields'], list)
                and isinstance(action['destination'], str) and action['destination']
                and isinstance(action['summary'], str) and action['summary']
                and isinstance(approval, dict) and approval.get('confirmed') is True
                and approval.get('action') == action)


def compare_package(required, included, excluded):
    """Compare normalized, source-extracted test names, not package marketing names.

    Suitable means item coverage only, NOT price, eligibility, language or deadline.
    Unknown and contradictory evidence block suitability.
    """
    need, have, omit = set(required), set(included), set(excluded)
    return {'suitable': bool(need) and need <= have and not need & omit,
            'excluded': sorted(need & omit), 'unknown': sorted(need - have - omit)}
