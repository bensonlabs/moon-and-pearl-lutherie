"""Check local routes, fragments, assets and basic document semantics."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import re
root = Path(__file__).resolve().parents[1]
errors = []
class Page(HTMLParser):
    def __init__(self, path):
        super().__init__()
        self.path, self.ids, self.refs = path, set(), []
        self.h1 = self.main = self.title = 0
        self.feed(path.read_text())
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        self.h1 += tag == 'h1'
        self.main += tag == 'main'
        self.title += tag == 'title'
        if 'id' in attrs:
            if attrs['id'] in self.ids:
                errors.append(f'{self.path.name}: duplicate id {attrs["id"]}')
            self.ids.add(attrs['id'])
        if tag == 'img' and 'alt' not in attrs:
            errors.append(f'{self.path.name}: image missing alt')
        for key in ('src', 'href'):
            if key in attrs:
                self.refs.append(attrs[key])
pages = {path.name: Page(path) for path in root.glob('*.html')}
for name, page in pages.items():
    if (page.h1, page.main, page.title) != (1, 1, 1):
        errors.append(f'{name}: needs one h1, main and title')
    for ref in page.refs:
        url = urlsplit(ref)
        if url.scheme or url.netloc:
            continue
        target = root / unquote(url.path) if url.path else page.path
        if not target.exists():
            errors.append(f'{name}: missing {ref}')
        if url.fragment and target.name in pages and url.fragment not in pages[target.name].ids:
            errors.append(f'{name}: missing fragment {ref}')
    if '\u2014' in page.path.read_text():
        errors.append(f'{name}: em dash found')
for asset in re.findall(r'url\([\'\"]?([^\)\'\"]+)', (root / 'styles.css').read_text()):
    if not asset.startswith(('data:', 'http')) and not (root / asset).exists():
        errors.append(f'CSS: missing {asset}')
if errors:
    raise SystemExit('\n'.join(errors))
print(f'Validated {len(pages)} pages: assets, routes, fragments, alt attributes, and document structure.')
