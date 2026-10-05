# Module T — Modern design systems & tokens

**Why it matters.** Design systems are at the point where a system stops being a Figma library people browse and becomes a **machine-readable source of truth** that code, linters and AI agents use directly. The stakes are high in operational and safety-critical UIs. If an agent or developer picks "a red" instead of `color.alert.warning`, that's a safety defect, not a cosmetic one.

**The shift.** A component library = pictures plus guidance that people interpret. A modern system = **named decisions (tokens) + components + rules a machine can check**. The UX Tools article "Design debt at machine speed" (Tommy Geoco, Mar 2026) makes the case: agents have no judgement of their own, so a system has to be enforced with lintable docs, custom lint rules, pre-commit hooks and CI gates, or inconsistency grows "at machine speed". The baseline is already poor. In the UX Tools 2024 survey (2,220 respondents), designers rate design-system satisfaction **4.19/5** and developers **3.42/5**. **46.3%** report significant spec-vs-implementation inconsistencies, and a spec takes **3.7 weeks** on average to become an implemented component. *(Strong as survey data; self-report.)*

Evidence grades: **Strong** = standard/spec/primary docs · **Moderate** = well-documented industry practice · **Practitioner** = expert opinion/case experience · **Contested** = active disagreement.

---

## 1. Lineage

| Year | Event / work | What it taught |
|---|---|---|
| 1964 | Karl Gerstner, *Designing Programmes* | Design rules, not one-off layouts: a "programme" generates solutions |
| 1965 | Unimark International founded (Vignelli, Noorda et al.) | Corporate identity run as a systematic, rule-bound practice |
| 1975 | NASA Graphics Standards Manual (Danne & Blackburn) | Standards manuals as governance: one mark, strict rules, many applications |
| 1977 | Alexander et al., *A Pattern Language* | Named, linked patterns as a shared vocabulary; naming is the system |
| 2011 | Bootstrap released (Twitter) | Shared CSS/components spread one consistent UI vocabulary across the web |
| 2013 | Brad Frost, "Atomic Design" | A composition hierarchy (atoms → pages) to reason about components |
| c. 2014 | "Design tokens" coined at Salesforce by Jina Anne & Jon Levine (Lightning Design System, public 2015) | Name design decisions and distribute them to every platform from one source |
| 2014 | Google Material Design | A public, opinionated system with motion, elevation and colour rules |
| 2015 | Nathan Curtis, "Team Models for Scaling a Design System" | Governance is an org-design problem (solitary/centralized/federated) |
| c. 2017 | Amazon open-sources Style Dictionary | Token build pipeline: one JSON source → many platform outputs |
| 2020 | Curtis, "Naming Tokens in Design Systems" | A naming taxonomy (namespace / object / base / modifier) |
| 2023 (Config, June) | Figma Variables: collections, modes, aliasing, scoping | Tokens become native objects in the design tool |
| 2025 (June) | Figma Dev Mode MCP server (beta) | Agents can read design context and variables directly |
| 2025-10-28 | DTCG Design Tokens Format Module **2025.10**, first stable version | A vendor-neutral interchange format for tokens |
| 2025 (Schema) | Figma: native DTCG import/export, extended collections, MCP server GA, "Check designs" linter | Design tool aligns with the standard; system linting moves into Figma |

*Grades: dates for DTCG, Figma Schema 2025 and Curtis articles are Strong; Salesforce "c. 2014" and Style Dictionary "c. 2017" are Moderate (secondary sources).*

---

## 2. Knowledge base

### 2.1 Token anatomy & DTCG syntax (Strong — DTCG 2025.10)
- A token is a JSON object with **`$value`** (required), **`$type`**, **`$description`**, **`$extensions`** (vendor data, reverse-domain keys; tools must keep it), **`$deprecated`** (bool or reason string).
- **Groups** are nested objects. `$type` set on a group is inherited by its tokens. `$root` names a group's base token, and `$extends` lets one group inherit another.
- **Aliases**: `"{group.token}"` resolves to the whole `$value`, while `"$ref": "#/json/pointer"` reaches inside one. Reference chains are fine; circular references are not.
- Names may not start with `$` or contain `{ } .`.
- **Types.** Primitive: color, dimension, fontFamily, fontWeight, duration, cubicBezier, number. Composite: border, strokeStyle, shadow, transition, gradient, typography.
- Colour values are objects (`colorSpace`, `components`, optional `alpha`, `hex` fallback); oklch and Display P3 are supported. File extension `.tokens` / `.tokens.json`; media type `application/design-tokens+json`.

```json
{
  "color": {
    "$type": "color",
    "red":   { "600": { "$value": { "colorSpace": "srgb", "components": [0.77, 0.11, 0.11], "hex": "#c41c1c" } } },
    "amber": { "500": { "$value": { "colorSpace": "srgb", "components": [0.96, 0.62, 0.04], "hex": "#f59e0b" } } },
    "alert": {
      "$description": "RESERVED. Safety semantics only. Never alias brand colours here.",
      "warning": { "$value": "{color.red.600}",   "$description": "Immediate action / hazard" },
      "caution": { "$value": "{color.amber.500}", "$description": "Abnormal, needs attention" }
    }
  },
  "space": { "$type": "dimension", "200": { "$value": { "value": 8, "unit": "px" } } }
}
```

### 2.2 Tiers (Moderate — industry consensus, naming varies)
| Tier | Example | Who references it |
|---|---|---|
| Primitive / global / reference | `color.red.600` | Only semantic tokens |
| Semantic / alias / system | `color.alert.warning`, `color.text.default` | Components and screens |
| Component | `button.primary.bg` | One component |
Rule: **product UI never references primitives**. Component tokens are optional. Add them only once a component needs them (Curtis: "start within, then promote across").

### 2.3 Naming (Practitioner — Curtis 2020)
Order: **namespace** (system/theme/domain) → **object** (component/element) → **base** (category · concept · property) → **modifier** (variant · state · scale · mode). Example: `ds.color.feedback.text.warning.hover`. Avoid homonyms such as `type`. Include only the levels you need. Name by **purpose**, not by appearance.

### 2.4 Modes, theming, multi-brand (Strong for Figma features; Moderate for practice)
- Figma Variables: **collections** contain **modes** (e.g. light/dark), variables can **alias** other variables, and **scoping** limits where a variable shows up in pickers. Mode limits were raised at Schema 2025 (Pro 10, Org 20 per collection).
- **Extended collections** (Schema 2025, Enterprise) let a core system be extended with brand themes. This suits a core system with several brands.
- For multi-brand work, swap **primitives/brand** values per theme and keep **semantic names stable**. Alert semantics stay identical across all brands.

### 2.5 Safety-critical alert tokens (Practitioner + Strong regulatory convention)
- Reserve **red = warning**, **amber = caution** (advisory: any colour except red or green per 14 CFR 25.1322; cyan/white is a common practitioner convention). Success/OK states go in `color.status.*`, never in `color.alert.*`. These colour conventions come from aviation cockpit alerting.
- **Never alias a brand colour to an alert role**, and never use alert tokens decoratively. If a brand red is close to warning red, change the brand usage instead.
- Alerts never rely on colour alone. Pair them with icon + text + position + (for warnings) sound/flash.
- Lint for it: forbid `color.alert.*` outside alert components, and forbid primitives that share a hue with alert colours in non-alert contexts.
- Dark and low-luminance modes need their own alert values that are dimmed but still told apart. Don't just invert.

### 2.6 Accessibility tokens (Strong — WCAG 2.2)
- Publish **contrast-paired fg/bg tokens** (`text.on-warning` next to `bg.warning`) and test each pair: 4.5:1 for text, 3:1 for UI components and focus indicators.
- Add `focus.ring.color/width/offset` tokens, minimum target-size tokens, and `motion.reduced` alternatives.

### 2.7 Spacing, typography, motion (Strong for syntax)
- Spacing: a dimension scale (4/8-based). Typography: DTCG composite `typography` tokens (family, size, weight, lineHeight, letterSpacing). Motion: `duration` plus `cubicBezier`, or the composite `transition`.

### 2.8 Pipeline (Moderate)
**Figma Variables → DTCG JSON** (native export rolling out since Schema 2025, or the Tokens Studio plugin) → **Git repo** (review + semver) → **Style Dictionary v5** (DTCG-aligned reference syntax; Node ≥22) → CSS custom properties / Swift / Android XML/Compose / TS. *Native export gaps reported in 2026: descriptions dropped, composite tokens lagging (Practitioner).*

### 2.9 Governance & contribution (Practitioner)
- Curtis's team models: **solitary** (one product team's system, offered to others), **centralized** (a dedicated team), **federated** (designers from product teams decide together). For a small-to-mid-size product company, a realistic setup is a small core owner (one senior designer) with federated contributors from each product area (e.g. each product and the marketing site).
- Brad Frost and Dan Mall (*Design That Scales*) both stress an explicit contribution path: propose → triage → pilot in product → promote into the system.

### 2.10 Adoption metrics (Moderate)
- Figma **library analytics** (component/variable insertions, detaches), code-scanning tools such as **Omlet** (component usage in React repos), **token coverage** (% of style declarations that use tokens rather than raw values), and lint-violation trends.
- Figma's **Check designs** linter (Schema 2025, early access) matches raw values to variables before handoff.

### 2.11 AI and agents consuming the system (Strong for tools, Practitioner for outcomes)
- The Figma MCP server (Dev Mode MCP beta June 2025, GA at Schema 2025) gives agents variables, components and Code Connect mappings. Schema 2025 added design-system **guidelines for AI**.
- Agents follow what they can parse. That means DTCG files, `$description` on every semantic token, Code Connect, and lint rules in CI. Prose guidelines alone don't constrain them.

---

## 3. Methods

| Method | How | Grade |
|---|---|---|
| Token audit | Grep code and inspect Figma for raw hex/px/ms. Group the hits, map each to an existing token or flag a missing one. Track coverage % | Moderate |
| Naming workshop | Card-sort the audit results into Curtis levels. Agree on the order and banned words. Write the result down as a lint config | Practitioner |
| Deprecation policy | Mark tokens with `$deprecated: "Use {x}"`, keep an alias for ≥1 minor release, remove at the next major. Codemod when possible | Strong (syntax) / Practitioner |
| Versioning | **Semver**: rename/remove = major, new token = minor, value tweak = patch (a *safety* colour value change gets a review even when it's a patch) | Moderate |
| Release notes | Changelog per release (Changesets or conventional commits). Include before/after swatches | Moderate |
| Lint rules | stylelint built-in `color-no-hex`; `stylelint-declaration-strict-value`; Atlassian's `@atlaskit/eslint-plugin-design-system` (`ensure-design-token-usage`) as a model; Mozilla's `use-design-tokens` stylelint rule | Strong (tools exist) |
| Visual regression | Storybook + **Chromatic** (or Playwright screenshots) on every token release. Test all modes | Moderate |
| Docs | zeroheight, Supernova, or Storybook docs generated from the token source, so the docs can't drift from it | Moderate |

---

## 4. Pattern checklist — your design system

- [ ] One token source in Git as DTCG 2025.10 JSON, with Figma Variables synced to it
- [ ] Three tiers in place, with no primitives referenced in product files or code
- [ ] `color.alert.warning` (red) / `color.alert.caution` (amber) reserved and documented as safety semantics
- [ ] No brand or sub-brand colour aliased to an alert role. A lint rule enforces it
- [ ] Every alert also has an icon, a text label and an a11y-paired `on-*` token
- [ ] Modes: light, dark and high-contrast, tested with users
- [ ] Contrast pairs auto-checked in CI (4.5:1 text, 3:1 non-text/focus)
- [ ] Focus, target-size and reduced-motion tokens
- [ ] Typography and spacing scales as tokens. Icon sizes and strokes tokenised
- [ ] Naming convention written down, with banned terms (no `blue-500` in semantic slots)
- [ ] `$description` on every semantic token, written for humans and agents
- [ ] Semver, changelog and a deprecation window
- [ ] Style Dictionary outputs for every platform you ship (web, desktop, mobile)
- [ ] Lint + visual regression gates in CI
- [ ] Figma library analytics and token-coverage % reviewed monthly
- [ ] Contribution path and a named owner per area
- [ ] MCP/Code Connect mapped so agents get the system, not screenshots

---

## 5. Designer tendencies that break systems

| Tendency | What happens | Psychology link | Counter |
|---|---|---|---|
| Naming by value (`blue-500` used for "primary action") | A rebrand or dark mode breaks the meaning | **Mental Model** (name ≠ intent) | Semantic tier + lint |
| One-off detaches / "just this once" hex | Drift. The agent copies it 100× | **Default Bias** (the easy path wins) | Make the token the default; Check designs |
| Gold-plating tokens (500 tokens on day 1) | Nobody can find the right one | **Cognitive Load**, **Chunking** | Start small, promote on second use |
| Using brand red for alerts "because it's close" | Safety meaning is lost | **Law of Similarity** (similar colour reads as the same meaning) | Reserved alert tier |
| Pushing all complexity onto consumers | Every team re-solves states and modes | **Tesler's Law** (complexity has to live somewhere: put it in the system) | Component tokens own the states |
| System as a side project | Docs drift, trust falls | **Sunk Cost Effect** (keep patching the old kit) | Roadmap + metrics + versioned releases |
| Documentation drift | Figma ≠ code ≠ docs | **Cognitive Load** | Generate docs from the token source |
| Not-Invented-Here / over-loving your own kit | Rejecting standards (DTCG) or contributions | **IKEA Effect** | Adopt the spec; federated review |
| Everything becomes a token (or a component) | Over-abstraction | **Law of the Instrument** | Tokenise repeated *decisions* only |

*Grade: Practitioner (mechanisms are Strong in psychology; their application to design systems is expert judgement).*

---

## 6. Reading list (ranked)

1. **DTCG Design Tokens Format Module 2025.10**: https://www.designtokens.org/tr/2025.10/format/
2. **Nathan Curtis — Naming Tokens in Design Systems** (2020): https://medium.com/eightshapes-llc/naming-tokens-in-design-systems-9e86c7444676
3. **UX Tools — Design debt at machine speed** (2026): https://www.uxtools.co/blog/design-debt-at-machine-speed
4. **Nathan Curtis — Team Models for Scaling a Design System** (2015): https://medium.com/eightshapes-llc/team-models-for-scaling-a-design-system-2cf9d03be6a0
5. **Style Dictionary docs (v5)**: https://styledictionary.com/
6. **Figma — Schema 2025 design-systems recap**: https://www.figma.com/blog/schema-2025-design-systems-recap/
7. **Atlassian — Use tokens in code / ESLint plugin**: https://atlassian.design/foundations/tokens/use-tokens-in-code
8. **UX Tools 2024 survey — Design Systems**: https://www.uxtools.co/survey/design-systems/overview
9. **Brad Frost — Atomic Design** (free online book): https://atomicdesign.bradfrost.com/
10. **Dan Mall — *Design That Scales*** (Rosenfeld, 2023)

---

## Sources
- https://www.designtokens.org/ (first stable version 2025.10, 28 Oct 2025)
- https://www.designtokens.org/tr/2025.10/format/
- https://www.designtokens.org/tr/2025.10/color/
- https://www.w3.org/community/design-tokens/2026/06/17/thank-you-jina-and-val/ (Jina Anne & Jon Levine coined the term at Salesforce)
- https://styledictionary.com/versions/v5/migration/
- https://github.com/style-dictionary/style-dictionary/releases
- https://help.figma.com/hc/en-us/articles/35794667554839-What-s-new-from-Schema-2025
- https://www.figma.com/blog/schema-2025-design-systems-recap/
- https://dev.to/slafleche/even-figma-isnt-sure-about-its-own-design-tokens-4mko
- https://alternativeto.net/news/2025/6/figma-launches-dev-mode-mcp-server-for-direct-ai-access-to-design-data
- https://www.uxtools.co/blog/design-debt-at-machine-speed
- https://www.uxtools.co/survey/design-systems/overview
- https://uxtools.co/survey/
- https://medium.com/eightshapes-llc/naming-tokens-in-design-systems-9e86c7444676
- https://medium.com/eightshapes-llc/team-models-for-scaling-a-design-system-2cf9d03be6a0
- https://atlassian.design/components/eslint-plugin-design-system/ensure-design-token-usage
- https://firefox-source-docs.mozilla.org/code-quality/lint/linters/stylelint-plugin-mozilla/rules/use-design-tokens.html
