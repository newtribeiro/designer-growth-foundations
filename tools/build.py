#!/usr/bin/env python3
"""Rebuild the wiki pages, index and semantic mind map from SKILL.md + data files.

Usage:  python3 tools/build.py          (run from the repository root)

Reads   SKILL.md, data/psych-principles.json, library/sources.json, tools/map-template.html
Writes  wiki/*.md (one page per node), wiki/index.md, wiki/lint-metrics.json,
        map/graph.json, map/designer-growth-map.html
"""
import json, os, re, shutil
from collections import defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P = lambda *a: os.path.join(ROOT, *a)
SK = open(P('SKILL.md'), encoding='utf-8').read()
PSY = {p['name']: p for p in json.load(open(P('data/psych-principles.json'), encoding='utf-8'))['principles']}
SRC = json.load(open(P('library/sources.json'), encoding='utf-8'))['items']

nodes, edges = {}, []

def N(i, label, cat, desc='', **kw):
    nodes[i] = dict(id=i, label=label, cat=cat, desc=desc, **kw)

def R(x):
    if x in nodes:
        return x
    c = [k for k in nodes if k.startswith(x)]
    assert len(c) == 1, (x, c)
    return c[0]

def E(a, b, rel):
    edges.append(dict(s=R(a), t=R(b), rel=rel))

# ---------- modes
MODES = [('ASSESS', 'Assess', 'Map skill level per domain on the Dreyfus scale from evidence; pick 3 growth edges.'),
         ('REFLECT', 'Reflect', 'Project debrief: timeline, designer-tendency audit, outcome vs decision quality.'),
         ('LINEAGE', 'Lineage', 'Trace a design move to its historical roots and original intent; build a study set.'),
         ('CURRICULUM', 'Curriculum', '4/8/12-week plan: input + application to real work + spaced review, interleaved.'),
         ('INGEST', 'Ingest', 'Add a source with the shared schema; update index, log, wiki pages and map.'),
         ('QUERY', 'Query', 'Answer from the wiki with citations; file reusable syntheses back as pages.'),
         ('LINT', 'Lint', 'Health-check: contradictions, stale claims, orphans, missing links, evidence, name hygiene.')]
for k, l, d in MODES:
    N('m_' + k, l, 'mode', d)

# ---------- domains (parsed from SKILL.md headings)
DOM = re.findall(r'^### (D\d+) · ([^\n(]+)', SK, re.M)
for k, l in DOM:
    N('d_' + k, f'{k} {l.strip()}', 'domain')

# ---------- deep modules
MOD = [('S', 'Safety-critical & HMI', 'modules/module-s-safety-critical-hmi.md', 'Situation awareness, human error, automation & trust, alarms, high-performance HMI, remote ops.'),
       ('A', 'Accessibility & inclusive design', 'modules/module-a-accessibility.md', 'WCAG 2.2, situational disability, contrast, targets, cognitive & motion, audits, law.'),
       ('T', 'Design systems & tokens', 'modules/module-t-design-tokens.md', 'DTCG 2025.10, tiers, naming, Figma variables & modes, pipeline, governance, lint/CI, agents.'),
       ('B', 'Brand identity', 'modules/module-b-brand-identity.md', 'Distinctive assets, brand architecture, identity systems, brand in product UI, mark stress tests.'),
       ('G', 'Game UX & player psychology', 'modules/module-g-game-ux.md', 'Hodent, SDT, flow, MDA, HUD taxonomy, onboarding, playtesting, game accessibility.')]
for k, l, f, d in MOD:
    N('mod_' + k, f'Module {k} · {l}', 'module', d, file=f)

# ---------- sources
for k, l, d in [('HD', 'Hack Design (68 lessons)', 'hackdesign.org/lessons: mostly 2013, plus 2018 and 2025 lessons.'),
                ('UXT', 'uxtools.co (69 articles)', 'Essays 2025-26 and guides 2020-22.'),
                ('UXC', 'uxtools Challenges (18)', 'Hands-on briefs: Understand, Ideate, Test, Implement.'),
                ('UXS', 'uxtools Surveys', '2024 Design Tools Survey (2,220) and 2026 State of Prototyping (1,478).'),
                ('PSY', 'Psychology principle catalogue', 'growth.design cognitive-bias names (data/psych-principles.json).'),
                ('KW', 'Karpathy · LLM Wiki', 'Raw sources, LLM-maintained wiki, schema; ingest, query, lint; index.md + log.md.')]:
    N('s_' + k, l, 'source', d)

# ---------- learning science
SCI = [('DP', 'Deliberate practice', 'Ericsson et al. 1993: narrow targets, feedback, focused repetition.'),
       ('DD', 'Desirable difficulties', 'Bjork 1994: spacing, interleaving, retrieval.'),
       ('RP', 'Reflective practice', 'Schön 1983: reflection in and on action.'),
       ('KOLB', 'Experiential cycle', 'Kolb 1984: experience, reflect, conceptualise, experiment.'),
       ('DREY', 'Skill stages', 'Dreyfus & Dreyfus 1980: novice to expert.'),
       ('WALLAS', 'Creativity stages', 'Wallas 1926: preparation, incubation, illumination, verification.'),
       ('FLOW', 'Flow', 'Csikszentmihalyi 1990: challenge slightly above skill.'),
       ('TASTE', 'Taste', 'Calibrated pattern library + articulated reasons.')]
for k, l, d in SCI:
    N('sci_' + k, l, 'science', d)

# ---------- tendencies (table in SKILL.md)
tsec = SK[SK.index('| Tendency |'):]; tsec = tsec[:tsec.index('\n\n')]
TEN = {}
for row in tsec.splitlines()[2:]:
    c = [x.strip() for x in row.strip('|').split('|')]
    name = re.sub(r'\*\*(.*?)\*\*.*', r'\1', c[0]).strip()
    tid = 't_' + re.sub(r'\W+', '', name)
    N(tid, name, 'tendency', f'Signal: {c[1]}. Counter: {c[2]}.', grade=c[3].replace('*', ''))
    TEN[tid] = row

# ---------- lineage (table in SKILL.md + module strands)
lsec = SK[SK.index('| Domain / move |'):]; lsec = lsec[:lsec.index('\n\n')]
LIN = {}
for row in lsec.splitlines()[2:]:
    c = [x.strip() for x in row.strip('|').split('|')]
    lid = 'l_' + re.sub(r'\W+', '', c[0])
    N(lid, c[0], 'lineage', f"{c[1].replace('*', '')}. Intent: {c[2]}")
    LIN[lid] = row
for k, l, d in [('HF', 'Human factors & accidents', 'Chapanis & Fitts 1940s, TMI 1979, Therac-25, AF447, 737 MAX (Module S).'),
                ('UD', 'Universal & inclusive design', 'Curb cuts, Section 508, Mace 1997, WCAG 1999-2023, Microsoft Inclusive 2016 (Module A).'),
                ('ID', 'Identity programmes', 'Aicher Lufthansa 1962, Rand IBM, C&G, Unimark 1970, NASA 1975, MIT Media Lab 2011 (Module B).'),
                ('GD', 'Game design & play', 'World 1-1 1985, Bartle 1996, MDA 2004, SDT 2006, Chen 2007, Hodent 2017 (Module G).')]:
    N('l_' + k, l, 'lineage', d)

# ---------- psychology edges from italic names in each section
def italics(txt):
    return {x for x in re.findall(r'(?<!\*)\*([A-Z][^*\n]{2,45}?)\*(?!\*)', txt) if x in PSY}

def Pl(src, txt, rel='explained by'):
    for p in italics(txt):
        pid = 'psy_' + re.sub(r'\W+', '', p)
        if pid not in nodes:
            q = PSY[p]
            N(pid, p, 'psych', f"Principle ({q['cycle']} step).", cluster=q['cluster'], grade=q['grade'], cycle=q['cycle'])
        E(src, pid, rel)

for tid, row in TEN.items(): Pl(tid, row)
for lid, row in LIN.items(): Pl(lid, row, 'kept alive by')
for k, _ in DOM:
    m = re.search(rf'### {k} · .*?(?=\n### |\n\*\*Coverage|\n## )', SK, re.S)
    if m: Pl('d_' + k, m.group(0))
for k, *_ in MOD:
    m = re.search(rf'## Module {k} — .*?(?=\n## )', SK, re.S)
    if m: Pl('mod_' + k, m.group(0))
for k, l, _ in SCI:
    m = re.search(rf'- \*\*{re.escape(l)}\*\*.*', SK)
    if m: Pl('sci_' + k, m.group(0))
for k, *_ in MODES:
    m = re.search(rf'### \d\. {k} — .*?(?=\n### |\n## )', SK, re.S)
    if m: Pl('m_' + k, m.group(0), 'uses')

# ---------- hand-curated semantic edges
HAND = [
 ('mod_S', ['d_D2', 'd_D6'], 'deepens'), ('mod_A', ['d_D1', 'd_D6', 'd_D7'], 'deepens'), ('mod_T', ['d_D6', 'd_D1'], 'deepens'),
 ('mod_B', ['d_D1', 'd_D5'], 'deepens'), ('mod_G', ['d_D4', 'd_D2', 'd_D9'], 'deepens'),
 ('mod_S', ['mod_A'], 'shares situational disability with'), ('mod_S', ['mod_T'], 'reserved alert tokens'), ('mod_T', ['mod_B'], 'brand tokens & alert exclusion'),
 ('mod_A', ['mod_T'], 'contrast-paired tokens'), ('mod_G', ['mod_S'], 'situation awareness'), ('mod_G', ['mod_A'], 'game accessibility'),
 ('s_HD', [f'd_D{i}' for i in range(1, 10)], 'feeds'), ('s_UXT', [f'd_D{i}' for i in [1, 2, 3, 4, 5, 6, 7, 8, 10]], 'feeds'),
 ('s_UXC', ['d_D2', 'd_D3', 'd_D4', 'd_D6'], 'feeds'), ('s_UXS', ['d_D10', 'd_D6'], 'feeds'),
 ('s_PSY', ['m_REFLECT', 'm_LINEAGE', 'm_LINT'], 'names for'), ('s_KW', ['m_INGEST', 'm_QUERY', 'm_LINT'], 'pattern for'),
 ('m_ASSESS', ['sci_DREY', 't_DunningKruger'], 'uses'), ('m_CURRICULUM', ['sci_DP', 'sci_FLOW', 'l_Learningbycopying'], 'uses'),
 ('m_REFLECT', ['sci_RP', 'sci_KOLB', 't_Hindsightbias'], 'uses'), ('m_LINEAGE', ['t_Bandwagon'], 'counters'),
 ('m_CURRICULUM', ['sci_WALLAS', 'sci_DD', 't_Planningfallacy'], 'uses'), ('m_INGEST', ['s_HD', 's_UXT', 's_UXC', 's_UXS'], 'built from'),
 ('m_LINT', ['s_HD', 's_UXT', 't_Confirmationbias'], 'checks'), ('m_QUERY', ['s_HD', 's_UXT'], 'cites'),
 ('sci_TASTE', ['d_D8', 't_Tastegap'], 'relates to'), ('sci_FLOW', ['mod_G'], 'core to'),
 ('l_Typography', ['d_D1'], 'roots of'), ('l_Whitespace', ['d_D1'], 'roots of'), ('l_Grids', ['d_D1', 'd_D6'], 'roots of'),
 ('l_Visualhierarchy', ['d_D1'], 'roots of'), ('l_Colour', ['d_D1'], 'roots of'), ('l_Iconspictograms', ['d_D1'], 'roots of'),
 ('l_Skeuomorphism', ['d_D1', 'd_D2'], 'roots of'), ('l_Supernormal', ['d_D5'], 'roots of'), ('l_Motion', ['d_D2'], 'roots of'),
 ('l_Depth3D', ['d_D9'], 'roots of'), ('l_Datavisualisation', ['d_D1'], 'roots of'), ('l_Systemscomponents', ['d_D6', 'mod_T'], 'roots of'),
 ('l_Humancentreddesign', ['d_D3', 'd_D5'], 'roots of'), ('l_Ethics', ['d_D5', 'd_D4'], 'roots of'), ('l_Behaviourdesign', ['d_D4'], 'roots of'),
 ('l_Process', ['d_D5'], 'roots of'), ('l_Personalstyle', ['d_D8', 'mod_B'], 'roots of'), ('l_Learningbycopying', ['d_D8'], 'roots of'),
 ('l_HF', ['mod_S'], 'roots of'), ('l_UD', ['mod_A'], 'roots of'), ('l_ID', ['mod_B', 'mod_T'], 'roots of'), ('l_GD', ['mod_G'], 'roots of'),
 ('t_Curseofknowledge', ['mod_A', 'mod_S', 'mod_G'], 'risk in'), ('t_Falseconsensus', ['d_D3', 'mod_G'], 'risk in'),
 ('t_Confirmationbias', ['d_D3'], 'risk in'), ('t_IKEA', ['mod_B', 'mod_T'], 'risk in'), ('t_Sunkcost', ['mod_T'], 'risk in'),
 ('t_Aestheticusability', ['d_D1', 'mod_A'], 'risk in'), ('t_Bandwagon', ['mod_B'], 'risk in'), ('t_Survivorship', ['d_D8'], 'risk in'),
 ('t_Satisficing', ['d_D5'], 'risk in'), ('t_Problemsolution', ['d_D5'], 'risk in'), ('t_Phantomcompetency', ['d_D10'], 'risk in'),
 ('t_Artifactseniority', ['d_D8'], 'risk in'), ('t_Nominalpathbias', ['mod_S'], 'risk in'), ('t_Designfixation', ['d_D5', 'sci_WALLAS'], 'risk in'),
 ('t_Primarygenerator', ['d_D5'], 'risk in'), ('t_Einstellung', ['d_D5'], 'risk in'), ('t_LawoftheInstrument', ['d_D3'], 'risk in')]
for a, bs, rel in HAND:
    for b in bs:
        E(a, b, rel)

CATS = [('mode', 'Modes'), ('domain', 'Domains'), ('module', 'Deep modules'), ('tendency', 'Designer tendencies'),
        ('science', 'Learning science'), ('lineage', 'Lineage'), ('psych', 'Psychology principles'), ('source', 'Sources')]
CATN = dict(CATS)
LES = [dict(t=x['title'], u=x['url'], d=x['domain'].split(' ')[0], s='HD' if x['source'] == 'hackdesign.org' else 'UXT', k=x['type']) for x in SRC]
used = {n['label'] for n in nodes.values() if n['cat'] == 'psych'}

# ---------- wiki pages
def slug(n):
    s = re.sub(r'-+', '-', re.sub(r'[^a-z0-9]+', '-', n['label'].lower())).strip('-')[:60]
    return ('tendency-' if n['cat'] == 'tendency' else '') + s
for n in nodes.values():
    n['slug'] = slug(n)
assert len({n['slug'] for n in nodes.values()}) == len(nodes), 'duplicate slugs'
adj = defaultdict(list)
for e in edges:
    adj[e['s']].append((e['rel'], e['t'], 'out')); adj[e['t']].append((e['rel'], e['s'], 'in'))
lk = lambda i: f"[[{nodes[i]['slug']}|{nodes[i]['label']}]]"

keep = {'index.md', 'log.md', 'lint-report.md', 'evidence-audit.md'}
os.makedirs(P('wiki'), exist_ok=True)
for f in os.listdir(P('wiki')):
    if f.endswith('.md') and f not in keep:
        os.remove(P('wiki', f))
for i, n in nodes.items():
    md = [f"---\ntype: {n['cat']}\nid: {i}\n---", f"# {n['label']}", '', f"*{CATN[n['cat']]}*", '']
    if n.get('desc'): md += [n['desc'], '']
    for k, lab in [('grade', 'Evidence'), ('cluster', 'Psych cluster'), ('cycle', 'Decision cycle'), ('file', 'Full module')]:
        if n.get(k): md.append(f"- **{lab}:** {n[k]}")
    g = defaultdict(set)
    for rel, o, d in adj[i]:
        g[rel if d == 'out' else f'← {rel}'].add(o)
    if g:
        md += ['', '## Relations'] + [f"- **{r}:** " + ', '.join(lk(o) for o in sorted(g[r], key=lambda x: nodes[x]['label'])) for r in sorted(g)]
    if i.startswith('d_'):
        code = n['label'].split(' ')[0]; it = [x for x in LES if x['d'] == code]
        md += ['', f'## Source items ({len(it)})', '', '| Title | Source | Type |', '|---|---|---|'] + [f"| [{x['t']}]({x['u']}) | {x['s']} | {x['k']} |" for x in it]
    open(P('wiki', n['slug'] + '.md'), 'w', encoding='utf-8').write('\n'.join(md) + '\n')

idx = ['# Wiki index', '', 'Every wiki page with a one-line summary, then every source item with its canonical title and link. Regenerated by `tools/build.py`.', '',
       f'Pages: {len(nodes)} · Relations: {len(edges)} · Source items: {len(LES)}', '']
for c, cn in CATS:
    ns = sorted([n for n in nodes.values() if n['cat'] == c], key=lambda n: n['label'])
    idx += [f'## {cn} ({len(ns)})', ''] + [f"- {lk(n['id'])} — {(n.get('desc') or '').split('. ')[0][:140]}" for n in ns] + ['']
idx += ['## Source items', '', 'Full table with years: `library/sources-index.md`.', '']
open(P('wiki', 'index.md'), 'w', encoding='utf-8').write('\n'.join(idx))

# ---------- lint metrics
deg = {i: len(adj[i]) for i in nodes}
doms = [k for k in nodes if k.startswith('d_')]
cov = []
for d in sorted(doms, key=lambda x: int(x[3:])):
    code = nodes[d]['label'].split(' ')[0]; it = [x for x in LES if x['d'] == code]
    mods = [o for r, o, dd in adj[d] if o.startswith('mod_')]
    cov.append(dict(d=nodes[d]['label'], hd=sum(x['s'] == 'HD' for x in it), ux=sum(x['s'] == 'UXT' and x['k'] == 'article' for x in it),
                    ch=sum(x['k'] == 'challenge' for x in it), mods=len(mods),
                    psy=sum(1 for r, o, dd in adj[d] if o.startswith('psy_')), lin=sum(1 for r, o, dd in adj[d] if o.startswith('l_'))))
lint = dict(weak=sorted([i for i in nodes if deg[i] <= 1], key=lambda i: (nodes[i]['cat'], nodes[i]['label'])), cov=cov,
            unknownPrinciples=sorted(x for x in re.findall(r'(?<!\*)\*([A-Z][a-z]+(?: [A-Za-z\'-]+)* (?:Effect|Bias|Law|Fallacy))\*(?!\*)', SK) if x not in PSY))
json.dump(lint, open(P('wiki', 'lint-metrics.json'), 'w'), indent=1)

# ---------- map
os.makedirs(P('map'), exist_ok=True)
data = dict(cats=CATS, nodes=list(nodes.values()), edges=edges, lessons=LES, psyUnused=[], psyCount=len(PSY))
json.dump(data, open(P('map', 'graph.json'), 'w', encoding='utf-8'), ensure_ascii=False)
tpl = open(P('tools', 'map-template.html'), encoding='utf-8').read()
html = tpl.replace('__DATA__', json.dumps(data, ensure_ascii=False).replace('</', '<\\/')).replace('__LINT__', json.dumps(lint).replace('</', '<\\/'))
open(P('map', 'designer-growth-map.html'), 'w', encoding='utf-8').write(html)
print(f'{len(nodes)} pages, {len(edges)} relations, {len(LES)} sources, {len(lint["weak"])} weak links, unknown principle names: {lint["unknownPrinciples"]}')
