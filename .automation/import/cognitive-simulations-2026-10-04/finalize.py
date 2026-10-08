"""Finalize only notes whose current bytes passed an independent audit."""
from pathlib import Path
import hashlib
import json
import re
import yaml

VAULT = Path(__file__).resolve().parents[3]
AUTO = VAULT / '.automation'
SPECS = [
    ('psychsim', 'PsychSim- Modeling Theory of Mind with Decision-Theoretic Agents',
     'psychsim-2026-10-04.json'),
    ('reputation', 'A Reputation Game Simulation- Emergent Social Phenomena from Information Theory',
     'reputation-game-2026-10-04.json'),
]

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

passed = []
for short, stem, metadata_name in SPECS:
    note = VAULT / 'Literature/Papers/Entries' / (stem + '.md')
    # Normalized evidence pointers are written by the coordinator only after review.
    evidence = json.loads((AUTO / 'audit/cognitive-simulations-2026-10-04' /
                           (short + '-accepted.json')).read_text())
    assert evidence['verdict'] == 'PASS'
    assert evidence['audited_sha256'] == digest(note), (short, 'note changed after audit')
    report = VAULT / evidence['report']
    assert evidence['report_sha256'] == digest(report)
    passed.append((short, note, metadata_name, evidence))

# Validate every audit gate before changing either note.
master_path = AUTO / 'import/papers.json'
master = json.loads(master_path.read_text())
completion = []
for short, note, metadata_name, evidence in passed:
    before = note.read_text()
    head, front, body = before.split('---', 2)
    assert not head.strip()
    front = re.sub(r'^  - (?:not audited|audit failed)\n', '', front, flags=re.M)
    front = re.sub(r'^⚠️:\n(?=\Z)', '⚠️: []\n', front, flags=re.M)
    updated_body = body.replace('\n## LLM Justification', '\n- Independent re-audit passed; import finalized.\n\n## LLM Justification', 1)
    assert updated_body.split('## Audit Log', 1)[0] == body.split('## Audit Log', 1)[0], 'Scientific content must remain unchanged.'
    assert updated_body.split('## LLM Justification', 1)[1] == body.split('## LLM Justification', 1)[1], 'Source justifications must remain unchanged.'
    after = '---' + front + '---' + updated_body
    note.write_text(after)
    meta_path = AUTO / 'import' / metadata_name
    meta = json.loads(meta_path.read_text())
    meta['audit_status'] = 'PASS after independent audit and required corrections/re-audit'
    meta['finalization'] = dict(evidence, final_sha256=digest(note),
                                administrative_only_change=True, finalized_at='2026-10-04')
    meta_path.write_text(json.dumps(meta, indent=2, ensure_ascii=False) + '\n')
    fm = yaml.safe_load(front)
    rel = str(note.relative_to(VAULT))
    master['papers'][rel] = {
        'imported_at': '2026-10-04', 'metadata_record': str(meta_path.relative_to(VAULT)),
        'reference_status': 'Source bibliography retained; cited-paper imports and external resolution skipped at user request.',
        'audit_status': 'passed independent audit', 'audit': evidence,
        'current_note': {'sha256': digest(note), 'warnings': fm.get('⚠️', []),
                         'source': fm['source'], 'doi': fm.get('doi')},
    }
    completion.append({'note': rel, 'audit': evidence, 'final_sha256': digest(note),
                       'warnings': fm.get('⚠️', [])})
master_path.write_text(json.dumps(master, indent=2, ensure_ascii=False) + '\n')
(AUTO / 'audit/cognitive-simulations-2026-10-04/completion.json').write_text(
    json.dumps({'date': '2026-10-04', 'notes': completion}, indent=2, ensure_ascii=False) + '\n')
print(json.dumps(completion, indent=2, ensure_ascii=False))
