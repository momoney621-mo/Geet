import pathlib
src = pathlib.Path("src/index.body.html").read_text()
i = src.index('<svg width="0"')
head, body = src[:i], src[i:]
head = head.replace('<meta name="claude:viewport-fit-sides" content="cover">\n', '')
out = ('<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
       '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
       + head + '<style>html,body{margin:0}img{max-width:100%}</style>\n</head>\n<body>\n' + body + '</body>\n</html>\n')
pathlib.Path("index.html").write_text(out)
print("built", len(out))
