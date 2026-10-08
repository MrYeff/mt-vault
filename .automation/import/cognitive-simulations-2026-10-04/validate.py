"""Check imported notes and links; this does not replace source auditing."""
from pathlib import Path
import hashlib
import json
import re
import yaml

VAULT = Path(__file__).resolve().parents[3]
NOTES = [
    'PsychSim- Modeling Theory of Mind with Decision-Theoretic Agents',
    'A Reputation Game Simulation- Emergent Social Phenomena from Information Theory',
]
results = []
for stem in NOTES:
    path = VAULT / 'Literature/Papers/Entries' / (stem + '.md')
    text = path.read_text()
    front = yaml.safe_load(text.split('---', 2)[1])
    definitions = set(re.findall(r'^\[\^([^\]]+)\]:', text, re.M))
    uses = set(re.findall(r'\[\^([^\]]+)\](?!:)', text))
    assert uses == definitions, (stem, uses - definitions, definitions - uses)
    for section in ['## Abstract', '## Research Questions', '## Model',
                    '### What does it represent?', '### How does it work?',
                    '### What can it answer?', '### Where does it apply?',
                    '### References', '## LLM Justification']:
        assert section in text, (stem, section)
    assert {'model', 'simulation'} <= set(front['tags'])
    assert not any(' ' in tag for tag in front['tags'])
    for link in front['authors']:
        target = re.fullmatch(r'\[\[([^|]+)(?:\|[^\]]+)?\]\]', link)[1]
        assert (VAULT / (target + '.md')).exists(), target
    assert '/tmp/' not in text, (stem, 'temporary process path in paper content')
    assert front['source'].startswith('https://')
    results.append({'note': str(path.relative_to(VAULT)),
                    'sha256': hashlib.sha256(path.read_bytes()).hexdigest(),
                    'footnotes': len(definitions), 'warnings': front.get('⚠️', [])})
reading = (VAULT / 'Simulation Reading List.md').read_text()
for stem in NOTES:
    assert '[[' + stem + ']]' in reading, stem
numbers = re.findall(r'^(\d+)\. \*\*', reading, re.M)
assert numbers == [str(n) for n in range(1, len(numbers) + 1)], numbers
out = {'checks': 'PASS', 'scope': 'Structure and new direct links only; bibliography targets intentionally not imported.', 'notes': results}
(Path(__file__).parent / 'structural-validation.json').write_text(json.dumps(out, indent=2, ensure_ascii=False) + '\n')
print(json.dumps(out, indent=2, ensure_ascii=False))
