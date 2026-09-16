import re,unicodedata
from pathlib import Path
from collections import defaultdict
from docx import Document

def norm(s):return re.findall(r'[a-z0-9]+',unicodedata.normalize('NFKD',s.lower()))
rows=[]
for row in Path('tmp_review/formatted_manuscript_pages.txt').read_text(encoding='utf-8').splitlines():
 m=re.match(r'\s*(\d+)\s{2,}(.*)$',row)
 if m and m.group(2).strip():rows.append((int(m.group(1)),m.group(2).strip()))
stream=[]
for ln,s in rows:
 for w in norm(s):stream.append((w,ln))
idx={k:defaultdict(list) for k in range(4,11)}
for k in idx:
 for pos in range(len(stream)-k+1):idx[k][tuple(w for w,n in stream[pos:pos+k])].append((pos,stream[pos][1],stream[pos+k-1][1]))
def find(tokens,side,approx=None):
 for k in range(min(10,len(tokens)),3,-1):
  words=tokens[:k] if side=='start' else tokens[-k:]
  hit=idx[k].get(tuple(words),[])
  if hit:
   if approx is not None:hit=sorted(hit,key=lambda v:abs(v[1]-approx))
   return hit[0][1 if side=='start' else 2],k,len(hit)
 return None
D=Document('review_output/Music_meta_analysis_BiO_formatted.docx')
for i,p in enumerate(D.paragraphs[:155]):
 t=norm(p.text)
 if len(t)<5:continue
 a=find(t,'start');b=find(t,'end',a[0] if a else None)
 print(f'{i:03d} {str(a):20s} {str(b):20s} {p.text[:95]}')
