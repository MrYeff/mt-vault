"""Extract ordered citation candidates from LaTeXML bibliography HTML.

This writes a review artifact, not notes. Titles need verification against the
source before import; unresolved items remain explicit rather than guessed.
"""
from html.parser import HTMLParser
import argparse
import hashlib
import json
from pathlib import Path

class Node:
    def __init__(self, tag='', attrs=()):
        self.tag, self.attrs, self.children = tag, dict(attrs), []
    def has(self, name):
        return name in self.attrs.get('class', '').split()
    def text(self):
        return ' '.join(''.join(x if isinstance(x, str) else x.text() for x in self.children).split())
    def find(self, name):
        found = []
        for child in self.children:
            if isinstance(child, Node):
                if child.has(name): found.append(child)
                found.extend(child.find(name))
        return found

class Parser(HTMLParser):
    VOID = {'area','base','br','col','embed','hr','img','input','link','meta','param','source','track','wbr'}
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.root = Node()
        self.stack = [self.root]
    def handle_starttag(self, tag, attrs):
        node = Node(tag, attrs)
        self.stack[-1].children.append(node)
        if tag not in self.VOID: self.stack.append(node)
    def handle_startendtag(self, tag, attrs):
        self.stack[-1].children.append(Node(tag, attrs))
    def handle_endtag(self, tag):
        for i in range(len(self.stack)-1, 0, -1):
            if self.stack[i].tag == tag:
                del self.stack[i:]
                break
    def handle_data(self, data):
        self.stack[-1].children.append(data)

def extract(path):
    raw = path.read_bytes()
    parser = Parser()
    parser.feed(raw.decode())
    citations = []
    for index, item in enumerate(parser.root.find('ltx_bibitem'), 1):
        blocks = [b.text() for b in item.find('ltx_bibblock')]
        citations.append({
            'index': index, 'source_id': item.attrs.get('id'),
            'blocks': blocks, 'citation': item.text(),
            'title_candidate': blocks[1].rstrip('.') if len(blocks) > 1 else None,
            'status': 'requires source verification',
        })
    return {'source_file': str(path), 'source_sha256': hashlib.sha256(raw).hexdigest(), 'entries': citations}

if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument('source', type=Path)
    args.add_argument('output', type=Path)
    cfg = args.parse_args()
    cfg.output.write_text(json.dumps(extract(cfg.source), indent=2, ensure_ascii=False) + '\n')
