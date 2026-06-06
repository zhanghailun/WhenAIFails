# Management Science Writing Skill

A compact, reusable guide for writing theory-driven `Management Science` (and similar OM / OR-style) papers. The goal is not to weaken rigor. The goal is to make the rigor serve a stronger managerial story.

## Core Mindset

A management science paper should not read like a technical note that happens to add managerial implications at the end. It should read like a paper motivated by an economically important question, where the modeling and theorems are tools for uncovering a managerial insight.

In practice:

- Start from the managerial problem, not from the technique.
- Keep reminding the reader why the result matters economically.
- Explain the trade-off behind the result, not only the result itself.
- Translate every theorem into design, policy, or practice.
- Preserve formal precision; never oversell beyond what the theorem proves.

The prose should generally move in the order: **structural insight → economic question → formal result → managerial meaning → practical implication**.

## Writing Rules

### 1. Lead with the question the manager cares about
Open a section by reminding the reader what was just established, raising the next economic question, and stating what this section will show and why it matters. Avoid openings that only announce what will be derived.

### 2. Translate structure into value
Whenever the paper identifies a structural property (connectivity, sparsity, overlap, monotonicity, convexity), explain what it changes operationally, why that changes costs / profits / service, and what would happen without it.

### 3. Make the trade-off explicit
A management paper should show tension, not only improvement. For each main argument, state both sides: connected vs. disconnected, sparse vs. fully flexible, simple heuristic vs. optimal policy, practical design vs. infeasible benchmark.

### 4. After every theorem, answer three questions
What does it say mathematically? Why does the result happen (mechanism)? Why should a manager care? A paragraph that answers only the first is still too technical.

### 5. Keep the benchmark visible
The economic meaning of a result usually depends on the benchmark. Name the benchmark up front and keep referring to it after the theorem is stated, so the reader always knows "compared to what".

### 6. Use interpretation words deliberately
Phrases like *economic value, managerial message, operationally, benchmark, trade-off, practical implication, mechanism, failure mode, tractable prescription* are useful when they earn their place. They should explain the result, not decorate it.

### 7. Precision over excitement
Prefer "same order as the benchmark", "captures the first-order value of X", "does not improve the order of cost savings". Avoid "same savings" when only an order result is proved, "optimal" unless optimality is formal, and vague praise such as "very effective" without saying relative to what.

### 8. Use narrative transitions, not mechanical ones
Replace "Below is our main result", "We next discuss", "It is easy to see" with transitions that explain function: "Lemma X bridges structure to performance", "The next theorem is the main quantitative payoff", "Corollary X gives the operational implication".

### 9. Use short pivot sentences
Short sentences mark shifts in logic and guide the reader: "The natural question is then economic." "We also show the corresponding trade-off." "This result matters operationally."

### 10. Justify modeling assumptions in practice
If the analysis fixes a parameter, takes a limit, or adopts a particular policy, explain why that choice is sensible in the application. The reader needs to know the assumption is not arbitrary and the conclusion is likely to matter in practice.

### 11. Carry constants explicitly
A management science audience forgives loose prose more than loose math. Whenever a result asserts an asymptotic claim, the proof must carry an explicit constant through every step.

- State the threshold constant explicitly rather than "small enough".
- Carry an explicit lower bound on the structural quantity through perturbation arguments.
- Distinguish per-element from total perturbations; combinatorial factors matter.
- If two parallel results use different constants, either reconcile them or explain the mechanism behind the gap. A factor-of-`N` discrepancy is an insight, not an embarrassment.

### 12. Parallel structure across cases
When a section studies several variants of the same phenomenon, give each case the same internal template:

1. One sentence stating which primitive is fixed and which varies.
2. A sentence giving the explicit bound or set on the varying primitive.
3. One or two sentences of real-world interpretation.
4. One sentence stating the manager's commitment (which rule is used and why).

Parallel structure lets the reader notice substantive differences without re-parsing prose.

### 13. Quantitative comparison across parallel results
When two parallel propositions deliver the same qualitative conclusion under different thresholds, compare them quantitatively:

1. State both thresholds in big-`O` form with the same constants visible.
2. Report the ratio in words ("Case A tolerates fluctuations `N` times looser than Case B").
3. Explain the mechanism (often one case benefits from a normalization the other lacks).
4. Translate the gap into a managerial sentence about which source of variation to fear most.

## Architecture for Robustness / Extension Sections

Sections that extend a base result to more general environments are the easiest place to drift into a bullet list of cases. Use this structure.

**Setup: one unified formulation, then a menu of cases.** Write a single setup block that (i) introduces the worst-case or sample-path version of the central structural quantity once, (ii) states the single lemma that carries through with the worst-case quantity in place of the stationary one, (iii) previews cases by source of non-stationarity, not by technique, and (iv) defers the unified quantitative payoff to a master theorem at the end.

**Each case: four blocks in this order.**
1. A short problem-statement paragraph following the parallel-structure template.
2. A single proposition, written in the same format as analogous propositions earlier.
3. A streamlined proof carrying explicit constants.
4. A managerial-insight paragraph following the four-part template (below).

Resist embedding interpretation inside the proof or breaking the proposition into sub-claims.

**Closing paragraph.** Name the three (or more) cases in parallel clauses, state the common conclusion in one sentence using the unified quantity, and translate the pattern into a single practical checklist item for the manager.

### When to hoist the master theorem into its own subsection

Symptoms of wrong structure: propositions keep forward-referencing a master theorem; the master theorem subsumes results from more than one preceding subsection; the theorem's interpretation is longer than the discussion that invokes it.

When two or more apply, move the master theorem out of the case section into a short closing subsection that (i) explains in one sentence why the extensions reduce to the same condition, (ii) states the theorem, (iii) lists which prior propositions verify its hypotheses, (iv) spells out scope by noting what the theorem does *not* assume, (v) closes with one paragraph translating the theorem into economic meaning and practical upshot.

### Sample-path / worst-case formulations

Extending a stationary theorem to a non-stationary setting rarely requires re-proving it. Replace the stationary quantity by its sample-path worst case and check the original proof goes through. Define the worst-case quantity in one display, note in one sentence which step uses it, then frame the rest of the section as verification exercises.

## The Managerial-Insight Paragraph: Four-Part Template

After each proposition, write one paragraph in this order:

1. One sentence naming which regime the proposition captures.
2. One sentence on the mechanism (continuity, weighted average, interior point, cross-segment feasibility, etc.).
3. One sentence on operational implication: what the manager can do, offline vs. real time, with which data.
4. One sentence on the failure mode or trade-off: what happens if the hypothesis fails, and what becomes the complementary priority.

The fourth sentence is the one most often missing. It is the one the management reader remembers.

## Link-Forward and Link-Back Transitions

- Link back at the opening: "Section X showed that efficiency survives on the supply side. A more pressing concern is on the demand side."
- Pose the question the section answers.
- Preview the payoff and its location.
- Close a case and name the next one with parallel phrasing.

## How to Revise a Technical Paragraph into a Management Science Paragraph

Use this conversion template, in order: state the formal object → say what it means in words → explain the mechanism → state the managerial implication. Not every paragraph needs all four sentences, but most theory paragraphs should follow this logic.

## Section-Level Storytelling Template

For a theory section: link back → raise the next economic question → clarify the benchmark and asymptotic setting → establish the benchmark result → show how the new design changes it → state the main theorem as the payoff → interpret corollaries in managerial language → close with concrete design or policy implications.

## Sections that Fix a Proxy and Optimize over Design

For late-stage sections that combine optimization, structural conditions, and prescription:

- Open with scope and intuition, not appendix-level algebra. Move algebraic justification of the objective to the appendix unless the main argument requires it.
- Link back only when the hinge needs it; avoid stock phrases like "natural follow-up question".
- State the problem and propositions with clean quantifiers. Fix what is primitive vs. choice object. Spell out "optimal" relative to which feasible set. Keep graph or combinatorial claims literally exact and tie them to the manager's decision budget.
- One home for each design insight. If decomposition of the proxy already signals which term is the design lever, do not repeat the discussion before the design subsection. A short bridge is enough.
- Managerial content in prose, not lists, in the body. Bullets are for slides and notes, not for the published body.
- For named regimes where a closed-form rule is provably optimal on a stated class of designs, say so explicitly: the regime, the economic reading, and why the rule is easy to implement.
- For extensions beyond the leading case, keep the body short and move longer notation to the appendix with a clear cross-reference.
- Lock terminology across body and appendix: one term per object.

## Introduction Writing

The introduction is a self-contained story that sells the research question to a busy editor and to a reader who has not seen the technical work. It should be readable aloud and lead from a familiar business reality to a formal research question and back to a managerial takeaway.

### Six-paragraph narrative architecture

1. **P1 Context.** Hook with the real-world setting in plain language. End by naming every decision object the paper studies.
2. **P2 Trade-off.** Make the central tension concrete through one domain-grounded example with numbers. Show both extremes and why neither works. Foreshadow the analytical message.
3. **P3 Difficulty.** Explain why the problem is hard on its own terms (stochastic environment, combinatorial design space, joint optimization). Justify the need for a structural insight. Do not preview the answer.
4. **P4 Research Question.** Identify the closest prior work, describe what it assumes and proves, name precisely which assumptions are restrictive in your application, and explain in one sentence why prior techniques do not carry over. State the research question as one interrogative sentence. Preview the methodological shift required, without revealing the answer.
5. **P5 Our Answer (managerial).** Answer P4 at a managerial level. Name the structural condition, describe the practical recipe, state what it means for the manager. Defer technical specifics to the contributions block. Close by pointing to it.
6. **Contributions block.** Four (sometimes five) formal contributions, each with a bold lead phrase and two to four sentences. This is where big-`O` orders, theorem references, decompositions, and numerical evidence live.
7. **P6 Roadmap.** One paragraph, one sentence per section.

A reader who stops at P2 should already understand the trade-off; at P4, the research question; at P5, the managerial takeaway. The contributions are for the reader who wants the technical spine.

### Separate the managerial answer (P5) from the contributions

- **P5 says what the paper means.** Prescriptive, plain-language, legible without the technical vocabulary. Verbs: capture, reduce to, need not.
- **The contributions block says what the paper proves.** Formal, with theorem references, explicit orders, characterizations, decompositions, citations.
- Test: if a sentence could appear in both, it belongs in the contributions and should be stripped from P5.

### Frame the paper as a new research question, not an extension

Avoid "we extend X to a more general setting"; that sounds incremental. In P4: state what prior work proves, name its restrictive assumptions, explain why its technique does not carry over, state the question, preview the methodological shift. Reframes the contribution from "we generalize X" to "we ask a question X cannot answer".

### Lead with the realistic regime, not the baseline

Open P1 with the regime practitioners actually face (skewed demand, time-varying preferences, heterogeneous segments). The tractable baseline of prior work belongs in P4. Anchor in business reality with a concrete fact or visible platform example.

### Keep all decision variables visible from P1

Every decision object that appears in the contributions block must be named in P1 and stay visible through P2 and P3. A common failure is to introduce one lever in P1 and surprise the reader in P5 by optimizing a second.

### Contributions block: four-item template

Each item has a bold lead phrase and two to four sentences.

1. **Model / representation.** What you formulate, what it generalizes, which mathematical object encodes the problem. Emphasize that this is the unified analytical language used throughout.
2. **Main structural theorem and robustness.** The central equivalence or sufficiency result. Fold robustness (general inputs, non-stationary environments) into the same item so the reader sees one object, not base case plus extension.
3. **Optimization / prescription.** The item that distinguishes the paper from prior work. State the closed-form structure, the class of instances on which a simple rule is provably optimal, and the precise form of the optimum.
4. **Numerical evidence.** Environments covered, parameter ranges, benchmarks, and three or four qualitative findings that match the theory.

Use formal verbs: formulate, prove, characterize, decompose, identify, validate. Avoid soft phrases such as "we explore", "we discuss", "we develop insights".

## Anti-AI, Pro-Human Prose

Management science readers are fast and skeptical. Prose that reads AI-generated loses them.

- Replace decorative verbs and nouns with plain ones (`prominent deployments` → `well-known examples`; `renders the problem analytically intractable` → `makes the problem hard to solve analytically`; `demand heterogeneity` → `this imbalance`).
- Delete filler adjectives: `inherently`, `fundamentally`, `significantly`, `truly`.
- Avoid AI-trope openers: `Remarkably`, `Astonishingly`, `At a high level`. Use `Surprisingly` only when the claim genuinely is surprising.
- Use `that is` or `namely` to unpack a definition rather than parenthetical em-dashes.

Aim to sound like a human researcher explaining the problem to a colleague.

## Preserve Precision When You Simplify

Some technical phrases survive even an aggressive plain-English pass because they carry meaning the theorem actually proves.

- Keep `same order as the benchmark`, not `same savings`.
- Keep `relative cost savings of order \Omega(1/\sqrt{S})`, not `comparable cost savings`.
- Keep `provably optimal on a broad class of designs`, not `always optimal`.
- Keep `combinatorially explosive` or `doubly exponential` when literally true, not `very large`.
- Keep the established technical phrase the rest of the paper uses over a plain-English substitute the body never introduces.

A good revision pass first rewrites for plain language, then restores the one or two technical phrases whose looser substitutes would mislead a reviewer.

## Terminology Lock

Lock one term per concept and use it everywhere in introduction, body, and appendix. Small vocabulary drift is the single most common source of referee complaints about clarity. A one-line terminology lock in the header comment block pays for itself at proofreading.

## Accuracy of Numerical and Empirical Claims

Every advertised feature in the contributions (lead times, lost sales, multiple utility models, etc.) must be implemented in the body. Before finalizing the contributions, search the body for each claim and confirm it. The same rule applies to theoretical claims: if the body proves an order bound only under a stated condition, the contributions may not assert it for any setting. The introduction is the paper's promise to the referee.

## Annotation Comment Structure

For a section that will be revised many times, use explicit comments.

Header comment block: each paragraph's role in one or two lines (overall logic flow), and the design principles that constrain word choice (lead with realistic regime, keep every lever visible, terminology lock, local style rules).

Per-paragraph comment: **Role** (what the paragraph does narratively), **Internal Logic** (order of ideas inside), **Big Picture** (what it sets up for the rest of the paper).

Trailing summary block: paragraph roles and approximate word counts; the role split between P5 and the contributions; a one-line style check.

## Local Style Constraints (per project)

Set these once at the top of the project and enforce throughout. A typical management science profile:

- Avoid em dashes.
- Avoid semicolons.
- Avoid emphasis font.
- Prefer readable, direct sentences over dense technical compression.
- Preserve notation and theorem precision.

## Revision Checklist

**General narrative**

- Does the opening raise a managerial or economic question?
- Does each theorem have interpretation after it (mechanism + managerial meaning)?
- Is the benchmark clear and kept visible?
- Is the trade-off explicit?
- Are claims stated with the same precision as the theorem?
- Are practical implications visible before the conclusion?
- Does the prose obey the local style constraints?

**Multi-case sections**

- Exactly one setup block defines the worst-case / sample-path quantity once?
- Each case follows the same four-block template?
- Master theorem in its own subsection rather than forward-referenced from inside a case?
- Closing paragraph names the common pattern and delivers a one-line diagnostic?

**Sections that fix a proxy then optimize design**

- Opening states scope and intuition without appendix-level algebra?
- Combinatorial / budget statements literally correct and tied to the manager's decision object?
- Each design insight developed in one place, with at most a short forward bridge?
- Terminology identical in body and appendix material tied to the same results?

**Rigor on constants**

- All thresholds stated with explicit constants?
- Per-element vs. total perturbations distinguished and justified by combinatorial factors?
- Parallel propositions with different constants either reconciled or explained as mechanism-driven insight?

**Managerial-insight paragraphs**

- Each post-proposition paragraph includes a failure-mode or trade-off sentence?
- Each translates the mechanism into an operational verb the manager can execute (precompute, solve, verify, monitor)?

**Introduction**

- P1 opens with a practitioner-facing fact, not a technical definition?
- Every decision variable in the contributions block already named in P1?
- P2 grounded in a single concrete example with numbers?
- P3 explains difficulty without previewing the answer?
- P4 research question stated as an interrogative sentence?
- P5 reproduces no sentence from the contributions block, ends by pointing forward?
- Contributions use active formal verbs (formulate, prove, characterize, identify, validate)?
- Paper framed as answering a new question, not extending prior work?
- Closest prior work named explicitly with its restrictive assumptions stated precisely?
- Every numerical or empirical claim in the contributions has a matching body section?
- Big-`O` claims stated with the same hypotheses under which they are proved?
- Decorative openers used at most once and on a defensible claim?
- Definitions unpacked with `that is` or `namely`, not em-dashes?
- One term locked per concept across introduction, body, and appendix?

## One-Sentence Summary

Write the paper so that every technical result is immediately translated into economic meaning, managerial insight, and practical design guidance.
