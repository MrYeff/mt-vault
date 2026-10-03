---
title: "Using artificial agents to understand laboratory experiments of common-pool resources with real agents"
tags:
  - model
  - simulation
authors:
  - "[[Literature/Authors/Wander Jager|Wander Jager]]"
  - "[[Literature/Authors/Marco A. Janssen|Marco A. Janssen]]"
publication date: 2002
source: https://marcojanssen.info/wp-content/uploads/2016/08/2002_Using_artificial_agents_to_understand_laboratory_experiments_of_common_pool_resources_with_real-agents.pdf
doi: 10.4337/9781781957240.00014
read status: Todo
⚠️:
  - audit failed
---
## Abstract

No separate abstract in chapter.

## Research Questions
> Research Questions extracted via LLM

- Can a heterogeneous artificial-agent model explain observed variation in real participants’ common-pool resource harvesting and collective outcomes?[^r1]

## Model
> Model extracted via LLM according to [[Model Notation]]

### What does it represent?
Eight Consumat agents allocate tokens between a fixed-return market and a common-pool resource, using satisfaction/uncertainty to choose a cognitive mode; the simulations are compared with earlier laboratory experiments.[^r2]

- State and equations below condense §§6.5–6.6; parameters without source values stay symbolic.[^r2][^r3]
- The chapter's neural predictor is a single-layer weighted-sum learner, rather than a multilayer network.[^r2][^r3]

```yml
World:
  agents: [Agent]
  endowment: 10 | 25
  investments: [[f64]] # round × agent
  returns: [[f64]]

Agent:
  svo: Individualistic | Competitive | Cooperative
  need_weights: [0..1] # social, personal, exploration; sum1
  satisfaction: f64
  uncertainty: 0..
  investment: 0..
  predictor_weights: [f64] # bias + three lag coefficients
  expected_other_tokens: f64
  cognition: Deliberate | Compare | Repeat | Imitate
```

### How does it work?
- The payoff/needs formulas and decision alternatives are given below. Each round's payoff uses the aggregate investments of all eight agents.[^r3][^r4]

```
AGENTS = 8
SAFE_RETURN = 0.05
COOPERATIVE_TOTAL = 36
NASH_TOTAL = 64
HISTORY_ROUNDS = 5
PREDICTOR_LAGS = 3
LEARNING_RATE = 0.5
HP_N_MIN = 0.5
HP_U_MAX = 0.1

payoff(x: f64, total: f64, endowment: f64) -> f64:
  F = (23 * total - 0.25 * total^2) / 100
  out = SAFE_RETURN * endowment if x == 0 else
        SAFE_RETURN * (endowment - x) + (x / total) * F

needs(agent: Agent, returns: [f64], total: f64):
  personal = own_return
  social = match agent.svo:
    Individualistic: own_return
    Competitive: 1 - exp(-C * own_return / mean(all_agents_returns))
    Cooperative: exp(-C^2 * (total - COOPERATIVE_TOTAL)^2)
  exploration = standard_deviation(own_returns over HISTORY_ROUNDS)
  satisfaction = dot(agent.need_weights, [social, personal, exploration])
  uncertainty = standard_deviation(own_returns over HISTORY_ROUNDS)

choose_investment(agent: Agent, previous_mean: f64) -> f64:
  if dissatisfaction and certainty: # Deliberate
    out = argmax(all feasible investments, predicted need satisfaction)
  if dissatisfaction and uncertainty: # Compare
    out = argmax([agent.previous_investment, previous_mean],
                 predicted need satisfaction)
  if satisfaction and certainty: # Repeat
    out = agent.previous_investment
  if satisfaction and uncertainty: # Imitate
    out = previous_mean
```

- Satisfaction is compared with `N_MIN`, uncertainty with `U_MAX`; the text does not fix equality tie handling. Deliberation evaluates alternatives using expected other investment and full knowledge of the payoff; comparison evaluates own versus population-average previous investment. Reasoned modes update mental-map information; resulting consumption changes payoff, needs and uncertainty.[^r2][^r4]
- Predictor: `EY[t,i]=W[t,i,0]+sum_{k=1..3} W[t,i,k]*Y_LAG[t,k]`, with previous total other-agent investments as inputs. Error `DELTA=Y_OBS−EY`; printed Eq.6.7 is `ΔW=LEARNING_RATE * DELTA * y_i/||y_i||`. The chapter labels this Widrow–Hoff learning, but its indexed scalar/vector correspondence and bias update are not fully specified; do not replace it with an invented standard gradient.[^r4]
- Source conflict: Eqs.6.3 and6.5 have square roots and sum inclusively from `t−5` to`t` while dividing by4; surrounding prose says standard deviation over the last five rounds. The block follows the prose five-round interpretation; exact replication must resolve this six-term/five-round inconsistency. `C`, initial-history handling and threshold ties are not supplied here.[^r3]

### What can it answer?
- Compare Homo economicus (only deliberates) against Homo psychologicus (`N_MIN=0.5`, `U_MAX=0.1`, all four modes); needs configurations personal, personal+social, personal+exploration, and all three; vary all counts of individualistic/competitive/cooperative agents summing to8. Initial total expectations are64 for individualists/competitors and36 for cooperators.[^r5]
- Test homogeneous needs/SVO and heterogeneous normalized need weights: draw each weight uniformly on(0,1), divide by their sum; average25 random weight allocations per SVO combination. Compare10/25-token conditions with six lab experiments using mean investment, mean within-round investment SD, and cumulative absolute round changes (Tables6.2–6.4; composite difference Eq.6.9). The10-token lab summaries cover30 rounds and25-token summaries20.[^r5]
- Psychological modes and heterogeneous needs/SVO can better reproduce fluctuations than universal rational deliberation; the chapter proposes follow-up human experiments rather than claiming these mechanisms are uniquely validated.[^r5][^r6]

### Where does it apply?
It models the specific no-communication common-pool laboratory game and generates hypotheses about cognitive/SVO heterogeneity. Additional empirical data are needed to distinguish mechanisms.[^r2][^r6]

## Metadata
### References

The accessible author-hosted chapter ends at printed p.102 with acknowledgements and supplies no bibliography. No original reference links were present in the import snapshot. A full consolidated book bibliography has not been obtained; references are therefore unresolved rather than reconstructed from guessed titles.[^r7]

## Audit Log
- Audit invalidated (2026-09-30): auditor admitted incomplete independent checks and premature flag removal. Previous valid audits, if any, remain separate.

- 2026-09-30: Initial/cheap audit failed; stronger source review corrected payoff mapping, all three needs and exact investments, threshold alternatives, forecast learning and tested configurations; visually verified SD/lookback source conflict and vector learning equation. Independent re-audit pending.

- WITHDRAWN audit claim (2026-09-30): the remaining-audit-c report overstated independent source checks; it does not establish a pass.

## LLM Justification
[^r1]: https://marcojanssen.info/wp-content/uploads/2016/08/2002_Using_artificial_agents_to_understand_laboratory_experiments_of_common_pool_resources_with_real-agents.pdf; §6.1 pp.75–77: chapter aim and game.
[^r2]: Same source; §6.1 pp.76–77: eight agents and10/25-token resource game; §6.5 pp.87–88: Consumat needs/uncertainty and four-mode overview/mental-map update.
[^r3]: Same source; §6.6 pp.89–90, Eqs.6.1–6.5: social/personal/exploration needs and weights. Visual check PDF pages16 (printed90): both SD equations have square roots, inclusive t−5..t bounds and divisor4 despite five-round prose.
[^r4]: Same source; §6.6 pp.90–92, Eqs.6.6–6.8 and adjacent investment-choice paragraphs: three lag single-layer forecast, printed normalized-input learning rule, eta0.5, exact deliberation/comparison/repetition/imitation investments.
[^r5]: Same source; §6.7 pp.92–98, Tables6.2–6.4, Eq.6.9, Figures6.5–6.8: HE/HP thresholds, need configurations/SVO mixtures, initial totals, normalized random need weights and25 allocations, laboratory comparison outcomes.
[^r6]: Same source; discussion pp.99–102: interpretation limits, five proposed empirical hypotheses and future validation.
[^r7]: Same author PDF; full28-page file, printed pp.75–102, last page acknowledgements and no bibliography; bibliography cannot be copied from this source.
