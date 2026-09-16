from copy import deepcopy
import re
from docx import Document
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

path='review_output/Music_meta_analysis_BiO_formatted.docx'
d=Document(path)
name=r"[A-Z][A-Za-zÀ-ÖØ-öø-ÿ'’\-]+"
pattern=re.compile(rf'(?<![\w,])({name}(?:\s+(?:and|&)\s+{name})?(?:\s+et al\.)?)\s+((?:19|20)\d{{2}}[a-z]?)\b')

def insert_like(run, value, anchor, mark):
    node=OxmlElement('w:r')
    if run._r.rPr is not None: node.append(deepcopy(run._r.rPr))
    if mark:
        props=node.find(qn('w:rPr'))
        if props is None: props=OxmlElement('w:rPr'); node.insert(0,props)
        hi=props.find(qn('w:highlight'))
        if hi is None: hi=OxmlElement('w:highlight');props.append(hi)
        hi.set(qn('w:val'),'yellow')
    t=OxmlElement('w:t');t.text=value
    if value.startswith(' ') or value.endswith(' '):t.set(qn('xml:space'),'preserve')
    node.append(t);anchor.addnext(node)
    return node

count=0
for p in d.paragraphs[:151]:
    for r in list(p.runs):
        src=r.text
        ms=list(pattern.finditer(src))
        if not ms:continue
        r.text=src[:ms[0].start()]
        anchor=r._r;pos=ms[0].start()
        for m in ms:
            if m.start()>pos:anchor=insert_like(r,src[pos:m.start()],anchor,False)
            anchor=insert_like(r,m.group(1)+', '+m.group(2),anchor,True)
            pos=m.end();count+=1
        if pos<len(src):insert_like(r,src[pos:],anchor,False)
d.save(path)
print('Formatted citations:',count)
