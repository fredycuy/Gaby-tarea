from pathlib import Path
import re

root = Path('.')
html_files = list(root.rglob('*.html'))
broken = []

for path in html_files:
    text = path.read_text(encoding='utf-8')
    for match in re.finditer(r'href=["\']([^"\']+)["\']', text):
        href = match.group(1)
        if href.startswith('#') or href.startswith('javascript:') or href.startswith('mailto:') or href.startswith('tel:') or href.startswith('http://') or href.startswith('https://'):
            continue
        target = (path.parent / href).resolve()
        if not target.exists():
            broken.append((str(path), href))

print(f'Checked {len(html_files)} HTML files')
print(f'Broken local refs: {len(broken)}')
for p, href in broken:
    print(f'{p} -> {href}')
