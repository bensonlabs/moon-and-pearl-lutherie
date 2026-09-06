"""Package the site without changing its GitHub Pages structure."""
from pathlib import Path
import shutil
root = Path(__file__).resolve().parents[1]
output = root / 'dist'
if output.exists():
    shutil.rmtree(output)
output.mkdir()
for pattern in ('*.html', '*.css', '*.js', 'sitemap.xml', 'robots.txt', '.nojekyll'):
    for source in root.glob(pattern):
        shutil.copy2(source, output / source.name)
shutil.copytree(root / 'assets', output / 'assets')
print(f'Prepared {len(list(output.rglob("*")))} static files and directories.')
