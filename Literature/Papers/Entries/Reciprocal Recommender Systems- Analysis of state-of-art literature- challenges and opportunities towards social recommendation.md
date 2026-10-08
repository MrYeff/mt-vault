---
title: "Reciprocal Recommender Systems: Analysis of state-of-art literature, challenges and opportunities towards social recommendation"
tags:
  - reciprocal_recommender_system
  - literature_review
  - "model"
authors:
  - "[[Literature/Authors/Iván Palomares|Iván Palomares]]"
  - "[[Literature/Authors/Carlos Porcel|Carlos Porcel]]"
  - "[[Literature/Authors/Luiz Augusto Sangoi Pizzato|Luiz Augusto Sangoi Pizzato]]"
  - "[[Literature/Authors/Ido Guy|Ido Guy]]"
  - "[[Literature/Authors/Enrique Herrera‐Viedma|Enrique Herrera‐Viedma]]"
publication date: 2020-12-07 
source: "https://arxiv.org/pdf/2007.16120v2"
doi: 10.1016/j.inffus.2020.12.001
read status: Todo
⚠️:
  - audit failed
---

## Abstract

There exist situations of decision-making under information overload in the Internet, where people have an overwhelming number of available options to choose from, e.g. products to buy in an e-commerce site, or restaurants to visit in a large city. Recommender systems arose as a data-driven personalized decision support tool to assist users in these situations: they are able to process user-related data, filtering and recommending items based on the user’s preferences, needs and/or behaviour. Unlike most conventional recommender approaches where items are inanimate entities recommended to the users and success is solely determined upon the end user’s reaction to the recommendation(s) received, in a Reciprocal Recommender System (RRS) users become the item being recommended to other users. Hence, both the end user and the user being recommended should accept the “matching” recommendation to yield a successful RRS performance. The operation of an RRS entails not only predicting accurate preference estimates upon user interaction data as classical recommenders do, but also calculating mutual compatibility between (pairs of) users, typically by applying fusion processes on unilateral user-to-user preference information. This paper presents a snapshot-style analysis of the extant literature that summarizes the state-of-the-art RRS research to date, focusing on the algorithms, fusion processes and fundamental characteristics of RRS, both inherited from conventional user-to-item recommendation models and those inherent to this emerging family of approaches. Representative RRS models are likewise highlighted. Following this, we discuss the challenges and opportunities for future research on RRSs, with special focus on (i) fusion strategies to account for reciprocity and (ii) emerging application domains related to social recommendation.

## Research Questions
> Research Questions extracted via LLM
- How do reciprocal recommenders estimate mutual compatibility when both people must accept a match?[^r1]
- What algorithmic, preference-fusion, evaluation, and application challenges characterize reciprocal recommendation?[^r1]

## Model
> Model extracted via LLM according to [[Model Notation]]

### What does it represent?
- A conceptual people-to-people recommender: successful matching requires positive responses from both users. Unilateral preferences and reciprocal ranking are distinct.[^r4]
- This notation covers normalized preference-score aggregation. The review also covers fusion of rankings, where the fused result is not a mutual-preference degree.[^r4]

```yml
World:
  users: [User]
  preferences: [UserId -> [UserId -> Score]]

User:
  profile: ()
  interactions: [()]

Score: 0..1
```

### How does it work?
- Estimate `p_x_y` and `p_y_x`, fuse them, then rank eligible users. Single-class systems allow any other user; two-class systems restrict candidates to the opposite class.[^r4]
- `FUSION` and eligibility are method-specific configurations. The conceptual synthesis defines neither an acceptance threshold nor simulated acceptance behavior.[^r4]

```
recommend(world: World, user: UserId) -> [UserId]:
  for other in ELIGIBLE(world.users, user):
    scores[other] = FUSION(
      world.preferences[user][other],
      world.preferences[other][user]
    )
  out = sort_descending(scores).keys()
```

- A common surveyed `FUSION` is the harmonic mean below; arithmetic and geometric means are alternatives. This example does not select one method for the entire review.[^r4]

```
harmonic(p_x_y: Score, p_y_x: Score) -> Score:
  if p_x_y == 0 or p_y_x == 0: out = 0
  else: out = 2 * p_x_y * p_y_x / (p_x_y + p_y_x)
```

### What can it answer?
- Organize algorithms, fusion functions and evaluation for bilateral recommendation; ranking a pair does not establish bilateral acceptance.[^r4]

### Where does it apply?
- Dating, recruitment, learning and social matching. This is the review's conceptual interface; individual surveyed algorithms and their evaluations are omitted.[^r3][^r4]

## Study Design
> Study design extracted via LLM

This is a literature analysis, not an empirical experiment or one fixed simulation. It classifies reciprocal-recommender algorithms, preference-fusion approaches, evaluation, and applications, and contributes the conceptual reciprocal-score model summarized above.[^r4][^r3]

## Metadata
### References
- [[Multistakeholder recommendation- Survey and research directions|Multistakeholder recommendation: Survey and research directions]]
- [[Multi-stakeholder recommendation and its connection to multi- sided fairness]]
- [[Context-aware recommender systems]]
- [[Recommender Systems- The textbook|Recommender Systems: The textbook]]
- [[Ccr - a content-collaborative reciprocal recommender for online dating]]
- [[Explicit and implicit user preferences in online dating]]
- [[User-to-user recommendation using the concept of movement patterns- A study using a dating social network|User-to-user recommendation using the concept of movement patterns: A study using a dating social network]]
- [[A Probabilistic Reciprocal Recommender with Temporal Dynamics]]
- [[A people-to-people content-based reciprocal recommender using hidden markov models]]
- [[A scalable people-to-people hybrid reciprocal recommender using hidden markov models]]
- [[A content based approach for recommending personnel for job positions]]
- [[Finding and matching communities in social networks using data mining]]
- [[Improving matching process in social network using implicit and explicit user information]]
- [[A survey on recommendations in location-based social networks]]
- [[Aggregation Functions- A Guide for Practitioners|Aggregation Functions: A Guide for Practitioners]]
- [[Offline and online evaluation of recommendations]]
- [[Matrix factorization model in collaborative filtering algorithms- A survey|Matrix factorization model in collaborative filtering algorithms: A survey]]
- [[Intelligent tourism recommender systems- a survey|Intelligent tourism recommender systems: a survey]]
- [[Comparing peer recommendation strategies in a mooc]]
- [[Recommender system for online dating service]]
- [[Hybrid recommender systems- Survey and experiments|Hybrid recommender systems: Survey and experiments]]
- [[Collaborative filtering for people to people recommendation in social networks]]
- [[Reciprocal and heterogeneous link prediction in social networks]]
- [[Procf- Probabilistic collaborative filtering for reciprocal recommendation|Procf: Probabilistic collaborative filtering for reciprocal recommendation]]
- [[A deep hybrid model for recommendation systems]]
- [[Cross-domain recommender systems]]
- [[A characterization methodology for candidates and recruiters interaction in online recruitment services]]
- [[Make new friends, but keep the old- Recommending people on social networking sites|Make new friends, but keep the old: Recommending people on social networking sites]]
- [[Withshare- A mobile application to support community coproduction activities|Withshare: A mobile application to support community coproduction activities]]
- [[A reciprocal collaborative method using relevance feedback and feature importance]]
- [[Improving matching process in social network]]
- [[A recommendation method for online dating networks based on social relations and demographic information]]
- [[A common neighbour based two-way collaborative recommendation method]]
- [[Performance evaluation of recommender systems]]
- [[User-adapted travel planning system for personalized schedule recommendation]]
- [[The network effects of recommending social connections]]
- [[Who will cite you back- reciprocal link prediction in citation networks|Who will cite you back? reciprocal link prediction in citation networks]]
- [[A graphical model formulation of collaborative filtering neighbourhood methods with fast maximum entropy training]]
- [[Large-scale decision-making- Characterization, taxonomy, challenges and future directions from an artificial intelligence and applications perspective|Large-scale decision-making: Characterization, taxonomy, challenges and future directions from an artificial intelligence and applications perspective]]
- [[A reciprocal recommender system for graduates’ recruitment]]
- [[A hybrid collaborative filtering model with deep structure for recommender systems]]
- [[If it’s convenient- Leveraging context in peer-to-peer variable service transaction recommendations|If it’s convenient: Leveraging context in peer-to-peer variable service transaction recommendations]]
- [[A survey of collaborative filtering algorithms for social recommender systems]]
- [[Scalable and explainable friend recommendation in campus social network system]]
- [[A trust-aware system for personalized user recommendations in social networks]]
- [[Group recommender systems- An introduction|Group recommender systems: An introduction]]
- [[The invisible contours of online dating communities- A social network perspective|The invisible contours of online dating communities: A social network perspective]]
- [[On the use of cross-domain user preferences and personality traits in collaborative filtering]]
- [[The covid-19 pandemic has changed education forever]]
- [[Increasing engagement through early recommender intervention]]
- [[Weighted content based methods for recommending connections in online social networks]]
- [[Recommender systems evaluations - Offline, online, time and a/a test|Recommender systems evaluations : Offline, online, time and a/a test]]
- [[A survey on solving cold start problem in recommender systems]]
- [[Recommendation systems for markets with two sided preferences]]
- [[Cluestr- Mobile social networking for enhanced group communication|Cluestr: Mobile social networking for enhanced group communication]]
- [[People recommendation on social media]]
- [[Mining expertise and interests from social media]]
- [[Same places, same things, same people-- Mining user similarity on social media|Same places, same things, same people?: Mining user similarity on social media]]
- [[Islands in the stream- A study of item recommendation within an enterprise social stream|Islands in the stream: A study of item recommendation within an enterprise social stream]]
- [[Do you know-- Recommending people to invite into your social network|Do you know?: Recommending people to invite into your social network]]
- [[What is your organization ‘like’ - a study of liking activity in the enterprise|What is your organization ‘like’ ? a study of liking activity in the enterprise]]
- [[Swimming against the streamz- Search and analytics over the enterprise activity stream|Swimming against the streamz: Search and analytics over the enterprise activity stream]]
- [[Do you want to know-- Recommending strangers in the enterprise|Do you want to know?: Recommending strangers in the enterprise]]
- [[Personalized recommendation of social software items based on social relations]]
- [[Recommending twitter users to follow using content and collaborative filtering approaches]]
- [[Ihr- An online recruiting system for xiamen talent service center|Ihr: An online recruiting system for xiamen talent service center]]
- [[ihr+- A mobile reciprocal job recommender system|ihr+: A mobile reciprocal job recommender system]]
- [[A job recommender system based on user clustering]]
- [[It’s a match! reciprocal recommender system for graduating students and jobs]]
- [[The perception of others- Inferring reputation from social media in the enterprise|The perception of others: Inferring reputation from social media in the enterprise]]
- [[Digital traces of interest- Deriving interest relationships from social media interactions|Digital traces of interest: Deriving interest relationships from social media interactions]]
- [[“masterful” matchmaking in service transactions- Inferred abilities, needs and interests versus activity histories|“masterful” matchmaking in service transactions: Inferred abilities, needs and interests versus activity histories]]
- [[Using interaction signals for job recommendations]]
- [[Urbansocialradar- A place-aware social matching model for estimating serendipitous interaction willingness in Korean cultural context|Urbansocialradar: A place-aware social matching model for estimating serendipitous interaction willingness in Korean cultural context]]
- [[People recommendation based on aggregated bidirectional intentions in social network site]]
- [[Intelligent group suggestions based on students’ conceptual understanding- (abstract only)|Intelligent group suggestions based on students’ conceptual understanding: (abstract only)]]
- [[Providing explanations for recommendations in reciprocal environments|Providing explanations for recommendations in reciprocal environments]]
- [[Optimally balancing receiver and recommended users’ importance in reciprocal recommender systems|Optimally balancing receiver and recommended users’ importance in reciprocal recommender systems]]
- [[People-to-people reciprocal recommenders]]
- [[Using a critic to promote less popular candidates in a people-to-people recommender system]]
- [[Interaction-based collaborative filtering methods for recommendation in online dating]]
- [[Online dating recommender systems- the split-complex number approach|Online dating recommender systems: the split-complex number approach]]
- [[A people-to-people recommendation system using tensor space models]]
- [[A people-to-people matching system using graph mining techniques]]
- [[Increasing mooc completion rates through social interactions- a recommendation system|Increasing mooc completion rates through social interactions: a recommendation system]]
- [[Does a Peer Recommender Foster Students’ Engagement in MOOCs-|Does a Peer Recommender Foster Students’ Engagement in MOOCs?]]
- [[Predicting positive and negative links in online social networks]]
- [[Mentor-spotting- recommending expert mentors to mentees for live trouble-shooting in codementor|Mentor-spotting: recommending expert mentors to mentees for live trouble-shooting in codementor]]
- [[Meet- a generalized framework for reciprocal recommender systems|Meet: a generalized framework for reciprocal recommender systems]]
- [[Incorporating facial attractiveness in photos for online dating recommendation|Incorporating facial attractiveness in photos for online dating recommendation]]
- [[Practical lessons for job recommendations in the cold-start scenario|Practical lessons for job recommendations in the cold-start scenario]]
- [[Rating prediction based job recommendation service for college students]]
- [[Employer oriented recruitment recommender service for university students]]
- [[Matching people and jobs- A bilateral recommendation approach|Matching people and jobs: A bilateral recommendation approach]]
- [[Encount’r- Exploring passive context-awareness for opportunistic social matching|Encount’r: Exploring passive context-awareness for opportunistic social matching]]
- [[Supporting opportunities for context-aware social matching- An experience sampling study|Supporting opportunities for context-aware social matching: An experience sampling study]]
- [[Making social matching context-aware- Design concepts and open challenges|Making social matching context-aware: Design concepts and open challenges]]
- [[Identifying opportunities for valuable encounters- Toward context-aware social matching systems|Identifying opportunities for valuable encounters: Toward context-aware social matching systems]]
- [[Reciprocal recommendation for job matching with bidirectional feedback|Reciprocal recommendation for job matching with bidirectional feedback]]
- [[A systematic literature review of multicriteria recommender systems]]
- [[Utilizing past relations and user similarities in a social matching system]]
- [[A social matching system for an online dating network- A preliminary study|A social matching system for an online dating network: A preliminary study]]
- [[A social trust based friend recommender for online communities]]
- [[Arikui - a dubious user detection system for online dating in japan]]
- [[Aggregation strategies in user-to-user reciprocal recommender systems]]
- [[Latent factor models and aggregation operators for collaborative filtering in reciprocal recommender systems]]
- [[Hybrid reciprocal recommender systems- Integrating item-to-user principles in reciprocal recommendation|Hybrid reciprocal recommender systems: Integrating item-to-user principles in reciprocal recommendation]]
- [[Online matchmaking using collaborative filtering and reciprocal recommender systems|Online matchmaking using collaborative filtering and reciprocal recommender systems]]
- [[Reciprocal recommendation- matching users with the right users|Reciprocal recommendation: matching users with the right users]]
- [[Reversed cf- A fast collaborative filtering algorithm using a k-nearest neighbor graph|Reversed cf: A fast collaborative filtering algorithm using a k-nearest neighbor graph]]
- [[Learning user preferences in online dating]]
- [[Recommending people to people- the nature of reciprocal recommenders with a case study in online dating|Recommending people to people: the nature of reciprocal recommenders with a case study in online dating]]
- [[Recon- A reciprocal recommender for online dating|Recon: A reciprocal recommender for online dating]]
- [[Reciprocal recommenders]]
- [[The effect of suspicious profiles on people recommenders]]
- [[Beyond friendship- The art, science and applications of recommending people to people in social networks|Beyond friendship: The art, science and applications of recommending people to people in social networks]]
- [[Finding someone you will like and who won’t reject you]]
- [[Stochastic matching and collaborative filtering to recommend people to people]]
- [[Sharing notes- An academic social network based on a personalized fuzzy linguistic recommender system|Sharing notes: An academic social network based on a personalized fuzzy linguistic recommender system]]
- [[Reciprocal peer recommendation for learning purposes]]
- [[Reciprocal recommender system for learners in massive open online courses (moocs)]]
- [[EARS- emotion-aware recommender system based on hybrid information fusion|EARS: emotion-aware recommender system based on hybrid information fusion]]
- [[Reciprocal ranking- A hybrid ranking algorithm for reciprocal recommendation|Reciprocal ranking: A hybrid ranking algorithm for reciprocal recommendation]]
- [[Friendsensing- Recommending friends using mobile phones|Friendsensing: Recommending friends using mobile phones]]
- [[Impression formation in corporate people tagging]]
- [[Recommending peers for learning- Matching on dissimilarity in interpretations to provoke breakdown|Recommending peers for learning: Matching on dissimilarity in interpretations to provoke breakdown]]
- [[Building a reciprocal recommendation system at scale from scratch- Learnings from one of japan’s prominent dating applications|Building a reciprocal recommendation system at scale from scratch: Learnings from one of japan’s prominent dating applications]]
- [[Bpr- Bayesian personalized ranking from implicit feedback|Bpr: Bayesian personalized ranking from implicit feedback]]
- [[A note on explicit versus implicit information for job recommendation]]
- [[Evaluating recommendation and search in the labor market]]
- [[Recommender Systems Handbook]]
- [[Expertise recommendation- A two-way knowledge communication channel|Expertise recommendation: A two-way knowledge communication channel]]
- [[Blinddate recommender- A context-aware ontology-based dating recommendation platform|Blinddate recommender: A context-aware ontology-based dating recommendation platform]]
- [[Privatejobmatch- A privacy-oriented deferred multi-match recommender system for stable employment|Privatejobmatch: A privacy-oriented deferred multi-match recommender system for stable employment]]
- [[A randomized approach for structural and message based private friend recommendation in online social networks]]
- [[Information retrieval models for contact recommendation in social networks]]
- [[Socio-spatial properties of online location-based social networks]]
- [[A graph-based friend recommendation system using genetic algorithm]]
- [[Relational learning via collective matrix factorization]]
- [[Gender-specific preference in online dating]]
- [[Numerical study of reciprocal recommendation with domain matching]]
- [[Managing diversity and inclusion- an international perspective|Managing diversity and inclusion: an international perspective]]
- [[Transitive node similarity for link prediction in social networks with positive and negative links]]
- [[Couplenet- Paying attention to couples with coupled attention for relationship recommendation|Couplenet: Paying attention to couples with coupled attention for relationship recommendation]]
- [[Transfer-learning based model for reciprocal recommendation]]
- [[Food recommender systems- Important contributions, challenges and future research directions|Food recommender systems: Important contributions, challenges and future research directions]]
- [[Multi-criteria Decision Making Methods- A Comparative Study|Multi-criteria Decision Making Methods: A Comparative Study]]
- [[Recommending who to follow on twitter based on tweet contents and social connections]]
- [[Online dating recommendations- matching markets and learning preferences|Online dating recommendations: matching markets and learning preferences]]
- [[Online reciprocal recommendation with theoretical performance guarantees]]
- [[A preference-driven database approach to reciprocal user recommendations in online social networks]]
- [[We-rec- A fairness-aware reciprocal recommendation based on walrasian equilibrium|We-rec: A fairness-aware reciprocal recommendation based on walrasian equilibrium]]
- [[Reciprocal recommendation system for online dating]]
- [[Characterization of user online dating behavior and preference on a large online dating site]]
- [[Supporting learners ’ group formation with reciprocal recommender technology]]
- [[Uninorm aggregation operators]]
- [[Question recommendation with constraints for massive open online courses]]
- [[Matching of social events and users- a two-way selection perspective|Matching of social events and users: a two-way selection perspective]]
- [[Reciprocal recommendation algorithm for the field of recruitment]]
- [[New to online dating- learning from experienced users for a successful match|New to online dating? learning from experienced users for a successful match]]
- [[Community-based recommendation for cold-start problem- A case study of reciprocal online dating recommendation|Community-based recommendation for cold-start problem: A case study of reciprocal online dating recommendation]]
- [[Recommendation in reciprocal and bipartite social networks- A case study of online dating|Recommendation in reciprocal and bipartite social networks: A case study of online dating]]
- [[You will succeed or not- matching prediction in a marriage consulting service|You will succeed or not? matching prediction in a marriage consulting service]]
- [[Intrank- Interaction ranking-based trustworthy friend recommendation|Intrank: Interaction ranking-based trustworthy friend recommendation]]
- [[A research analytics framework-supported recommendation approach for supervisor selection]]
- [[Community-based user recommendation in uni-directional social networks]]
- [[User recommendations in reciprocal and bipartite social networks–an online dating case study]]
- [[Multi-stakeholder recommendations- Case studies, methods and challenges|Multi-stakeholder recommendations: Case studies, methods and challenges]]
- [[Fairness in reciprocal recommendations- A speed-dating study|Fairness in reciprocal recommendations: A speed-dating study]]
- [[Applying different classification techniques in reciprocal job recommender system for considering job candidate preferences]]

## Audit Log
- 2026-10-03: Rebuilt References from all 170 numbered entries in the cached arXiv v2 source, in exact source order; removed surplus imported links and resolved opaque targets. The source-based repair preserved abstract/model content; `audit failed` remains pending independent full-source audit.

## LLM Justification
[^r1]: The paper’s abstract, at https://arxiv.org/pdf/2007.16120v2. The questions paraphrase the stated purpose, research scope, and reported approach.
[^r3]: Palomares et al., §§1, 4–6: snapshot-style literature analysis, representative algorithms, evaluation and application domains. Accessible author paper: https://arxiv.org/pdf/2007.16120v2; published DOI 10.1016/j.inffus.2020.12.001.
[^r4]: Palomares et al., §2 Definition 2.3/Eq. (3), Fig. 1 (not Fig. 2), Definitions 2.4–2.5; §3.2/Table 3 (fusion alternatives, score versus ranking fusion). Accessible author paper: https://arxiv.org/pdf/2007.16120v2.
