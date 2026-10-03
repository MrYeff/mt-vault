---
title: "Modelling the Evolution of Social Structure"
authors:
  - "[[Literature/Authors/Alistair Sutcliffe|Alistair Sutcliffe]]"
  - "[[Literature/Authors/Robin Dunbar|Robin Dunbar]]"
  - "[[Literature/Authors/D. Wang|D. Wang]]"
source: "https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0158605"
doi: "10.1371/journal.pone.0158605"
publication date: "2016-07-18"
tags:
  - "model"
  - "simulation"
  - "social_structure"
read status: Todo
⚠️:
  - audit failed
---

## Abstract

Although simple social structures are more common in animal societies, some taxa (mainly mammals) have complex, multi-level social systems, in which the levels reflect differential association. We develop a simulation model to explore the conditions under which multi-level social systems of this kind evolve. Our model focuses on the evolutionary trade-offs between foraging and social interaction, and explores the impact of alternative strategies for distributing social interaction, with fitness criteria for wellbeing, alliance formation, risk, stress and access to food resources that reward social strategies differentially. The results suggest that multi-level social structures characterised by a few strong relationships, more medium ties and large numbers of weak ties emerge only in a small part of the overall fitness landscape, namely where there are significant fitness benefits from wellbeing and alliance formation and there are high levels of social interaction. In contrast, ‘favour-the-few’ strategies are more competitive under a wide range of fitness conditions, including those producing homogeneous, single-level societies of the kind found in many birds and mammals. The simulations suggest that the development of complex, multi-level social structures of the kind found in many primates (including humans) depends on a capacity for high investment in social time, preferential social interaction strategies, high mortality risk and/or differential reproduction. These conditions are characteristic of only a few mammalian taxa.

## Research Questions
> Research Questions extracted via LLM

- Under which fitness conditions do multi-level social systems emerge?[^r1]
- How do alternative strategies for allocating social time compare across generations?[^r1]

## Model
> Model extracted via LLM according to [[Model Notation]]

### What does it represent?
- Social ties emerge from repeated cooperative interaction; evolutionary selection rewards trade-offs between foraging, relationship benefits, risk, and stress.[^e1]

### How does it work?
- Each cycle gives every agent a turn: forage according to its forage:social propensity, or choose a partner. Initial partner choice is random; later choices use remembered directed trust.[^e2]
- FtF favors strong ties, FtW weak ties, FtM middle ties; Staged progressively shifts from strong toward weak ties. New partners remain possible. For `n` existing ties in descending trust order with total `T`, FtF uses `p_j=t_j/T`, FtW uses `p_j=t_(n-j+1)/T`; select a new partner with probability `1-n/P`, otherwise apply the existing-tie rule. Staged uses `p_j=(t_j-(t_j-t_(n-j+1))/RC)/T`, with `RC` remaining cycles. The FtM formula/prose conflict is recorded below.[^e3]
- Cooperation adds `MAX_COMPRESSION-CI*trust`; rejection subtracts it, with `CI=(MAX_COMPRESSION-MIN_COMPRESSION)/MAX_TRUST`. Appendix Eq. (7) waning is `next=max(0,trust-MIN_WANING*(1+WANING_RATE-previous_trust/MAX_TRUST))`. `MIN_WANING` is an input without a reported value; the equation explicitly uses lagged `previous_trust`.[^e2]

The appendix's named objective functions expose the fitness mechanism; `mean_trust`, `ties`, `incoming`, `outgoing`, and `forage_turns` refer to an agent's lifetime history.[^e4]

```
AGENTS = 300
CYCLES_PER_GENERATION = 2000
GENERATIONS = 50
REPLACEMENT_SHARE = 0.20
ALLIANCE_COEFFICIENT = 0.05
RISK_COEFFICIENT = 0.005
MAX_TRUST = 100
MAX_COMPRESSION = 10
MIN_COMPRESSION = 0
WANING_RATE = 0.08

objectives(
  agent: Agent
):
  wellbeing = mean_trust * incoming/outgoing
  resource = forage_turns * ties
  alliance = mean_trust * ALLIANCE_COEFFICIENT * ties
  risk = mean_trust / (RISK_COEFFICIENT*(incoming+outgoing))
  stress = ties
  out = (wellbeing, resource, alliance, risk, stress)
```

- Rank-normalize each criterion across agents, apply run-specific weights, sum wellbeing/resource/alliance and subtract risk/stress. Replace the bottom `REPLACEMENT_SHARE` with offspring of the top share; inherit social strategy, without inheriting relationships. The experiments vary weights from 1 to 5, strategies, foraging/social propensity and rejection.[^e1][^e4]
- Source conflicts: main text labels resource `RS` and risk `R`, then writes `(R+WB+AL)-(RS+ST)`; appendix calls resource `R` and risk `RS`. Main prose calls stress a decreasing function of ties, but appendix defines `ST=ties`, a rising cost. Risk prose says more interactions raise risk, but its appendix ratio decreases with interaction count at fixed trust. These contradictions remain unresolved.[^e5]
- Appendix FtM formulas apply direct trust weights to the top half and reversed weights to the bottom half; the next page's prose says the reverse. The waning section's Eq. (7) depends on lagged trust, while the parameter summary calls decrease linear/8% per cycle. These additional conflicts require an explicit implementation choice.[^e7]
- This extraction omits mutation details and unspecified zero-denominator handling. It preserves the trust and search equations without resolving source contradictions.[^e2][^e3][^e4]

### What can it answer?
- It tests which preference strategies and fitness regimes yield many weak ties plus small stronger layers, and which strategies survive evolutionary competition.[^e6]

### Where does it apply?
- It is a functional model of animal/human social organization; it does not specify physiological or psychological mechanisms underlying relationships.[^e6]

## Metadata
### References
- [[SexualSelectionInPrimates]]
- [[ConnectedLivesTheProject1]]
- [[SocialBrainDistributedMind]]
- [[LucyToLanguageTheBenchmarkPapers]]
- [[MortalityInTraditionalHunterGathererPastoralistAndAgriculturalistCommunitiesTheValidityOfLongevityStudiesBasedOnMobilityAndSubsistenceStrategies]]
- [[PrimateSocialSystems]]
- [[ReproductiveDecisionsAnEconomicAnalysisOfGeladaBaboonSocialStrategies]]
- [[PerspectiveTakingAndMemoryCapacityPredictSocialNetworkSize]]
- [[StrongAndConsistentSocialBondsEnhanceTheLongevityOfFemaleBaboons]]
- [[StepwiseEvolutionOfStableSocialityInPrimates]]
- [[OnAimsAndMethodsOfEthology]]
- [[SocialBondsOfFemaleBaboonsEnhanceInfantSurvival]]
- [[CommunityStructureInSocialAndBiologicalNetworks]]
- [[NeocortexSizeAndSocialNetworkSizeInPrimates]]
- [[TheCostsOfFamilyAndFriendsAn18MonthLongitudinalStudyOfRelationshipMaintenanceAndDecay]]
- [[LimitedCommunicationCapacityUnveilsStrategiesForHumanInteraction]]
- [[DifferentStrokesFromDifferentFolksCommunityTiesAndSocialSupport]]
- [[HabitatQualityPopulationDynamicsAndGroupCompositionInColobusMonkeysColobusGuereza]]
- [[ReplyToLukasAndCluttonBrockInfanticideStillDrivesPrimateMonogamy]]
- [[EvolutionarySignificanceOfTheRoleOfFamilyUnitsInABroaderSocialSystem]]
- [[EconomicActionAndSocialStructureTheProblemOfEmbeddedness]]
- [[EvolutionaryGameTheoryMeetsSocialScienceIsThereAUnifyingRuleForHumanCooperation]]
- [[TimeAsALimitedResourceCommunicationStrategyInMobilePhoneNetworks]]
- [[LargeBodyAndSmallBrainAndGroupSizesAreAssociatedWithPredatorPreferencesForMammalianPrey]]
- [[MotivationLossesInSmallGroupsASocialDilemmaAnalysis]]
- [[SocialNetworksSupportCliquesAndKinship]]
- [[SocialNetworkSizeInHumans]]
- [[UncertaintyTrustAndCommitmentFormationInTheUnitedStatesAndJapan]]
- [[TargetArticleSelectiveInvestmentTheoryRecastingTheFunctionalSignificanceOfCloseRelationships]]
- [[ACommunityLevelEvaluationOfTheImpactOfPreyBehaviouralAndEcologicalCharacteristicsOnPredatorDietComposition]]
- [[SocialNetworksInPrimatesSmartAndTolerantSpeciesHaveMoreEfficientNetworks]]
- [[AttitudesAndCognitiveOrganization]]
- [[CooperationBehaviouralSynchronyAndStatusInSocialNetworks]]
- [[HumanSympathyGroups]]
- [[TimeAsAnEcologicalConstraint]]
- [[StrategicUseOfAllopreeningInFamilyLivingWrens]]
- [[BondednessAndSociality]]
- [[TheDevelopmentOfCooperativeRelationshipsAnExperiment]]
- [[TheNeedToBelongDesireForInterpersonalAttachmentsAsAFundamentalHumanMotivation]]
- [[SocialStressorsAndCopingMechanismsInWildFemaleBaboonsPapioHamadryasUrsinus]]
- [[DeterminantsAndEvolutionaryConsequencesOfDominanceAmongFemaleGeladaBaboons]]
- [[UsingTheFWordInPrimatology]]
- [[FriendshipCliquishnessAndTheEmergenceOfCooperation]]
- [[NetworkScalingRevealsConsistentFractalPatternInHierarchicalMammalianSocieties]]
- [[TheEvolutionOfFemaleSocialRelationshipsInNonhumanPrimates]]
- [[TheSocioecologyOfElephantsAnalysisOfTheProcessesCreatingMultitieredSocialStructures]]
- [[CloseSocialAssociationsInAnimalsAndHumansFunctionsAndMechanismsOfFriendship]]
- [[NiceGuysFinishFirstTheCompetitiveAltruismHypothesis]]
- [[TheStrengthOfWeakTies]]
- [[DynamicSpreadOfHappinessInALargeSocialNetworkLongitudinalAnalysisOver20YearsInTheFraminghamHeartStudy]]
- [[EvolutionaryDeterminantsOfModularSocietiesInColobines]]
- [[ExtravertsHaveLargerSocialNetworkLayers]]
- [[Persistence of social signatures in human communication]]
- [[RelationshipsAndTheSocialBrainIntegratingPsychologicalAndEvolutionaryPerspectives]]
- [[TheSpreadOfObesityInALargeSocialNetworkOver32Years]]
- [[WhyAreDiurnalPrimatesLivingInGroups]]
- [[TheBenefitsOfSocialCapitalCloseSocialBondsAmongFemaleBaboonsEnhanceOffspringSurvival]]
- [[FriendshipMaintenanceAnAnalysisOfIndividualAndDyadBehaviors]]
- [[SocialNetworksAndHealth]]
- [[TheDayToDayFunctioningOfCloseVersusCasualFriendships]]
- [[TheComplexStructureOfHunterGathererSocialNetworks]]
- [[SocialIsolationInAmericaChangesInCoreDiscussionNetworksOverTwoDecades]]
- [[Computational Modelling of Trust and Social Relationships]]
- [[AnEvaluationOfTheRolesOfPredationRateAndPredationRiskAsSelectivePressuresOnPrimateGroupingBehaviour]]
- [[FocusedGroomingNetworksAndStressAlleviationInWildFemaleBaboons]]
- [[EvolutionOfIndirectReciprocityByImageScoring]]
- [[PredationRiskAsAnInfluenceOnGroupSizeInCercopithecoidPrimatesImplicationsForSocialStructure]]
- [[EvolutionOfIndirectReciprocity]]
- [[DiscreteHierarchicalOrganizationOfSocialGroupSizes]]
- [[EcologicalAndSocialDeterminantsOfBirthIntervalsInBaboons]]
- [[SocialNetworkDeterminantsOfDepression]]
- [[EncephalizationIsNotAUniversalMacroevolutionaryPhenomenonInMammalsButIsAssociatedWithSociality]]
- [[InfanticideRiskAndTheEvolutionOfMaleFemaleAssociationInPrimates]]
- [[ManagingRelationshipDecay]]
- [[TheStructureOfOnlineSocialNetworksMirrorsThoseInTheOfflineWorld]]
- [[DoOnlineSocialMediaCutThroughTheConstraintsThatLimitTheSizeOfOfflineSocialNetworks]]
- [[DeaconSDilemmaTheProblemOfPairBondingInHumanEvolution]]
- [[NaturalAndSexualSelectionAndTheEvolutionOfMultiLevelSocietiesInsightsFromZebrasWithComparisonsToPrimates]]
- [[AShortHistoryOfWomenJohnLangdonDaviesmodernYouthAndMarriageHenryNeumann]]
- [[UnresolvedReference05F6D99945161209]]
- [[LivingInGroups]]
- [[UnresolvedReference33C91805D9299ACA]]
- [[UnresolvedReference988F62C5EDFC9883]]
- [[UnresolvedReferenceAB023E7BE93A4431]]
- [[UnresolvedReferenceE8B42A8915B0E089]]
- [[UnresolvedReferenceFB968D2C77F354E4]]
- [[EncephalisationIsNotAUniversalMacroevolutionaryPhenomenonInMammalsButIsAssociatedWithSociality]]
- [[ManagingRelationshipDecayNetworkGenderAndContextualEffects]]
- [[ThePersistence of social signatures in human communication]]
- [[PredatorDietChoicesAreAssociatedWithPreyLifeHistoryAndBehaviouralCharacteristicsInTerrestrialMammalCommunities]]
- [[PerspectiveTakingAndSocialNetworkSizeInHumans]]
- [[ExtravertsHaveLargerSocialNetworkLayersButDoNotFeelEmotionallyCloserToIndividualsAtAnyLayer]]
- [[NetworkedNeighborhoods]]
- [[FriendshipMaintenanceAnAnalysisOfIndividualAndDyadBehaviours]]
- [[OnTheAimsAndMethodsOfEthology]]
- [[PrimateOntogeny]]
- [[EcologicalDeterminantsOfBirthIntervalsBaboons]]

## Audit Log
- Audit invalidated (2026-09-30): auditor admitted relying on spot checks and previous reports before clearing flags. A full independent audit is still required.
- 2026-09-30: Full-source design audit found opaque fitness omitted objective functions; appendix not examined by prior extraction; resource/risk symbol contradiction hidden; stress and risk direction conflicts hidden. Corrected against the source passages below; independent re-audit pending.[^design]
- Independent audit found the agent count, four strategies, lifetime/generation schedule, fitness formula, criterion weights, selection, and resource competition omitted. These are now stated with source locators; the note identifies this as an evolutionary simulation rather than an empirical fit. At that stage, independent re-audit remained pending.

- WITHDRAWN audit claim (2026-09-30): incomplete source checks; this audit does not establish a pass.

## LLM Justification
[^r1]: The research questions are a concise transformation of the primary source’s abstract and stated aims. Source location: Methods/model description and Results. Source: [Modelling the Evolution of Social Structure](https://pmc.ncbi.nlm.nih.gov/articles/PMC4948869/).


[^e1]: Main text → Social Simulation Model: turns, 300 agents, four strategies, 2000 cycles/generation, 50 generations, ranked fitness, replacement of 20%, and no inherited relationships; Experimental Design varies five objective weights.

[^e2]: S1 Appendix pp.2–3, Eqs. (1)–(7), and Model Control Process: directed trust, compressed signed increments, and waning with lagged trust. Embedded equation images were visually checked in the rendered original DOCX. Summary of Parameters sets WaningR=0.08 but gives no MinWaning value.

[^e3]: S1 Appendix → Agent strategies and Interaction Process and Relationship Formation: new/existing partners, ranked trust selection, FtF/FtW/FtM probabilities and Staged shift. Embedded search formulas were visually checked on Appendix pp.4–5; Eqs. (8)–(10) give new/existing probability and total trust; Staged uses remaining cycles RC.

[^e4]: S1 Appendix → Objective Functions and Summary of Parameters: WB=mR*(Iin/Iout); resource R=Fr*N; AL=mR*(0.05*N); risk RS=mR/(0.005*Itot); ST=N; positive versus negative fitness terms. Main text explains rank normalization and run-specific weighting.

[^e5]: Main Social Simulation Model prose and fitness formula conflict in R/RS meanings and stress direction with S1 Objective Functions. Appendix Risk prose says increasing interactions incurs more risk, despite RS=mR/(b*Itot). Both descriptions are preserved without silently resolving them.

[^e6]: Main Results, sensitivity analyses, and Discussion: rarity of layered structures, competitive strategies, and explicit functional rather than mechanism-level explanation.

[^design]: Source audit checked the full text at https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0158605. Model footnotes identify the passages supporting the corrections.


[^e7]: S1 Appendix p.4 FtM formula paragraph (c) conflicts with p.5 explanation; p.3 Eq. (7) uses trust_(t-1), whereas Summary of Parameters describes linear/8% decay. These embedded formulas were checked visually.
