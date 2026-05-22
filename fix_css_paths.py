import re

for fname in ['gameapp/static/css/index.css', 'gameapp/static/css/home.css']:
    with open(fname, 'r', encoding='utf-8') as f:
        content = f.read()
    # Replace url(images/... with url(../images/... (relative to CSS dir)
    fixed = re.sub(r"url\((['\"]?)images/", r"url(\1../images/", content)
    with open(fname, 'w', encoding='utf-8') as f:
        f.write(fixed)
    count = content.count('url(images/') + content.count("url('images/") + content.count('url("images/')
    print(f'{fname}: fixed {count} broken image references')
