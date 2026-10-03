---
title: "Mixing beliefs among interacting agents"
authors:
  - "[[Literature/Authors/Guillaume Deffuant|Guillaume Deffuant]]"
  - "[[Literature/Authors/David B. Neau|David Neau]]"
  - "[[Literature/Authors/Frédéric Amblard|Frédéric Amblard]]"
  - "[[Literature/Authors/Gérard Weisbuch|Gérard Weisbuch]]"
source: "https://hal.inrae.fr/hal-02580278v1/file/Deffuant2001.pdf"
doi: "10.1142/S0219525900000078"
publication date: "2000-01"
tags:
  - "model"
  - "simulation"
read status: Todo
⚠️:
  - audit failed
---

## Abstract

We present a model of opinion dynamics where agents adjust continuous opinions on the occasion of random binary encounters whenever their difference in opinion is below a given threshold. High thresholds yield convergence of opinions towards an average opinion, but low thresholds result in several opinion clusters: members of the same cluster share the same opinion but do not adjust any more with members of other clusters.

## Research Questions
> Research Questions extracted via LLM

- When do pairwise opinion adjustments converge and when do they form distinct clusters?[^r1]
- How does the allowed opinion difference shape the resulting opinion distribution?[^r1]

## Model
> Model extracted via LLM according to [[Model Notation]]

### What does it represent?
- Agents hold continuous opinions; the paper also studies binary vectors of opinions on multiple shared subjects.[^d1]

### How does it work?
The continuous case uses one fixed confidence threshold and convergence parameter across the population.[^d1]

```yml
World:
  agents: [Agent]
  encounters: CompleteMixing | SquareLattice
  threshold: 0..
  convergence: 0..0.5

Agent:
  opinion: 0..1
```

The update uses both pre-encounter values, with a strict confidence test.[^d1]

```
sim_step(
  mut world: World
):
  i, j = random_pair(world.encounters)
  x = world.agents[i].opinion
  y = world.agents[j].opinion
  if abs(x-y) < world.threshold:
    world.agents[i].opinion = x + world.convergence*(y-x)
    world.agents[j].opinion = y + world.convergence*(x-y)
```

- Initialize continuous opinions uniformly on `[0,1]`. Complete mixing permits any pair; the local case randomly selects a connected pair on a square lattice with north/south/east/west neighbors.[^d2]
- Binary-vector variant: use Hamming distance over `m` binary subjects. For each differing subject, choose one agent randomly and let it copy the other's bit with probability μ; retain equal bits. This variant uses complete mixing.[^d3]
- Source conflict: the vector section allows agreement on at least `m-d` subjects but restates this as disagreement on at most `d-1` subjects. These differ at the boundary; no single threshold implementation is asserted here.[^d3]

The source's continuous-population counts conflict.[^d4]

```
FIGURE_1_MU = 0.5
RESULTS_PROSE_AGENT_COUNT = 1000
FIGURE_1_AGENT_COUNT = 2000
```

- This extraction omits the small-threshold density approximation and detailed vector-cluster statistics; it retains both encounter mechanisms and the source's boundary/count conflicts.[^d5]

### What can it answer?
- It tests consensus, opinion-cluster counts, convergence, and local-network percolation as confidence, convergence, and population vary.[^d2][^d5]

### Where does it apply?
- It is an abstract model of bounded pairwise influence, with complete mixing and a square-lattice example.[^d1][^d2]

## Metadata
### References
- [[IncreasingReturnsAndPathDependenceInTheEconomy|Increasing Returns and Path Dependence in the Economy]]
- [[RandomEconomiesWithManyInteractingAgents|Random Economies with Many Interacting Agents]]
- [[RationalGroupDecisionMakingARandomFieldIsingModelAtT0|Rational group decision making: A random field Ising model at T=0]]
- [[StochasticModelsForSpeciesFormationInEvolvingPopulations|Stochastic models for species formation in evolving populations]]
- [[DiffusionDinformationEtValuationsSquentielles|Diffusion d’information et valuations squentielles]]
- [[SelfOrganizingSocialSystemsNecessaryAndSufficientConditionsForTheEmergenceOfClusteringConsolidationAndContinuingDiversity|Self-Organizing Social Systems: Necessary and Sufficient Conditions for the Emergence of Clustering, Consolidation and Continuing Diversity]]
- [[RevisionsDesCroyancesDansUnSystemeDagentsEnInteraction|Révisions des croyances dans un système d’agents en interaction]]
- [[BayesianInteractionsAndCollectiveDynamicsOfOpinionHerdBehaviorAndMimeticContagion|Bayesian Interactions and Collective Dynamics of Opinions: Herd Behavior and Mimetic Contagion]]
- [[IntroductionToPercolationTheory|Introduction to Percolation Theory]]
- [[DynamicalAspectsInTheAdoptionOfAgriEnvironmentalMeasures|Dynamical aspects in the Adoption of Agri-Environmental Measures]]

## Audit Log
- 2026-09-30: Complete independent primary-source audit confirmed the model and recorded source conflicts. Rebuilt the 10-entry bibliography in source order: removed an unrelated imported work and two unresolved duplicate metadata tokens; restored Laslier, Latané/Nowak and Neau. Corrected publication precision to January 2000: the registry supplies no day, while the HAL cover cites 2001. Independent re-audit remains pending.[^metadata]
- Audit invalidated (2026-09-30): auditor admitted relying on spot checks and previous reports before clearing flags. A full independent audit is still required.
- 2026-09-30: Full-source design audit found continuous rules lacked readable state/procedure; vector-boundary and figure population conflicts require preservation. Corrected against the source passages below; independent re-audit pending.[^design]
- Independent source audit found network and variant details missing and the vector-opinion extension mischaracterized. Full paper review corrected the vector model to binary opinions with Hamming distance and probabilistic persuasion, corrected the convergence-parameter range and simultaneous updates, and recorded the source’s off-by-one threshold wording conflict. The N=1,000 prose versus N=2,000 figure-caption conflict also remains unresolved. At that stage, independent re-audit remained pending.

- WITHDRAWN audit claim (2026-09-30): incomplete source checks; this audit does not establish a pass.

## LLM Justification
[^r1]: Deffuant et al., “Mixing beliefs among interacting agents,” §1, p. 2; https://hal.inrae.fr/hal-02580278v1/file/Deffuant2001.pdf.



[^d1]: §2.1, basic-model Eqs. (1)–(2): randomly selected agents adjust when opinion difference is strictly below d; μ is taken between 0 and 0.5; d is fixed across the population.

[^d2]: §2.2 initializes uniform [0,1] opinions; §3 specifies square-grid four-neighbor encounters and the same confidence update.

[^d3]: §4.1: binary opinions over shared subjects, Hamming distance, complete mixing, per-differing-subject random persuasion with probability μ, and the conflicting m-d versus d-1 formulations. Original PDF pages 9–10 verified visually where text extraction garbles symbols.

[^d4]: §2.2 prose says N=1000; Figure 1 caption says N=2000 and μ=0.5. Original PDF page 4 verified visually.

[^d5]: §§2.1–2.2 density approximation and cluster results; §3 local percolation; §4.2 vector-cluster results.

[^design]: Source audit checked the full text at https://hal.inrae.fr/hal-02580278v1/file/Deffuant2001.pdf. Model footnotes identify the passages supporting the corrections.

[^metadata]: [Publisher-deposited Crossref record](https://api.crossref.org/works/10.1142/S0219525900000078): print/publication date-parts [2000,1], online [2011,11,20], volume 03, issue 01n04, pp. 87–98. The archived primary PDF cover instead cites 2001; January 2000 is registry metadata, not an inferred exact day.
