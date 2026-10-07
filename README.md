# Designer Growth Foundations

**[Open the interactive mind map →](https://newtribeiro.github.io/designer-growth-foundations/)**

A Claude skill for getting better **as a designer**, not just making a better design. It assesses skill level from evidence, plans learning cycles, debriefs projects for designer biases, traces design choices back through art and design history, and goes deep in five areas: safety-critical & HMI, accessibility, design tokens, brand identity and game UX.

The knowledge base follows Andrej Karpathy's [LLM Wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) pattern: raw sources → an interlinked wiki the model maintains → a schema (`SKILL.md`), with **ingest**, **query** and **lint** operations, an `index.md` and an append-only `log.md`.

## What's inside

| Path | What |
|---|---|
| `SKILL.md` | The skill: 7 modes (Assess, Reflect, Lineage, Curriculum, Ingest, Query, Lint), 10 competency domains, designer-bias table, learning science, lineage table, condensed deep modules, output conventions |
| `modules/` | Five deep modules (S safety-critical & HMI · A accessibility · T design tokens · B brand identity · G game UX), each with lineage, graded knowledge, methods, checklist, designer traps and sources |
| `wiki/` | 140 Obsidian-compatible pages with `[[wikilinks]]`, `index.md`, `log.md`, `lint-report.md`, `evidence-audit.md` |
| `index.html` | Interactive semantic mind map, also the [project site](https://newtribeiro.github.io/designer-growth-foundations/): radial graph, coverage matrix, cross-check panel, index |
| `library/` | Index of all 156 sources (68 Hack Design lessons, 69 uxtools.co articles, 18 challenges, 1 survey report) with canonical titles and links |
| `data/psych-principles.json` | The 61 psychology principle names the skill uses, with cluster, decision-cycle step and evidence grade |
| `tools/build.py` | Rebuilds the wiki pages, index and mind map from `SKILL.md` and the data files (Python 3, no dependencies) |

## Install

**Claude Code:** copy this folder to `~/.claude/skills/designer-growth-foundations/` (or `.claude/skills/` inside a project). The skill loads when a request matches its description.

**Claude apps:** zip the folder (with `SKILL.md` at the top level) and upload it as a custom skill in your settings.

### Make it yours

The skill is written for any mid-level to senior product designer. Tell Claude about your current work — the products you design, the systems you own, brand or side projects — in your own `CLAUDE.md`, project notes or memory. The skill asks for this context and ties its advice to it.

## Try it

- "Assess my skills from these three case studies."
- "Debrief my last logo project — I fell in love with the first sketch."
- "Where does the flat, grid-heavy dashboard look come from?"
- "Give me a 4-week plan for accessibility and design tokens."
- "Lint the knowledge base."

## Rebuild the wiki and map

```bash
python3 tools/build.py
```

Edit `SKILL.md` (domains, tendencies, lineage, modules) or the data files, then rebuild. Add a dated line to `wiki/log.md` and an entry to `CHANGELOG.md`.

## Evidence policy

Every research claim carries a grade: **Strong** (replicated research, standards), **Moderate**, **Practitioner** (expert practice, case evidence) or **Contested**. `wiki/evidence-audit.md` records the last re-verification of 19 high-stakes claims against primary sources; `wiki/lint-report.md` keeps a stale-claims register. Legal and platform-policy notes (accessibility law, platform terms) are design constraints, **not legal advice**.

## Sources and attribution

- [Hack Design](https://www.hackdesign.org/lessons/) — 68 curated lessons by their respective instructors.
- [UX Tools](https://www.uxtools.co/) — articles, challenges and surveys by Tommy Geoco, Taylor Palmer, Jordan Bowman and team.
- [growth.design](https://growth.design/psychology) — names of the cognitive biases and UX principles referenced.
- Module sources are cited inline in each module file.

This repository contains **an index and original synthesis only**. Lessons, articles and survey reports belong to their authors — follow the links to read them. The INGEST mode can rebuild full-text study notes locally in `library/local/`, which is git-ignored and should not be redistributed.

## License

- **Content** — `SKILL.md`, `modules/`, `wiki/`, `library/`, `data/` and the mind map's text: [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/) — see `LICENSE`. You may share and adapt it for any purpose, including commercially, as long as you give appropriate credit, link to the license and indicate if changes were made.
- **Code** — `tools/build.py`, `tools/map-template.html` and the script in `index.html`: [MIT](https://opensource.org/license/mit) — see `LICENSE-CODE`.

Third-party lessons, articles and surveys linked from this repository remain under their owners' terms and are not covered by these licenses.
