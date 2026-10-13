# SPDX-License-Identifier: MIT
"""Offline checks for this bundle's JSON-frontmatter OKF producer profile.

Adapted from nakabako health-checkup validator; removed private-state schema checks.
Not a full Markdown, YAML or OKF implementation. No network or writes.
"""
import argparse
import json
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit

SKILL = Path(__file__).resolve().parents[1]


def unique_json_object(pairs):
    """Reject ambiguous duplicate keys in this JSON producer profile."""
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError('duplicate JSON key: ' + key)
        result[key] = value
    return result


def validate_entrypoint_frontmatter(text):
    """Strict duplicate-key check for our scalar/block-mapping YAML profile.

    This is deliberately not a general YAML parser. Flow mappings, aliases,
    sequences and multiline scalar syntax are outside this producer profile.
    """
    parts = text.split('---', 2)
    if len(parts) != 3 or parts[0].strip():
        return ['SKILL.md: missing frontmatter']
    levels = {}
    errors = []
    for line in parts[1].splitlines():
        if not line.strip() or line.lstrip().startswith('#'):
            continue
        match = re.fullmatch(r'( *)([a-zA-Z][a-zA-Z0-9_-]*):(?: (.*))?', line)
        if not match:
            errors.append('SKILL.md: unsupported frontmatter producer syntax')
            continue
        indent, key, value = len(match[1]), match[2], match[3]
        if value and value[0] in '{}[]&*|>':
            errors.append('SKILL.md: unsupported frontmatter producer syntax')
        for depth in list(levels):
            if depth > indent:
                del levels[depth]
        keys = levels.setdefault(indent, set())
        if key in keys:
            errors.append('SKILL.md: duplicate YAML key: ' + key)
        keys.add(key)
    return errors


def validate_skill(root):
    """Check bundled dependencies, native metadata and claim attribution locally."""
    root = Path(root).resolve()
    okf = root / 'references/okf'
    errors = []
    required = ('SKILL.md', 'LICENSES.md', 'LICENSE-content', 'LICENSE-software',
                'references/okf/index.md', 'references/okf/log.md',
                'references/research-receipts.json', 'references/handoff.md', 'references/refresh.md',
                'references/dry-run.md', 'scripts/decision.py')
    for name in required:
        if not (root / name).is_file():
            errors.append('missing dependency: ' + name)

    if (root / 'SKILL.md').is_file():
        errors.extend(validate_entrypoint_frontmatter((root / 'SKILL.md').read_text()))

    def dependency(origin, target, bundle=False):
        parsed = urlsplit(target)
        if parsed.scheme or parsed.netloc or not parsed.path:
            return
        path = unquote(parsed.path)
        destination = ((okf / path.lstrip('/')) if bundle and path.startswith('/')
                       else origin.parent / path).resolve()
        if not destination.is_relative_to(root) or not destination.is_file():
            errors.append(f'{origin.relative_to(root)}: missing or escaping dependency {target}')

    for path in root.rglob('*.md'):
        text = path.read_text(encoding='utf-8')
        bundle = path.is_relative_to(okf)
        for target in re.findall(r'(?<!!)\[[^\]\n]*\]\(([^\s)]+)\)', text):
            dependency(path, target, bundle)
        if not bundle or path.name == 'log.md':
            continue
        try:
            parts = text.split('---', 2)
            if parts[0].strip() or len(parts) != 3:
                raise ValueError('missing JSON frontmatter')
            meta = json.loads(parts[1], object_pairs_hook=unique_json_object)
            if not isinstance(meta, dict):
                raise ValueError('frontmatter must be object')
            if path == okf / 'index.md':
                if meta.get('okf_version') != '0.2':
                    raise ValueError('expected OKF 0.2')
                continue
            for key in ('type', 'title', 'description', 'generated', 'status', 'sources'):
                if key not in meta:
                    raise ValueError('missing ' + key)
            if meta['status'] not in ('draft', 'stable', 'deprecated'):
                raise ValueError('invalid native status')
            sources = meta['sources']
            ids = [source['id'] for source in sources]
            if len(ids) != len(set(ids)):
                raise ValueError('duplicate source IDs')
            body = parts[2]
            refs = set(re.findall(r'\[\^([^\]]+)\]', body))
            definitions = set(re.findall(r'^\[\^([^\]]+)\]:', body, re.M))
            if not refs <= definitions or not refs <= set(ids):
                raise ValueError('footnote missing definition or source attribution')
            for source in sources:
                dependency(path, source['resource'], True)
            ext = meta.get('x_nakabako', {})
            for claim in ext.get('statement_ids', []):
                if f'id="{claim}"' not in body:
                    raise ValueError('statement ID missing anchor')
            if ext.get('research_evidence'):
                dependency(path, ext['research_evidence'], True)
        except (ValueError, KeyError, TypeError) as exc:
            errors.append(f'{path.relative_to(root)}: invalid producer metadata: {exc}')
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--skill', type=Path, default=SKILL)
    args = parser.parse_args()
    errors = validate_skill(args.skill)
    for error in errors:
        print(error)
    if not errors:
        print('PASS: portable dependencies and OKF producer-profile checks')
    return bool(errors)


if __name__ == '__main__':
    raise SystemExit(main())
