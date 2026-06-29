#!/usr/bin/env python3
"""
Diff NotebookLM's CRIME-Q output against the human gold standard.

Usage:
    python score_notebooklm.py notebooklm_output.txt [Study_ID]

Accepts flexible input: Markdown pipe tables, TSV, or CSV exported from the
NotebookLM Google Sheet workflow. Study segments are detected by known Study_IDs
appearing in the text, the filename, or an optional Study_ID argument. Reports
overall + per-item agreement and every mismatch (gold vs NotebookLM score).
"""
import csv, io, os, sys, re, importlib.util
from collections import defaultdict

spec = importlib.util.spec_from_file_location("gs", "build_gold_standard.py")
gs = importlib.util.module_from_spec(spec); spec.loader.exec_module(gs)
GOLD, ITEMS, ITEM_NAME = gs.A, gs.ITEMS, gs.ITEM_NAME
STUDIES = list(GOLD.keys())
SHORT_TO_STUDY = {
    'Niehues2011': 'Niehues_2011_BCNEURO',
    'Camargo2013': 'Camargo_2013_PSYN',
    'Pangemanan2024': 'Pangemanan_2024_PHJ',
    'Chikahisa2007': 'Chikahisa_2007_BBR',
    'Terzioglu2020': 'Terzioglu_2020_CMJ',
    'Chen2019': 'Chen_2019_BIOMEDRI',
    'Cheng2024': 'Cheng_2024_HLYN',
    'Escribano2014': 'Escribano_2014_APPANBSC',
    'Milbratz2017': 'Milbratz_2017_ALN',
    'Freitas2020': 'Freitas_2020_ECNE',
    'Flores2018': 'Flores_2018_NP',
    'Fu2023': 'Fu_2023_TRANSPSY',
    'Fu2025': 'Fu_2025_TRANSPSY',
    'Krishnamurthy2025': 'Krishnamurthy_2025_INDIANJTRADITKNOW',
    'Ren2024': 'Ren_2024_ASEAN',
    'Saghari2021': 'Saghari_2021_BIOINTERFACE',
    'Li2010': 'Li_2010_BR',
    'Papadakakis2019': 'Papadakakis_2019_BBR',
    'Rizzolo2021': 'Rizzolo_2021_CC',
    'Sampaio2017': 'Sampaio_2017_PSYNEURO',
}
STUDY_ALIASES = {sid: sid for sid in STUDIES}
STUDY_ALIASES.update(SHORT_TO_STUDY)

VALID = {'yes':'Yes','no':'No','partly':'Partly','unclear':'Unclear','na':'NA','n/a':'NA'}

def norm_item(s):
    s = s.upper().replace(' ', '').replace('（','(').replace('）',')')
    m = re.match(r'(\d+)([XYZ])\(?(\d)?\)?', s)
    if not m: return None
    num, lett, sub = m.groups()
    return f"{num}{lett}({sub})" if sub else f"{num}{lett}"

ITEMSET = {norm_item(i): i for i in ITEMS}

def norm_score(s):
    return VALID.get(s.strip().lower().strip('.'), None)

def resolve_study(s):
    return STUDY_ALIASES.get(s.strip())

def norm_score_header(s):
    h = s.strip().upper().replace('ï¼ˆ','(').replace('ï¼‰',')')
    if h in {'STUDY', 'STUDY_ID', 'STUDYID', 'STUDY_TITLE'}:
        return None
    if h.endswith('_JUSTIFICATION') or h.endswith('_VERBATIM'):
        return None
    if h.startswith('ITEM_'):
        h = h[5:]
    if h.endswith('_SCORE'):
        h = h[:-6]
    item = norm_item(h)
    return ITEMSET.get(item)

def split_delimited(line, delimiter):
    try:
        return next(csv.reader(io.StringIO(line), delimiter=delimiter))
    except csv.Error:
        return line.split(delimiter)

def parse_row(line):
    """Parse one Markdown/TSV/CSV row and return (item, score), if present."""
    if '|' in line:
        cells = [c.strip() for c in line.strip().strip('|').split('|')]
    elif '\t' in line:
        cells = [c.strip() for c in split_delimited(line, '\t')]
    elif ',' in line:
        cells = [c.strip() for c in split_delimited(line, ',')]
    else:
        return None, None
    if len(cells) < 2:
        return None, None

    # Handles both 4-column per-study sheets:
    # Item,SCORE,JUSTIFICATION,VERBATIM
    # and wider exports where the first two useful cells are still item/score.
    if cells[0].strip().lower() in {'item', 'study_id', 'study id'}:
        return None, None
    it = norm_item(cells[0])
    sc = norm_score(cells[1])
    return it, sc

def parse_delimited_cells(line):
    if '|' in line:
        return [c.strip() for c in line.strip().strip('|').split('|')]
    if '\t' in line:
        return [c.strip() for c in split_delimited(line, '\t')]
    if ',' in line:
        return [c.strip() for c in split_delimited(line, ',')]
    return None

def parse_wide_delimited(text):
    """Parse wide one-row-per-study TSV/CSV/Markdown tables."""
    out = defaultdict(dict)
    lines = [ln for ln in text.splitlines() if ln.strip()]
    for i, line in enumerate(lines):
        headers = parse_delimited_cells(line)
        if not headers or not headers:
            continue
        if headers[0].strip().lower() not in {'study', 'study_id', 'study id'}:
            continue
        score_cols = [(idx, norm_score_header(h)) for idx, h in enumerate(headers)]
        score_cols = [(idx, item) for idx, item in score_cols if item]
        if not score_cols:
            continue
        for row_line in lines[i + 1:]:
            cells = parse_delimited_cells(row_line)
            if not cells or len(cells) < 2:
                continue
            sid = resolve_study(cells[0])
            if not sid:
                if out:
                    break
                continue
            for idx, item in score_cols:
                if idx < len(cells):
                    sc = norm_score(cells[idx])
                    if sc:
                        out[sid][item] = sc
    return out

def parse_wide_vertical(text):
    """Parse NotebookLM page dumps where table cells appear one per line."""
    out = defaultdict(dict)
    lines = [ln.strip() for ln in text.splitlines() if ln.strip()]
    stop_tokens = {'keep_pin', 'Save to note', 'copy_all', 'thumb_up', 'thumb_down'}
    for start, line in enumerate(lines):
        if line.strip().lower() not in {'study', 'study_id', 'study id'}:
            continue
        first_study = None
        for pos in range(start + 1, len(lines)):
            if resolve_study(lines[pos]):
                first_study = pos
                break
        if first_study is None:
            continue
        headers = lines[start:first_study]
        score_cols = [(idx, norm_score_header(h)) for idx, h in enumerate(headers)]
        score_cols = [(idx, item) for idx, item in score_cols if item]
        if not score_cols:
            continue
        study_positions = []
        for pos in range(first_study, len(lines)):
            sid = resolve_study(lines[pos])
            if sid:
                study_positions.append((pos, sid))
        for n, (pos, sid) in enumerate(study_positions):
            end = study_positions[n + 1][0] if n + 1 < len(study_positions) else len(lines)
            for stop in range(pos + 1, end):
                if lines[stop] in stop_tokens:
                    end = stop
                    break
            values = [v for v in lines[pos:end] if not re.fullmatch(r'\d+', v)]
            for idx, item in score_cols:
                if idx < len(values):
                    sc = norm_score(values[idx])
                    if sc:
                        out[sid][item] = sc
        if out:
            break
    return out

def parse_wide(text):
    out = parse_wide_delimited(text)
    vertical = parse_wide_vertical(text)
    for sid, scores in vertical.items():
        out[sid].update(scores)
    return out

def parse(text, source_name="", forced_study=None):
    """Return {study_id: {item: score}}."""
    wide = parse_wide(text)
    if wide:
        return wide

    # segment by study id occurrences
    hits = []
    for alias, sid in STUDY_ALIASES.items():
        for m in re.finditer(re.escape(alias), text):
            hits.append((m.start(), sid))
        if forced_study in {sid, alias} or sid in source_name or alias in source_name:
            hits.append((0, sid))
    hits.sort()
    out = defaultdict(dict)
    if not hits:
        print("WARNING: no known Study_IDs found in the file. Add a Study_ID header, put the Study_ID in the filename, or pass it as the second argument."); return out
    for i,(pos,sid) in enumerate(hits):
        end = hits[i+1][0] if i+1 < len(hits) else len(text)
        seg = text[pos:end]
        for line in seg.splitlines():
            it, sc = parse_row(line)
            if it not in ITEMSET: continue
            if sc: out[sid][ITEMSET[it]] = sc
    return out

def main():
    if len(sys.argv) < 2:
        print("usage: python score_notebooklm.py <notebooklm_output.txt|csv|tsv> [Study_ID]"); return
    path = sys.argv[1]
    forced_study = sys.argv[2] if len(sys.argv) > 2 else None
    text = open(path, encoding='utf-8-sig').read()
    pred = parse(text, os.path.basename(path), forced_study)

    total=agree=0
    per_item = defaultdict(lambda:[0,0])   # item -> [agree, total]
    mismatches=[]; missing=[]
    for sid in STUDIES:
        for it in ITEMS:
            g = GOLD[sid][it][0]
            p = pred.get(sid,{}).get(it)
            if p is None:
                missing.append((sid,it)); continue
            total+=1; per_item[it][1]+=1
            if p==g: agree+=1; per_item[it][0]+=1
            else: mismatches.append((sid,it,g,p))

    print("="*70)
    print(f"NotebookLM vs gold standard")
    expected = len(pred) * len(ITEMS)
    print(f"Studies parsed: {len(pred)}/{len(STUDIES)} | cells compared: {total}/{expected or 400}")
    if total: print(f"OVERALL AGREEMENT: {agree}/{total} = {100*agree/total:.1f}%")
    print("="*70)
    print("\nPer-item agreement (sorted worst first):")
    for it in sorted(ITEMS, key=lambda i: (per_item[i][0]/per_item[i][1]) if per_item[i][1] else 1):
        a,t = per_item[it]
        if t: print(f"  {it:7s} {ITEM_NAME[it][:34]:34s} {a}/{t} = {100*a/t:3.0f}%")
    print(f"\nMISMATCHES ({len(mismatches)}):  study | item | GOLD vs NotebookLM")
    for sid,it,g,p in mismatches:
        print(f"  {sid:36s} {it:7s} {g:8s} -> {p}")
    missing = [(sid, it) for sid, it in missing if sid in pred]
    if missing:
        print(f"\nNOT PARSED ({len(missing)} cells) — NotebookLM output missing these item rows:")
        bystudy=defaultdict(list)
        for sid,it in missing: bystudy[sid].append(it)
        for sid,its in bystudy.items(): print(f"  {sid}: {', '.join(its)}")

if __name__ == '__main__':
    main()
