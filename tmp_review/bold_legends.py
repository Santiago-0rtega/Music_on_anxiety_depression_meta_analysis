from docx import Document
from docx.enum.text import WD_COLOR_INDEX
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from copy import deepcopy

path='review_output/Music_meta_analysis_BiO_formatted.docx'
d=Document(path)
for idx in (138,140,142,144,146,148,150):
    p=d.paragraphs[idx]
    # The first full stop closes the figure number; the next closes its summary sentence.
    stops=0
    for r in list(p.runs):
        source=r.text
        cut=None
        for pos,ch in enumerate(source):
            if ch=='.':
                stops+=1
                if stops==2:cut=pos+1;break
        if cut is None:
            r.bold=True;r.font.highlight_color=WD_COLOR_INDEX.YELLOW
        else:
            rest=source[cut:]
            r.text=source[:cut]
            r.bold=True;r.font.highlight_color=WD_COLOR_INDEX.YELLOW
            if rest:
                new=OxmlElement('w:r')
                if r._r.rPr is not None:
                    props=deepcopy(r._r.rPr)
                    for tag in ('w:b','w:highlight'):
                        for node in props.findall(qn(tag)):props.remove(node)
                    new.append(props)
                t=OxmlElement('w:t');t.text=rest
                if rest.startswith(' ') or rest.endswith(' '):t.set(qn('xml:space'),'preserve')
                new.append(t);r._r.addnext(new)
            break
d.save(path)
