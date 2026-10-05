# Module S — Safety-critical, enterprise & HMI design

This module covers what the Hack Design and uxtools.co libraries leave out: interfaces where an error can cost lives, equipment or a patient's safety. Use it if you design control-room, clinical, industrial, energy or transport software.

**The shift:** in consumer UX the cost of a bad design is friction and churn. In safety-critical UX it is loss of control. The design goal moves from *conversion and delight* to **situation awareness, error tolerance and calibrated trust in automation**.

---

## 1. Lineage — how this field was born from accidents

| Year | Event / work | What it taught designers |
|---|---|---|
| 1940s | Chapanis: shape-coded cockpit knobs (B-17 flap and landing-gear controls looked identical) | "Pilot error" was design error. Birth of human factors. |
| 1947 | Fitts & Jones: analysis of 460 "pilot error" incidents | Most errors were predictable from the control/display layout. |
| 1979 | Three Mile Island | Alarm flood: hundreds of alarms in the first minutes; a key indicator showed the *command* sent, not the valve's *actual* state. |
| 1985–87 | Therac-25 radiation overdoses (Leveson & Turner 1993) | Fast keyboard editing raced the software; cryptic "Malfunction 54" messages were routinely dismissed. |
| 2009 | Air France 447 | Automation handed control back in a degraded state; mode and stall cues weren't understood in time. |
| 2018–19 | Boeing 737 MAX (MCAS) | Automation that operators didn't know existed cannot be supervised. |


## 2. Knowledge base

### 2.1 Situation awareness (SA) — Endsley 1995
Three levels: **L1 Perception** (what's happening) → **L2 Comprehension** (what it means for my goals) → **L3 Projection** (what will happen next).
SA-oriented design principles (Endsley, Bolté & Jones, *Designing for Situation Awareness*, 2003/2011):
- Organise information around **operator goals**, not around subsystems or data sources.
- Present L2 and L3 **directly** (e.g. "tank reaches the low-level threshold in 4 min") instead of making operators compute them from raw values.
- Keep a **global overview** always visible; detail on demand.
- Make critical cues salient; reduce everything else.
- Watch the **SA demons**: attentional tunnelling, requisite memory trap, workload/fatigue/stress, data overload, misplaced salience, complexity creep, errant mental models, out-of-the-loop syndrome.
- Measure: **SAGAT** (freeze the simulation, ask probe questions; Endsley 1988), SART self-rating (Taylor 1990).
Grade: Strong (decades of aviation, military, medical research).

### 2.2 Human error — Reason 1990, Rasmussen 1983, Norman 1981
- **Slips** (right intent, wrong action), **lapses** (forgot a step), **mistakes** (wrong intent), **violations** (deliberate shortcuts).
- Rasmussen: skill-, rule-, knowledge-based behaviour — design differently for each.
- Norman's slip types: mode errors, capture errors, description errors (similar controls).
- **Swiss cheese model**: accidents pass through aligned holes in several defences; the UI is one layer.
- Design responses: forcing functions (interlocks, lock-ins, lockouts), constraints, undo, visible modes, error messages that state recovery. Confirmation dialogs only for irreversible or rare actions — routine confirmations get clicked through.
Grade: Strong.

### 2.3 Automation & trust
- **Ironies of Automation** (Bainbridge 1983): automating the easy parts leaves humans the hardest parts, with less practice and less awareness.
- **Stages × levels** (Parasuraman, Sheridan & Wickens 2000): automate information acquisition, analysis, decision selection or action implementation, each at a chosen level.
- **Automation surprises / mode awareness** (Sarter & Woods 1995): "What is it doing? Why? What will it do next?"
- **Trust calibration** (Lee & See 2004): avoid misuse (over-trust) and disuse (under-trust); show reliability and reasoning.
- Design: always show automation state, intent and next action; make takeover clean and fast; degrade gracefully with a clear explanation.
Grade: Strong.

### 2.4 Alarms & alerting
- Industrial benchmarks (EEMUA 191 / ISA-18.2 / IEC 62682): **< 1 alarm per 10 minutes** per operator is acceptable; 1–2 manageable; **≥ 10 annunciated alarms in any 10 minutes = alarm flood** (ISA-18.2 wording; standards are paywalled, figures checked via secondary sources). Priority mix ≈ **80% low / 15% medium / 5% high**. Standing alarms at handover < 5–10. Every alarm must require an operator action — otherwise it isn't an alarm.
- Aviation (14 CFR 25.1322): **red = warning**, **amber/yellow = caution**, advisory = any colour except red or green; red, amber and yellow use elsewhere on the flight deck must be limited so they don't dilute alerting.
- Message pattern: **what** happened + **why it matters** + **what to do**. Distinguish acknowledge vs reset, latching vs non-latching. Redundant coding (colour + shape + text + sound). Support shelving with accountability.
Grade: Strong (standards built from incident data). Sources: [EEMUA 191 summary](https://open-exam-prep.com/study-guides/nebosh-hse-process-safety/process-hazard-control/alarm-management-eemua191) · [14 CFR 25.1322](https://www.law.cornell.edu/cfr/text/14/25.1322)

### 2.5 High-performance HMI — ISA-101 (2015), Hollifield et al. (2008)
- Muted, mostly greyscale screens; **colour reserved for abnormal states**, so abnormal pops (*Von Restorff Effect*).
- Show values against their **normal range** (analog indicators, trends), not bare numbers.
- Display hierarchy: L1 overview → L2 area/unit → L3 detail → L4 diagnostic.
Grade: Moderate–Strong (industry consensus + incident evidence).

### 2.6 Workload
- **NASA-TLX** (Hart & Staveland 1988): mental, physical and temporal demand, performance, effort, frustration.
- **Multiple resource theory** (Wickens 2002): visual, auditory and manual channels compete less than two tasks on the same channel — use audio and haptics for alerts when eyes are busy.
Grade: Strong.

### 2.7 Remote monitoring
- A remote operator loses the cues of being on site (sound, vibration, smell) — the interface must substitute for them.
- Communication: show connection status and latency, and warn before a connection degrades.
- **Data freshness**: stale data must look stale (timestamp, greyed or hatched values).

### 2.8 Standards worth knowing
ISO 9241-110:2020 (interaction principles: suitability for the task, self-descriptiveness, conformity with expectations, learnability, controllability, use-error robustness, user engagement) · ISO 9241-210 (human-centred design process) · IEC 62366-1 (medical usability engineering — its *use-related risk analysis* and *summative validation* transfer well) · ISO 11064 (control centre ergonomics) · MIL-STD-1472H (human engineering) · FAA HF-STD-001 · ISA-101.01 · ISA-18.2 / IEC 62682.

## 3. Methods — how to work on safety-critical UI

1. **Goal-directed task analysis** (Endsley) → list SA requirements (L1/L2/L3) per operator goal.
2. **Cognitive task analysis / Critical Decision Method** (Klein): interview operators about real incidents and hard calls.
3. **Hierarchical task analysis** for procedures, including emergency procedures.
4. **Use-related risk analysis** (UI-FMEA): for each task step — possible use error → consequence → severity × likelihood × detectability → design mitigation.
5. **Off-nominal scenario testing**: loss of communication, equipment failure, sensor disagreement, shift handover. Measure time-to-detect, time-to-correct, errors, SAGAT probes, NASA-TLX.
6. **In-situ testing**: the real work environment — lighting, noise, interruptions, fatigue (end of shift).
7. **Heuristic review** using ISO 9241-110 + the SA principles above.

## 4. Pattern checklist (for operational software)

- [ ] Persistent overview of critical state (system status, connectivity, key resources, process state, mode) — never covered by modals or toasts.
- [ ] Mode always visible; mode changes announced.
- [ ] Projections shown directly (time to threshold, time to empty, projected state) — L3 SA.
- [ ] Alert colours reserved and tokenised (`color.alert.warning`, `color.alert.caution`, `color.alert.advisory`; success/OK lives in `color.status.*`, never in the alert namespace); brand colours never collide with them.
- [ ] Every alert = what + why + action; no alert without a required action; alert rate checked against benchmarks.
- [ ] Irreversible commands need a distinct deliberate action (not a reflexive "OK").
- [ ] Safe defaults.
- [ ] Stale data looks stale; latency shown when it matters.
- [ ] Redundant coding: colour + shape + text (+ sound for high priority).
- [ ] Values shown against normal ranges/trends, not only as numbers.
- [ ] Automation shows state, intent, next action, and how to take over.
- [ ] Degraded-mode UI designed, not left to chance.
- [ ] Event log and replay for handover and debriefing.

## 5. Designer tendencies that are dangerous here

- **Curse of knowledge** — designers are not operators; nothing replaces watching real operators under load.
- **Designing for the nominal path only** — the emergency path is the product.
- **Consumer-pattern transfer** — vanishing toasts, swipe-to-dismiss alerts, hidden menus, playful motion during critical states.
- **Minimalism that hides state** — "clean" can mean "operator can't see the problem".
- **Confirmation overuse** — trains click-through; reserve it for the irreversible.
- **Colour for brand or decoration** — dilutes alert meaning.
- **Optimism about automation** — design for its failure and the handover.

Psychology cross-links (`data/psych-principles.json`): *Cognitive Load*, *Feedback Loop*, *Feedforward*, *Mental Model*, *Signifiers*, *Selective Attention*, *Banner Blindness* (alarm fatigue), *Von Restorff Effect*, *Default Bias* (safe defaults), *Recognition Over Recall*, *Chunking*, *Negativity Bias*, *Weber's Law* (change detection), *Expectations Bias*.

## 6. Reading list (ranked)

1. Endsley, Bolté & Jones — *Designing for Situation Awareness* (2nd ed. 2011)
2. Reason — *Human Error* (1990)
3. Hollifield et al. — *The High Performance HMI Handbook* (2008)
4. Bainbridge — "Ironies of Automation" (*Automatica*, 1983) — short, free
5. Lee & See — "Trust in Automation: Designing for Appropriate Reliance" (*Human Factors*, 2004)
6. Wickens, Hollands et al. — *Engineering Psychology and Human Performance*
7. Norman — *The Design of Everyday Things* (revised 2013), chapters on error
8. Leveson — *Engineering a Safer World* (2011) and the Therac-25 investigation (1993)
