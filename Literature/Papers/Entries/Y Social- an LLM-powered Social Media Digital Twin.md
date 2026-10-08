---
title: "Y Social: an LLM-powered Social Media Digital Twin"
tags:
  - model
  - simulation
authors:
  - "[[Literature/Authors/Giulio Rossetti|Giulio Rossetti]]"
  - "[[Literature/Authors/Massimo Stella|Massimo Stella]]"
  - "[[Literature/Authors/Rémy Cazabet|Rémy Cazabet]]"
  - "[[Literature/Authors/Katherine Abramski|Katherine Abramski]]"
  - "[[Literature/Authors/Erica Cau|Erica Cau]]"
  - "[[Literature/Authors/Salvatore Citraro|Salvatore Citraro]]"
  - "[[Literature/Authors/Andrea Failla|Andrea Failla]]"
  - "[[Literature/Authors/Riccardo Improta|Riccardo Improta]]"
  - "[[Literature/Authors/Virginia Morini|Virginia Morini]]"
  - "[[Literature/Authors/Valentina Pansanella|Valentina Pansanella]]"
publication date: 2024-08-01
source: https://arxiv.org/pdf/2408.00818
doi: 10.48550/arXiv.2408.00818
read status: Todo
⚠️:
  - audit failed
---
## Abstract

In this paper we introduce Y, a new-generation digital twin designed to replicate an online social media platform. Digital twins are virtual replicas of physical systems that allow for advanced analyses and experimentation. In the case of social media, a digital twin such as Y provides a powerful tool for researchers to simulate and understand complex online interactions. {\tt Y} leverages state-of-the-art Large Language Models (LLMs) to replicate sophisticated agent behaviors, enabling accurate simulations of user interactions, content dissemination, and network dynamics. By integrating these aspects, Y offers valuable insights into user engagement, information spread, and the impact of platform policies. Moreover, the integration of LLMs allows Y to generate nuanced textual content and predict user responses, facilitating the study of emergent phenomena in online environments. To better characterize the proposed digital twin, in this paper we describe the rationale behind its implementation, provide examples of the analyses that can be performed on the data it enables to be generated, and discuss its relevance for multidisciplinary research.

## Research Questions
> Research Questions extracted via LLM

- How can Y Social provide a configurable, LLM-powered digital twin for controlled simulation and analysis of online social-media interactions?[^r1]

## Model
> Model extracted via LLM according to [[Model Notation]]

### What does it represent?
Y Social combines a REST platform/data server, an LLM server and one or more synchronized simulation clients to model content and social ties.[^r2]

The state/action types and schedule summarize Figure 2 and Algorithm 1; configurable servers, clients and recommenders are opaque interfaces.[^r2][^r3]

```yml
World:
  users: [User]
  posts: [Post]
  follows: [(UserId, UserId)]
  news: [Article]
  clock: (day: u32, slot: u32)

User:
  profile: # prompted role
    age: u32
    leaning: str
    education: str
    nationality: str
    languages: [str]
    interests: [str]
    big_five: [High | Low] # five dimensions;32 combinations
  llm: ...
  content_recommender: ...
  follow_recommender: ...
  round_actions: u32

Post:
  author: UserId
  parent: PostId?
  text: str
  mentions: [UserId]
  hashtags: [str]
  reactions: [UserId -> Like | Dislike | Neutral]
  emotions: [str]
  created_round: u32
  original_shared_news: PostId?

Article:
  title: str
  summary: str
  source: str

Action: News | Post | Comment | Reply | Share | Read | Search | None | Follow
```

### How does it work?
The workflow follows Algorithm 1; its second follow loop iterates over all agents, while its comment says only a configured fraction of active agents follows. This loop/comment discrepancy is retained rather than silently resolving it.[^r3]

```
sim_loop(mut world: World, config: ...):
  generate/register users; connect platform and LLM servers
  for day in config.days:
    for slot in config.slots:
      h = platform.current_slot() # synchronize each client
      count = int(|world.users| * config.hourly_activity[h])
      active = random_sample_without_replacement(world.users, count)
      for user in active:
        LLM.select_action([News, Post, Comment, Reply, Share,
                           Read, Search, None])
        execute selected action(s) within user's round_actions
      for user in world.users: # literal Algorithm1 follow loop
        select_action([Follow, None])
        # comment: configured daily-follow fraction among active agents
    add config.new_agents_per_iteration users
```

- `Read`: rank a content shortlist, randomly choose one, prompt YES/NO/NEUTRAL, store reaction; then ask whether to follow/unfollow its author. `Post`: generate a new interest-topic discussion. `Comment`: generate a contribution with configured preceding-thread context. `Reply`: target threads recently mentioning the agent; `Search`: filter by hashtags used in its recent posts.[^r4]
- `Follow`: rank candidates, transform scores to probabilities and sample a tie; direct selection is topology-driven, with no LLM prompt. `News`: comment on an RSS article's title/summary; `Share`: repost previously shared news with a new comment and retain origin linkage. Generated text has extracted mentions/hashtags and GoEmotions annotations; role prompts condition on profile and request up to200 characters.[^r4]
- Content recommenders: random, reverse chronology, recent popularity (`likes+dislikes`), follower-based, follower-plus-popularity; each returns `k` recent items and can include a configurable non-follower share. Tie recommenders: random, common-neighbor count, Jaccard, Adamic–Adar and degree-product preferential attachment; optional political homophily bias. Visibility and context windows are configured, rather than universal constants.[^r5]

### What can it answer?
- The political demonstration begins with1000 users, adds10/day for100 days (2400 hourly rounds), and ends with2000. The paper calls its model `llama3-7b`; content uses ReverseChronoFollowersPopularity with60% followed-author exposure, tie suggestions use preferential attachment, visibility is36 rounds, and sources comprise600 curated RSS feeds.[^r6]
- Descriptive analyses cover content/reactions/emotions, networks, topology and controversy; this demonstrates available outputs rather than validates human behavior.[^r6]

The generic configuration example prints `days=365`, although adjacent prose describes100; these are separate/conflicting example settings, so the case-study duration above follows §4.1 explicitly.[^r3][^r6]

### Where does it apply?
- Configure social-media scenarios, distributed clients, mixed LLMs, and changes to curation, profiles, and news.[^r2][^r3][^r6]
- Empirical activity rates initialize hourly activation.[^r2][^r3][^r6]
- Predictive fidelity depends on the scenario; the demonstration does not establish it.[^r2][^r3][^r6]

## Metadata
### References
- [[Voices of rape- Cognitive networks link passive voice usage to psychological distress in online narratives|Voices of rape: Cognitive networks link passive voice usage to psychological distress in online narratives]]
- [[Cognitive network science reveals bias in gpt-3, gpt-3.5 turbo, and gpt-4 mirroring math anxiety in high-school students]]
- [[Gpt-4 technical report]]
- [[Friends and neighbors on the web]]
- [[Llama 3 model card]]
- [[A systematic review of machine learning techniques for stance detection and its applications]]
- [[More is different- Broken symmetry and the nature of the hierarchical structure of science|More is different: Broken symmetry and the nature of the hierarchical structure of science]]
- [[Data mining for the social sciences- An introduction|Data mining for the social sciences: An introduction]]
- [[Effective choice in the prisoner’s dilemma]]
- [[Agent-based modeling in economics and finance- Past, present, and future|Agent-based modeling in economics and finance: Past, present, and future]]
- [[Scale-free networks- a decade and beyond|Scale-free networks: a decade and beyond]]
- [[Scale-free networks]]
- [[Tweeting from left to right- Is online political communication more than an echo chamber-|Tweeting from left to right: Is online political communication more than an echo chamber?]]
- [[A survey on digital twin- Definitions, characteristics, applications, and design implications|A survey on digital twin: Definitions, characteristics, applications, and design implications]]
- [[Auditing algorithmic bias on twitter]]
- [[Modeling echo chambers and polarization dynamics in social networks]]
- [[Social media use and mental health among young adults]]
- [[Agent-based models in sociology]]
- [[Quantitative social science- the survey|Quantitative social science: the survey]]
- [[Social media and mental health]]
- [[The persuasive power of large language models]]
- [[Echo chambers, rabbit holes, and algorithmic bias- How youtube recommends content to real users|Echo chambers, rabbit holes, and algorithmic bias: How youtube recommends content to real users]]
- [[Language models are few-shot learners]]
- [[Multimodal sentimental analysis for social media applications- A comprehensive review|Multimodal sentimental analysis for social media applications: A comprehensive review]]
- [[An empirical survey of data augmentation for limited data learning in nlp]]
- [[Opinion dynamics with backfire effect and biased assimilation]]
- [[Do the socially rich get richer- a nuanced perspective on social network site use and online social capital accrual|Do the socially rich get richer? a nuanced perspective on social network site use and online social capital accrual]]
- [[Analyzing the impact of filter bubbles on social network polarization]]
- [[Introduction to modern information retrieval]]
- [[Simulating opinion dynamics with networks of llm-based agents]]
- [[The echo chamber effect on social media]]
- [[The Effect of People Recommenders on Echo Chambers and Polarization|The effect of people recommenders on echo chambers and polarization]]
- [[Manifesto of computational social science]]
- [[The game of life]]
- [[Sts-epr- Modelling individual mobility considering the spatial, temporal, and social dimensions together|Sts-epr: Modelling individual mobility considering the spatial, temporal, and social dimensions together]]
- [[A decade of social bot detection]]
- [[Cooperation, behavioural synchrony and status in social networks]]
- [[A simulation-based approach to analyze the information diffusion in microblogging online social network]]
- [[Introducing counsellme- A dataset of simulated mental health dialogues for comparing llms like haiku, llamantino and chatgpt against humans|Introducing counsellme: A dataset of simulated mental health dialogues for comparing llms like haiku, llamantino and chatgpt against humans]]
- [[Emergence of scale-free networks in social interactions among large language models]]
- [[Mixing beliefs among interacting agents]]
- [[Echo chambers in the age of misinformation]]
- [[Modeling confirmation bias and polarization]]
- [[Goemotions- A dataset of fine-grained emotions|Goemotions: A dataset of fine-grained emotions]]
- [[Modeling civil violence- An agent-based computational approach|Modeling civil violence: An agent-based computational approach]]
- [[Exposure inequality in people recommender systems- the long-term effects|Exposure inequality in people recommender systems: the long-term effects]]
- [[- i’m in the bluesky tonight-- Insights from a year worth of social data|" i’m in the bluesky tonight": Insights from a year worth of social data]]
- [[Link recommendations- Their impact on network structure and minorities|Link recommendations: Their impact on network structure and minorities]]
- [[The rise of social bots]]
- [[A theory of social comparison processes]]
- [[Limits of large language models in debating humans]]
- [[S3- Social-network simulation system with large language model-empowered agents|S3: Social-network simulation system with large language model-empowered agents]]
- [[The role of homophily in the emergence of opinion controversies]]
- [[Quantifying controversy on social media]]
- [[Using agent-based modelling to evaluate the impact of algorithmic curation on social media]]
- [[Understanding echo chambers in e-commerce recommender systems]]
- [[Emergence in social simulation]]
- [[Simulation for the social scientist]]
- [[The strength of weak ties]]
- [[Less than you think- Prevalence and predictors of fake news dissemination on facebook|Less than you think: Prevalence and predictors of fake news dissemination on facebook]]
- [[Information diffusion in online social networks- A survey|Information diffusion in online social networks: A survey]]
- [[A closer look at skip-gram modelling]]
- [[Human-like intuitive behavior and reasoning biases emerged in large language models but disappeared in chatgpt]]
- [[A survey on stance detection for mis- and disinformation identification]]
- [[Community-cross-instruct- Unsupervised instruction generation for aligning large language models to online communities|Community-cross-instruct: Unsupervised instruction generation for aligning large language models to online communities]]
- [[Disinformation and misinformation through the internet- Findings of an exploratory study|Disinformation and misinformation through the internet: Findings of an exploratory study]]
- [[Communicating with algorithms- A transfer entropy analysis of emotions-based escapes from online echo chambers|Communicating with algorithms: A transfer entropy analysis of emotions-based escapes from online echo chambers]]
- [[Digital twins in sport- Concepts, taxonomies, challenges and practical potentials, 2024|Digital twins in sport: Concepts, taxonomies, challenges and practical potentials, 2024]]
- [[Will the global village fracture into tribes- recommender systems and their effects on consumer fragmentation|Will the global village fracture into tribes? recommender systems and their effects on consumer fragmentation]]
- [[Causally estimating the effect of youtube’s recommender system using counterfactual bots]]
- [[Mining triadic closure patterns in social networks]]
- [[The principles of experimental design and their application in sociology]]
- [[Evaluating and inducing personality in pre-trained language models]]
- [[Degenerate feedback loops in recommender systems]]
- [[On the inadequacy of nominal assortativity for assessing homophily in networks]]
- [[Algorithmic bias- review, synthesis, and future research directions|Algorithmic bias: review, synthesis, and future research directions]]
- [[Challenges of hate speech detection in social media- Data scarcity, and leveraging external resources|Challenges of hate speech detection in social media: Data scarcity, and leveraging external resources]]
- [[Experimental evidence of massive-scale emotional contagion through social networks]]
- [[Sentiment analysis in the age of generative ai]]
- [[Stance detection- A survey|Stance detection: A survey]]
- [[Open models, closed minds- on agents capabilities in mimicking human personalities through open large language models|Open models, closed minds? on agents capabilities in mimicking human personalities through open large language models]]
- [[Do llm agents exhibit social behavior-|Do llm agents exhibit social behavior?]]
- [[A survey on deep learning for named entity recognition]]
- [[Large language model-empowered agents for simulating macroeconomic activities]]
- [[The link prediction problem for social networks]]
- [[Argumentation mining- State of the art and emerging trends|Argumentation mining: State of the art and emerging trends]]
- [[Agent-based social simulation of the covid-19 pandemic- A systematic review|Agent-based social simulation of the covid-19 pandemic: A systematic review]]
- [[Divided by the algorithm- the (limited) effects of content-and sentiment-based news recommendation on affective, ideological, and perceived polarization|Divided by the algorithm? the (limited) effects of content-and sentiment-based news recommendation on affective, ideological, and perceived polarization]]
- [[An introduction to the five-factor model and its applications]]
- [[Birds of a Feather- Homophily in Social Networks|Birds of a feather: Homophily in social networks]]
- [[Quantification in social networks]]
- [[Stance and sentiment in tweets]]
- [[The language of opinion change on social media under the lens of communicative action]]
- [[Learning opinion dynamics from social traces]]
- [[Flaming on youtube]]
- [[From perils to possibilities- Understanding how human (and ai) biases affect online fora|From perils to possibilities: Understanding how human (and ai) biases affect online fora]]
- [[Toward a standard approach for echo chamber detection- Reddit case study|Toward a standard approach for echo chamber detection: Reddit case study]]
- [[Unveiling the truth and facilitating change- Towards agent-based large-scale social movement simulation|Unveiling the truth and facilitating change: Towards agent-based large-scale social movement simulation]]
- [[Statistical methods in social science research]]
- [[An agent-based model of message propagation in the facebook electronic social network]]
- [[Clustering and preferential attachment in growing networks]]
- [[Mixing patterns in networks]]
- [[The structure and function of complex networks]]
- [[Cognitive islands and runaway echo chambers- Problems for epistemic dependence on experts|Cognitive islands and runaway echo chambers: Problems for epistemic dependence on experts]]
- [[Echo chambers and epistemic bubbles]]
- [[From mean-field to complex topologies- network effects on the algorithmic bias model|From mean-field to complex topologies: network effects on the algorithmic bias model]]
- [[Modeling algorithmic bias- simplicial complexes and evolving network topologies|Modeling algorithmic bias: simplicial complexes and evolving network topologies]]
- [[Mass media impact on opinion evolution in biased digital environments- a bounded confidence model|Mass media impact on opinion evolution in biased digital environments: a bounded confidence model]]
- [[Network formation and dynamics among multi-llms]]
- [[A survey on the impact of ai-based recommenders on human behaviours- methodologies, outcomes and future directions|A survey on the impact of ai-based recommenders on human behaviours: methodologies, outcomes and future directions]]
- [[The filter bubble- What the Internet is hiding from you|The filter bubble: What the Internet is hiding from you]]
- [[Generative agents- Interactive simulacra of human behavior|Generative agents: Interactive simulacra of human behavior]]
- [[Generative agents- Interactive simulacra of human behavior|Generative agents: Interactive simulacra of human behavior]]
- [[Social Simulacra- Creating Populated Prototypes for Social Computing Systems|Social simulacra: Creating populated prototypes for social computing systems]]
- [[Human-ai coevolution]]
- [[Fighting misinformation on social media using crowdsourced judgments of news source quality]]
- [[The psychology of fake news]]
- [[Opinion formation on social networks with algorithmic bias- dynamics and bias imbalance|Opinion formation on social networks with algorithmic bias: dynamics and bias imbalance]]
- [[Effect of algorithmic bias and network structure on coexistence, consensus, and polarization of opinions]]
- [[Multidimensional political polarization in online social networks]]
- [[- this (smart) town ain’t big enough-- Smart small towns and digital twins for sustainable urban and regional development|" this (smart) town ain’t big enough": Smart small towns and digital twins for sustainable urban and regional development]]
- [[Modelling opinion dynamics in the age of algorithmic personalisation]]
- [[Cooperate or collapse- Emergence of sustainability behaviors in a society of llm agents|Cooperate or collapse: Emergence of sustainability behaviors in a society of llm agents]]
- [[Opinion dynamics on interacting networks- media competition and social influence|Opinion dynamics on interacting networks: media competition and social influence]]
- [[The amplification paradox in recommender systems]]
- [[Facebook and texting made me do it- Media-induced task-switching while studying|Facebook and texting made me do it: Media-induced task-switching while studying]]
- [[Conformity- a path-aware homophily measure for node-attributed networks|Conformity: a path-aware homophily measure for node-attributed networks]]
- [[The closed loop between opinion formation and personalized recommendations]]
- [[Analyzing the changing landscape of the covid-19 vaccine debate on twitter]]
- [[Dynamic models of segregation]]
- [[Experimentable digital twins—streamlining simulation-based systems engineering for industry 4.0]]
- [[An agent-based model of collective emotions in online communities]]
- [[Validating viral marketing strategies in twitter via agent-based social simulation]]
- [[Quasi-experiments- interrupted time-series designs|Quasi-experiments: interrupted time-series designs]]
- [[When llm meets hypergraph- A sociological analysis on personality via online social networks|When llm meets hypergraph: A sociological analysis on personality via online social networks]]
- [[Social media its impact with positive and negative aspects]]
- [[Algorithmic bias amplifies opinion fragmentation and polarization- A bounded confidence model|Algorithmic bias amplifies opinion fragmentation and polarization: A bounded confidence model]]
- [[Social simulation in the social sciences- A brief overview|Social simulation in the social sciences: A brief overview]]
- [[Influence of augmented humans in online interactions during voting events]]
- [[Bots increase exposure to negative and inflammatory content in online social systems]]
- [[Using cognitive psychology to understand gpt-like models needs to extend beyond human biases]]
- [[The online disinhibition effect]]
- [[Digital twin in healthcare- Recent updates and challenges|Digital twin in healthcare: Recent updates and challenges]]
- [[Cognitive load during problem solving- Effects on learning|Cognitive load during problem solving: Effects on learning]]
- [[Digital twin in industry- State-of-the-art|Digital twin in industry: State-of-the-art]]
- [[Self-enhancement through online dating profiles- The role of anticipated future interaction, self-disclosure, and perceived success in mate attraction|Self-enhancement through online dating profiles: The role of anticipated future interaction, self-disclosure, and perceived success in mate attraction]]
- [[Echo chambers and viral misinformation- Modeling fake news as complex contagion|Echo chambers and viral misinformation: Modeling fake news as complex contagion]]
- [[Simulating social media using large language models to evaluate alternative news feed algorithms]]
- [[The drivers of online polarization- Fitting models to data|The drivers of online polarization: Fitting models to data]]
- [[Friend networking sites and their relationship to adolescents’ well-being and social self-esteem]]
- [[Journalists on twitter- self-branding, audiences, and involvement of bots|Journalists on twitter: self-branding, audiences, and involvement of bots]]
- [[Modelling dynamical processes in complex socio-technical systems]]
- [[Social comparison, social media, and self-esteem]]
- [[That is your evidence-- Classifying stance in online political debate|That is your evidence?: Classifying stance in online political debate]]
- [[Computer-mediated communication- Impersonal, interpersonal, and hyperpersonal interaction|Computer-mediated communication: Impersonal, interpersonal, and hyperpersonal interaction]]
- [[Social network analysis- Methods and applications|Social network analysis: Methods and applications]]
- [[Digital twin-oriented complex networked systems based on heterogeneous node features and interaction rules]]
- [[Can large language model agents simulate human trust behaviors-|Can large language model agents simulate human trust behaviors?]]
- [[Urban generative intelligence (ugi)- A foundational platform for agents in embodied city environment|Urban generative intelligence (ugi): A foundational platform for agents in embodied city environment]]
- [[Bubbles bursting- Investigating and measuring the personalisation of social media searches|Bubbles bursting: Investigating and measuring the personalisation of social media searches]]
- [[The social digital twin- the social turn in the field of smart cities|The social digital twin: the social turn in the field of smart cities]]
- [[The impact of youtube recommendation system on video views]]

## Audit Log
- 2026-10-03: Rebuilt Metadata/References from all 162 numbered entries in the full arXiv source, in source order with publisher-visible title labels. The prior import stopped at 99 and used compact opaque targets; 63 omitted source entries are now included. No titles were inferred from old IDs. Abstract and YAML warning unchanged. Independent audit pending.

- Audit invalidated (2026-09-30): auditor admitted incomplete independent checks and premature flag removal. Previous valid audits, if any, remain separate.

- 2026-09-30: Initial/cheap audit failed; stronger source review corrected Algorithm1 exact active-count schedule and follow-loop conflict, state/observations, primitive action mechanisms, recommender scoring and case-study configuration. Independent re-audit pending.

- WITHDRAWN audit claim (2026-09-30): the remaining-audit-c report overstated independent source checks; it does not establish a pass.

## LLM Justification
[^r1]: https://arxiv.org/html/2408.00818; Abstract and Introduction: platform digital-twin aims.
[^r2]: Same source; §3, Figure1 and Figure2: architecture and stored user/content/news/follow/clock state.
[^r3]: Same source; §3.2.2 “Simulation Configuration” and “Simulation workflow,” Algorithm1: fixed-count activity sampling, synchronization, action and second follow loops, daily growth; comment versus loop eligibility discrepancy; example days365 versus adjacent prose100.
[^r4]: Same source; §3.2.1 “Actions and Prompts”: READ selection/reaction, POST, COMMENT/REPLY/SEARCH context/filters, FOLLOW probability sampling, NEWS/SHARE prompts and annotations; profile preprompt and five BigFive dimensions.
[^r5]: Same source; §3.1.1 “Content Recommendations” and “Follows Recommendations”: ranking variants, k, exposure share and homophily bias.
[^r6]: Same source; §4.1 simulation configuration and §4.2 generated-data examples:100days/2400rounds/1000→2000, stated llama3-7b, recommenders,60%,36rounds,600feeds and descriptive scope.
