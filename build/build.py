"""Rigenera index.html: python build/conv.py && python build/build.py"""
import pathlib
B=pathlib.Path(__file__).resolve().parent
t=(B/'template.html').read_text(encoding='utf-8')
t=t.replace('/*KATEX*/',(B/'katex_inline.css').read_text(encoding='utf-8'))
t=t.replace('/*DATA*/',(B/'data.json').read_text(encoding='utf-8').replace('</','<\\/'))
head='<!doctype html>\n<html lang="it">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n<link rel="manifest" href="manifest.json">\n<link rel="icon" href="favicon-32.png">\n<link rel="apple-touch-icon" href="apple-touch-icon.png">\n<meta name="theme-color" content="#2e5c8a">\n<meta name="mobile-web-app-capable" content="yes">\n<meta name="apple-mobile-web-app-capable" content="yes">\n<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">\n<meta name="apple-mobile-web-app-title" content="Fisica">\n'
i=t.index('<header class="topbar">')
page=head+t[:i]+'<style>:root{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}body{margin:0}img{max-width:100%}[hidden]{display:none!important}</style>\n</head>\n<body>\n'+t[i:]+'\n</body>\n</html>\n'
(B.parent/'index.html').write_text(page,encoding='utf-8')
print('index.html',len(page))
