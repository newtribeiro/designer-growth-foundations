# Module G — Game UX & player psychology

**Who this is for.** Designers moving into games from product UX: HUDs, menus, onboarding, progression, settings and accessibility in any genre.

**Why this matters.** Product UX trained you to make tasks faster. Game UX starts from the opposite point: the difficulty is the product, and players chose to be there. Your job is to remove *unintended* friction (unclear UI, unreadable feedback, confusing menus) while protecting the *intended* challenge the game is built around.

**The shift:**
- **From** task efficiency, conversion and "reduce friction everywhere"
- **To** motivation (competence, autonomy, relatedness), flow (challenge matched to skill), fairness, and keeping the *right* friction
- **For the interface:** *inform without stealing attention from play.* The UI wins when players read the game's state at a glance and feel their success came from their own skill.

Evidence grades: **Strong** (peer-reviewed, replicated) · **Moderate** (peer-reviewed, limited replication or a large applied dataset) · **Practitioner** (industry talks and guidelines, widely adopted) · **Contested** (weak or disputed evidence). Platform certification rules are a design constraint, not legal advice.

---

## 1. Lineage

| Year | Event / work | What it taught |
|---|---|---|
| 1985 | *Super Mario Bros.* World 1-1 (Nintendo) | Teach through level design rather than text. The first Goomba and the first ? block are safe lessons. (Widely documented design history; Practitioner) |
| 1990 | Csikszentmihalyi, *Flow* | Optimal experience happens when challenge matches skill and goals and feedback are clear |
| 1995 | Endsley, situation awareness model (Human Factors 37(1)) | SA has three levels: L1 perceive, L2 comprehend, L3 project. Real-time HUDs serve all three |
| 1996 | Bartle, "Hearts, Clubs, Diamonds, Spades" | First player typology (Achievers, Explorers, Socialisers, Killers). By its author's own account it is "not conventionally rigorous" |
| 2002 | Medlock et al., RITE method (UPA 2002, Microsoft Games) | Fix problems between participants. Bring decision-makers into the testing |
| 2004 | Hunicke, LeBlanc & Zubek, MDA | Designers build Mechanics, which produce Dynamics, which players feel as Aesthetics. Players experience it in reverse |
| 2006 | Ryan, Rigby & Przybylski, SDT in games (Motivation & Emotion 30(4)) | Competence, autonomy and relatedness predict enjoyment and continued play (PENS measure) |
| 2007 | Jenova Chen, "Flow in Games (and Everything Else)", CACM 50(4) | Build adaptive choices into the core activity instead of difficulty menus |
| 2009 | Fagerholt & Lorentzon, *Beyond the HUD* (Chalmers thesis) | Four interface types (diegetic, non-diegetic, spatial, meta) from two axes: is it in the fiction, and is it in the 3D space? |
| 2009 | Desurvire & Wiberg, PLAY heuristics | Heuristic evaluation adapted to games and validated against high- and low-rated titles |
| 2012 | Game Accessibility Guidelines launched | Accessibility guidance in three tiers: basic, intermediate, advanced |
| 2016 | First Game UX Summit (Epic Games, Durham NC, May 12) | Game UX became its own discipline. Ubisoft Toronto co-hosted 2017 |
| 2017 | Hodent, *The Gamer's Brain* (CRC Press) | Game UX = **usability + "engage-ability"**, grounded in perception, attention and memory |

## 2. Knowledge base

### 2.1 Perception, attention, memory in play (Hodent) — Practitioner, built on Strong cognitive science
- Perception is subjective. Players see what they expect, so meaning depends on the game's existing conventions (colors, icon shapes, sound cues).
- Attention is the scarcest resource. Players can't multitask. When attention divides, performance drops. **Selective Attention**: in a high-intensity moment, anything outside the action stops existing, including most of your HUD.
- Memory is fallible. Players forget tutorials. Teach by doing, then reinforce.
- **Usability pillars** (as Hodent presents them in talks and the book): signs and feedback, clarity, form follows function, consistency, minimum workload, error prevention and recovery, flexibility.
- **Engage-ability**: motivation (SDT and meaningful rewards), emotion (game feel, discovery), and game flow (difficulty and learning curves).

### 2.2 Motivation
| Model | Core | Grade | Use in design |
|---|---|---|---|
| SDT / PENS (Ryan, Rigby, Przybylski 2006) | Competence, autonomy, relatedness. Intuitive controls and presence also matter | **Strong** | Feedback should build competence ("I understood why I failed"). Keep autonomy: offer choices, don't force a single path |
| Quantic Foundry Gamer Motivation Model (Yee) | 12 motivations in 6 pairs: Action (Destruction, Excitement), Social (Competition, Community), Mastery (Challenge, Strategy), Achievement (Completion, Power), Immersion (Fantasy, Story), Creativity (Design, Discovery). Factor analysis of 140k+ gamers | **Moderate** (large dataset, commercial, self-report) | Check your audience's profile rather than assuming it |
| Bartle 1996 | 4 types on 2 axes | **Contested / historical** | Useful as vocabulary only. Don't segment players with it |
| MDA (2004) | M→D→A | **Practitioner** | A UI choice is a mechanic too: a quest marker (mechanic) changes exploration (dynamic) and can turn discovery into errand-running (aesthetic) |

**Variable Reward** drives retention, but loot-box style rewards read as manipulation and draw regulatory scrutiny in some markets. Prefer rewards tied to mastery and visible progress (**Goal Gradient Effect**).

### 2.3 Flow & challenge — Strong (Csikszentmihalyi); Practitioner (Chen)
- Flow needs clear goals, immediate feedback, and challenge matched to skill. Any interruption breaks the **Flow State**.
- Chen's principle: adaptivity belongs inside the activity (optional paths, assist modes players opt into), not only in a difficulty menu at the start.
- Rule: pop-ups, tutorials and notifications never interrupt high-load moments. Queue them for natural pauses.

### 2.4 HUD types & placement
| Type (Fagerholt & Lorentzon 2009) | In fiction? | In 3D space? | Typical example | Design implication |
|---|---|---|---|---|
| Diegetic | Yes | Yes | An in-world map or an ammo counter on a weapon | Most immersive, but can be hard to read under pressure. Test legibility |
| Non-diegetic | No | No | Minimap, ability bar, inventory slots, score bar | Clearest. Keep it to the screen edges and minimal |
| Spatial | No | Yes | Health bars above units, range indicators, quest markers | Great for location-bound info. Watch clutter in crowded scenes |
| Meta | Yes | No | Low-health screen tint, blood splatter | Strong emotional signal. Pair with another cue for accessibility |

Map a game's HUD yourself. **Banner Blindness**: permanent panels get tuned out, so show secondary info on events or in pauses, and let players customise or hide HUD elements.

### 2.5 Real-time information under time pressure — Strong (SA, cognitive load) / Practitioner (glanceability)
- Map each HUD element to an SA level. **L1** (perceive): "enemy nearby." **L2** (comprehend): "my shield is down, so I can't survive this fight." **L3** (project): "the storm closes in 30 s." Show L1 during action; save L3 planning detail for menus, maps and pauses.
- Glanceability means one idea per element, readable in under a second, iconic before textual, and placed consistently.
- Peripheral cues (a color pulse at an edge, a directional sound indicator) beat text when attention is elsewhere. Use them sparingly or they become noise.
- **Cognitive Load**: the intrinsic load of play is already high. Any extraneous load from the UI comes straight out of the player's game.

### 2.6 Onboarding & tutorials — Practitioner
- Teach in context and just in time, the World 1-1 way. No front-loaded tour or wall of text.
- **Curse of Knowledge**: the team knows the jargon and the controls. A first-time player doesn't.
- Introduce one mechanic at a time, let the player practise it safely, then combine it with what they already know.

### 2.7 Feedback & "juice" — Practitioner (Swink, *Game Feel* 2008; Jonasson & Purho, "Juice it or lose it", 2012)
- Juice means amplified feedback (motion, sound, particles, screen shake). It makes actions feel good, but too much hides game state and can harm players sensitive to motion. Offer a reduce-motion or screen-shake setting.
- **Peak-End Rule**: end levels and sessions on a clear moment of achievement. **Feedback Loop**: make the cause of success or failure readable so players learn from it.

### 2.8 Fairness, monetisation & platform requirements
- Competitive games need visible, consistent rules; hidden advantages and unclear hit feedback feel unfair even when they aren't.
- Monetisation UX (currencies, bundles, timers) is where dark patterns cluster. Show real-money prices clearly and avoid fake urgency.
- Console and store platforms publish certification requirements (save behaviour, button prompts, system UI). Read the current versions for each platform you ship on and keep a dated log; they change.

### 2.9 Game accessibility — Practitioner
- Game Accessibility Guidelines (since 2012): basic, intermediate and advanced tiers.
- Xbox Accessibility Guidelines v3.2 (June 2023): 23 guidelines numbered 101–123, e.g. 101 Text display, 102 Contrast, 103 Additional channels for visual and audio cues, 112 UI navigation.
- Baseline: never encode meaning in color alone (many games already use color for teams), scalable subtitles and text, full control remapping, a reduce-motion option, and difficulty or assist options that don't shame the player.

---

## 3. Methods
| Method | How | Grade | Use |
|---|---|---|---|
| Think-aloud | Players narrate while playing | Practitioner | Works in menus and slow sections. During intense play, use retrospective think-aloud over a recording |
| RITE (Medlock et al. 2002) | Fix as soon as an issue appears, sometimes after one participant. Stakeholders observe | Practitioner | Fast iteration on tutorials, menus and HUD layouts |
| Telemetry / heatmaps | Event logs: deaths, quits, time per level, menu paths | Practitioner | Find where players get stuck or quit. Collect with consent and a clear privacy notice |
| Biometrics (eye tracking, EDA) | Gaze shows which HUD elements are actually read | Moderate (lab cost) | One eye-tracking study via a university lab when budget allows |
| Heuristic review | PLAY (Desurvire & Wiberg 2009), HEP (Desurvire et al. CHI 2004), Hodent's pillars | Practitioner | Pre-test sweep of each build |
| Competitive teardown | HUDs, menus and onboarding of 3–5 games in the same genre | Practitioner | Capture screenshots with dates and note conventions players already know |
| Review mining | Store reviews and community forums. Tag by theme and sentiment | Practitioner | Find recurring complaints about UI, difficulty and controls |

---

## 4. Game UI checklist
- [ ] Every HUD element mapped to an SA level and a reason to exist
- [ ] No pop-up, tutorial or notification interrupts a high-intensity moment
- [ ] HUD elements readable in under 1 s at 16:9, 21:9 and 16:10, and on a TV at couch distance
- [ ] Players can scale, move or hide non-essential HUD elements
- [ ] Feedback makes the cause of success and failure clear
- [ ] Onboarding teaches one mechanic at a time, in play
- [ ] Accessibility: color plus shape, scalable text and subtitles, full remapping, reduce motion, no flashing above 3 Hz
- [ ] Prices and currencies are clear; no fake urgency
- [ ] Platform certification requirements checked and logged with dates
- [ ] Sessions and levels end on a clear achievement (Peak-End Rule)

---

## 5. Designer tendencies (and the psychology they trip)
| Tendency | Why it happens | Counter |
|---|---|---|
| Designing for yourself as an expert player | **False Consensus Effect**, **Curse of Knowledge** | Recruit across skill levels. Test with first-time players |
| Information dumping ("we have the data, show it") | Product habit of surfacing everything | Budget by **Cognitive Load** and SA level |
| Productivity-app patterns (badges, streaks, nudges) everywhere | Transferring growth playbooks | **Variable Reward** and streaks can feel manipulative. Reward mastery instead |
| Interrupting play to teach or sell | Wanting the feature to be seen | **Selective Attention** and **Flow State**: defer to natural pauses |
| A permanent panel "for discoverability" | Fear of being ignored | **Banner Blindness**: it gets ignored anyway. Use event-driven display |
| Removing all friction | Product UX instinct | The challenge is the product. Remove only *unintended* friction |
| No visible progress | Focusing on single levels | **Goal Gradient Effect** plus **Feedback Loop**: show improvement over time |

---

## 6. Reading list (ranked)
1. Celia Hodent — *The Gamer's Brain* (CRC Press, 2017; 2nd ed. listed for 2026) — https://celiahodent.com/the-gamers-brain/
2. Ryan, Rigby & Przybylski (2006) — The Motivational Pull of Video Games — https://doi.org/10.1007/s11031-006-9051-8
3. Hunicke, LeBlanc & Zubek (2004) — MDA — https://users.cs.northwestern.edu/~hunicke/MDA.pdf
4. Jenova Chen (2007) — Flow in Games (and Everything Else), CACM — https://khoury.northeastern.edu/~lieber/courses/csu670/f08/materials/p31-chen-flow-in-games.pdf
5. Steve Swink — *Game Feel* (2008)
6. Quantic Foundry Gamer Motivation Model — https://quanticfoundry.com/gamer-motivation-model/
7. Desurvire & Wiberg (2009) — PLAY heuristics — https://link.springer.com/doi/10.1007/978-3-642-02774-1_60
8. Xbox Accessibility Guidelines — https://learn.microsoft.com/en-us/gaming/accessibility/guidelines
9. Bartle (1996) — read as history — https://mud.co.uk/richard/hcds.htm

---

## Sources
- https://www.oreilly.com/library/view/mastering-ui-development/9781787125520/78296d1f-f5be-4af9-8ed6-b47ece9c8bda.xhtml
- https://acuresearchbank.acu.edu.au/item/8q128/the-motivational-pull-of-video-games-a-self-determination-theory-approach
- https://khoury.northeastern.edu/~lieber/courses/csu670/f08/materials/p31-chen-flow-in-games.pdf
- https://users.cs.northwestern.edu/~hunicke/MDA.pdf
- https://quanticfoundry.com/gamer-motivation-model/
- https://mud.co.uk/richard/hcds.htm
- https://celiahodent.com/the-gamers-brain/
- https://thevideogamelibrary.org/book/the-gamer-s-brain-how-neuroscience-and-ux-can-impact-video-game-design
- https://www.designative.info/2019/03/28/the-ux-of-fortnite-celia-hodent/
- https://www.unrealengine.com/events/game-ux-summit-2016-recap-and-2017-event-announcement
- https://en.wikipedia.org/wiki/RITE_Method
- https://link.springer.com/doi/10.1007/978-3-642-02774-1_60
- https://gameaccessibilityguidelines.com/
- https://learn.microsoft.com/en-us/gaming/accessibility/guidelines
