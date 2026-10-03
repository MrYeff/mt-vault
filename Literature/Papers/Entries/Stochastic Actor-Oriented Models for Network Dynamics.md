---
title: "Stochastic Actor-Oriented Models for Network Dynamics"
tags:
  - social_network
  - statistical_model
  - "model"
authors:
  - "[[Literature/Authors/Tom A. B. Snijders|Tom A. B. Snijders]]"
publication date: 2017-01-06
source: "https://www.stats.ox.ac.uk/~snijders/SAOM_ARStat1.pdf"
doi: 10.1146/annurev-statistics-060116-054035
read status: Todo
⚠️:
  - audit failed
---

## Abstract

This article discusses the stochastic actor-oriented model for analyzing panel data of networks. The model is defined as a continuous-time Markov chain, observed at two or more discrete time moments. It can be regarded as a generalized linear model with a large amount of missing data. Several estimation methods are discussed. After presenting the model for evolution of networks, attention is given to coevolution models. These use the same approach of a continuous-time Markov chain observed at a small number of time points, but now with an extended state space. The state space can be, for example, the combination of a network and nodal variables, or a combination of several networks. This leads to models for the dynamics of multivariate networks. The article emphasizes the approach to modeling and algorithmic issues for estimation; some attention is given to comparison with other models.

## Research Questions
> Research Questions extracted via LLM
- How can stochastic actor-oriented models represent and estimate network change from sparse panel observations?[^r1]
- How can the approach be extended to coevolving networks and actor attributes?[^r1]

## Model
> Model extracted via LLM according to [[Model Notation]]

### What does it represent?
- A continuous-time Markov chain for panel observations of a directed network on fixed actors. A change opportunity belongs to one actor, who can keep the state or toggle one outgoing tie; self-ties are excluded.[^r3]
- `RATE_COEFFICIENTS`, `PERIOD_SCALE` and `OBJECTIVE_WEIGHTS` are model parameters. `RATE_STATISTICS` and `EFFECTS` are specified by the application; they are not extra behavioral assumptions.[^r3]

```yml
World:
  actors: [Actor]
  network: Network
  time: Time

Actor: ()
Time: f64
Network: [ActorId -> [ActorId -> bool]]

Choice:
  Keep
  Toggle:
    receiver: ActorId
```

### How does it work?
- Eq. (3) supplies one possible rate parameterization; Eqs. (1)–(2), (4)–(6) define event timing, actor selection and choice. The typed loop simulates a transition up to a panel-wave boundary.[^r3]

```
sim_loop(mut world: World, wave_end: Time):
  while world.time < wave_end:
    for i in world.actors.ids():
      rates[i] = PERIOD_SCALE * exp(dot(
        RATE_COEFFICIENTS, RATE_STATISTICS(i, world.network)
      ))
    dt = exponential(rate=sum(rates))
    if world.time + dt >= wave_end:
      world.time = wave_end
      break
    world.time += dt
    i = sample(normalize(rates))
    options = [Keep] + [Toggle(j) for j in world.actors.ids() if j != i]
    for option in options:
      candidate = apply_copy(world.network, i, option)
      weights[option] = exp(objective(i, world.network, candidate))
    chosen = sample(normalize(weights))
    apply(mut world.network, i, chosen)


objective(i: ActorId, previous: Network, candidate: Network) -> f64:
  values = [effect(i, previous, candidate) for effect in EFFECTS]
  out = dot(OBJECTIVE_WEIGHTS, values)
```

- Standard choices include current-state effects `Σⱼ xᵢⱼ` (outdegree), `Σⱼ xᵢⱼxⱼᵢ` (reciprocity) and `Σⱼₖ xᵢⱼxⱼₖxᵢₖ` (transitive triplets). Persistent reciprocity uses `Σⱼ x⁰ᵢⱼx⁰ⱼᵢxᵢⱼxⱼᵢ`, making the objective path-dependent.[^r3]
- Rates/effects may use covariates and vary between periods. Panel observations do not intervene in the process. Restricted admissible sets are possible; the loop uses the usual unrestricted keep/toggle set.[^r3]

### What can it answer?
- Estimate how actor/network effects relate to panel-network change, using simulated trajectories in moments, GMM or likelihood estimation.[^r4]

### Where does it apply?
- Longitudinal network panels. This core transition summary omits estimation algorithms, application-specific effects and extensions for actor-attribute or multivariate-network coevolution.[^r3][^r4]

## Metadata
### References
- [[Estimation of stochastic actor-oriented models for the evolution of networks by generalized method of moments]]
- [[Stochastic approximation: A generalisation of the Robbins-Monro procedure]]
- [[Random Graphs]]
- [[What is network science?]]
- [[On unification of the asymptotic theory of nonlinear econometric models]]
- [[Nonparametric bayes dynamic modelling of relational data]]
- [[On the evolution of random graphs]]
- [[The Development of Social Network Analysis: A Study in the Sociology of Science]]
- [[A survey of statistical network models]]
- [[Methods of identification in social networks]]
- [[Diffusion of innovations in dynamic networks]]
- [[Discrete temporal models for social networks]]
- [[Large sample properties of generalized method of moments estimators]]
- [[Latent space approaches to social network analysis]]
- [[A dynamic model for social networks]]
- [[Temporal networks]]
- [[Statistical analysis of longitudinal network data with changing composition]]
- [[Victims, bullies, and their defenders: A longitudinal study of the coevolution of positive and negative networks]]
- [[Curved exponential family models for social networks]]
- [[Goodness of fit of social network models]]
- [[Social and Economic Networks]]
- [[Statistical Analysis of Network Data: Methods and Models]]
- [[Longitudinal models]]
- [[Simultaneous modeling of initial conditions and time heterogeneity in dynamic networks: An application to Foreign Direct Investments]]
- [[Bayesian inference for dynamic social network data]]
- [[A separable model for dynamic networks]]
- [[Stochastic Approximation and Recursive Algorithms and Applications]]
- [[Conditional independence in dynamic networks]]
- [[Statistical Models for Social Network Dynamics]]
- [[Finding observed information when using the EM algorithm]]
- [[Exponential Random Graph Models]]
- [[Limited-dependent and Qualitative Variables in Econometrics]]
- [[Networks. An Introduction]]
- [[Markov Chains]]
- [[A missing information principle: theory and applications]]
- [[Hierarchical longitudinal models of relationships in social networks]]
- [[Smoke rings: Social network analysis of friendship groups, smoking and drug-taking]]
- [[New method of stochastic approximation type]]
- [[On the geometry of discrete exponential families with application to exponential random graph models]]
- [[Manual for Siena version 4.0]]
- [[A stochastic approximation method]]
- [[The score function approach for sensitivity analysis of computer simulation models]]
- [[Efficient estimation from a slowly convergent Robbins-Monro process]]
- [[Stochastic approximation]]
- [[On a stochastic approximation procedure based on averaging]]
- [[Instability, sensitivity, and degeneracy of discrete exponential families]]
- [[Markov models for digraph panel data: Monte Carlo-based derivative estimation]]
- [[Siena algorithms]]
- [[The statistical evaluation of social network dynamics]]
- [[Statistical models for social networks]]
- [[The multiple flavours of multilevel issues for networks]]
- [[Introduction to the special issue on network dynamics]]
- [[Introduction to the special issue on network dynamics (part 2)]]
- [[Maximum likelihood estimation for social network dynamics]]
- [[A model for the multiplex dynamics of two-mode and one-mode networks, with an application to employment preference, friendship, and advice]]
- [[New specifications for exponential random graph models]]
- [[Stochastic actor-oriented models for network dynamics (Snijders and Pickup, 2017)|Stochastic actor-oriented models for network dynamics]]
- [[Actor-based Models for Analyzing Network Dynamics]]
- [[Social Network Dynamics by Examples]]
- [[Modeling the co-evolution of networks and behavior]]
- [[Introduction to actor-based models for network dynamics]]
- [[Dynamic networks and behavior: Separating selection from influence]]
- [[The calculation of posterior distributions by data augmentation]]
- [[Dynamics of advice-seeking networks among judges at the commercial court of Paris]]
- [[p2: A random effects model with covariates for directed graphs]]
- [[Network–behavior dynamics]]
- [[Logit models and logistic regression for social networks: I. An introduction to Markov graphs and p*]]
- [[Collective dynamics of small-world networks]]
- [[Background, rationale and design of the West of Scotland 11 to 16 study]]
- [[A mixed effects model for longitudinal relational and network data, with applications to international trade and conflict]]

## Audit Log
- Bibliography correction (2026-09-30): replaced the incomplete or mixed imported list with all 70 references from the audited primary source. Original links remain in the import snapshot; independent re-audit required.
- Independent bibliography audit (2026-09-30): the preserved import has 112 links against 70 references in the accepted manuscript and publisher list. It includes unresolved identifiers, container titles and works absent from this source; reference reconciliation is required.
- Independent full-source audit (2026-09-30): core transition claims passed, but the publication date failed against the publisher's Review in Advance date. Corrected 16 January to 6 January 2017; independent re-audit required.
- Audit invalidated (2026-09-30): auditor admitted clearing flags before completing independent source checks. A new independent audit is required.
- Strong source review (2026-09-30): Added actors/time and explicit CTMC rates, event time, admissible options, objective softmax and structural effects; fixed wave-boundary advancement and made custom effects/rate statistics explicit configuration. Independent re-audit pending.
- Initial independent audit: failed on missing model mechanisms, abstract fidelity, or source-access reporting; see `vault/.automation/audit/next-forty-54-66-initial-2026-09-30.json`. Revisions added source-located model detail; independent re-audit remains pending.

- WITHDRAWN audit claim (2026-09-30): previously reported PASS; source claims, current extraction, metadata, references and footnotes checked against the available primary source. See `vault/.automation/audit/remaining-audit-b-2026-09-30.json`.

## LLM Justification
[^r1]: The paper’s abstract, at https://www.annualreviews.org/content/journals/10.1146/annurev-statistics-060116-054035. The questions paraphrase the stated purpose, research scope, and reported approach.
[^r3]: Snijders, accepted Annual Review manuscript, §2 pp. 4–9: opportunity rates Eqs. (1)–(3), options (4a–b), multinomial choice (5), linear objective (6), structural/path-dependent effects (7)–(10), observation timing and period heterogeneity. Full author manuscript: https://www.stats.ox.ac.uk/~snijders/SAOM_ARStat1.pdf.
[^r4]: Snijders, accepted Annual Review manuscript, §3 “Estimation” and later coevolution discussion: moments/GMM/maximum-likelihood methods and enlarged state spaces. Full author manuscript: https://www.stats.ox.ac.uk/~snijders/SAOM_ARStat1.pdf.
