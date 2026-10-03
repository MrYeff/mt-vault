---
title: "Bias Reduction in Social Networks Through Agent-Based Simulations"
tags:
  - "model"
  - "simulation"
authors:
  - "[[Literature/Authors/Nathan Bartley|Nathan Bartley]]"
  - "[[Literature/Authors/Keith Burghardt|Keith Burghardt]]"
  - "[[Literature/Authors/Kristina Lerman|Kristina Lerman]]"
publication date: 2024-10-22
source: "https://arxiv.org/pdf/2409.16558"
doi: "10.1007/978-3-031-71975-2_5"
read status: Todo
⚠️: []
---
## Abstract

Online social networks use recommender systems to suggest relevant information to their users in the form of personalized timelines. Studying how these systems expose people to information at scale is difficult to do as one cannot assume each user is subject to the same timeline condition and building appropriate evaluation infrastructure is costly. We show that a simple agent-based model where users have fixed preferences affords us the ability to compare different recommender systems (and thus different personalized timelines) in their ability to skew users' perception of their network. Importantly, we show that a simple greedy algorithm that constructs a feed based on network properties reduces such perception biases comparable to a random feed. This underscores the influence network structure has in determining the effectiveness of recommender systems in the social network context and offers a tool for mitigating perception biases through algorithmic feed construction.

## Research Questions
> Research Questions extracted via LLM
- How do alternative feed algorithms affect users’ exposure to network members and their perceptions of a binary trait’s prevalence?[^r1]
- Can a greedy feed-selection strategy reduce local exposure bias while retaining feed utility?[^r2]

## Model
> Model extracted via LLM according to [[Model Notation]]

- The model overlays fixed binary traits and simulated activity on a sampled Twitter follower network of about 173,000 users and 1.5 million edges.[^r3]
- It examines feed exposure for 5,599 core users over 36 hourly ticks.[^r3]
- At each tick, users activate with probability 0.083 and active users generate a lognormal number of tweets (μ=0, σ=1); core users then receive policy-specific feeds and like same-trait tweets with probability 0.20 or other-trait tweets with probability 0.05.[^r3]
- Observed edges are reset at t=24. Trait prevalence is held fixed within each run and tested at P(X=1) ∈ {0.05, 0.15, 0.50}. (Sections 3.1–3.3.)[^r3]

### What does it represent?
A Twitter/X-like environment used to compare feed strategies’ effects on network exposure and perceived trait prevalence, not changing preferences or friendship formation. [^r3]

### How does it work?

```yml
World:
  users: [User]
  edges: [FollowEdge]
  tweets: [Tweet]
  feed_policy: FeedPolicy
  core_users: [CoreUser]
  trait_prevalence: TraitPrevalence
  feed_length: FeedLength
  tick: 0..SIMULATION_TICKS

User:
  trait: TRAIT_0 | TRAIT_1
  active: bool
  likes: [TweetId]

CoreUser:
  user: UserId

FollowEdge:
  source: UserId
  target: UserId

TraitPrevalence:
  LOW_TRAIT_PREVALENCE
  MEDIUM_TRAIT_PREVALENCE
  HIGH_TRAIT_PREVALENCE

FeedLength:
  FEED_LENGTH_30
  FEED_LENGTH_50
  FEED_LENGTH_100

FeedPolicy:
  Random: ...
  ReverseChronological: ...
  NeuralCollaborativeFiltering: ...
  WideAndDeep: ...
  MinimizeRho: ...

Tweet:
  author: UserId
  created_at: 0..SIMULATION_TICKS
```

```
TRAIT_0 = 0
TRAIT_1 = 1
LOW_TRAIT_PREVALENCE = 0.05
MEDIUM_TRAIT_PREVALENCE = 0.15
HIGH_TRAIT_PREVALENCE = 0.50

SIMULATION_TICKS = 36
USER_ACTIVATION_PROBABILITY = 0.083
TWEET_COUNT_LOG_MEAN = 0.0
TWEET_COUNT_LOG_SD = 1.0
TWEET_COUNT_DISTRIBUTION = LogNormal(TWEET_COUNT_LOG_MEAN, TWEET_COUNT_LOG_SD)

FEED_LENGTH_30 = 30
FEED_LENGTH_50 = 50
FEED_LENGTH_100 = 100
SAME_TRAIT_LIKE_PROBABILITY = 0.20
OTHER_TRAIT_LIKE_PROBABILITY = 0.05
NETWORK_RESET_TICK = 24
```

```
sim_step(
  mut world: World
):

  activate_users(
    world,
    probability = USER_ACTIVATION_PROBABILITY,
  )
  generate_tweets(
    world,
    count_distribution = TWEET_COUNT_DISTRIBUTION,
  )

  for user in world.core_users:
    candidates = tweets_from_friends_and_friends_of_friends(user)
    feed = select_feed(
      candidates,
      world.feed_policy,
      length = world.feed_length,
    )
    update_observed_edges(user, authors_and_sources(feed))
    like_same_trait_tweet(SAME_TRAIT_LIKE_PROBABILITY)
    like_other_trait_tweet(OTHER_TRAIT_LIKE_PROBABILITY)

  if world.tick == NETWORK_RESET_TICK:
    reset_observed_edges(world)

  world.tick += 1
```

- Tested feed lengths are 30, 50, and 100; the simulation spans 36 hourly ticks.[^r4]
- Random feeds shuffle candidate tweets; reverse-chronological feeds sort them by time.[^r4]
- Neural Collaborative Filtering and Wide & Deep are retrained each tick for 10 epochs on the core users’ likes.[^r4]
- The greedy MinimizeRho policy selects observed edges to reduce ρₖₓ, defined from the difference between the mean in-degree of X=1 nodes and the overall mean in-degree (scaled by prevalence and standard deviations).[^r4]
- Feed candidates are tweets from friends and friends-of-friends. (Sections 3.1–3.4, Eq. 1.)[^r4]

### What can it answer?
The model compares local bias and inequality in attention across feed policies, alongside precision and network exposure measures; its outcomes concern simulated feeds and perceptions. [^r5]

### Where does it apply?
To the specified synthetic behavior layered on a sampled Twitter follower network; conclusions are conditional on the fixed traits, engagement probabilities, candidate exposure, and feed algorithms described. [^r3][^r4]

## Metadata
### References
> ⚠️ These links have not been reconciled with the paper's bibliography; completeness and mapping remain unverified.

- [[TheMajorityIllusionInSocialNetworks]]
- [[ExposureToIdeologicallyDiverseNewsAndOpinionOnFacebook]]
- [[Feedvis]]
- [[AMultiViewDeepLearningApproachForCrossDomainUserModelingInRecommendationSystems]]
- [[ITweetHonestlyITweetPassionatelyTwitterUsersContextCollapseAndTheImaginedAudience]]
- [[FirstILikeItThenIHideIt]]
- [[WideDeepLearningForRecommenderSystems]]
- [[RepastHpcAPlatformForLargeScaleAgentBasedModeling]]
- [[NeuralCollaborativeFiltering]]
- [[FriendshipParadoxBiasesPerceptionsInDirectedNetworks]]
- [[UnresolvedReference6B232C695FB37CB8]]
- [[MeasuringMisinformationInVideoSearchPlatformsAnAuditStudyOnYoutube]]
- [[HowYoutubeLeadsPrivacySeekingUsersAwayFromReliableInformation]]
- [[ProblematicMachineBehavior]]
- [[AnAuditOfMisinformationFilterBubblesOnYoutubeBubbleBurstingAndRecentBehaviorChanges]]
- [[TheDualEchoChamberModelingSocialMediaPolarizationForInterventionalRecommending]]
- [[SystemsBiologyAtTheGigaScaleLargeMultiscaleModelsOfComplexHeterogeneousMulticellularSystems]]
- [[LargeScaleAgentBasedSimulationsOfOnlineSocialNetworks]]
- [[TheAmplificationParadoxInRecommenderSystems]]
- [[AsymmetricIdeologicalSegregationInExposureToPoliticalNewsOnFacebook]]
- [[HowDoSocialMediaFeedAlgorithmsAffectAttitudesAndBehaviorInAnElectionCampaign]]
- [[ADataDrivenAgentBasedSimulationOfThePublicBicycleSharingSystemInSejongCity]]
- [[AnAgentBasedModelOfRedditInteractionsAndModeration]]
- [[UnresolvedReferenceDB424F1B7EFF7746]]
- [[UnresolvedReference7D303A93E2DBD680]]
- [[SimulatingSocialMediaUsingLargeLanguageModelsToEvaluateAlternativeNewsFeedAlgorithms]]
- [[UnresolvedReference46B36FA47C2E8D35]]
- [[UnresolvedReference1FCABCBA1A5DE3B8]]

## Audit Log
- Initial audit failed because the feed loop implied that all network nodes receive feeds, omitted fixed trait-prevalence scenarios, hid most feed-policy procedures, and used the proceedings’ 2025 copyright year as the publication date. Corrected the modeled feed recipients and policy details, added source parameter values, and set the eBook publication date to 2024-10-22. Awaiting independent re-audit.

- Independent re-audit passed after the source and bibliography corrections.

## LLM Justification
[^r1]: Primary full text, “User Behavior,” “Model Parameters,” and “Bias & Performance Metrics,” pp. 2–4; Discussion, pp. 4–6.
[^r2]: Primary full text, Abstract and Discussion, which describe the greedy approach and comparative outcome.
[^r3]: Primary full text, §§3.1–3.3, pp. 1–3, including network, modeled core users, time-step sequence, behavior, reset, and fixed prevalence conditions.
[^r4]: Primary full text, §§3.1–3.4, pp. 2–4; feed candidates and algorithms, Eq. 1, training procedure, and feed lengths.
[^r5]: Primary full text, §3.4, pp. 3–4, metrics; results in §4.
