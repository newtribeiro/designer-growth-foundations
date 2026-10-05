# Module A — Accessibility & inclusive design

**Why it matters.** About one in six people lives with a significant disability, and everyone meets *temporary* and *situational* limits: a broken arm, bright sun on a phone, a baby in one arm, a noisy room. The Microsoft Inclusive Design toolkit puts these on one spectrum, so designing for permanent disability improves the product for everyone. Accessibility built into the design system is cheaper and more reliable than fixes at the end. **The shift:** stop asking "does it pass the audit?" and ask "who is excluded by this mismatch, and in which conditions?" Then design the token, component or flow so the accessible version is the default.

---

## 1. Lineage

| Year | Event / work | What it taught designers |
|---|---|---|
| 1945 | First curb cut, Kalamazoo, Michigan | Physical barriers are design decisions |
| 1972 | Official curb cut at Telegraph Ave, Berkeley, after disability activists had made unofficial ones | Disabled people drive design change. The *curb-cut effect* (Blackwell, SSIR 2017): strollers, carts and luggage all benefit |
| 1990 | Americans with Disabilities Act signed (26 July) | Access became a civil right, not charity |
| 1997 | *Principles of Universal Design*, NC State (Ron Mace and a working group) | Seven principles, e.g. Tolerance for Error and Perceptible Information |
| 1998 | Section 508 amendment (US federal ICT must be accessible) | Procurement drives accessibility. The 2017 refresh (in effect 18 Jan 2018) aligned it to WCAG 2.0 |
| 1999 | WCAG 1.0 (5 May) | First web accessibility standard, with three priority levels |
| 2008 | WCAG 2.0 (11 Dec) | Technology-neutral, testable success criteria. POUR principles. A/AA/AAA |
| 2016 | Microsoft Inclusive Design toolkit (© 2016) | Persona spectrum: permanent / temporary / situational |
| 2018 | WCAG 2.1 (5 June): +17 SC, incl. 1.4.11 non-text contrast and 1.4.10 reflow | Mobile, low vision and cognition brought into scope |
| 2018 | Kat Holmes, *Mismatch: How Inclusion Shapes Design* (MIT Press, 16 Oct) | Disability is a *mismatch* between person and design. Design *with* excluded people |
| 2019 | *Robles v. Domino's*: 9th Cir. ruling 15 Jan, US Supreme Court denied cert 7 Oct | Websites and apps tied to a place of business are exposed under ADA Title III |
| 2019 | Accessible Canada Act (Royal Assent 21 June, in force 11 July) | Canada's federal goal is "barrier-free by January 1, 2040" |
| 2019 | European Accessibility Act, Directive (EU) 2019/882 (signed 17 Apr) | Product and service accessibility is now an EU market-access issue |
| 2023 | WCAG 2.2 (5 Oct): 9 new SC, 4.1.1 Parsing removed | Targets, focus, cognition and authentication |
| 2024 | ADA Title II web rule (Federal Register 24 Apr): WCAG 2.1 AA for US state and local governments | WCAG is now law-by-reference in the US public sector |
| 2025 | EAA requirements apply from 28 June 2025 | Consumer-facing ICT sold in the EU must comply |

## 2. Knowledge base

### 2.1 Standards and key criteria — **Strong** (normative W3C text)
- **POUR:** Perceivable, Operable, Understandable, Robust. WCAG 2.2 has 13 guidelines with criteria at levels A, AA and AAA. It is backward-compatible, so meeting 2.2 also meets 2.1 and 2.0. WCAG 2.2 is also ISO/IEC 40500:2025.
- **Contrast:** 1.4.3 requires **4.5:1** for normal text and **3:1** for large text (≥18 pt, or ≥14 pt bold). There is no rounding, so 4.499:1 fails. 1.4.6 (AAA) requires **7:1**. 1.4.11 Non-text Contrast requires **3:1** for UI component boundaries, states, focus indicators and meaningful graphics. Disabled controls are exempt, which is a trap: the user still has to *notice* a disabled control.
- **New in WCAG 2.2 (5 Oct 2023):**

| SC | Level | Requirement (short) |
|---|---|---|
| 2.4.11 Focus Not Obscured (Min) | AA | The focused element is not *entirely* hidden by author content (sticky bars, toasts, drawers) |
| 2.4.12 Focus Not Obscured (Enh) | AAA | No *part* of the focused element is hidden |
| 2.4.13 Focus Appearance | AAA | Focus indicator is ≥2 CSS px thick with 3:1 change in contrast |
| 2.5.7 Dragging Movements | AA | Anything done by dragging can also be done with a single pointer without dragging |
| 2.5.8 Target Size (Min) | AA | **24×24 CSS px**, with exceptions for spacing (24 px circle), an equivalent control, inline targets, user-agent controls, and essential cases (e.g. map pins) |
| 3.2.6 Consistent Help | A | Help mechanisms appear in the same relative order across pages |
| 3.3.7 Redundant Entry | A | Information already entered is auto-populated or available to select |
| 3.3.8 Accessible Authentication (Min) | AA | No cognitive-function test (recall, transcription, puzzles) unless an alternative or assist exists |
| 3.3.9 Accessible Authentication (Enh) | AAA | As above, with no object-recognition or personal-content exceptions |

- **Platform targets (Practitioner, from vendor guidance):** Android/Material: 48×48 dp (about 9 mm) with 8 dp spacing. Apple HIG: 44×44 pt. WCAG's 2.5.5 (AAA) is 44×44 CSS px.
- **WCAG 3:** still a **Working Draft** (latest update Sept 2026). W3C says it is "not expected to be a completed W3C standard for a few more years", that it will not supersede WCAG 2, and that teams should meet WCAG 2.2 now. **APCA is not normative.** An AG WG co-chair stated in 2024 that APCA is not in the current draft. Use APCA only as an exploratory second opinion, never as the pass/fail bar. — **Contested** (status still moving).

### 2.2 Disability spectrum and prevalence — **Strong**
- WHO: about **1.3 billion people (16%, 1 in 6)** experience significant disability (fact sheet, Mar 2023).
- Statistics Canada, Canadian Survey on Disability 2022: **27% of Canadians aged 15+ (8.0 million)** have a disability that limits daily activities. Most common types are pain-related (62% of those with a disability), flexibility (40%), and mobility and mental-health (39% each).
- Microsoft persona spectrum: Touch = one arm / arm injury / new parent. See = blind / cataract / distracted driver. Hear = deaf / ear infection / bartender. Speak = non-verbal / laryngitis / heavy accent. Microsoft's US limb example: about 26k permanent, 13M temporary and 8M situational, so designing for the permanent case serves 21M+.

### 2.3 Perception: contrast, CVD, low vision, glare — **Strong / Practitioner**
- Red-green colour vision deficiency affects about **1 in 12 males and 1 in 200 females** of Northern European ancestry (MedlinePlus Genetics). Blue-yellow CVD is rarer than 1 in 10,000. A red/green "OK/fault" pair with no other cue fails roughly 8% of male operators (1.4.1 Use of Colour).
- Low contrast text is the **#1 web failure**, found on 83.9% of home pages (WebAIM Million 2026).
- Glare (Practitioner): bright light lowers the effective contrast of any screen. Treat 4.5:1 as a *floor* for anything used outdoors and aim for AAA (7:1) on critical information. Avoid thin weights and mid-grey text on mid-grey surfaces, and offer a high-contrast theme.

### 2.4 Motor: targets, tremor, limited dexterity — **Strong (WCAG) / Practitioner (platform guidance)**
- 24 px (AA) is the floor. Platform guidance (48 dp / 44 pt) is a better default for touch; people with tremor or limited dexterity benefit from larger targets and generous spacing. Avoid placing destructive actions next to frequent ones.
- 2.5.7 means drawing, sliders, list reordering and timeline scrubbing each need a non-drag alternative (buttons, steppers, numeric entry). Fitts's Law covers acquisition time: bigger and closer targets are faster.
- Two-step confirmation or undo for irreversible actions (deleting data, sending payments) is safer than tiny "Are you sure?" buttons.

### 2.5 Cognitive and stress — **Strong (W3C COGA Note) / Moderate (stress literature)**
- W3C *Making Content Usable for People with Cognitive and Learning Disabilities* (WG Note, 29 Apr 2021) sets 8 objectives:
  1. Help users understand what things are.
  2. Help users find what they need.
  3. Use clear content.
  4. Help users avoid and correct mistakes.
  5. Help users focus.
  6. Don't rely on memory.
  7. Provide help.
  8. Support personalisation.
- Under stress everyone loses working memory, so apply Cognitive Load and Recognition Over Recall. Show state; don't make people remember it. Use plain error language ("Card expired — update your card to continue"), not codes.
- 3.3.8: no CAPTCHAs or forced password transcription. Allow paste and password managers, and support passkeys.

### 2.6 Motion and vestibular — **Strong**
- 2.3.3 Animation from Interactions (AAA): non-essential motion can be disabled. Vestibular reactions include nausea and migraine. Honour `prefers-reduced-motion` (CSS media query or JS).
- 2.3.1 (A): nothing flashes more than three times per second. This matters for alert animations and games.

### 2.7 Screen readers and semantics — **Strong**
- WebAIM Million 2026 found failures on 95.9% of home pages, averaging 56.1 errors per page. The top six were low contrast (83.9%), missing alt (53.1%), missing form labels (51%), empty links (46.3%), empty buttons (30.6%) and missing document language (13.5%). Those six account for 96% of detected errors.
- Implications for the design system: every icon-only button needs an accessible name (spec it in the component's documentation), inputs need visible labels rather than placeholders, use native elements first, and announce state changes such as status alerts through live regions, sparingly.

### 2.8 Legal landscape — **Strong (statutes) / not legal advice**
> This summary is for orientation only. It is not legal advice; confirm obligations with counsel.
- **Canada:** The *Accessible Canada Act* applies to federally regulated entities: federal departments, Crown corporations, banks, airlines, telecoms and broadcasters, the CAF and the RCMP. Its seven priority areas include ICT and procurement, and it sets the 2040 barrier-free goal. A private hardware or software maker is not generally in scope unless it sells to or contracts with in-scope bodies, where *procurement* pulls in accessibility requirements. Provincial acts also apply (e.g. Ontario's AODA).
- **US:** Section 508 governs federal ICT procurement and references WCAG 2.0 AA, so it matters for any US government customers. The ADA Title II rule requires WCAG 2.1 AA for state and local governments, and the April 2026 interim final rule moved deadlines to **26 Apr 2027** (population ≥50k) and **26 Apr 2028** (smaller). Title III litigation (Robles) covers public-facing sites.
- **EU:** The EAA has applied since 28 June 2025. EN 301 549 (v3.2.1, 2021) is the harmonised ICT standard for the Web Accessibility Directive, and an EAA-aligned revision is in progress. EN 301 549 incorporates WCAG and adds non-web software and hardware clauses, which is relevant to desktop software.

## 3. Methods — audit workflow

1. **Automated scan** with axe DevTools, Lighthouse or WAVE. This catches only part of the problem: in GOV.UK's 2017 test page with 143 known barriers, the best single tool found 37–41% and all ten tools together found 71%. Deque's 2021 study (a vendor study of 13k+ pages) found axe covered 57% of issues *by volume*. Criterion-based estimates are commonly 20–30%. **Treat a clean scan as necessary, not sufficient.**
2. **Keyboard-only pass:** check Tab order, a visible focus ring, no traps, Esc closes overlays, and that focus is never hidden under sticky panels (2.4.11).
3. **Screen reader pass:** NVDA + Firefox/Chrome on Windows, which matters for desktop apps, and VoiceOver on macOS/iOS. Complete one real task, not a page tour.
4. **Zoom and reflow:** 200% text resize (1.4.4) and reflow at 320 CSS px width, the equivalent of 400% zoom (1.4.10), with no loss of content.
5. **Contrast:** check every token pair, including states (hover, focus, selected, error) and charts against 1.4.11. Run CVD simulation on all status colours.
6. **Test with disabled users:** recruit and pay participants. Simulation is not a substitute (see §7).
7. **Acceptance criteria in user stories**, for example: "Given keyboard only, when the alert modal opens, then focus moves to its heading and Esc returns focus to the trigger."

## 4. Pattern checklist (design system + product)

**Tokens and foundations**
- [ ] Every text/background token pair is documented with its ratio. Body text ≥4.5:1; critical text targets 7:1.
- [ ] UI borders, icons, chart strokes and **focus rings** are ≥3:1 against adjacent colours.
- [ ] A dedicated focus token: ≥2 px, high-contrast, and visible on dark, light *and* image/video backgrounds (a dual-ring outline).
- [ ] Status semantics (`color.alert.warning` / `color.alert.caution` / `color.alert.advisory`, plus `color.status.*` for success) are never colour-only: pair each with an icon, a shape and a text label. CVD-checked.
- [ ] High-contrast and dark themes are defined as token sets, not one-off overrides.
- [ ] Motion tokens include a reduced-motion variant, and no flashing above 3 Hz.

**Components**
- [ ] Minimum target of 24 px for AA, but the **DS default is 44–48 px** for touch components, with spacing ≥8 px.
- [ ] Icon-only buttons have a required `aria-label` / accessible-name prop documented.
- [ ] Inputs have persistent visible labels, with errors in text linked to the field.
- [ ] Draggable components (sliders, sortable lists, timelines) offer a non-drag alternative.
- [ ] Destructive or irreversible actions use two-step confirmation or undo, kept spatially separated.
- [ ] Toasts and sticky headers never cover the focused element. Critical alerts persist until acknowledged.

**Flows**
- [ ] Data already entered is reused (e.g. shipping → billing address) (3.3.7).
- [ ] Login works with a password manager or passkey and has no cognitive test (3.3.8).
- [ ] Help and support are in a consistent location (3.2.6).
- [ ] Alert copy is plain and action-first. Units and thresholds are shown, not remembered.

## 5. Designer tendencies that cause accessibility failures

| Tendency | Failure it causes | Psychology cross-link |
|---|---|---|
| Accessibility as final QA | Late retrofits that get cut at release | Default Bias: whatever ships in the DS is what everyone uses |
| Low-contrast "premium" aesthetic | Fails 1.4.3 and is unreadable in bright light | Aesthetic-Usability Effect, Contrast |
| Colour-only status (red/green dots) | Invisible to about 8% of men with CVD | Signifiers, Visual Hierarchy |
| Placeholder-as-label | Label disappears and memory load rises | Recognition Over Recall, Cognitive Load |
| Designing at 1x on a perfect monitor indoors | Tiny targets and glare failures | Empathy Gap, Fitts's Law |
| Icon-only controls "everyone understands" | No accessible name and ambiguous meaning | Curse of Knowledge |
| Ableist / one-size personas | Excludes permanent, temporary and situational users | Empathy Gap |
| Decorative motion everywhere | Vestibular harm and distraction under stress | Cognitive Load |
| Hiding focus rings because they're "ugly" | Keyboard users get lost | Signifiers |

## 6. Art and design history lineage

- **Isotype (Otto Neurath, Vienna, 1920s):** pictorial statistics for the general public, an early "perceptible information" system.
- **Otl Aicher, Munich 1972 Olympics:** pictograms drawn on a square grid with 45°/90° angles for a multilingual audience. They later shaped airport wayfinding (Frankfurt) and are the ancestor of modern product icon sets.
- **Ron Mace and Universal Design (1997):** seven principles. Mace originated the term "universal design".
- **Pattie Moore (three years from c. 1980):** an industrial designer who disguised herself as an 85-year-old across US cities (*Disguised*). She seeded the use of "empathy tools" and age suits. **Contested:** disability simulation is now criticised for producing pity and inaccurate insight. Prefer co-design with disabled people (Holmes).
- **Curb cuts (1945/1972):** the founding metaphor of inclusive design.

## 7. Reading list (ranked)

1. W3C, *WCAG 2.2* and *What's New in WCAG 2.2* — https://www.w3.org/WAI/standards-guidelines/wcag/new-in-22/
2. Kat Holmes, *Mismatch: How Inclusion Shapes Design* (MIT Press, 2018) — https://mitpress.mit.edu/9780262539487/mismatch/
3. Microsoft Inclusive Design toolkit and *Inclusive 101* guidebook — https://inclusive.microsoft.design/
4. W3C COGA, *Making Content Usable* — https://www.w3.org/TR/coga-usable/
5. WebAIM Million (annual) — https://webaim.org/projects/million/
6. Understanding SC 1.4.11 Non-text Contrast and 2.5.8 Target Size — https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html
7. Game Accessibility Guidelines — https://gameaccessibilityguidelines.com/ and the Xbox Accessibility Guidelines — https://learn.microsoft.com/en-us/gaming/accessibility/guidelines
8. A. G. Blackwell, "The Curb-Cut Effect", SSIR 2017 — https://ssir.org/articles/entry/the_curb_cut_effect
9. GOV.UK, "What we found when we tested tools on the world's least-accessible webpage" — https://accessibility.blog.gov.uk/2017/02/24/what-we-found-when-we-tested-tools-on-the-worlds-least-accessible-webpage/
10. NC State, *Principles of Universal Design* — https://design.ncsu.edu/research/center-for-universal-design/

## Sources

- https://www.w3.org/WAI/standards-guidelines/wcag/new-in-22/
- https://www.w3.org/WAI/standards-guidelines/wcag/
- https://www.w3.org/WAI/standards-guidelines/wcag/wcag3-intro/
- https://www.w3.org/press-releases/1999/wcag/
- https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html
- https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html
- https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html
- https://www.w3.org/WAI/WCAG22/Understanding/animation-from-interactions.html
- https://www.w3.org/TR/coga-usable/
- https://www.yatil.net/blog/wcag-3-is-not-ready-yet (APCA status, quoting AG WG co-chair, 2024 update)
- https://webaim.org/projects/million/
- https://www.who.int/news-room/fact-sheets/detail/disability-and-health
- https://www150.statcan.gc.ca/n1/daily-quotidien/231201/dq231201b-eng.htm
- https://www.canada.ca/en/employment-social-development/programs/accessible-canada/act-summary.html
- https://www.canada.ca/en/employment-social-development/programs/accessible-canada-regulations-guidance.html
- https://commission.europa.eu/strategy-and-policy/policies/justice-and-fundamental-rights/disability/union-equality-strategy-rights-persons-disabilities-2021-2030/european-accessibility-act_en
- https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32019L0882
- https://accessible-eu-centre.ec.europa.eu/content-corner/news/eaa-comes-effect-june-2025-are-you-ready-2025-01-31_en
- https://www.etsi.org/human-factors-accessibility/en-301-549-v3-the-harmonized-european-standard-for-ict-accessibility
- https://www.ada.gov/resources/2024-03-08-web-rule/
- https://www.section508.gov/manage/laws-and-policies/
- https://www.supremecourt.gov/docket/docketfiles/html/public/18-1539.html
- https://ssir.org/articles/entry/the_curb_cut_effect
- https://inclusive.microsoft.design/
- https://inclusive.microsoft.design/tools-and-activities/Inclusive101Guidebook.pdf
- https://awards.ixda.org/projects/microsoft-inclusive-toolkit
- https://mitpress.mit.edu/9780262539487/mismatch/
- https://mitpressbookstore.mit.edu/book/9780262539487
- https://medlineplus.gov/genetics/condition/color-vision-deficiency/
- https://www.deque.com/blog/automated-testing-study-identifies-57-percent-of-digital-accessibility-issues/
- https://accessibility.blog.gov.uk/2017/02/24/what-we-found-when-we-tested-tools-on-the-worlds-least-accessible-webpage/
- https://gameaccessibilityguidelines.com/
- https://learn.microsoft.com/en-us/gaming/accessibility/guidelines
- https://design.ncsu.edu/research/center-for-universal-design/
- https://www.ageing.ox.ac.uk/blog/Ageing-in-America-40-years-on%20
- https://languagecollections-blog.lib.cam.ac.uk/2022/05/13/otl-aicher-a-visual-communication-innovator/
- https://support.google.com/accessibility/android/answer/7101858?hl=en
- https://developer.apple.com/design/human-interface-guidelines/accessibility
