import re,unicodedata
from pathlib import Path
from docx import Document
from collections import defaultdict

def norm(s):
 s=unicodedata.normalize('NFKD',s.lower())
 return re.findall(r'[a-z0-9]+',s)
def read(path):
 rows=[]
 for line in Path(path).read_text(encoding='utf-8').splitlines():
  m=re.match(r'^\s*(\d+)\s{2,}(.*?)\s*$',line)
  if m and m.group(2).strip():rows.append((int(m.group(1)),m.group(2).strip()))
 return rows
old=read('tmp_review/source_manuscript_current_pages.txt');new=read('tmp_review/formatted_manuscript_pages.txt')
stream=[]
for n,s in new:
 for w in norm(s):stream.append((w,n))
indexes={k:defaultdict(list) for k in (3,4,5,6)}
for k,idx in indexes.items():
 for i in range(len(stream)-k+1):idx[tuple(w for w,n in stream[i:i+k])].append(stream[i][1])
def locate(n):
 arr=[(ln,s) for ln,s in old if ln==n]
 if not arr:return None
 s=arr[0][1];tok=norm(s)
 for k in (6,5,4,3):
  if len(tok)<k:continue
  matches=[]
  for i in range(len(tok)-k+1):matches+=indexes[k].get(tuple(tok[i:i+k]),[])
  if matches:return min(matches,key=lambda a:abs(a-n)),k,s
 return None
D=Document(r'C:\Users\zannt\OneDrive\Papers sub\Biology Open\Music meta\Comments from the Reviewers.docx')
for i,p in enumerate(D.paragraphs):
 if not (p.text.startswith('We ') or p.text.startswith('The revised')):continue
 refs=re.findall(r'\blines?\s+(\d+)(?:\s*[-–]{1,2}\s*(\d+))?',p.text,re.I)
 if refs:
  print('PARA',i)
  for a,b in refs:
   aa=locate(int(a));bb=locate(int(b)) if b else None
   print(' ',a,b,'=>',aa[:2] if aa else None,bb[:2] if bb else None,'OLD',aa[2][:90] if aa else '')
