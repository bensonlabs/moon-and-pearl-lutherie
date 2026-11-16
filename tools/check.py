"""Check local routes, fragments, assets and basic document semantics."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
from urllib.robotparser import RobotFileParser
from xml.etree import ElementTree
import re
import sys
root = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path(__file__).resolve().parents[1]
origin = 'https://moonandpearllutherie.com'
errors = []
class Page(HTMLParser):
    def __init__(self, path):
        super().__init__()
        self.path, self.ids, self.refs = path, set(), []
        self.h1 = self.main = self.title = 0
        self.in_head = False
        self.canonicals, self.robots = [], set()
        self.feed(path.read_text())
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'head':
            self.in_head = True
        if tag == 'link' and 'canonical' in attrs.get('rel', '').lower().split():
            self.canonicals.append(attrs.get('href'))
            if not self.in_head:
                errors.append(f'{self.path.name}: canonical must be in head')
        if tag == 'meta' and attrs.get('name', '').lower() in ('robots', 'googlebot'):
            self.robots.update(re.split(r'[\s,]+', attrs.get('content', '').lower()))
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
    def handle_endtag(self, tag):
        if tag == 'head':
            self.in_head = False
pages = {path.name: Page(path) for path in root.glob('*.html')}
robots = RobotFileParser()
robots.parse((root / 'robots.txt').read_text().splitlines())
preferred = set()
for name, page in pages.items():
    canonical = origin + ('/' if name == 'index.html' else '/' + name)
    noindex = bool(page.robots & {'noindex', 'none'})
    if name == 'inquiry-thanks.html':
        if not noindex:
            errors.append(f'{name}: must remain noindex')
    elif noindex:
        errors.append(f'{name}: content page unexpectedly blocks indexing')
    if not noindex:
        preferred.add(canonical)
        if page.canonicals != [canonical]:
            errors.append(f'{name}: needs exactly one canonical: {canonical}')
        if not robots.can_fetch('Googlebot', canonical):
            errors.append(f'{name}: blocked by robots.txt')
    if (page.h1, page.main, page.title) != (1, 1, 1):
        errors.append(f'{name}: needs one h1, main and title')
    for ref in page.refs:
        url = urlsplit(ref)
        if not url.netloc or url.netloc == urlsplit(origin).netloc:
            if url.path in ('index.html', '/index.html'):
                errors.append(f'{name}: homepage link must use /: {ref}')
        if url.scheme or url.netloc:
            continue
        target = root / unquote(url.path).lstrip('/') if url.path else page.path
        if target.is_dir():
            target = target / 'index.html'
        if not target.exists():
            errors.append(f'{name}: missing {ref}')
        if url.fragment and target.name in pages and url.fragment not in pages[target.name].ids:
            errors.append(f'{name}: missing fragment {ref}')
    if '\u2014' in page.path.read_text():
        errors.append(f'{name}: em dash found')
locations = [node.text for node in ElementTree.parse(root / 'sitemap.xml').findall(
    '{http://www.sitemaps.org/schemas/sitemap/0.9}url/{http://www.sitemaps.org/schemas/sitemap/0.9}loc')]
if len(locations) != len(set(locations)) or set(locations) != preferred:
    errors.append('sitemap.xml must list each indexable canonical URL exactly once')
if origin + '/sitemap.xml' not in (robots.site_maps() or []):
    errors.append('robots.txt must advertise the canonical sitemap')
for asset in re.findall(r'url\([\'\"]?([^\)\'\"]+)', (root / 'styles.css').read_text()):
    if not asset.startswith(('data:', 'http')) and not (root / asset).exists():
        errors.append(f'CSS: missing {asset}')
if errors:
    raise SystemExit('\n'.join(errors))
print(f'Validated {len(pages)} pages: assets, routes, fragments, alt attributes, document structure, canonicals, sitemap, and indexing rules.')
