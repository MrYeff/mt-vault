---
title: "Social Relationships and the Emergence of Social Networks"
tags:
  - social_network
  - simulation
  - "model"
authors:
  - "[[Literature/Authors/Alistair Sutcliffe|Alistair Sutcliffe]]"
  - "[[Literature/Authors/Di Wang|Di Wang]]"
  - "[[Literature/Authors/Robin Dunbar|Robin Dunbar]]"
publication date: 2012-10-31 
source: "https://www.jasss.org/15/4/3/3.pdf"
doi: 10.18564/jasss.2059
read status: Todo
⚠️:
  - audit failed
---

## Abstract

In complex social systems such as those of many mammals, including humans, groups (and hence ego-centric social networks) are commonly structured in discrete layers. We describe a computational model for the development of social relationships based on agents' strategies for social interaction that favour more less-intense, or fewer more-intense partners. A trust-related process controls the formation and decay of relationships as a function of interaction frequency, the history of interaction, and the agents' strategies. A good fit of the observed layers of human social networks was found across a range of model parameter settings. Social interaction strategies which favour interacting with existing strong ties or a time-variant strategy produced more observation-conformant results than strategies favouring more weak relationships. Strong-tie strategies spread in populations under a range of fitness conditions favouring wellbeing, whereas weak-tie strategies spread when fitness favours foraging for food. The implications for modelling the emergence of social relationships in complex structured social networks are discussed.

## Research Questions
> Research Questions extracted via LLM
- Can interaction strategies and trust-related relationship formation reproduce the layered structure observed in human social networks?[^r1]
- Under what fitness conditions do strategies favoring stronger existing ties or weaker ties spread?[^r1]

## Model
> Model extracted via LLM according to [[Model Notation]]

### What does it represent?
- Agents form directed trusting relationships while allocating turns to foraging or social interaction. Strategy governs partner search; response may cooperate or defect.[^r3]
- The notation covers relationship state and the basic selection experiment; it does not reconstruct unspecified inherited probability functions.[^r3][^r4]

```yml
World:
  agents: [Agent]
  cycle: u32
  generation: u32

Agent:
  strategy: FavourFew | MediumTies | FavourMany | Staged
  trust: [AgentId -> f64]
  successful_contacts: [AgentId -> 0..]
  incoming: 0..
  outgoing: 0..
  forage_turns: 0..
  defects: 0..
```

### How does it work?
- Each cycle gives every agent one turn; `FM` selects foraging (+1 resource) or social contact. Partners are initially random.[^r3]
- Search later favors high-trust, midpoint or low-trust relationships; Staged shifts from high-trust toward weak/unknown partners over the lifetime.[^r3]
- Successful-interaction memory drives search; previous defections are not separately used in partner choice.[^r3]
- Cooperation raises initiator → responder trust; defection lowers it and increments defect count. Prose specifies increasing logarithmic compression, buffering high-trust ties against both signs, and logarithmic decay that weakens stronger ties less.[^r3]
- ⚠️ The printed §2.6 algorithm instead gives increments/decrements `MaxCR - CI * Trust` and `Trust -= W`; it does not define enough detail to identify these with the logarithmic prose.[^r5]
- §4.4 selects log increase/linear decrease. These alternatives are retained as a source conflict; no single exact trust/decay implementation is inferred.[^r5]
- The following fitness equations are transcribed from §4.2. `ties` means the ego's existing relationships; the paper leaves zero-tie/zero-outgoing division unspecified.[^r4]

```
fitness(agent: Agent, ties: [AgentId]) -> (f64, f64):
  n = ties.length()
  wellbeing = sum(agent.trust[ties]) * agent.incoming / agent.outgoing / n
  resource = agent.forage_turns * n
  out = (wellbeing, resource)
```

- Basic selection: `LIFETIME=2000` cycles, `N=300` equally split among strategies, `GENERATIONS=20`. Rank wellbeing and resource, sum weighted ranks, replace the bottom 20% with copies sampled from the top 20%. The weights and forage/social ratio are experimental controls.[^r4]

### What can it answer?
- Measure ranked ego trust, strong/medium/weak ties (upper/middle/lower trust terciles), and strategy survival across generations under wellbeing/resource trade-offs.[^r4]

### Where does it apply?
- Mechanism experiments on layered ego networks. Exact inherited search/decay functions, kin seeding and the later mutation/crossover experiments are omitted; unresolved trust rules prevent treating this summary as a complete reproducible simulator.[^r3][^r4][^r5]

## Metadata
### References
- [[IsFriendshipAkinToKinship]]
- [[SmallGroupsAsComplexSystemsFormationCoordinationDevelopmentAndAdaptation]]
- [[TheNeedToBelongDesireForInterpersonalAttachmentsAsAFundamentalHumanMotivation]]
- [[SpatialBehaviorInGroupsAnAgentBasedApproach]]
- [[TheEvolutionOfReciprocityInSizableGroups]]
- [[TargetArticleSelectiveInvestmentTheoryRecastingTheFunctionalSignificanceOfCloseRelationships]]
- [[HumanSympathyGroups]]
- [[CoevolutionOfNeocortexSizeGroupSizeAndLanguageInHumans]]
- [[TheSocialBrainHypothesis]]
- [[MindTheGapOrWhyHumansArenTJustGreatApes]]
- [[BrainAndBehaviourInPrimateEvolutionInPHKappelerJSilkEds]]
- [[UnderstandingPrimateBrainEvolution]]
- [[SocialNetworksSupportCliquesAndKinship]]
- [[TimeAsAnEcologicalConstraint]]
- [[TheStrengthOfWeakTies]]
- [[EconomicActionAndSocialStructureTheProblemOfEmbeddedness]]
- [[TheGeneticalEvolutionOfSocialBehaviourIAndIi]]
- [[NiceGuysFinishFirstTheCompetitiveAltruismHypothesis]]
- [[TheDayToDayFunctioningOfCloseVersusCasualFriendships]]
- [[AttitudesAndCognitiveOrganization]]
- [[SocialNetworkSizeInHumans]]
- [[NetworkScalingRevealsConsistentFractalPatternInHierarchicalMammalianSocieties]]
- [[FriendshipCliquishnessAndTheEmergenceOfCooperation]]
- [[EffectsOfTrustOnComplexAdaptiveSupplyNetworksAnAgentBasedSimulationStudy]]
- [[SenseAndNonsenseEvolutionaryPerspectivesOnHumanBehaviour]]
- [[GroupSizeGroomingAndSocialCohesionInPrimates]]
- [[TimeManagementInGreatApesImplicationsForGorillaBiogeography]]
- [[SizeMattersVariationInPersonalNetworkSizePersonalityAndEffectOnInformationTransmission]]
- [[TheEvolutionOfTrustAndCooperationBetweenStrangersAComputationalModel]]
- [[AltruismAndKinshipACrossCulturalExperimentalStudy]]
- [[SocialIsolationInAmericaChangesInCoreDiscussionNetworksOverTwoDecades]]
- [[EvolutionOfIndirectReciprocityBySocialInformationTheRoleOfTrustAndReputationInEvolutionOfAltruism]]
- [[SocializationInSmallGroupsTemporalChangesInIndividualGroupRelationsInLBerkowitzEd]]
- [[EvolutionOfIndirectReciprocityByImageScoring]]
- [[EvolutionOfIndirectReciprocity]]
- [[TowardsABehaviouralTheoryLinkingTrustReciprocityAndReputationInEOstromJWalkerEds]]
- [[FriendshipMaintenanceAnAnalysisOfIndividualAndDyadBehaviours]]
- [[HowCanSocialNetworksEverBecomeComplexModellingTheEmergenceOfComplexNetworksFromLocalSocialExchanges]]
- [[ASocialIdentityModelForDeindividualisationPhenomena]]
- [[TrustInCloseRelationships]]
- [[CommunicationInSocialNetworksEffectsOfKinshipNetworkSizeAndEmotionalCloseness]]
- [[TheDevelopmentOfCooperativeRelationshipsAnExperiment]]
- [[ExploringVariationsInActiveNetworkSizeConstraintsAndEgoCharacteristics]]
- [[EvolutionaryGameTheoryMeetsSocialScienceIsThereAUnifyingRuleForHumanCooperation]]
- [[KeepingAndEndingCasualCloseAndBestFriendships]]
- [[ACommunityLevelEvaluationOfTheImpactOfPreyBehaviouralAndEcologicalCharacteristicsOnPredatorDietComposition]]
- [[PerspectiveTakingAndSocialNetworkSizeInHumans]]
- [[Computational Modelling of Trust and Social Relationships]]
- [[RelationshipsAndTheSocialBrainIntegratingPsychologicalAndEvolutionaryPerspectives]]
- [[AnIntegrativeTheoryOfIntergroupConflictInWAustinAndSWorchelEds]]
- [[EvolutionaryPsychologyAndTheGenerationOfCultureITheoreticalConsiderations]]
- [[DevelopmentalSequenceInSmallGroups]]
- [[DifferentStrokesFromDifferentFolksCommunityTiesAndSocialSupport]]
- [[DoesTheInternetIncreaseDecreaseOrSupplementSocialCapital]]
- [[ConnectedLivesTheProjectInPPurcellEd]]
- [[CultureEvolves]]
- [[ADeductiveApproachToFriendshipNetworks]]
- [[StabilityOfGroupsWithCostlyBeliefsAndPractices]]
- [[UncertaintyTrustAndCommitmentFormationInTheUnitedStatesAndJapan]]
- [[SympathyAndPunishmentEvolutionOfCooperationInPublicGoodsGame]]
- [[DevelopingTrustInLargeScalePeerToPeerSystems]]
- [[DiscreteHierarchicalOrganizationOfSocialGroupSizes]]

## Audit Log
- Audit invalidated (2026-09-30): auditor admitted clearing flags before completing independent source checks. A new independent audit is required.
- Strong source review (2026-09-30): Corrected date, typed relationship state and added actual wellbeing/resource fitness and selection. Recorded trust prose/control-algorithm conflict; exact inherited partner-search/decay functions remain explicitly unresolved. Independent re-audit pending.
- Initial independent audit: failed on missing model mechanisms, abstract fidelity, or source-access reporting; see `vault/.automation/audit/next-forty-54-66-initial-2026-09-30.json`. Revisions added source-located model detail; independent re-audit remains pending.

- WITHDRAWN audit claim (2026-09-30): previously reported PASS; source claims, current extraction, metadata, references and footnotes checked against the available primary source. See `vault/.automation/audit/remaining-audit-b-2026-09-30.json`.

## LLM Justification
[^r1]: The paper’s abstract, at https://www.jasss.org/15/4/3/3.pdf. The questions paraphrase the stated purpose, research scope, and reported approach.
[^r3]: Sutcliffe, Wang & Dunbar, §§2.1–2.6 (trust, strategies, turn control and inherited formula references), §6.10 (defection memory not used in partner selection; ego-network scope). Full text: https://www.jasss.org/15/4/3.html.
[^r4]: Sutcliffe et al., §§3.1–3.3 (controls and tercile outcomes), §4.2 (wellbeing/resource equations; viewed in full PDF p. 4 because HTML equations are images), §§4.3–4.5 (selection, initial population, cycles, generations and experimental weights), §5 (separate genotype/mutation experiments). Full text: https://www.jasss.org/15/4/3/3.pdf.
[^r5]: Unresolved source conflict: §2.4 specifies a log-ratio rule for positive and negative trust changes; §2.6 printed Model-Control instead uses ±(MaxCR−CI×Trust), then subtracts W, while its notes specify logarithmic waning. §4.4 selects “Log increase/linear decrease.” Exact functions are referred to Sutcliffe & Wang (2012); this summary records the disagreement rather than inventing a resolution. Publication header: 31-Oct-2012. Full text: https://www.jasss.org/15/4/3/3.pdf.
