"""Move research source caches into the vault and update automation paths.

Run after source reviewers stop using /tmp. Files are content-addressed;
original paths, URLs and referring records stay in the source index.
"""
from pathlib import Path
import hashlib
import json
import re
import shutil
import zipfile

VAULT = Path(__file__).resolve().parents[2]
AUTO = VAULT / '.automation'
DEST = AUTO / 'sources'
FILES = DEST / 'files'
FILES.mkdir(parents=True, exist_ok=True)
EXTENSIONS = {'.pdf', '.html', '.txt', '.docx', '.png', '.json'}
PREFIXES = ('acting-', 'agent4rec-', 'audit-', 'cohesion-', 'deff', 'github-',
            'oasis-', 'recsim-', 'remaining-kraut-', 'simsom-', 'sopra-',
            'strong-', 'strong68', 'structure-', 'verified-','verified70')
candidates = {p for p in Path('/tmp').iterdir()
              if p.is_file() and not p.is_symlink() and p.suffix.lower() in EXTENSIONS
              and (p.name.startswith(PREFIXES) or re.fullmatch(r'(?:5[4-9]|6[0-6])\.txt', p.name))}
for source_dir in [Path('/tmp/strong54-66-sources'), Path('/tmp/verified68')]:
    if source_dir.exists():
        candidates.update(p for p in source_dir.rglob('*') if p.is_file()
                          and not p.is_symlink() and p.suffix.lower() in EXTENSIONS)

index_path = DEST / 'index.json'
index = json.loads(index_path.read_text()) if index_path.exists() else {'schema_version': 1, 'files': {}}
records = {}
for path in AUTO.rglob('*.json'):
    if DEST in path.parents: continue
    try: records[path] = json.loads(path.read_text())
    except (ValueError, UnicodeError): continue

references = {}
def inspect(value, record, context=None):
    context = context or {}
    if isinstance(value, dict):
        context = dict(context)
        for key in ['note', 'note_path', 'file', 'paper', 'url', 'primary_source', 'source_url', 'source_read', 'source']:
            item = value.get(key)
            if isinstance(item, str) and (item.endswith('.md') or item.startswith('http')):
                context[key] = item
        for item in value.values(): inspect(item, record, context)
    elif isinstance(value, list):
        for item in value: inspect(item, record, context)
    elif isinstance(value, str):
        for source in candidates:
            if str(source) in value:
                item = {'record': str(record.relative_to(VAULT)), 'context': context}
                items = references.setdefault(str(source), [])
                if item not in items: items.append(item)

# Avoid scanning duplicated full-text metadata repeatedly for every path.
patterns = re.compile('|'.join(re.escape(str(p)) for p in sorted(candidates, key=lambda p: -len(str(p))))) if candidates else None
def inspect_fast(value, record, context=None):
    context = context or {}
    if isinstance(value, dict):
        context = dict(context)
        for key in ['note', 'note_path', 'file', 'paper', 'url', 'primary_source', 'source_url', 'source_read', 'source']:
            item = value.get(key)
            if isinstance(item, str) and (item.endswith('.md') or item.startswith('http')):
                context[key] = item
        for item in value.values(): inspect_fast(item, record, context)
    elif isinstance(value, list):
        for item in value: inspect_fast(item, record, context)
    elif isinstance(value, str) and patterns:
        for match in patterns.finditer(value):
            item = {'record': str(record.relative_to(VAULT)), 'context': context}
            items = references.setdefault(match.group(), [])
            if item not in items: items.append(item)
for path, data in records.items(): inspect_fast(data, path)

mapping = {}
for source in sorted(candidates):
    raw = source.read_bytes()
    digest = hashlib.sha256(raw).hexdigest()
    suffix = source.suffix.lower()
    kind = {'pdf': 'download', 'html': 'download', 'txt': 'derived_text',
            'docx': 'supplement', 'png': 'rendered_page', 'json': 'metadata'}[suffix[1:]]
    if raw.startswith(b'%PDF'): suffix = '.pdf'
    elif raw.startswith(b'PK'):
        try:
            with zipfile.ZipFile(source) as archive:
                if 'word/document.xml' in archive.namelist(): suffix = '.docx'; kind = 'supplement'
        except zipfile.BadZipFile: pass
    target = FILES / (digest + suffix)
    if target.exists():
        assert hashlib.sha256(target.read_bytes()).hexdigest() == digest
        source.unlink()
    else:
        shutil.move(str(source), target)
    mapping[str(source)] = str(target)
    entry = index['files'].setdefault(digest, {
        'path': str(target.relative_to(VAULT)), 'sha256': digest,
        'bytes': len(raw), 'kind': kind, 'original_paths': [], 'records': [],
    })
    if str(source) not in entry['original_paths']: entry['original_paths'].append(str(source))
    for record in references.get(str(source), []):
        if record not in entry['records']: entry['records'].append(record)

# Use exact old paths; leave historical timestamps and note hashes intact.
replacement = re.compile('|'.join(re.escape(p) for p in sorted(mapping, key=len, reverse=True))) if mapping else None
def relocate(value):
    if isinstance(value, dict): return {k: relocate(v) for k,v in value.items()}
    if isinstance(value, list): return [relocate(v) for v in value]
    if isinstance(value, str) and replacement:
        return replacement.sub(lambda m: mapping[m.group()], value)
    return value
for path, data in records.items():
    updated = relocate(data)
    if updated != data: path.write_text(json.dumps(updated, indent=2, ensure_ascii=False) + '\n')
index['last_archived_at'] = '2026-09-30'
index['scope'] = 'Saved caches, extracted text, supplements and rendered pages. Cache availability does not establish source authenticity or audit completion.'
index_path.write_text(json.dumps(index, indent=2, ensure_ascii=False) + '\n')
print(json.dumps({'moved_cache_paths': len(mapping), 'unique_saved_files': len(index['files']),
                  'index': str(index_path.relative_to(VAULT))}))
