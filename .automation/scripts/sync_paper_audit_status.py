"""Synchronize current warnings and source fields without inferring audit passes."""
from pathlib import Path
import hashlib
import json
import yaml

VAULT = Path(__file__).resolve().parents[2]
manifest = VAULT / '.automation/import/papers.json'
data = json.loads(manifest.read_text())
for note in sorted((VAULT / 'Literature/Papers/Entries').glob('*.md')):
    text = note.read_text()
    front = yaml.safe_load(text.split('---', 2)[1])
    entry = data['papers'].setdefault(str(note.relative_to(VAULT)), {})
    entry['current_note'] = {
        'sha256': hashlib.sha256(text.encode()).hexdigest(),
        'warnings': front.get('⚠️') or [],
        'source': front.get('source'),
        'doi': front.get('doi'),
    }
manifest.write_text(json.dumps(data, indent=2, ensure_ascii=False) + '\n')
