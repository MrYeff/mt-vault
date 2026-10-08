---
title: "The latent cognitive structures of social networks"
tags:
  - model
authors:
  - "[[Literature/Authors/Izabel Aguiar|Izabel Aguiar]]"
  - "[[Literature/Authors/Johan Ugander|Johan Ugander]]"
publication date: 2024-04-25
source: https://www.cambridge.org/core/journals/network-science/article/latent-cognitive-structures-of-social-networks/5C675C255AB9B9FE5A6A9F2E39E4909C
doi: 10.1017/nws.2024.7
read status: Todo
---
## Abstract

When people are asked to recall their social networks, theoretical and empirical work tells us that they rely on shortcuts, or heuristics. Cognitive social structures (CSSs) are multilayer social networks where each layer corresponds to an individual’s perception of the network. With multiple perceptions of the same network, CSSs contain rich information about how these heuristics manifest, motivating the question, Can we identify people who share the same heuristics? In this work, we propose a method for identifying cognitive structure across multiple network perceptions, analogous to how community detection aims to identify social structure in a network. To simultaneously model the joint latent social and cognitive structure, we study CSSs as three-dimensional tensors, employing low-rank nonnegative Tucker decompositions (NNTuck) to approximate the CSS—a procedure closely related to estimating a multilayer stochastic block model (SBM) from such data. We propose the resulting latent cognitive space as an operationalization of the sociological theory of social cognition by identifying individuals who share relational schema. In addition to modeling cognitively independent, dependent, and redundant networks, we propose a specific model instance and related statistical test for testing when there is social-cognitive agreement in a network: when the social and cognitive structures are equivalent. We use our approach to analyze four different CSSs and give insights into the latent cognitive structures of those networks.

## Research Questions
> Research Questions extracted via LLM

- Can multiple perceived networks reveal shared relational schemas, latent social/cognitive structure, and social-cognitive agreement?[^r1]

## Model
> Model extracted via LLM according to [[Model Notation]]

### What does it represent?
A Poisson factor model of multiple perceptions of the same directed network: outgoing/incoming social memberships and shared cognitive schemas.[^r2]

The types and rate below summarize Eq. (1) and Definitions 1–4; memberships are nonnegative weights, not normalized probabilities.[^r2][^r3]

```yml
CSS:
  ties: [[[u32]]] # N × N × L; layer = respondent

NNTuck:
  U: [[0..]] # N × K outgoing memberships
  V: [[0..]] # N × K incoming memberships
  Y: [[0..]] # L × C cognitive memberships
  G: [[[0..]]] # K × K × C affinities
  variant: Independent | Dependent | Redundant | Agreement
```

### How does it work?
The model rate and agreement-fitting order are specified below. Algorithm 1's tensor multiplicative formulas are omitted; the block states the objective and the additional constraints/order defining Algorithm 2.[^r2][^r3][^r5]

```
RESTARTS_STANDARD = 20
RESTARTS_AGREEMENT = 50
CV_MASKS = 5

rate(m: NNTuck, i: u32, j: u32, l: u32) -> 0..:
  out = sum(a,b,c: m.U[i,a] * m.V[j,b] * m.Y[l,c] * m.G[a,b,c])
  # CSS.ties[i,j,l] ~ Poisson(out)

fit_agreement(css: CSS) -> NNTuck:
  initialize nonnegative Y, V, G; U = Y; K = C < L
  repeat Algorithm 2 termination criterion:
    multiplicatively update V, then U, then Y (Algorithm 1)
    U = Y = (U + Y) / 2
    multiplicatively update G (Algorithm 1)
    retain iterate with lowest KL(css, rate)
  out = best retained iterate across RESTARTS_AGREEMENT starts
```

- `Independent`: `C=L`, `Y=I`; `Dependent`: `C<L`, free `Y`; `Redundant`: `C=1`, `Y=ones`; `Agreement`: `K=C<L`, `U=Y`. Standard fitting maximizes Poisson likelihood (equivalently minimizes KL divergence), keeping fixed factors fixed.[^r2][^r3]
- Algorithm 1 converges monotonically to a local optimum; Algorithm 2's averaging is heuristic, nonmonotone and has no convergence guarantee. Multiple starts provide no certificate of a global maximum.[^r5]
- Ordinary Wilks LRT validity fails because NNTuck is nonidentifiable and global maximum-likelihood fits are not assured.[^r6]
- The paper uses randomly split data with split-LRT, which does not require identifiability or nestedness.[^r6]
- It is lower-powered, its split may be suboptimal, and it still requires a maximized null likelihood; agreement-test conclusions therefore require particular caution.[^r6]
- The paper does not specify a complete tensor-splitting implementation here.[^r6]
- Five train/test masks and best-of-20 fitting select dimensions by average test AUC; split-LRT compares redundancy against `C=2`, dependence against independence and agreement against a sufficiently large dependent alternative; final factors are visualized and interpreted.[^r4][^r6]

### What can it answer?
It identifies respondents whose perceived networks share a generative schema and evaluates social–cognitive agreement in four CSS datasets. The split-LRT supports agreement for Krackhardt friendship and Hunter week-six friendship; it favors allowing social and cognitive spaces to differ for Krackhardt advice and Hunter week one. The latter begins with gender-aligned social/cognitive groupings that are less evident in week six. Schemas are interpreted after fitting and contextualized against limited metadata; the factorization does not directly name their cognitive content.[^r4]

### Where does it apply?
It applies to multilayer perceptions over common nodes, with CSS normally having one respondent per layer (`L=N`); its block-model structure may miss schemas such as triadic closure.[^r2][^r4]

## Metadata
### References

- [[A factor model of multilayer network interdependence]]
- [[Computing a nonnegative matrix factorization–provably]]
- [[Relational schemas and the processing of social information]]
- [[Efficient and principled method for detecting communities in networks]]
- [[The diffusion of microfinance]]
- [[Structural measures for multiplex networks]]
- [[Informant accuracy in social network data IV- a comparison of clique-level structure in behavioral and cognitive network data|Informant accuracy in social network data IV: a comparison of clique-level structure in behavioral and cognitive network data]]
- [[A macrosociological theory of social structure]]
- [[Cognitive social structures in social network research- a review|Cognitive social structures in social network research: a review]]
- [[Just like a woman- Effects of gender-biased perceptions of friendship network brokerage on attributions and performance|Just like a woman? Effects of gender-biased perceptions of friendship network brokerage on attributions and performance]]
- [[Humans use compression heuristics to improve the recall of social networks]]
- [[The microstructures of network recall- how social networks are encoded and represented in human memory|The microstructures of network recall: how social networks are encoded and represented in human memory]]
- [[Best rank (R, R, R) super-symmetric tensor approximation-a continuoustime approach]]
- [[Name generators in surveys of personal networks]]
- [[An approach for relating social structure to cognitive structure]]
- [[Emergent leadership structures in informal groups- a dynamic, cognitively informed network model|Emergent leadership structures in informal groups: a dynamic, cognitively informed network model]]
- [[A note on likelihood ratio tests for models with latent variables]]
- [[Latent network models to account for noisy, multiply reported social network data]]
- [[Community detection, link prediction, and layer interdependence in multilayer networks]]
- [[Spectral entropies as information-theoretic tools for complex network comparison]]
- [[Structural reducibility of multilayer networks]]
- [[Mathematical formulation of multilayer networks]]
- [[Subjective probabilities of interpersonal relationships]]
- [[Culture and cognition]]
- [[When does non-negative matrix factorization give a correct decomposition into parts-|When does non-negative matrix factorization give a correct decomposition into parts?]]
- [[Relational schemas to investigate the process of leadership emergence]]
- [[Filling in the blanks- a theory of cognitive categories and the structure of social affiliation|Filling in the blanks: a theory of cognitive categories and the structure of social affiliation]]
- [[Cognitive structure and informant accuracy]]
- [[The psychology of interpersonal relations]]
- [[Statnet- an R package for the statistical modeling of social networks|Statnet: an R package for the statistical modeling of social networks]]
- [[Latent space approaches to social network analysis]]
- [[A social cognitive conception of social structure]]
- [[Krackhardt data over time- the evolution and emergent properties of network perceptions|Krackhardt data over time: the evolution and emergent properties of network perceptions]]
- [[Social network schemas and the learning of incomplete networks]]
- [[Scalable symmetric Tucker tensor decomposition]]
- [[Nested stochastic block model for simultaneously clustering networks and nodes]]
- [[Layer communities in multiplex networks]]
- [[Maximizing the spread of influence through a social network]]
- [[Organizational network perceptions versus reality- a small world after all-|Organizational network perceptions versus reality: a small world after all?]]
- [[Informant accuracy in social network data]]
- [[Nonnegative tucker decomposition]]
- [[Tensor decompositions and applications]]
- [[Cognitive social structures]]
- [[Assessing the political landscape- structure, cognition, and power in organizations|Assessing the political landscape: structure, cognition, and power in organizations]]
- [[Structural leverage in marketing]]
- [[Systematic biases in social perception]]
- [[Algorithms for non-negative matrix factorization]]
- [[Evolution on a dancing landscape- organizations and networks in dynamic Blau space|Evolution on a dancing landscape: organizations and networks in dynamic Blau space]]
- [[An ecology of affiliation]]
- [[Comparing clusterings by the variation of information]]
- [[Identities in flux- cognitive network activation in times of change|Identities in flux: cognitive network activation in times of change]]
- [[The small world problem]]
- [[Coarse thinking and persuasion]]
- [[The acquaintance process]]
- [[Hierarchical block structures and high-resolution model selection in large networks]]
- [[Disentangling homophily, community structure, and triadic closure in networks]]
- [[Bayesian poisson Tucker decomposition for learning the structure of international relations]]
- [[Latent space models for network perception data]]
- [[A latent space model for cognitive social structures data]]
- [[A discussion of Tse and Davidson, A note on universal inference]]
- [[Clustering network layers with the strata multilayer stochastic block model]]
- [[On the choice of the splitting ratio for the split likelihood ratio test]]
- [[Volume-regularized nonnegative Tucker decomposition with identifiability guarantees]]
- [[Tensorial and bipartite block models for link prediction in layered networks and temporal networks]]
- [[The child in America- behavior problems and programs|The child in America: behavior problems and programs]]
- [[A note on universal inference]]
- [[Universal inference]]
- [[Social network analysis- methods and applications|Social network analysis: methods and applications]]
- [[The large-sample distribution of the likelihood ratio for testing composite hypotheses]]
- [[Alternating proximal gradient method for sparse nonnegative Tucker decomposition]]
- [[Active matrix factorization for surveys]]


## Audit Log
- 2026-10-03: Independent full-source re-audit passed. Independent full-source model/content audit passed; root separately compared all71source reference titles and order, including four titles outside article-title spans. `audit failed` removed after the pass.
- Audit invalidated (2026-09-30): auditor admitted incomplete independent checks and premature flag removal. Previous valid audits, if any, remain separate.

- 2026-09-30: Strong source review corrected redundant/agreement constraints, restart counts, Algorithm 2 order/averaging, and invalid ordinary-LRT implication. Independent re-audit pending.

- WITHDRAWN audit claim (2026-09-30): the remaining-audit-c report overstated independent source checks; it does not establish a pass.

## LLM Justification
[^r1]: https://www.cambridge.org/core/journals/network-science/article/latent-cognitive-structures-of-social-networks/5C675C255AB9B9FE5A6A9F2E39E4909C; §1 states the motivating question and contributions.
[^r2]: Same source; §§1 and 3.1, pp. 202–211, defines CSS layers and the NNTuck factorization.
[^r3]: Same source; §§3.2–3.4, Definitions 1–4: exact variant constraints and fixed-factor fitting.
[^r4]: Same source; §§3.5–4, pp. 218–229, defines inference tests and analyzes four empirical CSS datasets.
[^r5]: Same source; §3.4 and Appendix B, Algorithms 1–2: initialization Y,V,G then U=Y; updates V→U→Y, average U/Y, then core; retain best iterate; 20 standard starts; Appendix C/Figure C1 specifies 50 agreement starts and lack of guarantees.
[^r6]: Same source; §3.5, Definitions 5–8 and Appendix C: nonidentifiability, Wilks failure, split-LRT, random splitting, power and null-MLE caveats; §4 pipeline gives cross-validation and comparisons.
