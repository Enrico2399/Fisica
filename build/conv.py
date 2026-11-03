import re, json, base64, os, sys
import pathlib
ROOT=str(pathlib.Path(__file__).resolve().parent.parent)
def match_brace(s,i):
    # s[i]=='{' -> index of matching '}'
    d=0
    for k in range(i,len(s)):
        c=s[k]
        if c=='\\': continue
        if c=='{' and (k==0 or s[k-1]!='\\'): d+=1
        elif c=='}' and (k==0 or s[k-1]!='\\'):
            d-=1
            if d==0: return k
    raise ValueError(s[i:i+80])
def args(s,i,n):
    out=[]
    for _ in range(n):
        while s[i] in ' \n': i+=1
        if s[i]=='[':
            j=s.index(']',i); i=j+1
            while s[i] in ' \n': i+=1
        j=match_brace(s,i); out.append(s[i+1:j]); i=j+1
    return out,i
def replace_cmd(s,cmd,n,fn):
    out=[];i=0
    pat='\\'+cmd+'{'
    while True:
        k=s.find('\\'+cmd,i)
        if k<0: out.append(s[i:]);break
        nxt=k+len(cmd)+1
        if nxt<len(s) and (s[nxt].isalpha()): out.append(s[i:nxt]);i=nxt;continue
        out.append(s[i:k])
        a,j=args(s,nxt,n)
        out.append(fn(*a)); i=j
    return ''.join(out)
def split_math(s):
    # returns list of (is_math, text) ; math kept raw with delimiters
    parts=[];i=0;buf=''
    while i<len(s):
        if s.startswith('\\[',i):
            j=s.index('\\]',i); parts.append((0,buf));buf='';parts.append((1,s[i:j+2]));i=j+2
        elif s[i]=='$' and (i==0 or s[i-1]!='\\'):
            j=i+1
            while s[j]!='$' or s[j-1]=='\\': j+=1
            parts.append((0,buf));buf='';parts.append((1,s[i:j+1]));i=j+1
        else: buf+=s[i];i+=1
    parts.append((0,buf));return parts
def esc(t): return t.replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')
def text2html(s):
    segs=split_math(s); s=''
    for m,t in segs:
        s+= t.replace('\\ris{','\\boxed{') if m else replace_cmd(t,'ris',1,lambda a:'$\\boxed{'+a+'}$')
    maths=[]
    buf=[]
    for m,t in split_math(s):
        if m:
            maths.append(esc(t.replace('\\displaystyle','')))
            buf.append('\x00%d\x00'%(len(maths)-1))
        else: buf.append(t)
    t=esc(''.join(buf))
    for _ in range(3):
        t=replace_cmd(t,'textbf',1,lambda a:'<b>'+a+'</b>')
        t=replace_cmd(t,'emph',1,lambda a:'<em>'+a+'</em>')
        t=replace_cmd(t,'textit',1,lambda a:'<em>'+a+'</em>')
        t=replace_cmd(t,'textsc',1,lambda a:a)
        t=replace_cmd(t,'textcolor',2,lambda c,a:'<b>'+a+'</b>')
        t=replace_cmd(t,'color',1,lambda a:'')
        t=replace_cmd(t,'upshape',0,lambda :'')
    rep=[("``","\u201c"),("''","\u201d"),("---","\u2014"),("--","\u2013"),("\\S","\u00a7"),("\\%","%"),("\\checkmark","\u2713"),("\\textbullet","\u2022"),
         ("\\qquad","&emsp;&emsp;"),("\\quad","&emsp;"),("\\ "," "),("\\,"," "),("\\\\[-1pt]","<br>"),("\\\\","<br>"),("\\dots","\u2026"),("~"," "),("\\par",""),("\\hfill",""),("\\small",""),("\\scriptsize",""),("\\noindent",""),("{,}",","),("\\&","&amp;"),("\\bfseries","")]
    for a,b in rep: t=t.replace(a,b)
    t=re.sub(r'\{([^{}\x00]*)\}',r'\1',t)
    t=re.sub('\x00(\\d+)\x00',lambda m:maths[int(m.group(1))],t)
    return t.strip()
def items(body):
    body=re.sub(r'\\begin\{(enumerate|itemize)\}(\[[^\]]*\])?','',body)
    body=re.sub(r'\\end\{(enumerate|itemize)\}','',body)
    parts=[p.strip() for p in re.split(r'\\item\b',body)]
    return [text2html(p) for p in parts[1:] if p]
# ---------------- ESERCIZI
FSEC={'Compito':None,'Cinematica':2,'Dinamica':3,'Corpo':5,'Fluidi':6,'Termodinamica':8,'Onde meccaniche':4,'Elettrostatica':9,'Corrente':11,'Campo magnetico':12,'Induzione':13,'Onde elettromagnetiche':14,'Dielettrici':10,'Ottica':14}
def fsec_for(num,secname):
    special={'F1a':[5],'F1b':[8],'F2a':[10],'F2b':[13],'10.1':[4],'10.2':[4],'22.1':[7],'22.2':[7],'23.1':[7],'23.2':[7],'23.3':[7],'23.4':[7],
             '30.3':[10,9],'31.1':[11,7],'36.2':[13,12],'37.1':[13,12],'43.1':[12],'44.1':[12],'42.1':[10],'42.2':[10],'42.3':[10],'32.2':[12],'26.1':[9,3],'27.1':[9],'9.1':[2],'9.2':[2],'9.3':[2],'9.4':[2],'9.5':[2],'9.6':[2],'11.6':[3],'15.1':[3,5],'17.2':[5,2]}
    if num in special: return special[num]
    for k,v in FSEC.items():
        if secname.startswith(k): return [v]
    return []
src=open(f'{ROOT}/src/esercizi.tex',encoding='utf-8').read()
src=src[src.index('\\section{Compito'):src.index('\\end{document}')]
sections=[]
for sm in re.finditer(r'\\section\{(.*?)\}\n(.*?)(?=\\section\{|\Z)',src,re.S):
    name=sm.group(1); body=sm.group(2)
    exs=[]
    for em in re.finditer(r'\\es\{(.*?)\}\{(.*?)\}\n(.*?)(?=\\es\{|\Z)',body,re.S):
        num,title,b=em.groups()
        b=re.sub(r'(?m)^%.*$','',b)
        ex={'num':num,'title':text2html(title)}
        k=b.find('\\testo{')
        if k>=0:
            a,_=args(b,k+6,1); ex['testo']=text2html(a[0])
        k=b.find('\\idea{')
        if k>=0:
            a,_=args(b,k+5,1); ex['idea']=text2html(a[0])
        k=b.find('\\nota{')
        if k>=0:
            a,_=args(b,k+5,1); ex['nota']=text2html(a[0])
        m=re.search(r'\\begin\{enumerate\}(.*)\\end\{enumerate\}',b,re.S)
        ex['passi']=items(m.group(0)) if m else []
        ex['f']=fsec_for(num,name)
        ex['img']=num.replace('.','_') if os.path.exists(f'{ROOT}/img/{num.replace(".","_")}.png') else None
        exs.append(ex)
    sections.append({'name':text2html(name),'ex':exs})
# ---------------- FORMULARIO
fs=open(f'{ROOT}/src/formulario_esame.tex',encoding='utf-8').read()
fs=fs[fs.index('\\section{Come'):fs.index('\\end{multicols*}')]
fsecs=[];n=0
def conv_block(b):
    html=[]
    # tokens: tab, environments, subsection, text
    pat=re.compile(r'\\begin\{tab\}\{([^\n]*?)\}\n(.*?)\\end\{tab\}|\\begin\{(oro|svolto|bx)\}((?:\{[^{}]*\})*)\n?(.*?)\\end\{\3\}|\\begin\{(esame|errori)\}(.*?)\\end\{\6\}|\\subsection\{(.*?)\}',re.S)
    pos=0
    for m in pat.finditer(b):
        pre=b[pos:m.start()].strip()
        if pre: html.append('<p>'+text2html(pre)+'</p>')
        pos=m.end()
        if m.group(2) is not None:
            rows=[r.strip() for r in re.split(r'\\\\\s*(?:\\hline)?',m.group(2)) if r.strip() and r.strip()!='\\hline']
            t=['<div class="tw"><table>']
            for r in rows:
                hd=r.startswith('\\hd')
                r=r.replace('\\hd','').strip()
                cells=[c.strip() for c in re.split(r'(?<!\\)&',r)]
                tag='th' if hd else 'td'
                t.append('<tr>'+''.join(f'<{tag}>{text2html(c)}</{tag}>' for c in cells)+'</tr>')
            t.append('</table></div>'); html.append(''.join(t))
        elif m.group(3):
            kind=m.group(3); a=re.findall(r'\{([^{}]*)\}',m.group(4)); title=a[-1] if a else ''
            body=m.group(5)
            cls={'oro':'gold','svolto':'ex','bx':'info'}[kind]
            if kind=='svolto': title='esempio svolto — '+title
            inner=('<ol>'+''.join('<li>'+x+'</li>' for x in items(body))+'</ol>') if '\\item' in body and 'enumerate' in body else (('<ul>'+''.join('<li>'+x+'</li>' for x in items(body))+'</ul>') if '\\item' in body else text2html(body))
            html.append(f'<div class="box {cls}"><span class="lbl">{text2html(title)}</span>{inner}</div>')
        elif m.group(6):
            kind=m.group(6); cls={'esame':'gold','errori':'warn'}[kind]; title={'esame':"nell'esame",'errori':'errori da evitare'}[kind]
            html.append(f'<div class="box {cls}"><span class="lbl">{title}</span>{text2html(m.group(7))}</div>')
        elif m.group(8):
            html.append('<h4>'+text2html(m.group(8))+'</h4>')
    rest=b[pos:].strip()
    if rest: html.append('<p>'+text2html(rest)+'</p>')
    return ''.join(html)
for sm in re.finditer(r'\\section\{(.*?)\}\n(.*?)(?=\\section\{|\Z)',fs,re.S):
    fsecs.append({'n':n,'name':text2html(sm.group(1)),'html':conv_block(sm.group(2))}); n+=1
imgs={}
for f in os.listdir(f'{ROOT}/img'):
    if f.endswith('.png'):
        imgs[f[:-4]]='data:image/png;base64,'+base64.b64encode(open(f'{ROOT}/img/{f}','rb').read()).decode()
import sys as _s; _s.path.insert(0,str(pathlib.Path(__file__).resolve().parent))
from teoria import T as TEO
teoimg={}
for f in os.listdir(f'{ROOT}/img_teo'):
    if f.endswith('.png'):
        teoimg[f[:-4]]='data:image/png;base64,'+base64.b64encode(open(f'{ROOT}/img_teo/{f}','rb').read()).decode()
json.dump({'sections':sections,'formulario':fsecs,'img':imgs,'teo':{str(k):v for k,v in TEO.items()},'teoimg':teoimg},open(f'{ROOT}/build/data.json','w',encoding='utf-8'),ensure_ascii=False)
print(len(sections),sum(len(s['ex']) for s in sections),len(fsecs))
