---
name: designer-growth-foundations
description: Self-improvement engine for product designers — assess skills, plan learning, debrief for designer biases, trace psychology and art-history lineage, and five deep modules (safety-critical/HMI, accessibility, tokens, brand, game UX). Runs as a Karpathy-style LLM wiki over Hack Design and uxtools.co with ingest, query and lint.
---

# Designer Growth Foundations

A deep-learning system for **getting better as a designer**, not just making a better design. It combines four layers:

1. **Curriculum** — all 68 Hack Design lessons (hackdesign.org/lessons) + the uxtools.co library (69 articles, 18 hands-on challenges, 2024 Design Tools Survey, 2026 State of Prototyping), ingested Oct 2026 and regrouped into 10 competency domains, each tagged with status (timeless / update the tool / evidence flag). Lines prefixed **UXT ·** are uxtools.co; unprefixed lines are Hack Design.
   Plus five **deep modules** with lineage, graded knowledge, methods, checklist and designer traps: **S** safety-critical & HMI · **A** accessibility & inclusive design · **T** design systems & tokens · **B** brand identity · **G** game UX & player psychology.
2. **Learning science** — how skill is actually built: deliberate practice, spacing, retrieval, reflection, taste.
3. **Designer psychology** — the tendencies and biases designers show *about their own work* (fixation, curse of knowledge, IKEA effect…), with detection signals and counter-moves.
4. **Art & design history** — the lineage behind each domain, so you study sources, not just trends.

Companion (optional): a *design-psychology* skill covering biases of *users*. This skill is about the *designer*. When a principle name appears in *italics* below it is an exact entry in `data/psych-principles.json` (names from growth.design's cognitive-bias catalogue) — cross-link to it.

## Knowledge base — LLM Wiki architecture

The library follows Andrej Karpathy's **LLM Wiki** pattern ([gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)): instead of re-deriving answers from raw sources every time, Claude maintains a persistent, interlinked wiki where cross-references and contradictions are already worked out. "The tedious part of maintaining a knowledge base is not the reading or the thinking — it's the bookkeeping" — that bookkeeping is Claude's job.

| Layer | What | Where | Rule |
|---|---|---|---|
| **Raw sources** | Index of Hack Design (68 lessons) and uxtools.co (69 articles, 18 challenges, surveys): canonical title, URL, domain, type, year | `library/sources-index.md`, `library/sources.json` | Immutable: append new sources, never rewrite old entries. Full-text extracts are not redistributed — INGEST regenerates them locally into `library/local/` (git-ignored) |
| **Wiki** | Synthesis pages: 5 deep modules + one page per node (domain, mode, module, tendency, lineage strand, principle, science concept, source) with `[[wikilinks]]` | `modules/*.md`, `wiki/*.md` (Obsidian-compatible) | Claude maintains it; every page links to its relations |
| **Schema** | This SKILL.md: structure, conventions, workflows | `SKILL.md` | Edit via pull request; bump `CHANGELOG.md` |
| **Navigation** | `wiki/index.md` (every page and every source item with canonical title, URL, domain) · `wiki/log.md` (append-only, `## [YYYY-MM-DD] op \| title`) · `wiki/lint-report.md` · `index.html` (semantic mind map; rebuild with `tools/build.py`) | `wiki/`, `map/` | Update index and log on every ingest/lint |

**Where the files are:** paths are relative to this repository (`modules/`, `wiki/`, `library/`, `map/`). If you keep a personal copy elsewhere, set the location once in your own CLAUDE.md or project notes. If a file can't be reached, work from this SKILL.md, say which file you could not open, and never claim to have saved or read a file you couldn't reach.

## Who this is for

Mid-level to senior product / UX / UI designers who want to grow deliberately. Senior level means: skip beginner career lessons unless asked; push toward *taste, judgement, systems, evidence, leadership and lineage*. Before personalising advice, ask for (or read from the user's own project notes) their current work: the products they design, the systems they own, any brand or side projects. Tie examples to that work.

## When to use

- "How do I get better at X", "what should I practise", "build me a learning plan", "level up my typography/motion/research…"
- "Review how I handled this project", "what did I get wrong", "debrief", "retro on my process"
- "Where does this style/trend come from", "what's the history behind…", "who should I study for…"
- "Assess my skills", "what am I weak at"
- "Add this source/course/book to my design learning library"
- "Get me better at designing operator / control-room / safety-critical UI", alarm or alert design, situation awareness, automation handover (→ Module S)
- Accessibility, WCAG, contrast, inclusive design, situational disability (→ Module A) · tokens, Figma variables, DTCG, design-system governance (→ Module T) · logo, identity, brand architecture (→ Module B) · game UX, HUDs, onboarding, player motivation (→ Module G)

## Seven modes

Pick from the request; combine when useful. Always name the lessons, principles and historical references used.

### 1. ASSESS — map skill level and growth edges
1. Use the 10 domains below plus a row for each deep module relevant to the work (S operational/safety-critical, A accessibility, T tokens, B brand, G game UX). For each, rate on the **Dreyfus scale** (1 Novice → 2 Advanced beginner → 3 Competent → 4 Proficient → 5 Expert) *from evidence*: shipped work, portfolio pieces, critique feedback. Ask for or look at artefacts (Figma files, portfolio, shipped work) rather than self-rating alone — self-ratings carry *Dunning-Kruger Effect* and *Self-Serving Bias*.
2. For each domain write: evidence seen → level → the *next observable behaviour* that would prove the next level.
3. Output a table `Domain | Level | Evidence | Next-level behaviour | Leverage for current work (H/M/L)` and a text radar (e.g. `Visual craft ████░`).
4. Pick **3 growth edges**: highest leverage × largest distance to the next level. Weight by the user's current work and goals.

### 2. REFLECT — project debrief and designer-bias audit
Schön's *reflection-on-action* + Kolb's cycle (experience → reflect → conceptualise → experiment).
1. Reconstruct the timeline: brief → first idea → key decisions → what shipped → what users did.
2. Run the **Designer Tendencies checklist** (below). For each, mark ✅ avoided / ⚠️ showed up / ❓ can't tell, with evidence.
3. Separate *outcome* from *decision quality* (*Hindsight Bias*): was the decision good given what was known?
4. Output: `Keep | Change | Bias that showed up + counter-move | Lesson to revisit (canonical title) | Next step`. Keep it to the few that matter.
5. If the prompt conflicts with stored project context (memory, project docs, earlier artifacts), name the difference instead of silently picking one.

### 3. LINEAGE — trace a design choice through history
1. Name the visual or interaction move (e.g. "flat UI with generous white space and a modular grid").
2. Trace it: origin movement → key figures/works → original *intent* (often social or technical, not aesthetic) → how it was transmitted to digital → what got lost. Ground every step in the lineage tables or cited sources; mark your own reading as interpretation.
3. Explain the *psychology* that made it survive (e.g. Gestalt grouping → *Law of Proximity*, *Law of Prägnanz*).
4. Give a **study set**: 3 historical works + 2 contemporary works (from the libraries/modules, or labelled "suggested — verify") + 1 primary text.
5. Use it to make choices *knowingly*: borrow the intent, not just the surface. Flag cultural appropriation risks (e.g. using Mingei or Ma as decoration without the underlying idea).

### 4. CURRICULUM — plan a learning cycle
1. Start from ASSESS growth edges (or ask for the 1–3 goals).
2. Build a 4, 8 or 12-week plan as a table: 3 sessions/week of 60–120 min, each = 1 input (a library lesson/article or a module reading-list item) + 1 application to the user's own work + 1 spaced review. One of the 3 weekly sessions is a *lineage* session. End each 4-week block with a capstone (Hack Design "Summer Vacation": *make something you couldn't make when the block began* and share it). A curriculum is the one output where length is expected — keep each cell short.
3. Mix in the **deep modules** (S, A, T, B, G).
4. Respect *Planning Fallacy*: plan 70% capacity; fit around the user's routine (deep-work blocks, creative practice) if they share it.

### 5. INGEST — extend the library with new sources
For each new source. New deep modules follow the same template: why/shift → lineage table → graded knowledge base → methods → checklist → designer traps (with psych links) → ranked reading → sources; then add a condensed section here and nodes to the mind map:
1. Extract with the same schema: `Title — Author (Domain) · URL · Year · Thesis · Resources · Exercises · Takeaways · Skills trained`.
2. Tag: domain (D1–D10 or new), **status** (Timeless / Update-tool / Evidence-flag / Dated), **evidence grade** (Strong / Moderate / Practitioner / Contested), psychology links, lineage links.
3. Append to the `library/` files and the JSON; update the domain map in this SKILL.md, then run `tools/build.py` to refresh the wiki and map.
4. Fetch slowly (sequential, not parallel) — hackdesign.org rate-limits bursts. Summarising fetches can mis-attribute quotes: flag anything odd and re-fetch before citing.
5. Re-check sources that change (uxtools.co publishes weekly): add new articles, don't rewrite old entries.
6. After every ingest: update `wiki/index.md`, add/refresh the affected wiki pages and their `[[links]]`, append a `## [date] ingest | title` line to `wiki/log.md`, and add nodes/edges to the mind map.

### 6. QUERY — answer from the wiki
1. Read `wiki/index.md` first, then the relevant wiki pages and module files; go to raw sources only for exact quotes, titles or URLs.
2. Answer with citations to wiki pages and canonical source titles/URLs; grade evidence.
3. If the answer is a reusable synthesis (a comparison, a decision, a new connection), offer to file it back as a wiki page and log it (`## [date] query | title`).

### 7. LINT — health-check the knowledge base
Run on request, after large ingests, and at least monthly. Check and report in `wiki/lint-report.md`, then log it:
1. **Contradictions** — the same fact stated differently across SKILL.md, modules and libraries (numbers, dates, token names, rules).
2. **Stale claims** — time-sensitive facts past their re-check date (see the stale-claims register in `wiki/lint-report.md`: platform rules, tool features, legal dates, survey stats, draft standards).
3. **Orphans & weak links** — wiki pages or map nodes with ≤ 1 relation; principles cited only once.
4. **Missing cross-references** — a page mentions a concept that has its own page but doesn't link it.
5. **Evidence** — re-verify a sample of high-stakes claims against primary sources; record CONFIRMED / CORRECTED / UNVERIFIABLE with date and URL.
6. **Title & name hygiene** — titles match the canonical headings in the raw sources; principle names match `data/psych-principles.json`.
Fix what can be fixed, list the rest as open items, and update SKILL.md (and `CHANGELOG.md`) if the schema changed.

## Competency map — 10 domains × 156 items

Legend: **T** timeless principle · **U** principle holds, tool/specs dated → use the modern equivalent · **E** evidence flag (see notes) · ★ high value for a senior designer. Hack Design year 2013 unless stated. **UXT ·** = uxtools.co (Tommy Geoco essays 2025–26, Taylor Palmer / Jordan Bowman guides 2020–22; grade Practitioner unless noted).

### D1 · Visual craft & brand (type, layout, colour, icons, data, brand)
- ★ Dive Into Typography — Kerem Suer · T · kerning/letterform games (type.method.ac, shape.method.ac), *Thinking With Type*, *Helvetica* film
- ★ Typography in Product Design — Jared Erondu · T · "Typography exists to honor content"; strip-the-text test; iA "Web is 95% typography"
- Exploring the World of Typefaces — Sacha Greif · U · font identification habit (WhatFont, WhatTheFont); Google Fonts → today also variable fonts
- Responsive Typography in Action — Jem Gold · U · 5 variations of one post rated for readability; contrast through scale (→ fluid type / clamp())
- ★ Typography in Practice — Moiz Syed · T · Boulton grids, Spiekermann *Type on Screens*, Bringhurst *webtypography.net*, TypeRadio (Vignelli, Irma Boom)
- ★ White Space: Designing the Invisible — David Kadavy · T · active vs passive white space (Boulton); Inge Druckrey *Teaching to See*; Tufte 1+1=3
- ★ Achieving Visual Hierarchy — Lise Statelman · T · squint/blur test; "hierarchy tells a story that culminates in action"
- Designing with Grids — Reda Lemeden · U · fluid grids (Marcotte); "great designers know when to break them"; Bourbon Neat → CSS Grid / Figma auto-layout
- UI Design with Purpose — Travis Silverman · T · "content shouts, UI whispers"; redesign a screen in the opposite style (flat ↔ skeuomorphic)
- Building Color Confidence — Joanne Chang · T/E · colour vocabulary (hue, chroma, value, tint, shade, tone); palettes from photos. **E:** colour-meaning articles are cultural convention, not universal psychology
- ★ The Medium and Mechanics of Iconography — P.J. Onori · T · Peirce's icon/index/symbol; "the floppy disk means save"; Octicons as a system
- Using Icons in Interfaces — Brent Jackson · T · test icons out of context; icon + label for infrequent users
- Vector Interface Design — Jeff Broderick · U · replicate with shapes only; halve your layer count (Photoshop → Figma vector networks)
- ★ Designing Data (2018) — James De Angelis · T · chart choice by question; 39 perception studies (Elliott); choropleths
- ★ UXT · Brand as Product's Secret Weapon (2025) · as function commoditises, brand experience differentiates; brand and product design must stop being siloed (→ Module B)
- UXT · 7 Changes in Brand World-Building (2026) · brand books must govern generated/streamed UI and co-created content
- Psych anchors: *Visual Hierarchy*, *Contrast*, *Law of Proximity*, *Law of Similarity*, *Aesthetic-Usability Effect*

### D2 · Interaction, motion & prototyping
- ★ Great Animations (2025) — Emil Kowalski · T · springs over linear; <200 ms ease-out; frequency-aware motion; "Developing Taste"; WWDC 2018 *Designing Fluid Interfaces*
- ★ Animation, Direct Manipulation & Feedback — Ben Taylor · T · Bret Victor; animated transitions explain state change; NN/g "When the UI is too fast"
- ★ The Human Element — Scott Hurff · T · Disney's 12 principles in UI; *progressive reduction* (reward proficiency); Bret Victor's "Brief Rant"
- The Little Things Matter — Kyle Bragger · T · Little Big Details; transitional interfaces; "un-signup" (Stripe); show don't tell (Flinto)
- Bringing Depth to Design (2025) — Anand Sharma · T · Three.js, GSAP, Rive state machines, Spline, Mixamo
- Prototyping with Framer — Cemre Güngör · U · Framer.js classic → Framer / ProtoPie / Rive
- Quartz Composer — Dave O'Brien · U · QC is discontinued → Origami Studio / ProtoPie; keep the "watch → build along → rebuild blind" method
- Rapid Prototyping Tools — Joe Robinson · T · Wizard-of-Oz ("Aardvark"), fake it → trash it → build it
- Designing with Code — Chris Lee · U · design in the browser, DevTools as a craft tool (AngularJS → React / v0 / AI codegen)
- ★ UXT · Your UI Needs More Walt Disney (2025) · "If your UI only works 80% of the time, the perception of quality breaks" — robustness of interaction is perceived quality
- UXT · Motion Design's System Update (2025) · motion is now state-driven logic (state machines), not garnish
- ★ UXT · How Designers Can Prevent User Errors (2021) · redesign so errors can't happen; don't blame or train users (→ Module S)
- UXT · How Prototyping Has Changed / This Is the State of Prototyping in 2026 · prototyping is where AI change in design converges
- UXT · UX Lessons from Big Sur (2020) · "the interface shouldn't draw attention to itself"
- UXT challenges: Wireframe · Digital Prototype · Form
- Psych anchors: *Feedback Loop*, *Feedforward*, *Labor Illusion*, *Fitts's Law*, *Delighters*

### D3 · Research & evidence
- ★ Getting Started with Design Research (2018) — Joel Califa · T · NN/g research cheat sheet; usability tests, interviews, field studies first
- ★ User Research with JTBD Interviews (2018) — Alex Baldwin · T/E · milkshake story; Moesta/Spiek timeline interview; *When Coffee & Kale Compete*. **E:** "10 interviews ≈ 1,000 surveys" is a practitioner claim
- Designing With Your Ears — Arthur Bodolec · T · research objectives first; "Avoiding Bullshit Personas"; recruiting
- Understanding the User in UX — Grace Ng · T · Fogg model; interview tips; Krug usability demo
- An Introduction to UX Design — Dan Zambonini · T/E · Norman, Tognazzini first principles; spot convenience-over-experience in everyday objects. **E:** salary figures stale
- Win the Internet with A/B Testing — Manik Rathee · T · hypothesis + event plan + external variables; significance pitfalls (Cennydd Bowles)
- Mobile App Analytics Is Not That Special — Kyle Wild · T · AARRR; deep engagement events; one metric that matters
- Designs That Convert (2018) — Daniel Zarick · T · positioning, funnel's weakest stage first, compounding gains, pricing
- ★ How to Prove Your Design's Value — Nick Disabato · T · research + measurement + experimentation = influence; *Personal MBA*, *About Face*
- ★ UXT · Translating User Research Into Design (2022) · research that never reaches the design is "performative"
- ★ UXT · How Research Teams Are Keeping Up with Build Teams (2026) · 2023 research cadence can't match 2026 build speed — continuous, lighter loops
- ★ UXT · When to Skip UX Research (2021) · every project should rely on insight, but research isn't always step one
- UXT · The Best UX Research Methods in a Pinch (maximise insights per time and money) · Quicker UX Research Synthesis · Fixing User Personas ("discovered, not created") · Usability Testing in 4 Simplified Steps · How to Maximize the Research You're Already Doing · 12 Ways to Use Other Departments in Research · What Developers Need from UX Research · Fast and Cheap Ways to Find Participants · 17 Research Tools · User Research: Is It Worth It?
- UXT challenges: User Interview · Journey Map · Competitive Analysis · User Persona · Empathy Map · Survey · Usability Test · Card Sorting · Heuristic Evaluation · Diary Study
- Psych anchors: *Confirmation Bias*, *Observer-Expectancy Effect*, *Survey Bias*, *Hawthorne Effect*, *False Consensus Effect*

### D4 · Behaviour & psychology
- Effective Behavior Design — Alex Baldwin · T · Fogg Behavior Model + Behavior Grid; define behaviours precisely
- ★ Designing Habit-Forming Products — Nir Eyal · T/E · Hook model; Paul Graham "Acceleration of Addictiveness". **E:** run an ethics check: would users thank you if they understood exactly how it works?
- User On-boarding and the NUX (2018) — Matt Brown · T · UserOnboard teardowns; early wins; Solitaire as mouse tutorial
- Defining & Expanding UX — Patrick Algrim · T · iA "Learning to See"; redraw a checkout flow; speed as experience
- UXT · The Psychology of User Decisions (2020) · predictable subconscious patterns (→ companion design-psychology skill)
- UXT challenge: Onboarding
- Psych anchors: *Variable Reward*, *Internal Trigger*, *Goal Gradient Effect*, *Investment Loops*, *Default Bias*

### D5 · Product thinking, quality & philosophy
- ★ Deciding What's Good: Design Principles — Kate Rutter · T · Rams' 10; write 5–7 product principles; 10-minute critique; team vocabulary
- ★ Designing Quality Products — Nathan Manousos · T · Saul Bass on quality vs money; Ive on saying no; "Don't throw it over the fence"
- ★ Embracing the Ordinary: Super Normal (2025) — Alex Baldwin · T · Fukasawa & Morrison; "good design doesn't scream"
- A Holistic Guide to Product Design — Joseph Huang · T · Innovator's Dilemma; minimum *delightful* product; distribution beats design alone
- The All-Encompassing UX — Cat Noone · T · UX across marketing, support; Andrew Stanton storytelling
- Power to the People: Human-Centred Design — Chad Mazzola · T · Kathy Sierra "Minimum Badass User"; Wilson Miner *When We Build*; Ryan Singer UI & capability
- Creative Problem Solving & Everyday Design — Andy Hagerman · T · d.school Bootleg, Gamestorming, "What do prototypes prototype?", Duarte
- Run Your First Design Sprint (2018) — Xander Pollock · T · GV Sprint; verifiable questions
- ★ Moving Beyond "Move Fast and Break Things" (2025) — Avery Erwin · T · Google PAIR guidebook; Slow Media manifesto; strategic slowdown
- Why Design? — Alex Baldwin · T · Chimero *Shape of Design* talk; Monteiro *How Designers Destroyed the World*; working definition of design
- What Is Design? Why Is It Important? — Wells Riley · T · "not purely aesthetic nor wholly analytical"
- ★ UXT · What Happens When "Decent Design" Is the Default (2026) · when AI makes decent the baseline, you need "uncommon effort or uncommon taste"
- ★ UXT · You Can't Prompt This (2025) · "craft is the last unfair advantage"
- ★ UXT · What No One Explains About the Design Process (2021) · "Design is not a process, it's a practice" — judgement, relationships, craft
- UXT · Showing Up for Design Quality (2026) · "Quality alone doesn't compound. Quality plus participation does."
- UXT · Monitor Stands Have More Personality Than Software (2026) · execution got cheap; returns to conviction went up
- Psych anchors: *Occam's Razor*, *Tesler's Law*, *Second-Order Effect*, *Peak-End Rule*

### D6 · Systems, structure & platforms
- ★ Design System Fundamentals (2018) — Diana Mounter · T · pilot projects (Dan Mall); everything is a component; InVision DS handbook
- ★ It's All Just Systems Design — Ian Storm Taylor · T · atomic design; refactoring a design; API design ↔ UI design
- Making the Content Flow: RWD — Karolina Szczur · U · content inventory → breakpoints; style guides (→ tokens)
- Designing for Mobile Web — Julie Ann Horvath · U · patterns libraries; icon fonts → SVG; Bootstrap 2 → modern CSS
- The Amazing New Mobile Web — Luke Beard · U · mobile-first is now the default
- Design Your App for Multiple Platforms — Nikki Will · T · use both iOS and Android daily; don't port, adapt
- Designing Your First iPhone App — Brian Benitez · U · pixel-fitting, lo-fi at 1x (→ points, safe areas, Dynamic Type)
- ★ UXT · Design Debt at Machine Speed (2026) · when agents build UI, the design system must become a machine-readable enforcement layer — canonical docs, lint rules, pre-commit hooks, CI gates (→ Module T)
- UXT · The How (and Why) of User Flows (2020) · design toward goals, not pages · UX Design for Navigation Menus (2020)
- UXT challenges: User Flow · Information Architecture · Design System · Accessibility
- Psych anchors: *Mental Model*, *Law of Similarity*, *Recognition Over Recall*, *Chunking*, *Tesler's Law*

### D7 · Language, communication & facilitation
- ★ Content Strategy for Interfaces — Amy Thibodeau · T · "this but not that" voice list; content-type standards; read-aloud test
- (also: Designing Data, Creative Problem Solving → Duarte, All-Encompassing UX → Stanton)
- UXT · 7 Practical Tips for Better Microcopy (2020) · fastest way to improve an interface
- UXT · Running an Effective Design Kickoff Meeting (2021) · 33 Activity Ideas for Remote UX Workshops (2021; the source actually lists 37)
- UXT · Ideas from Developers on Handling UX Feedback (2022) · This Design Tool Blew Up Our Inbox (2025: "design feedback is still a mess")
- Psych anchors: *Cognitive Load*, *Framing*, *Storytelling Effect*, *Curse of Knowledge*

### D8 · Self, taste & career
- ★ Finale: Better at Design by Being Self-Aware — Tuhin Kumar · T · Monteiro *Design Is a Job*, Chimero, Julie Zhuo; list 3 things to improve; articulate why you admire designers
- ★ Closing the Creative Gap (2018) — Kathleen Warner · T · observe → deconstruct → imitate → create; Ira Glass *The Gap*; Wilson Miner *Steal This Talk*
- ★ Creating a Unique Personal Design Style (2018) — Meg Lewis · T · 3 traits → 3 mood boards → 1 merged style board; inspired without copying
- Cultivating Compassion — Whitney Hess · T/E · People Styles; empathic listening; Ford Empathy Belly. **E:** power-pose effects on hormones and risk-taking failed to replicate (Ranehill et al. 2015); only self-reported feelings of power replicated
- Know Your Tools — Marc Edwards · U · tools as second nature; one-layer challenge (constraint); colour management
- Vim as a Design Tool — Adam Morse · U · automate your most-dreaded repetitive task (→ Figma plugins, scripts, AI)
- Practical AI Tools (2025) — Alex Baldwin · T · Karpathy "How I use LLMs"; Bolt, v0, Claude Projects, Perplexity
- How to Get Your First Design Job — Devon Ko · T · trajectory, prolificness, documented process
- Kickstarting Your Design Career — Janna Hagan · T · soft skills get you hired; written short/long goals
- Summer Vacation — Wells Riley · T · consolidation + capstone + share publicly
- Hello World — Wells Riley · T · *Objectified* (Hustwit)
- ★ UXT · The Artifact Stopped Proving Seniority (2026) · the senior job moves upstream: what should exist, who makes it, the standard it must meet, what gets killed
- ★ UXT · I Was Wrong About Taste (2026) · "Taste is not just what you make. It is what you choose to care about. It is who you make room for."
- ★ UXT · Designers and "Phantom Competency" (2026) · AI lets you ship beyond your real skill — stay uncomfortable until skill catches up
- ★ UXT · How These Designers Are Learning Today (2026) · "The loop matters more than the tool": generate → evaluate → plan → iterate
- UXT · 5 Principles of Exceptional Case Studies (2022) · treat the portfolio as a design project for its reader
- UXT · The Portfolio Is Becoming a Playground (2026; reviewers decide in ~55 s) · How to Share Your Design Work in 2026 · Design's Hardest Role Has a Two-Year Clock · How Linear Hires Designers · What Is AI Doing to Design Career Ladders? · The Year Design Communities Go Small (and Real) · Switching Careers to UX
- Psych anchors: *Dunning-Kruger Effect*, *IKEA Effect*, *Spotlight Effect*, *Self-Serving Bias*

### D9 · Emergent media
- Designing for Augmented Reality (2018) — Bushra Mahmood · T · legibility over unknown backgrounds; shared AR vocabulary
- Start Learning 3D (2018) — Devon Ko · U · Cinema 4D Lite (→ Blender / Spline)
- (also: Bringing Depth to Design, Practical AI Tools)
- Psych anchors: *Skeuomorphism*, *Mental Model*, *Signifiers*

### D10 · AI-native practice & design ops (new — from uxtools.co 2025–26)
- ★ UXT · The 4 Levels of AI Fluency · "I don't need AI tools to do my job. I need AI to do the work." Most designers stall at level 2
- ★ UXT · The Only AI Workflow I Use in Production · Figma → Claude Code with designer control over the system
- ★ UXT · Stochastic vs. Deterministic Design · new tools compete on bets about design labour, not features
- ★ UXT · Designing the Next Flow State · the real working surface is the document between you and the agent
- ★ UXT · "Agent-Permeable" Is the New Mobile-Responsive · products must adapt to autonomous interaction
- UXT · Interfaces That Rearrange for Each User (just-in-time UI) · Your Team Isn't AI-Installed · The 30-Second Test ("a chatbot is a window, an agent is a loop") · Pages Are Becoming Teammates · The Year of the Connected Canvas · Discovery Code and New Bottlenecks (human feedback now slower than iteration) · Play Out the End of Design Work (trust, not velocity, is the bottleneck) · The Next Gap in Design Work · Build Interfaces to Understand Systems · A Room Full of Prototypers · "Any Input = Any Output" · 3 Ways MagicPath Closes the Design-to-Code Gap · Gen Image / Generative Media Workflows · The Fog Between Layoffs and Prototyping
- UXT · Designers Who Vibe Code Are Happier at Work · **E:** correlational survey data, not causal
- UXT · 7 Takeaways from the 2020 Design Tools Survey · **E:** extraction unreliable — re-fetch before citing
- UXT · Surveys (Moderate — large but self-selected samples): see Tooling context below
- Psych anchors: *Law of the Instrument*, *Labor Illusion*, *Second-Order Effect*, *Expectations Bias*

**Coverage read-out (Hack Design + uxtools):** D1 16 · D2 18 · D3 32 · D4 6 · D5 16 · D6 14 · D7 6 · D8 23 · D9 2 · D10 23. Research and career are now deep; behaviour, emergent media, brand and language are still thin in the libraries — the deep modules S, A, T, B, G cover them.

### Tooling context (uxtools surveys)
- **2024 Design Tools Survey** (2,220 respondents): Figma holds 82.3% of UI design, ~87% of basic prototyping, 59.2% of design systems/handoff; FigJam 48.8% of whiteboarding. ProtoPie out-scores Figma on prototyping satisfaction; ~1 in 5 Figma users use another tool for advanced prototyping. Spec-to-implementation averages 3.7 weeks; design-system satisfaction is 4.19 for designers vs 3.42 for developers; 46.3% report significant spec-vs-build inconsistencies. Research tooling is fragmented (top 3 = 30.3%).
- **2026 State of Prototyping** (1,478 respondents): Claude is the second-most-used weekly design tool (50.8%) after Figma; 5 of the top 10 weekly tools are AI; design engineers adopt AI far more than IC designers (80.9% vs 35.0%); only 32.8% trust AI output for production (with review).
- Implication: tool choice isn't the differentiator; craft, systems that enforce themselves, and design-to-code fluency are.

## Designer tendencies — biases about your *own* work

Use in REFLECT and whenever the user critiques their own process. Signal → counter-move → source.

| Tendency | Signal in your process | Counter-move | Source / grade |
|---|---|---|---|
| **Design fixation** | Concepts all resemble the first reference you looked at | Diverge *before* looking at references; do 3 intentionally different directions; bring in a distant-domain analogy | Jansson & Smith 1991 · Strong |
| **Primary generator / anchoring on first idea** | Concept 1 survives every round untouched | "Kill your darling" round: argue for the best alternative | Darke 1979; *Anchoring Bias* · Moderate |
| **Einstellung / functional fixedness** | Reaching for the familiar pattern even when the problem differs | Re-describe the problem without UI nouns; ask "what would this be if not a screen?" | Luchins 1942; Duncker 1945 · Strong |
| **Law of the Instrument** | Every problem becomes a component, a modal, a dashboard | Name the job first (JTBD), then the form | *Law of the Instrument* · Practitioner |
| **Curse of knowledge** | You can't see why users don't "get it"; labels use internal jargon | Read-aloud test, 5-second test, a novice walkthrough | *Curse of Knowledge* · Strong |
| **False consensus** | "Users will obviously…" without data | Write the assumption down as a falsifiable hypothesis | *False Consensus Effect* · Strong |
| **Confirmation bias in research** | Interview guide leads; you remember the quotes that agree | Pre-register what would prove you wrong; have someone else code the notes | *Confirmation Bias*, *Observer-Expectancy Effect* · Strong |
| **IKEA effect / endowment** | Over-valuing work you built; defending pixels in critique | Separate "my work" from "the work"; critique a stranger's version of the same brief | *IKEA Effect* · Strong |
| **Sunk cost** | Continuing a direction because of time spent | Ask "would I start this today?" at each milestone | *Sunk Cost Effect* · Strong |
| **Aesthetic-usability blind spot** | Beautiful mockups pass critique, fail tests | Test in greyscale / lo-fi; measure tasks not opinions | *Aesthetic-Usability Effect* · Strong |
| **Bandwagon / trend herding** | Work looks like this year's Dribbble/Mobbin | LINEAGE mode: trace the trend; borrow intent, not surface | *Bandwagon Effect* · Moderate |
| **Survivorship bias in inspiration** | Studying only polished shots, not failures or constraints | Study case studies with constraints and post-mortems | *Survivorship Bias* · Strong |
| **Taste gap** | Frustration that your work doesn't match your taste | Normal for growth; volume + iteration closes it | Ira Glass; Hack Design "Closing the Creative Gap" · Practitioner |
| **Dunning-Kruger (both directions)** | Over-confidence in new domains; under-rating mastered ones | Calibrate with external evidence and critique | *Dunning-Kruger Effect* · Contested (statistical-artefact debate) |
| **Planning fallacy** | Design estimates always slip | Reference-class estimates from past tickets; plan to 70% | *Planning Fallacy* · Strong |
| **Satisficing too early** | First workable answer ships | Set a quality bar up front (D5 principles) | Herbert Simon 1956 · Strong |
| **Problem/solution co-evolution ignored** | Treating the brief as fixed | Reframe the brief explicitly; designers solve by conjecture (Lawson 1979, Dorst & Cross 2001) | Moderate |
| **Hindsight bias in retros** | "We should have known" | Judge decisions by info available then | *Hindsight Bias* · Strong |
| **Phantom competency** | AI-assisted output is better than what you could make or critique unaided | Periodically rebuild key pieces by hand; review AI output against principles you can state | uxtools 2026 · Practitioner |
| **Artifact = seniority** | Measuring yourself by output volume or polish | Shift effort upstream: what should exist, the bar it must meet, what to kill | uxtools 2026 · Practitioner |
| **Nominal-path bias** (safety-critical) | Specs and tests cover the happy path; emergencies are an afterthought | Design and test off-nominal scenarios first (Module S) | Human-factors practice (off-nominal scenario testing, Module S) · Practitioner |

## Learning science — how growth actually happens

- **Deliberate practice** (Ericsson et al. 1993): narrow targets at the edge of ability, immediate feedback, focused repetition. Volume alone isn't enough. Grade: Strong for structure; the "10,000 hours" figure is a popular distortion.
- **Desirable difficulties** (Bjork 1994): spacing, interleaving and retrieval (recall before you look) feel slower but stick. → *Spacing Effect*, *Recognition Over Recall* (for learning, force recall).
- **Reflective practice** (Schön 1983): designers think through a "reflective conversation with the materials" — sketching is thinking. Reflection-in-action (while sketching) and on-action (debrief).
- **Experiential cycle** (Kolb 1984): experience → reflect → conceptualise → experiment. Apply each input to real work to close the loop.
- **Skill stages** (Dreyfus & Dreyfus 1980): novices need rules, experts see situations holistically. Senior growth = making tacit judgement explicit (principles, critique language) so it can be taught and defended.
- **Creativity stages** (Wallas 1926): preparation → incubation → illumination → verification. Protect incubation (unstructured creative time counts).
- **Flow** (Csikszentmihalyi 1990): challenge slightly above skill → *Flow State*.
- **Taste** = calibrated pattern library + articulated reasons. Build it by explaining *why* you admire work (Hack Design Finale, Kowalski "Developing Taste").
- Evidence flags: growth-mindset interventions have small average effects in large replications (keep the attitude, don't oversell it); learning styles (visual/auditory "matching") are not supported — don't plan around them.

## Lineage — art & design history behind each domain

| Domain / move | Roots (movement → figures, works, dates) | Original intent | Psychology that keeps it alive |
|---|---|---|---|
| Typography | Gutenberg (c. 1450) → Garamond, Bodoni → Futura (Renner 1927) → Tschichold *Die neue Typographie* 1928 → Helvetica (Miedinger 1957) → Bringhurst *Elements of Typographic Style* 1992 | Legibility at scale; modernity; neutral voice | *Visual Hierarchy*, *Law of Similarity*, *Cognitive Load* |
| White space | Japanese *Ma* (間) and Zen ink painting → Tschichold's asymmetric layout → Swiss International Style | Emptiness as active form; tension and focus | *Law of Proximity*, *Von Restorff Effect*, *Centre-Stage Effect* |
| Grids | Medieval page canons (Villard de Honnecourt / Van de Graaf) → Bauhaus → Gerstner *Designing Programmes* 1964 → Vignelli/Unimark (NYC subway 1970) → Müller-Brockmann *Grid Systems* 1981 | Objective, rational order; programmes not one-offs | *Law of Prägnanz*, *Chunking* |
| Visual hierarchy & composition | Renaissance perspective (Brunelleschi c. 1415, Alberti *De pictura* 1435) → chiaroscuro (Caravaggio) → Gestalt (Wertheimer 1923) → Arnheim *Art and Visual Perception* 1954 | Directing the eye to the story's climax | *Visual Hierarchy*, *Contrast*, *Selective Attention* |
| Colour | Isaac Newton's *Opticks* (1704) → Goethe *Theory of Colours* 1810 → Chevreul simultaneous contrast 1839 → Itten (Bauhaus) → Albers *Interaction of Color* 1963 | Colour is relative, perceived in context | *Contrast*, *Weber's Law*, *Sensory Appeal* |
| Icons & pictograms | Egyptian hieroglyphs → Isotype (Neurath & Arntz, 1920s–30s) → Aicher's Munich 1972 Olympic pictograms → Susan Kare's Macintosh icons 1984 | A universal visual language across languages | *Picture Superiority Effect*, *Signifiers*, *Recognition Over Recall* |
| Skeuomorphism ↔ flat | Trompe-l'œil → Arts & Crafts honesty of materials → Bauhaus/Swiss reduction → iOS 6 → iOS 7 (2013) | Familiarity during transition vs honesty to the medium | *Skeuomorphism*, *Familiarity Bias*, *Mental Model* |
| Super normal / restraint | Shaker furniture → Mingei (Yanagi, 1920s) → Rams' 10 principles → Fukasawa & Morrison *Super Normal* 2006 | Beauty of anonymous, well-used everyday objects | *Occam's Razor*, *Familiarity Bias*, *Aesthetic-Usability Effect* |
| Motion | Muybridge's motion studies 1878 → Futurism (Balla) → Disney's 12 principles (Thomas & Johnston, *The Illusion of Life* 1981) → Apple fluid interfaces | Believable life; weight and intent | *Feedback Loop*, *Feedforward*, *Labor Illusion*, *Delighters* |
| Depth / 3D | Linear perspective → stereoscopy (Wheatstone 1838) → Sutherland's Sketchpad 1963 & head-mounted display 1968 | Simulating presence | *Skeuomorphism*, *Mental Model* |
| Data visualisation | Playfair 1786 → Nightingale 1858 → Minard 1869 → Bertin *Semiology of Graphics* 1967 → Tufte 1983 | Argument through evidence | *Picture Superiority Effect*, *Chunking*, *Framing* |
| Systems & components | Gerstner's programmes → Unimark manuals → Christopher Alexander *A Pattern Language* 1977 → Atomic Design (Frost 2013) | Reusable rules that generate many solutions | *Law of Similarity*, *Mental Model*, *Tesler's Law* |
| Human-centred design | Dreyfuss *Designing for People* 1955 → Norman *The Design of Everyday Things* 1988 → IDEO / d.school | Fit the object to the person | *Mental Model*, *Cognitive Load* |
| Ethics & responsibility | Garland's *First Things First* 1964 (renewed 2000) → Papanek *Design for the Real World* 1971 → Monteiro → deceptive.design | Designers are accountable for impact | *Second-Order Effect*, *Reactance* |
| Behaviour design | Skinner's reinforcement schedules (1950s) → Fogg's captology (Stanford) → Eyal's Hook | Shape repeated behaviour | *Variable Reward*, *Shaping*, *Internal Trigger* |
| Process & problem framing | Simon *The Sciences of the Artificial* 1969 → Rittel & Webber "wicked problems" 1973 → Schön 1983 → Cross *Designerly Ways of Knowing* 2006 | Design as its own way of knowing | *Second-Order Effect* |
| Personal style & authorship | Arts & Crafts (Morris) vs Modernist anonymity → Paul Rand → Saul Bass → Meg Lewis | Voice vs neutrality | *Halo Effect*, *Singularity Effect* |
| Learning by copying | Renaissance workshops; copyists at the Louvre; calligraphy copybooks | Internalise the master's decisions | *Spacing Effect*, *Shaping* |

Starter reading: Meggs' *History of Graphic Design* · Gombrich *The Story of Art* · Berger *Ways of Seeing* · Arnheim *Art and Visual Perception* · Albers *Interaction of Color* · Lupton *Thinking with Type* · Smarthistory (free, online) · Cooper Hewitt and Letterform Archive online collections.

## Module S — Safety-critical, enterprise & HMI design

Full module: `modules/module-s-safety-critical-hmi.md` (lineage, standards, methods, checklist, reading list). Use it for control rooms, healthcare, industrial process, energy, transport and other operational software. **The shift:** from conversion and delight to **situation awareness, error tolerance and calibrated trust in automation**.

**Lineage:** Chapanis shape-coded knobs and Fitts & Jones 1947 ("pilot error" was design error) → Three Mile Island 1979 (alarm flood; display showed the command, not the valve's actual state) → Therac-25 1985–87 → Air France 447 (2009) → 737 MAX MCAS.

**Knowledge base (all Strong unless noted):**
- **Situation awareness** (Endsley 1995): L1 perceive → L2 comprehend → L3 project. Organise by operator goals; show L2/L3 directly ("tank reaches the low-level threshold in 4 min"); always-visible overview; watch the SA demons (attentional tunnelling, memory trap, overload, misplaced salience, complexity creep, errant mental models, out-of-the-loop). Measure with SAGAT freeze probes.
- **Human error** (Reason 1990; Rasmussen; Norman): slips, lapses, mistakes, violations; Swiss cheese model. Use forcing functions, constraints, undo, visible modes; confirm only the irreversible.
- **Automation** (Bainbridge 1983 *Ironies of Automation*; Parasuraman, Sheridan & Wickens 2000; Sarter & Woods; Lee & See 2004): show what it's doing, why, what next, how to take over; calibrate trust; design the handover and degraded mode.
- **Alarms**: EEMUA 191 / ISA-18.2 — < 1 alarm per 10 min acceptable, ≥ 10 per 10 min = flood (ISA-18.2; via secondary sources, standards are paywalled), priority mix ≈ 80/15/5 low/med/high, every alarm needs an action. Aviation 14 CFR 25.1322: red = warning, amber/yellow = caution, advisory never red or green; limit red/amber elsewhere. Message = what + why + action; redundant coding.
- **High-performance HMI** (ISA-101; Hollifield et al. 2008 · Moderate–Strong): greyscale base, colour only for abnormal, values against normal ranges and trends, display hierarchy overview → diagnostic.
- **Workload**: NASA-TLX; Wickens' multiple resources (move alerts to audio/haptic when eyes are busy).
- **Remote monitoring**: the interface must replace the cues of being on site; stale data must look stale.
- **Standards**: ISO 9241-110:2020, ISO 9241-210, IEC 62366-1 (use-related risk analysis), ISO 11064, MIL-STD-1472H, ISA-101, ISA-18.2/IEC 62682.

**Methods:** goal-directed task analysis → SA requirements · cognitive task analysis / Critical Decision Method · use-related risk analysis (use error × severity × likelihood × detectability) · off-nominal scenario tests (loss of communication, equipment failure, sensor disagreement, shift handover) measuring time-to-detect, errors, SAGAT, NASA-TLX · testing in the real work environment.

**Checklist:** persistent critical-state overview · visible, announced modes · projections shown · alert colours reserved and tokenised in the design system (`color.alert.warning/caution/advisory`; success lives in `color.status.*`), never colliding with brand colours · no alert without an action · distinct deliberate action for irreversible commands · safe defaults · stale data marked · redundant coding · ranges/trends over raw numbers · automation transparency · designed degraded mode · event log/replay.

**Designer traps here:** curse of knowledge (you are not the operator), nominal-path bias, consumer patterns (vanishing toasts, swipe-to-dismiss alerts), minimalism that hides state, confirmation overuse, brand colour diluting alerts, automation optimism. Psych links: *Cognitive Load*, *Feedback Loop*, *Feedforward*, *Mental Model*, *Banner Blindness* (alarm fatigue), *Von Restorff Effect*, *Default Bias*, *Recognition Over Recall*, *Weber's Law*.

**Read first:** Endsley et al. *Designing for Situation Awareness* · Reason *Human Error* · Hollifield *The High Performance HMI Handbook* · Bainbridge "Ironies of Automation" · Lee & See "Trust in Automation".

## Module A — Accessibility & inclusive design

Full module: `modules/module-a-accessibility.md`. **The shift:** from "does it pass the audit?" to "who is excluded by this mismatch, and in which conditions?" Microsoft's permanent/temporary/situational spectrum shows that designing for permanent disability also serves people with temporary injuries and situational limits (bright sun, one hand busy, a noisy room), so the accessible version should be the default token/component.

**Lineage:** curb cuts → Section 508 (1998, refreshed 2018) → Mace's universal design principles (1997) → WCAG 1.0 (1999) → 2.0 (2008) → 2.1 (2018) → 2.2 (5 Oct 2023) → Microsoft Inclusive Design (2016) → Holmes *Mismatch* (2018) → Accessible Canada Act (2019) → Domino's v. Robles (2019) → European Accessibility Act applies (28 Jun 2025).

**Knowledge (Strong unless noted):** WCAG 2.2 (Recommendation 5 Oct 2023; updated edition Dec 2024) added 9 criteria incl. 2.5.8 Target Size (Minimum) 24×24 CSS px (AA), 2.4.11 Focus Not Obscured, 2.5.7 Dragging Movements, 3.2.6 Consistent Help, 3.3.7 Redundant Entry, 3.3.8 Accessible Authentication; removed 4.1.1. Contrast 4.5:1 text, 3:1 large text, 7:1 AAA (4.5:1 for large text), 3:1 for UI parts and focus (1.4.11), no rounding. WCAG 3 is a Working Draft; APCA is not normative. Prevalence: WHO 1.3 bn (16%); Statistics Canada 27% of Canadians 15+ (2022); red-green CVD ≈ 8% of men / 0.5% of women (N. European ancestry). WebAIM Million 2026: 95.9% of home pages fail; low-contrast text on 83.9%. Automated tools catch a minority of barriers (GOV.UK 2017: best tool 37–41%, all ten 71%; Deque's vendor figure 57% by count). Cognitive: W3C COGA *Making Content Usable*. Motion: prefers-reduced-motion. Law (not legal advice): ACA, EAA, EN 301 549, ADA Title II rule (2024).

**Methods:** automated scan → keyboard-only pass → screen reader (NVDA, VoiceOver) → zoom 200/400% + reflow → token contrast matrix → test with disabled users → accessibility acceptance criteria in every user story.
**Traps:** a11y as final QA · low-contrast aesthetic · colour-only status · placeholder as label · designing at 1x on a perfect monitor · personas without disability. Psych: *Curse of Knowledge*, *Empathy Gap*, *Aesthetic-Usability Effect*, *Fitts's Law*, *Default Bias*.

## Module T — Design systems & tokens

Full module: `modules/module-t-design-tokens.md`. **The shift:** from a component library people interpret to a **machine-readable source of truth** (named decisions + components + rules a machine can check) that code, linters and AI agents consume. In operational UI, an agent picking "a red" instead of `color.alert.warning` is a safety defect.

**Lineage:** Gerstner *Designing Programmes* (1964) → NASA Graphics Standards Manual (1975) → Alexander *A Pattern Language* (1977) → Bootstrap (2011) → Atomic Design (2013) → "design tokens" coined at Salesforce (Jina Anne & Jon Levine, c. 2014) → Material (2014) → Figma Variables (Config 2023) → **W3C DTCG 2025.10, first stable version (28 Oct 2025; Format, Color and Resolver modules)**.

**Knowledge:** DTCG syntax — `$value`, `$type`, `$description`, `$extensions`, `$deprecated`, `{alias.refs}`, groups, `.tokens.json` (Strong). Tiers primitive → semantic → component (Moderate). Naming levels (Nathan Curtis 2020) and team models solitary/centralised/federated (Curtis 2015) (Practitioner). Figma: collections, modes (light/dark/high-contrast, multi-brand), aliasing; Schema 2025 added native DTCG import/export, extended collections, MCP server, a "Check designs" linter (early access). Pipeline: Figma → DTCG JSON → Style Dictionary v5 → CSS/Swift/Android. Enforcement: stylelint `color-no-hex`, Atlassian/Mozilla token lint rules, visual regression, CI gates (uxtools "Design Debt at Machine Speed"). Baseline pain (uxtools 2024): DS satisfaction 4.19 designers vs 3.42 developers; 46.3% significant spec-vs-build inconsistencies; 3.7 weeks spec-to-build. Safety rule: `color.alert.*` tokens (warning, caution, advisory) carry `$description`, are reserved, and brand tokens never alias into them.
**Traps:** naming by value (`blue-500` used semantically) · detaching one-offs · gold-plating · system as side project · documentation drift · not-invented-here. Psych: *Law of Similarity*, *Mental Model*, *Tesler's Law*, *IKEA Effect*, *Sunk Cost Effect*, *Law of the Instrument*.

## Module B — Brand identity

Full module: `modules/module-b-brand-identity.md`. **The shift:** from logo-making to building **distinctive, governable assets** — a small set (mark, colour, type, shape, motion, sound, voice) recognisable without the name, surviving a 16 px favicon, coded as tokens so product UI and generated interfaces stay on-brand, with brand colours kept apart from reserved status and alert colours.

**Lineage:** Aicher's Lufthansa (1962) · Rand's IBM (1956; stripes 1972) and his 1991 line that a logo "derives its meaning from the quality of the thing it symbolizes" · Chermayeff & Geismar Chase (1960), Mobil (1964) · Unimark NYC Transit manual (1970) · Danne & Blackburn NASA manual (1975; worm back as secondary mark 2020) · Bass AT&T (1983) · MIT Media Lab dynamic identity (2011).

**Knowledge:** Wheeler & Meyerson *Designing Brand Identity* 6th ed. (2024): research → strategy → identity → touchpoints → managing assets. Johnson *Branding in Five and a Half Steps* (2016). Neumeier: brand = gut feeling; "onlyness" test. Sharp/Romaniuk distinctive assets, Fame × Uniqueness grid — Moderate for consumer goods, **Contested** when transferred to B2B. Brand architecture: branded house / endorsed / sub-brand / house of brands (Aaker & Joachimsthaler 2000). Psychology: mere exposure (Zajonc 1968) and processing fluency (Reber, Schwarz & Winkielman 2004) Strong; colour → brand personality (Labrecque & Milne 2012) and Aaker's personality dimensions (1997) Moderate; pop colour psychology Contested. Brand in product UI (uxtools 2025–26). Trademark search in your national office before committing (not legal advice).
**Traps:** falling for the first mark · trend-chasing "blanding" · designing in isolation from the UI · brand colour colliding with status colours · judging marks only at large size · IKEA effect. Psych: *Halo Effect*, *Familiarity Bias*, *Von Restorff Effect*, *Picture Superiority Effect*, *Singularity Effect*, *Bandwagon Effect*, *Anchoring Bias*.

## Module G — Game UX & player psychology

Full module: `modules/module-g-game-ux.md`. **The shift:** from task efficiency to motivation, flow and fairness — players chose the difficulty. Remove *unintended* friction (unclear UI, unreadable feedback) and protect the *intended* challenge; the UI should **inform without stealing attention from play**.

**Lineage:** Super Mario Bros. World 1-1 teaching through level design (1985) · Bartle's player types (1996) · RITE method (Medlock et al., 2002) · MDA framework (Hunicke, LeBlanc & Zubek 2004) · SDT/PENS in games (Ryan, Rigby & Przybylski 2006) · Chen "Flow in Games" (2007) · Fagerholt & Lorentzon HUD taxonomy (2009) · PLAY heuristics (Desurvire & Wiberg 2009) · Hodent *The Gamer's Brain* (2017).

**Knowledge:** Hodent — usability + engage-ability, grounded in perception/attention/memory (Practitioner on Strong science). Motivation: competence, autonomy, relatedness (Strong); Quantic Foundry motivations (Moderate); Bartle (Contested/historical). Flow: challenge matched to skill. HUD types: diegetic, non-diegetic, spatial, meta. Real-time info under time pressure = Module S situation awareness (L1–L3), glanceability, peripheral cues. Onboarding in play, one mechanic at a time. Feedback and "juice" (Swink *Game Feel*). Monetisation UX without dark patterns; platform certification requirements change, so keep a dated log. Game accessibility: Game Accessibility Guidelines, Xbox Accessibility Guidelines v3.2.
**Traps:** designing for yourself as an expert player · information dumping · productivity-app patterns in a game · interrupting play to teach or sell · removing all friction. Psych: *Flow State*, *Cognitive Load*, *Selective Attention*, *Banner Blindness*, *False Consensus Effect*, *Curse of Knowledge*, *Reactance*, *Peak-End Rule*.

## Output conventions

- **Titles:** the domain map uses short names. When citing, use the canonical title and URL from `wiki/index.md` or the raw library headings.
- **Psychology names:** principles are the italic names listed in `data/psych-principles.json` (61 names from growth.design's cognitive-bias catalogue; a companion *design-psychology* skill is optional); italics are also used for book titles. Use the exact principle name.
- **Evidence:** one scale — Strong / Moderate / Practitioner / Contested (abbreviated S/M/P/C). A split grade (e.g. "Moderate (consumer) / Contested (B2B)") is fine when the evidence differs by context. Historical facts in lineage tables are documented history, not graded findings.
- Every recommendation ends in a concrete next step the user can take in their own work.
- **Safety tokens:** `color.alert.warning` (red) and `color.alert.caution` (amber) are reserved; `color.alert.advisory` is any colour except red or green; success/OK is `color.status.success`; brand tokens never alias into `color.alert.*`.
- **Dated tools:** use the modern equivalent and mention the swap once per response (QC → Origami/ProtoPie, Photoshop UI → Figma, icon fonts → SVG, AngularJS → React/v0).
- **Context:** use the user's own notes or memory for facts about their projects; when the prompt conflicts with them, say so.
- Keep advice to the few highest-leverage items (CURRICULUM excepted).
- **Saving:** offer to save plans, debriefs and filed-back syntheses to the user's chosen location and log them in `wiki/log.md`. Only say a file was saved after the save succeeded.
