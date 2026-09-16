from pathlib import Path
import re, unicodedata
from docx import Document
B=Path(r'C:\Users\zannt\OneDrive\Papers sub\Biology Open\Music meta\New folder\refs.bib').read_text(encoding='utf-8-sig')
blocks=re.split(r'(?m)(?=^@\w+\{)',B)
def fields(block):
 m=re.match(r'@(\w+)\{([^,]+),',block); typ,key=m.groups(); s=block[m.end():]; d={'type':typ,'key':key}
 i=0
 while i<len(s):
  m=re.search(r'([A-Za-z_-]+)\s*=\s*',s[i:]);
  if not m: break
  name=m.group(1).lower(); i+=m.end(); q=s[i:i+1]
  if q=='{':
   depth=1; j=i+1
   while j<len(s) and depth:
    if s[j]=='{':depth+=1
    elif s[j]=='}':depth-=1
    j+=1
   val=s[i+1:j-1]; i=j
  elif q=='"':
   j=s.find('"',i+1); val=s[i+1:j];i=j+1
  else:
   m2=re.match(r'([^,}\n]+)',s[i:]);val=m2.group(1).strip() if m2 else '';i+=len(m2.group(0)) if m2 else 1
  d[name]=val
 return d
entries=[]
for x in blocks:
 if x.startswith('@'):
  try: entries.append(fields(x))
  except Exception as e: print('PARSE',x[:60],e)
d=Document(r'C:\Users\zannt\OneDrive\Papers sub\Biology Open\Music meta\Music_meta_analysis_revised.docx')
refs=[p.text for p in d.paragraphs[156:]]
def norm(s):return re.sub(r'[^a-z0-9]+','',unicodedata.normalize('NFKD',s).lower())
used=[];missing=[];dupes=[]
for r in refs:
 year=re.search(r'\b(19|20)\d{2}\b',r)
 first=norm(r.split(',')[0])
 cand=[e for e in entries if norm(e.get('author','').split(',')[0])==first and e.get('year')==(year.group(0) if year else '')]
 if len(cand)==1:used.append(cand[0]['key'])
 elif len(cand)==0:missing.append(r[:90])
 else:dupes.append((r[:60],[e['key'] for e in cand]))
print('entries',len(entries),'refs',len(refs),'unique_matches',len(used),'missing',len(missing),'dupes',len(dupes))
print('MISSING',*missing,sep='\n')
print('DUPES',*dupes,sep='\n')
