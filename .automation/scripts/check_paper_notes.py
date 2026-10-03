"""Check note structure; this does not audit claims against papers."""
from pathlib import Path
import collections
import json
import re
import yaml

VAULT = Path(__file__).resolve().parents[2]
ALLOWED = {'title', 'tags', 'authors', 'publication date', 'source', 'doi', 'read status', '⚠️'}
results = []
for path in sorted((VAULT / 'Literature/Papers/Entries').glob('*.md')):
    text = path.read_text()
    issues = []
    try:
        _, front, body = text.split('---', 2)
        meta = yaml.safe_load(front)
    except Exception as error:
        results.append({'note': str(path.relative_to(VAULT)), 'issues': [str(error)]})
        continue
    if extra := set(meta) - ALLOWED:
        issues.append(f'Unexpected metadata: {sorted(extra)}')
    for tag in meta.get('tags') or []:
        if re.search(r'\s', tag):
            issues.append(f'Tag contains whitespace: {tag}')
    for author in meta.get('authors') or []:
        if not author.startswith('[['):
            issues.append(f'Author is not a wiki link: {author}')
    if len(re.findall(r'^```', body, re.M)) % 2:
        issues.append('Unclosed code fence')
    definitions = re.findall(r'^\[\^([^\]]+)\]:', body, re.M)
    uses = re.findall(r'\[\^([^\]]+)\](?!:)', body)
    for key, count in collections.Counter(definitions).items():
        if count > 1:
            issues.append(f'Duplicate footnote: {key}')
    if missing := set(uses) - set(definitions):
        issues.append(f'Undefined footnotes: {sorted(missing)}')
    if unused := set(definitions) - set(uses):
        issues.append(f'Unused footnotes: {sorted(unused)}')
    if body.count('## Audit Log') > 1:
        issues.append('Duplicate Audit Log headings')
    results.append({'note': str(path.relative_to(VAULT)), 'warnings': meta.get('⚠️') or [], 'issues': issues})
print(json.dumps({'scope': 'Structure only; independent source audit required', 'notes': results}, indent=2, ensure_ascii=False))
