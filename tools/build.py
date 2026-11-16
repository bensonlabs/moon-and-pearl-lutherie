"""Package the site without changing its GitHub Pages structure."""
from pathlib import Path
import shutil
import subprocess
import sys
root = Path(__file__).resolve().parents[1]
subprocess.run([sys.executable, str(root / 'tools/check.py')], check=True)
output = root / 'dist'
if output.exists():
    shutil.rmtree(output)
output.mkdir()
for pattern in ('*.html', '*.css', '*.js', 'sitemap.xml', 'robots.txt', '.nojekyll'):
    for source in root.glob(pattern):
        shutil.copy2(source, output / source.name)
shutil.copytree(root / 'assets', output / 'assets')
subprocess.run([sys.executable, str(root / 'tools/check.py'), str(output)], check=True)
print(f'Prepared {len(list(output.rglob("*")))} static files and directories.')
