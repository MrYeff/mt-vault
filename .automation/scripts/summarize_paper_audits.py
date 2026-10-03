"""Record audit reports and outstanding flags; no flags are changed here."""
from pathlib import Path
import hashlib
import json
import yaml

VAULT = Path(__file__).resolve().parents[2]
reports = sorted((VAULT / '.automation/audit').glob('remaining-audit-*-2026-09-30.json'))
notes = []
for path in sorted((VAULT / 'Literature/Papers/Entries').glob('*.md')):
    raw = path.read_bytes()
    front = yaml.safe_load(raw.decode().split('---', 2)[1])
    notes.append({
        'note': str(path.relative_to(VAULT)),
        'sha256': hashlib.sha256(raw).hexdigest(),
        'warnings': front.get('⚠️') or [],
    })
summary = {
    'date': '2026-09-30',
    'reports': [str(p.relative_to(VAULT)) for p in reports],
    'total_notes': len(notes),
    'pending_audit': sum(any(w in n['warnings'] for w in ['not audited', 'audit failed', 'require reimport']) for n in notes),
    'fulltext_unavailable': sum('fulltext unavailable' in n['warnings'] for n in notes),
    'notes': notes,
    'scope': 'Check each report validity field before using its conclusions. Withdrawn reports do not establish passes. Formatting and structural checks are not source audits.',
}
(VAULT / '.automation/audit/remaining-summary-2026-09-30.json').write_text(json.dumps(summary, indent=2, ensure_ascii=False) + '\n')
print(json.dumps({k:v for k,v in summary.items() if k != 'notes'}, indent=2))
