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

- [[The echo chamber effect on social media]]
- [[Persistent interaction patterns across social media platforms and over time]]
- [[Three roots of online toxicity- disembodiment, accountability, and disinhibition|Three roots of online toxicity: disembodiment, accountability, and disinhibition]]
- [[The affective resonance of norm-violation rhetoric in social media]]
- [[Post-post-api age- studying digital platforms in scant data access times|Post-post-api age: studying digital platforms in scant data access times]]
- [[LLM social simulations are a promising research method]]
- [[Generative agent-based modeling with actions grounded in physical- social- or digital space using Concordia|Generative agent-based modeling with actions grounded in physical, social, or digital space using Concordia]]
- [[Do large language models solve the problems of agent-based modeling- A critical review of generative social simulations|Do large language models solve the problems of agent-based modeling? A critical review of generative social simulations]]
- [[A survey on the application of large language models in agent-based modeling and simulation]]
- [[Generative agents in agent-based modeling- overview, validation, and emerging challenges|Generative agents in agent-based modeling: overview, validation, and emerging challenges]]
- [[Six fallacies in substituting large language models for human participants]]
- [[The collective Turing test- large language models can generate realistic multi-user discussions|The collective Turing test: large language models can generate realistic multi-user discussions]]
- [[Can large language models simulate spoken human conversations-|Can large language models simulate spoken human conversations?]]
- [[Are LLM-powered social media bots realistic-|Are LLM-powered social media bots realistic?]]
- [[A new sociology of humans and machines]]
- [[Machine culture]]
- [[Large AI models are cultural and social technologies]]
- [[Social Simulacra- Creating Populated Prototypes for Social Computing Systems|Social simulacra: creating populated prototypes for social computing systems]]
- [[Simulating subjects- the promise and peril of artificial intelligence stand-ins for social agents and interactions|Simulating subjects: the promise and peril of artificial intelligence stand-ins for social agents and interactions]]
- [[Human murmuration- group polarisation as compression in interaction-language dynamics captured by large language models|Human murmuration: group polarisation as compression in interaction-language dynamics captured by large language models]]
- [[The logic of appropriateness]]
- [[The social construction of reality]]
- [[Out of one, many- using language models to simulate human samples|Out of one, many: using language models to simulate human samples]]
- [[Language models surface the unwritten code of science and society]]
- [[Agent-based computational models and generative social science]]
- [[A critical guide to empirical validation of agent-based models in economics- methodologies, procedures, and open problems|A critical guide to empirical validation of agent-based models in economics: methodologies, procedures, and open problems]]
- [[A method for agent-based models validation]]
- [[Generative agents- interactive simulacra of human behavior|Generative agents: interactive simulacra of human behavior]]
- [[Y Social- an LLM-powered Social Media Digital Twin|Y social: an LLM-powered social media digital twin]]
- [[Beyond red vs. blue- the political typology|Beyond red vs. blue: the political typology]]
- [[“I can’t keep it up.” A dataset from the defunct Voat.co news aggregator]]
- [[Growth and inequality of participation in online communities]]
- [[Origins of power-law degree distribution in the heterogeneity of human activity in social networks]]
- [[Exploring network structure, dynamics, and function using NetworkX]]
- [[A clarified typology of core-periphery structure in networks]]
- [[Power-law distributions in empirical data]]
- [[ToxiGen- a large-scale machine-generated dataset for adversarial and implicit hate speech detection|ToxiGen: a large-scale machine-generated dataset for adversarial and implicit hate speech detection]]
- [[Sentence-BERT- sentence embeddings using Siamese BERT-networks|Sentence-BERT: sentence embeddings using Siamese BERT-networks]]
- [[BERTopic- neural topic modeling with a class-based TF-IDF procedure|BERTopic: neural topic modeling with a class-based TF-IDF procedure]]
- [[BERTs of a feather- studying inter- and intra-group communication via information theory and language models|BERTs of a feather: studying inter- and intra-group communication via information theory and language models]]
- [[Large language model discourse dynamics]]
- [[A simulation framework for studying recommendation-network co-evolution in social platforms]]
- [[Can we fix social media- Testing prosocial interventions using generative social simulation|Can we fix social media? Testing prosocial interventions using generative social simulation]]
- [[LLMs and generative agent-based models for complex systems research]]
- [[Echoing- identity failures when LLM agents talk to each other|Echoing: identity failures when LLM agents talk to each other]]
- [[Are LLM agents behaviorally coherent- Latent profiles for social simulation|Are LLM agents behaviorally coherent? Latent profiles for social simulation]]
- [[Towards understanding sycophancy in language models]]
- [[Simple synthetic data reduces sycophancy in large language models]]
- [[Sycophancy in large language models- causes and mitigations|Sycophancy in large language models: causes and mitigations]]
- [[Multi-platform aggregated dataset of online communities (MADOC)]]

## Audit Log
- 2026-10-03: Rebuilt all 50 References from the complete publisher bibliography in exact order, resolving all opaque targets to verified source titles. Primary article and separate Table 4 source review retained; `audit failed` remains pending independent re-audit.
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
