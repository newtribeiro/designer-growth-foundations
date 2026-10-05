# Lint report

LINT mode, first full run (2026-10-04). Re-run the automated part with `python3 tools/build.py` (writes `wiki/lint-metrics.json`).

## Summary

| Check | Result |
|---|---|
| Evidence re-verification (19 high-stakes claims) | 18 confirmed · 1 corrected · 0 unverifiable — see `evidence-audit.md` |
| Skill test (4 prompts × 9 rubric items) | ≈90% pass before fixes; defects fixed in this release |
| Contradictions found | 5 → all resolved |
| Weak links (≤ 1 relation) | 44 — mostly principles cited once (informational) |
| Principle names not in `data/psych-principles.json` | 0 |

## Contradictions resolved

1. **Alert token names** differed across modules → canonical `color.alert.warning | caution | advisory`; success/OK in `color.status.*`; brand tokens never alias into `color.alert.*`.
2. **Advisory colour** → any colour except red or green (14 CFR 25.1322); cyan/white kept as a practitioner convention.
3. **Alarm flood threshold** → ≥ 10 alarms in 10 minutes (ISA-18.2, via secondary sources; the standard is paywalled).
4. **uxtools 2024 survey 4.19 vs 3.42** → design-system satisfaction scores, not handoff ratings.
5. **Power pose** → hormone and risk-taking effects failed to replicate (Ranehill et al. 2015); self-reported feelings of power did.

## Coverage by domain

| Domain | Hack Design | uxtools articles | Challenges | Deep modules | Psych anchors | Lineage strands |
|---|---|---|---|---|---|---|
| D1 Visual craft & brand | 14 | 2 | 0 | 3 | 5 | 8 |
| D2 Interaction, motion & prototyping | 9 | 6 | 3 | 2 | 5 | 2 |
| D3 Research & evidence | 9 | 13 | 10 | 0 | 5 | 1 |
| D4 Behaviour & psychology | 4 | 1 | 1 | 1 | 5 | 2 |
| D5 Product thinking, quality & philosophy | 11 | 5 | 0 | 1 | 4 | 4 |
| D6 Systems, structure & platforms | 7 | 3 | 4 | 3 | 5 | 2 |
| D7 Language, communication & facilitation | 1 | 5 | 0 | 1 | 4 | 0 |
| D8 Self, taste & career | 11 | 12 | 0 | 0 | 4 | 2 |
| D9 Emergent media | 2 | 0 | 0 | 1 | 3 | 1 |
| D10 AI-native practice & design ops | 0 | 22 | 0 | 0 | 4 | 0 |

**Findings:** D10 *AI-native practice* has no lineage strand; D7 *Language* has no lineage strand; D3 *Research* is deep in sources but has no deep module.

## Stale-claims register

| Claim | Where | Re-check |
|---|---|---|
| Xbox Accessibility Guidelines version; platform certification requirements | Module G | Yearly |
| Figma features (DTCG import/export, MCP server, Check designs, mode limits) | Module T | Quarterly |
| Style Dictionary version | Module T | Quarterly |
| WCAG 3 status; APCA | Module A | Twice a year |
| ADA Title II deadlines; EAA; ACA regulations | Module A | Twice a year |
| uxtools survey stats and new articles | D10, tooling context | Monthly ingest |
| WebAIM Million figures | Module A | Each spring |
| Prevalence statistics (WHO, Statistics Canada) | Module A | Yearly |

## Next actions

1. Add lineage strands for D7 and D10.
2. Re-fetch "7 Takeaways from the 2020 Design Tools Survey".
3. Next evidence sample: distinctive-asset research in B2B (Module B); Hodent pillars and Quantic Foundry list (Module G); Figma DTCG export status (Module T).
