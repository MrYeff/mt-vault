---
title: "Towards operational validation of LLM-agent social simulations: a replicated study of a Reddit-like technology forum"
tags:
  - model
  - simulation
authors:
  - "[[Literature/Authors/Aleksandar Tomašević|Aleksandar Tomašević]]"
  - "[[Literature/Authors/Darja Cvetković|Darja Cvetković]]"
  - "[[Literature/Authors/Sara Major|Sara Major]]"
  - "[[Literature/Authors/Slobodan Maletić|Slobodan Maletić]]"
  - "[[Literature/Authors/Miroslav Anđelković|Miroslav Anđelković]]"
  - "[[Literature/Authors/Ana Vranić|Ana Vranić]]"
  - "[[Literature/Authors/Boris Stupovski|Boris Stupovski]]"
  - "[[Literature/Authors/D. Vudragović|D. Vudragović]]"
  - "[[Literature/Authors/Aleksandar Bogojević|Aleksandar Bogojević]]"
  - "[[Literature/Authors/Marija Mitrović Dankulov|Marija Mitrović Dankulov]]"
publication date: 2026-06-11
source: https://link.springer.com/article/10.1140/epjds/s13688-026-00674-x
doi: 10.1140/epjds/s13688-026-00674-x
read status: Todo
⚠️:
  - audit failed
---
## Abstract

Validation of LLM-agent social simulations remains underdeveloped, with most studies relying on subjective assessments or single runs. We address this gap by running 30 independent 30-day simulations of a technology forum modeled on Voat’s v/technology, using stateless Dolphin Mistral 24B agents on the Y Social platform, and evaluating operational validity across five dimensions: activity patterns, network structure, toxicity, topical coverage, and stylistic convergence. Against 30 matched, non-overlapping 30-day Voat comparison windows, results show overlapping 99% confidence intervals for unique users, root posts, and daily active users, while comments, average thread length, and mean toxicity remain higher in simulation. Both simulated and empirical networks exhibit core–periphery structure, though simulated cores are larger and more diffuse and repeated interactions are less frequent. Topic alignment is near-complete, but toxicity is misallocated across content layers: simulated root posts are substantially more toxic than real submissions, while simulated comments are less toxic than Voat comments. These findings demonstrate that LLM agents in platform-faithful environments can reproduce familiar online regularities, while systematic divergences—particularly those linked to stateless agent design and content-layer calibration—point to concrete directions for future improvement.

## Research Questions
> Research Questions extracted via LLM

- How well do repeated LLM-agent simulations reproduce Voat v/technology activity, network, toxicity, topical, and stylistic patterns, and where do they diverge?[^r1]

## Model
> Model extracted via LLM according to [[Model Notation]]

### What does it represent?
A technology forum on Y Social, with a stateful platform and stateless Dolphin Mistral 24B Venice Edition personas. Thread histories and interests provide continuity through server data passed to fresh prompts.[^r2]

The state and schedule below condense §§3.2–3.3 and Table 4; persona sampling is for face validity and its political weights are heuristic.[^r2][^r3][^r4]

```yml
World:
  users: [User]
  items: [Item]
  links: [str] # fixed 1000-URL Voat catalog
  day: u32

User:
  persona:
    locale: EnglishUS
    age: 18..60
    education: str
    toxicity: AbsolutelyNo | No | Moderately
    political_segment: str
  interests: [str] # initially 2–5 of 10 technology categories
  last_active: time
  budget: 1..10

Item:
  author: UserId
  parent: ItemId?
  text: str
  created: time
  likes: u32
  dislikes: u32

Action: None | Post | Read | Comment | Search | ShareLink
```

### How does it work?
The menu weights are relative sampling weights for opportunities, not realized action probabilities; the LLM chooses among the sampled options.[^r4]

```
DAYS = 30
START_USERS = 50
URLS = 1000
VISIBILITY_ROUNDS = 96
PARENT_CONTEXT = 3
ZIPF_S = 2.5
CHURN = 0.90
GROWTH = 0.30
MENU_WEIGHTS = {Post: 0.005, ShareLink: 0.06, Comment: 0.06,
                Read: 0.40, Search: 0.10}
TOXICITY_WEIGHTS = [0.80, 0.15, 0.05]
POLITICAL_WEIGHTS = [0.35, 0.25, 0.25, 0.15]

sim_step(mut world: World):
  active = daily_activated_subset(world.users)
  for user in active:
    budget = truncated_Zipf(1..10, ZIPF_S)
    repeat budget times:
      menu = [None] + weighted_sample_without_replacement(MENU_WEIGHTS, 2)
      feed = items excluding own posts and age > VISIBILITY_ROUNDS
      sort feed by (likes + dislikes) descending, recency descending
      context = at most PARENT_CONTEXT prior thread items
      choice = LLM(menu, persona, interests, feed, context)
      execute choice and store resulting content/reaction/interest changes
  pre_churn = |world.users|
  remove CHURN fraction with longest inactivity; break ties randomly
  add GROWTH * pre_churn users sampled as at initialization
  world.day += 1
```

- `Post` creates a root item; `Comment` appends a reply; `Read` consumes content and can shift interests; `Search` uses interests to retrieve topical items; `ShareLink` propagates existing news or ingests from the fixed URL catalog and can change interests. Interests influence future prompts/exposure. The article does not give a numerical interest-update formula or a full daily activation algorithm, so those are left as source-described operations.[^r3][^r4]
- Mentions prioritize local reply dependencies. There is no internal long-term conversation memory; visible thread context is capped uniformly at three items.[^r2][^r3]

### What can it answer?
- Calibration uses 10 non-overlapping 30-day Voat v/technology windows; validation compares 30 independent 30-day runs against 30 separate matched windows. Five dimensions cover activity/network structure, toxicity, topical/semantic coverage and stylistic convergence; main comparisons use 99% intervals.[^r5]
- Interaction graph: undirected commenter↔parent-author edges, omit self-interactions, count repeats and divide all counts by the graph maximum. Measure density, degree, weighted degree, weighted clustering and a two-class core/periphery SBM on the largest component. Toxicity uses ToxiGen RoBERTa; semantic retrieval uses all-MiniLM-L6-v2; BERTopic compares topics; token convergence entropy measures local accommodation.[^r5]
- Activity distributions and topics resemble the benchmark, but comments/thread lengths, network concentration and content-layer toxicity differ. Convergence tracks the three-item context window, without evidence of persistent persona learning.[^r6]

### Where does it apply?
Results concern the configured small technology forum, fixed catalog and persona/LLM setup; read/search weights and persona sampling are heuristic. The study tests operational distributions rather than individual human cognition.[^r2][^r4][^r6]

## Metadata
### References

- [[TheEchoChamberEffectOnSocialMedia]]
- [[UnresolvedReferenceE8BC353948A37E5F]]
- [[UnresolvedReference98BC45A297115430]]
- [[ResearchHandbookOnSocialMediaAndSociety]]
- [[UnresolvedReference1C432B2A3E67A8B1]]
- [[UnresolvedReference5C3CD3FBC705D25A]]
- [[Generative agent-based modeling with actions grounded in physical- social- or digital space using Concordia]]
- [[UnresolvedReference30D55262B73F0A85]]
- [[UnresolvedReferenceCAC06713FBC9A8CC]]
- [[UnresolvedReference16DBF7A7966B562A]]
- [[UnresolvedReference8811ABE22ABA1B20]]
- [[UnresolvedReferenceB894D092E8BBEA75]]
- [[UnresolvedReferenceAAB0459375F45260]]
- [[AreLlmPoweredSocialMediaBotsRealistic]]
- [[UnresolvedReference3E5F9DB4B0E44264]]
- [[UnresolvedReference57126B4D29AE231E]]
- [[UnresolvedReference58841ACD921FC1B9]]
- [[ProceedingsOfThe35thAnnualAcmSymposiumOnUserInterfaceSoftwareAndTechnology]]
- [[UnresolvedReference29F1E6543685E365]]
- [[UnresolvedReference062E4EE72A20C155]]
- [[TheOxfordHandbookOfPoliticalScience]]
- [[TheSocialConstructionOfReality]]
- [[OutOfOneManyUsingLanguageModelsToSimulateHumanSamples]]
- [[UnresolvedReferenceCF3869956352273C]]
- [[AgentBasedComputationalModelsAndGenerativeSocialScience]]
- [[UnresolvedReference3B6AE7454F308F31]]
- [[UnresolvedReferenceFF129DD65F74C7B3]]
- [[ProceedingsOfThe36thAnnualAcmSymposiumOnUserInterfaceSoftwareAndTechnology]]
- [[Y Social- an LLM-powered Social Media Digital Twin]]
- [[UnresolvedReference96BF1DBE962109AA]]
- [[UnresolvedReferenceDACC73FBC5AD3906]]
- [[ProceedingsOfThe2017AcmConferenceOnComputerSupportedCooperativeWorkAndSocialComputing]]
- [[UnresolvedReferenceC0F875FAAC97F0D4]]
- [[ProceedingsOfThe7thPythonInScienceConferenceScipy2008]]
- [[UnresolvedReference69F6EBC6C31ABDE9]]
- [[UnresolvedReferenceE37EDCB785151572]]
- [[ProceedingsOfThe60thAnnualMeetingOfTheAssociationOfComputationalLinguistics]]
- [[ProceedingsOfThe2019ConferenceOnEmpiricalMethodsInNaturalLanguageProcessingAndThe9thInternationalJointConferenceOnNaturalLanguageProcessingEmnlpIjcnlp]]
- [[UnresolvedReference9D0D41B7688E8BD2]]
- [[UnresolvedReferenceF6DA5E636DCCDAAA]]
- [[ProceedingsOfTheAnnualMeetingOfTheCognitiveScienceSociety]]
- [[UnresolvedReference4BCDC29F0F085B24]]
- [[UnresolvedReferenceCE604C9D7BDE90AF]]
- [[UnresolvedReferenceEC33E78D99266402]]
- [[EchoingIdentityFailuresWhenLlmAgentsTalkToEachOther]]
- [[AreLlmAgentsBehaviorallyCoherentLatentProfilesForSocialSimulation]]
- [[TowardsUnderstandingSycophancyInLanguageModels]]
- [[UnresolvedReferenceB2CB594782085900]]
- [[SycophancyInLargeLanguageModelsCausesAndMitigations]]
- [[UnresolvedReferenceA6421A0E4780CE84]]


## Audit Log
- Audit invalidated (2026-09-30): auditor admitted incomplete independent checks and premature flag removal. Previous valid audits, if any, remain separate.

- 2026-09-30: Initial/cheap audit failed; stronger source review corrected server state, feed ordering and bounds, exact three-choice weighted menus and budget, churn-before-growth, calibrated weights, interest-feedback limits and evaluation graph. Independent re-audit pending.

- WITHDRAWN audit claim (2026-09-30): the remaining-audit-c report overstated independent source checks; it does not establish a pass.

## LLM Justification
[^r1]: https://link.springer.com/article/10.1140/epjds/s13688-026-00674-x; Abstract and §1: operational validation aim.
[^r2]: Same source; §2.3 and §3 Methods opening: architecture, appropriateness framework, stateless prompts, mentions and topic catalog.
[^r3]: Same source; §3.1–3.2, Tables 2–3: 1000 links, persona sampling, actions, interests, popularity/recency feed, own-post exclusion, 96 rounds and K=3.
[^r4]: Same source; §3.3 and https://link.springer.com/article/10.1140/epjds/s13688-026-00674-x/tables/4: 30 days/50 agents, 90% churn then30% pre-churn growth, action weights, repeated three-option menus and Zipf budgets; no full activation/interest-change algorithm provided in article.
[^r5]: Same source; §3.1 calibration and §3.4 Validation: samples, graph construction/normalization, SBM, toxicity/semantic/topic/entropy measures.
[^r6]: Same source; §§4–5: benchmark divergences and convergence-window interpretation.
