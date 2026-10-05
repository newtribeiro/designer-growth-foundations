# Module B — Brand identity

**Why it matters.** A brand is how people recognise and trust a product before they use it. The same skills cover a company identity, a product brand inside a larger portfolio, client work and a studio's own identity.

**The shift:** stop treating the job as *logo-making* and start building **distinctive, governable assets**: a small set of elements (mark, colour, type, shape, motion, sound) that buyers can recognise without the name present, that survive a 16px favicon, a monochrome print and an embroidered shirt, and that are coded as tokens so the product UI and any generated interface stay on-brand. Brand colours should stay distinct from semantic UI colours (error red, warning amber), and brand tokens never alias into `color.alert.*` or `color.status.*`.

Evidence grades: **Strong** (replicated peer-reviewed), **Moderate** (peer-reviewed, limited/contextual), **Practitioner** (expert consensus or case evidence), **Contested** (credible disagreement or claims extended beyond their evidence).

---

## 1. Lineage table

| Year | Event/work | What it taught |
|---|---|---|
| 1956 / 1972 | Paul Rand: IBM logo (City Medium, 1956), then the striped 8-bar version (1972) | Evolve the mark, don't replace it. Continuity is an asset. One IBM exec said the stripes reminded him of a "Georgia chain gang", so expect early resistance |
| 1960 | Chermayeff & Geismar: Chase Manhattan octagon | An abstract mark picks up meaning through exposure. Executives who resisted it were wearing it on cufflinks within months |
| 1962 | Otl Aicher: Lufthansa (crane, lowercase Helvetica Bold, yellow RAL 1028) | A whole system (livery, type, colour) is the identity, not just the mark |
| 1964 | C&G: Mobil (red "o") | One letter carrying colour can be the distinctive asset |
| 1970 | Vignelli & Noorda (Unimark): NYCTA Graphics Standards Manual | Wayfinding-grade rules: the guidelines are part of the design |
| 1975 | Danne & Blackburn: NASA Graphics Standards Manual ("worm") | Treat the manual as a product. The worm was retired in 1992 and came back as a secondary mark in 2020, so retired assets keep their equity |
| 1983 | Saul Bass: AT&T globe (after the Bell breakup) | A mark can carry a corporate transition. Christian Annyas's blog claim that a Bass logo lasts 34 years on average is **Practitioner** (one blogger's count, not a study) |
| 1991 | Rand, "Logos, Flags, and Escutcheons" (AIGA) | "A logo derives its meaning from the quality of the thing it symbolizes, not the other way around." |
| 1997 | Aaker, "Dimensions of Brand Personality" (JMR) | Five dimensions: sincerity, excitement, competence, sophistication, ruggedness |
| 2000 | Aaker & Joachimsthaler, "The Brand Relationship Spectrum" (CMR) | Branded house ↔ house of brands, with endorsed and sub-brand options in between |
| 2003/05 | Neumeier, *The Brand Gap* | A brand is "a person's gut feeling about a product, service, or company" |
| 2010 | Sharp, *How Brands Grow* (Ehrenberg-Bass) | Growth comes from mental and physical availability, and distinctive assets build mental availability |
| 2010–11 | MIT Media Lab algorithmic identity (TheGreenEyl, E Roon Kang): 40,000 forms × 12 colourways | Dynamic identities are possible |
| 2012 | Labrecque & Milne, "Exciting red and competent blue" (JAMS 40:5) | Hue, saturation and value shift perceived brand personality and purchase intent |
| 2014 | Pentagram (Bierut, Fay): MIT Media Lab on a 7×7 grid, with glyphs for 23 groups | Even dynamic systems need a fixed core. Flexibility belongs at the edges |
| 2016 | Michael Johnson, *Branding: In Five and a Half Steps* | The "half step" is turning strategy into design |
| 2018 | Lufthansa drops yellow for blue | Critics called it "bland and pointless". Removing a famous asset is a cautionary tale |
| 2018 | Romaniuk, *Building Distinctive Brand Assets* (OUP) | The Fame × Uniqueness grid for measuring assets |
| 2021–23 | B2B Institute × Ehrenberg-Bass, *How B2B Brands Grow* | The 95-5 rule: up to 95% of B2B buyers are out-of-market at any given time |
| 2024 | Wheeler & Meyerson, *Designing Brand Identity* **6th ed.** (Wiley) | Five phases: research, strategy, identity, touchpoints, asset management |
| 2025–26 | uxtools: "Brand as Product's Secret Weapon" (Apr 2025), "7 Changes in Brand World-Building" (Sep 2026) | Brand now lives inside generated interfaces, sound and motion |

## 2. Knowledge base

### 2.1 What a brand is
- **Neumeier:** a brand is a gut feeling held by *other people*. "It's not what you say it is. It's what they say it is." His five disciplines are differentiate, collaborate, innovate, validate, cultivate. *Practitioner.*
- **Wheeler & Meyerson (6th ed., 2024):** a five-phase process.
  1. Conducting research
  2. Clarifying strategy
  3. Designing identity
  4. Creating touchpoints
  5. Managing assets

  A product designer's leverage is in phases 1 and 5. Designers tend to skip both.
- **Johnson (2016):** investigation → strategy & narrative → *the half-step* → design → implementation → engagement.
- **Rand:** the mark only reflects quality. A mark earns its meaning from the quality of what it represents.

### 2.2 Distinctive assets & mental availability: **Moderate (FMCG) / Contested (B2B transfer)**
- **Mental availability** means being "easily thought of in buying situations". **Distinctive assets** are the non-name cues (colour, shape, logo, character, sound) that trigger the brand.
- **Romaniuk grid.** Test the asset with the brand name hidden, then plot two measures:
  - **Fame:** the % of category buyers who link the asset to your brand.
  - **Uniqueness:** your share of all brand attributions for that asset.

| Fame \ Uniqueness | High uniqueness | Low uniqueness |
|---|---|---|
| **High fame** | Core asset: protect it and use it everywhere | Shared category cue: pair it with something unique or you help competitors |
| **Low fame** | Emerging asset: invest in it and show it next to proven assets | Not an asset: redesign or retire |

- **Grade rationale:** the evidence base is large Ehrenberg-Bass empirical work, mostly in consumer goods. The B2B Institute reports carry the ideas into B2B (95-5 rule, category entry points), but they are institute-published, not independently replicated.
- **Implication for a small brand:** it can't buy fame. Pick one or two assets and use them consistently at every touchpoint.

### 2.3 Brand architecture
| Model | Example pattern | When it fits |
|---|---|---|
| Branded house | "Parent Product", parent dominant | Best when trust transfers from the parent |
| Endorsed brand | "Product, by Parent" | Gives the product its own personality while keeping the parent's assurance |
| Sub-brand | Co-driver mark | Use when the product needs a distinct segment story |
| House of brands | Parent invisible | Only if the product must be distanced, e.g. a different channel or risk profile |

**Rule:** decide the architecture *before* drawing the mark. It sets lockups, the colour hierarchy and naming rules. (Aaker & Joachimsthaler 2000; *Practitioner/Moderate*.)

### 2.4 Identity system components
| Component | Governable spec | Note |
|---|---|---|
| Mark (symbol + wordmark + lockups) | Clear space, min size, approved lockups | A simplified version for small sizes, embroidery and etching |
| Typography | Primary + UI fallback, numerals | Tabular figures for data-heavy UI |
| Colour | Brand palette **plus a reserved-semantic exclusion zone** | Brand hues kept distinct from error and warning colours |
| Shape/graphic device | Grid, angle, pattern | Can echo the product's form |
| Motion | Easing, duration, logo reveal | Matches the brand's personality |
| Sound | Start-up chime, alert ≠ brand sound | uxtools 2026: "Sound is brand", and sound now belongs in brand documentation |
| Voice | Tone ladder: marketing → docs → error copy | Errors are factual, never cute |
| Imagery | Photography rules | Real people and real use |
| Data/UI | Design tokens (`brand.*` vs `color.alert.*` / `color.status.*`) | Brand tokens can never be aliased into `color.alert.*` |

### 2.5 Brand in product UI & generated interfaces (*Practitioner*)
- uxtools (Geoco, 2025): products are converging on the same look, so brand is the differentiator. Start from words, story and emotion before visuals, and treat brands as "seasonal" systems: a stable core with evolving expression. "The strongest outcomes still come from people who know what they're trying to say." (Phi Hoang, Perplexity)
- uxtools (Geoco, 2026): "Interfaces get generated, not coded". "Mixed media has to land in a product". "Your brand has to hold up while strangers are driving it."
- **Implication:** an AI or a developer can only stay on-brand if the brand exists as **tokens + rules + examples**. A PDF of logos isn't enough.

### 2.6 Brand psychology (graded)
| Claim | Evidence | Grade |
|---|---|---|
| Repeated exposure increases liking | Zajonc 1968, plus later meta-analyses | **Strong** (effect is modest and diminishes with heavy repetition) |
| Easy-to-process stimuli are liked and trusted more | Reber, Schwarz & Winkielman 2004 (processing fluency) | **Strong** in the lab, *Moderate* for logos specifically |
| Colour shifts perceived brand personality (blue → competence, red → excitement) | Labrecque & Milne 2012 | **Moderate**: the associations are learned and cultural, not universal |
| Brands have measurable personality dimensions | Aaker 1997 | **Moderate**: the dimensions don't fully generalise across cultures |
| "Colour X makes people feel Y" infographics | Pop colour psychology | **Contested/weak**. Don't cite these in client decks |

### 2.7 B2B/industrial trust signals (*Practitioner*)
- Restraint and precision: consistent grids, engineered type and a quiet palette tend to read as competence.
- Proof over promise: certifications, specs, case data and real deployments.
- Consistency across product, packaging, docs, UI and events. In a 95-5 market, buyers remember you through consistency.

### 2.8 Evaluating a mark
Run these tests in order:
1. **16px favicon/app icon**
2. **Monochrome** (1-colour, black and white)
3. **Reversal** (light on dark)
4. **Busy photo** and **sky backgrounds**
5. **Low contrast**
6. **Fabrication**: print, embroidery, laser etch, moulded plastic
7. **Distinctiveness search**: your national trademark database (e.g. USPTO, EUIPO, CIPO), reverse-image search, and a competitor map

Then the **squint test** and the **5-second recall** test (show the mark, hide it, have someone draw it from memory).

**Trademark basics** (*not legal advice*). Search existing marks first. Goods and services are classed under the Nice Classification. Registrations are time-limited and renewable, many offices accept non-traditional marks (sounds, colours, shapes), and a mark can be lost if it stops being distinctive. Use a trademark agent or lawyer before committing to a name or mark.

## 3. Methods

| Method | How | Output |
|---|---|---|
| Brand audit | Inventory every touchpoint (site, product, packaging, UI, decks). Mark each one consistent, inconsistent or missing | Audit grid + top 5 fixes |
| Competitive visual audit | Collect marks, primary colours and type for ~10 competitors in your category. Plot them on a hue wheel and a geometric↔organic / warm↔cold map | Whitespace map showing where your brand can be *ownable* |
| Onlyness statement (Neumeier, *Zag*) | "Our [What] is the only [category] that [How] for [Who] in [Where] who [Why] during [When]." If you can't say "only", go back to strategy | One-sentence positioning |
| Naming funnel | Long list (100+) → screen for meaning in your markets' languages, domain, trademark conflicts, pronunciation → shortlist 5 → test with users | Defensible name |
| Thumbnail-to-vector | 100 pencil thumbnails → 10 refined → 3 vectored on a grid → test before polish | Construction drawings |
| Stress tests | Run the §2.8 sequence on real product renders and print, at small sizes and low contrast | Pass/fail matrix |
| Guidelines doc | Core (never changes), flexible (seasonal), tokens, do/don't, examples, downloadable assets | Living site or Figma library, not a static PDF |
| Governance | Owner, request/approval flow, asset library, quarterly audit, token versioning | RACI + review cadence |

## 4. Brand checklist

- [ ] Architecture chosen (branded / endorsed / sub-brand) and signed off before mark exploration
- [ ] Onlyness statement written and passes the "only" test
- [ ] Competitor colour/mark map done, and the brand sits in open space
- [ ] Palette stays distinct from error and warning colours, with `brand.*` tokens kept separate from `color.alert.*` and `color.status.*`
- [ ] Mark passes 16px, mono, reversed, photo, low-contrast and fabrication tests
- [ ] Lockups defined (clear space, hierarchy, min sizes)
- [ ] 1–2 assets nominated as the "distinctive assets" and applied consistently
- [ ] Name/mark cleared by a trademark agent in each market
- [ ] Motion and sound specs written, and the brand sound is distinct from alert tones
- [ ] Voice ladder covers error and alert copy
- [ ] Guidelines published with token file and owner
- [ ] Baseline fame/uniqueness test planned (unbranded recognition with category buyers)

## 5. Designer tendencies

| Tendency | Why it bites | Countermeasure | Psychology cross-link |
|---|---|---|---|
| Falling for the first mark | First idea anchors the rest | 100-thumbnail minimum before choosing | **Anchoring Bias** |
| Loving your own work | Effort inflates value | Blind-review the work alongside competitors' marks | **IKEA Effect** |
| Trend-chasing ("blanding": geometric sans, flat, pastel) | Familiar ≠ distinctive. You end up looking like everyone else (cf. Lufthansa 2018 critics) | Run the competitive audit first and aim for the open space | **Bandwagon Effect**, **Familiarity Bias** |
| Judging logos at poster size | Hides 16px and small-print failures | Review small and in mono first | **Aesthetic-Usability Effect** (beauty masks function) |
| One slick mockup sells the mark | Stakeholders judge the whole from one glossy render | Show stress-test failures alongside the hero render | **Halo Effect** |
| Designing in isolation from product UI | The brand breaks in the app and alert states | Run brand-to-UI token mapping early | — |
| Brand colours colliding with alert semantics | A red/amber brand colour dilutes error and warning signals | Keep brand and semantic tokens separate | **Von Restorff Effect** (alerts must stay the odd one out) |
| Over-explaining the mark | Abstract marks get their meaning through use (Chase) | Explain with one story, then rely on consistent use | **Storytelling Effect** |
| Text-only identities | Images are remembered better than words | Build a pictorial asset alongside the wordmark | **Picture Superiority Effect** |
| Statistics instead of a face in case studies | One concrete story moves buyers more than numbers | Lead with one customer and one story | **Singularity Effect** |

## 6. Reading list (ranked)

1. Wheeler & Meyerson, *Designing Brand Identity*, 6th ed. (Wiley, 2024): the process reference. https://www.wiley-vch.de/en/areas-interest/art-culture/designing-brand-identity-978-1-119-98481-8
2. Romaniuk, *Building Distinctive Brand Assets* (OUP, 2018): the measurement method. https://www.goodreads.com/book/show/39198119
3. Neumeier, *The Brand Gap* + *Zag*: definitions and onlyness. https://danmall.com/learn/the-business-of-design/onlyness
4. Johnson, *Branding: In Five and a Half Steps* (Thames & Hudson, 2016). https://www.johnsonbanks.co.uk/templates/thought/branding-in-five-and-a-half-steps
5. Sharp, *How Brands Grow* + B2B Institute reports. https://marketingscience.info/b2b-reports/
6. Rand, "Logos, Flags, and Escutcheons" (1991, free). https://paulrand.design/writing/articles/1991-logos-flags-and-escutcheons.html
7. NASA 1975 / NYCTA 1970 manuals (Standards Manual reissues). https://standardsmanual.com/pages/about
8. uxtools, "Brand as Product's Secret Weapon" and "7 Changes in Brand World-Building". https://www.uxtools.co/blog/brand-as-product-s-secret-weapon
9. Labrecque & Milne 2012 (JAMS): colour evidence. https://link.springer.com/article/10.1007/s11747-010-0245-y
10. Eye Magazine, "Symbols and survival" (C&G). https://eyemagazine.com/feature/article/symbols-and-survival

## Sources
- https://www.uxtools.co/blog/brand-as-product-s-secret-weapon
- https://www.uxtools.co/blog/7-changes-in-brand-world-building
- https://www.wiley-vch.de/en/areas-interest/art-culture/designing-brand-identity-978-1-119-98481-8
- https://www.johnsonbanks.co.uk/templates/thought/branding-in-five-and-a-half-steps
- https://www.samuelthomasdavies.com/book-summaries/business/the-brand-gap
- https://danmall.com/learn/the-business-of-design/onlyness
- https://paulrand.design/writing/articles/1991-logos-flags-and-escutcheons.html
- https://www.ibm.com/history/logo
- https://eyemagazine.com/feature/article/symbols-and-survival
- https://imjustcreative.com/saul-bass-logo-designs-past-present/2011/03/24
- https://standardsmanual.com/pages/about
- https://www.astronomy.com/space-exploration/nasa-brings-back-retro-worm-logo-from-the-1970s/
- https://www.dezeen.com/2018/02/05/lufthansa-airline-updates-yellow-100-year-old-logo-livery-redesign/amp/
- https://www.creativeapplications.net/project/mit-media-lab-identity-processing/
- https://www.pentagram.com/news/mit-media-lab
- https://umbrex.com/resources/frameworks/marketing-frameworks/distinctive-brand-assets-framework-ehrenberg-bass/
- https://tianpan.co/zh/blog/2025/09/01/building-distinctive-brand-assets-by-jenni-romaniuk
- https://marketingscience.info/b2b-reports/
- https://link.springer.com/article/10.1007/s11747-010-0245-y
- https://gsb.stanford.edu/faculty-research/publications/dimensions-brand-personality
- https://pages.ucsd.edu/~pwinkielman/reber-schwarz-winkielman-beauty-PSPR-2004.pdf
- https://moodle.novasbe.pt/pluginfile.php/672530/mod_resource/content/1/aaker-joachimsthaler-2000-the-brand-relationship-spectrum-the-key-to-the-brand-architecture-challenge.pdf
