---
title: "Computational Modelling of Trust and Social Relationships"
tags:
  - model
  - simulation
authors:
  - "[[Literature/Authors/Alistair Sutcliffe|Alistair Sutcliffe]]"
  - "[[Literature/Authors/Di Wang|Di Wang]]"
publication date: 2012-01-31
source: https://www.jasss.org/15/1/3.html
doi: 10.18564/jasss.1912
read status: Todo
⚠️: []
---
## Abstract

A computational model for the development of social relationships is described. The model implements agent strategies for social interaction based on Dunbar's Social Brain Hypothesis (SBH). A trust related process controls the formation and decay of relationships as a function of interaction frequency, the history of interaction, and the agents' strategies. A good fit the SBH predictions was found across a range of model parameter settings, which varied the waning rate of trust, defect/cooperation rates for agents, and linear/log functions for trust increase and decay. Social interaction strategies which favour interacting with existing strong ties or a time variant strategy produced more SBH conformant results than strategies favour more weaker relationships. The prospects for modeling the emergence of social relationships are discussed.

## Research Questions
> Research Questions extracted via LLM
- Can a computational trust process generate relationship layers consistent with the Social Brain Hypothesis?[^r1]
- How do interaction strategies and trust increase and waning functions affect the simulated relationship layers?[^r2]

## Model
> Model extracted via LLM according to [[Model Notation]]

### What does it represent?
The model represents agents forming and maintaining social relationships through interactions, with trust controlling relationship strength. The study explores mechanisms related to the Social Brain Hypothesis. (Sections 1–2.)[^r1]

### How does it work?
- Most experiments run for 3000 cycles. On each cycle, each focal agent gets a turn; the FM ratio determines whether it forages or takes a social turn.[^r2][^r5]
- On a social turn, the agent reads relationship history and selects an alter: the probability of choosing a new agent is 1−Nₜ,ᵢ/P, while existing ties are chosen with probability Nₜ,ᵢ/P and then ranked or weighted by the agent's strategy.[^r2][^r5]
- Initially all strategies select a stranger at random; thereafter the four strategies favor strong, middle-ranked, weak, or staged (strong early, progressively weaker later) ties.[^r2][^r5]
- The alter cooperates or defects; cooperative response increases directed trust, while defection decreases it and increments the defection counter. After this interaction update, trust wanes, with a floor at zero.[^r2][^r5]
- The tested trust update variants combine linear or logarithmic trust increase with linear or logarithmic waning. The logarithmic increase experiments use MaxCR=10, MinCR=0, and MaxTrust=100.[^r2][^r5]
- The paper compares these combinations and reports that logarithmic increase with linear decrease best fits the Social Brain Hypothesis layer distribution.[^r2][^r5]
- Waning rate/cost, defection rate, cycle count, and FM are experimental controls. (Sections 3.3–3.23, 3.25; Equations (8)–(10); Sections 4.5–4.10.)[^r2][^r5]

### What can it answer?
- Outputs include trust, relationship frequency by trust rank, and average relationship counts by layer. (Sections 3.26–3.27, 4, and 5.8.)[^r3]
- Because trust is continuous, strong, medium, and weak outcomes are operationalized as upper, middle, and lower terciles of the trust distribution. (Sections 3.26–3.27, 4, and 5.8.)[^r3]
- The authors report more SBH-conformant patterns for strong-tie and staged strategies than strategies favoring weaker ties, under tested parameter settings. (Sections 3.26–3.27, 4, and 5.8.)[^r3]
- Defections are a global parameter rather than remembered per relationship, limiting analysis of relationship-specific non-cooperation and mistrust. (Sections 3.26–3.27, 4, and 5.8.)[^r3]

### Where does it apply?
It is a computational account of relationship formation under its specified trust and partner-selection assumptions; the paper’s fit to theoretical layer predictions is not validation of a platform intervention. (Sections 1, 4–5.)[^r4]

## Metadata
### References
- [[ConnectedLivesTheProject1]]
- [[DeterminantsOfGroupSizeInPrimatesAGeneralModel]]
- [[MultiAgentSystemEngineering]]
- [[CollaborativeReputationMechanismsInElectronicMarketplaces]]
- [[FormalAnalysisOfModelsForTheDynamicsOfTrustBasedOnExperiences]]
- [[EvolutionOfCooperationWhenFeedbackToReputationScoresIsVoluntary]]
- [[SocialTrustACognitiveApproach]]
- [[TrustInMultiAgentSystems]]
- [[PerspectiveTakingAndMemoryCapacityPredictSocialNetworkSize]]
- [[TheCostsOfFamilyAndFriendsAn18MonthLongitudinalStudyOfRelationshipMaintenanceAndDecay]]
- [[CommunicationInSocialNetworksEffectsOfKinshipNetworkSizeAndEmotionalCloseness]]
- [[ALongitudinalStudyOfFriendshipDevelopment]]
- [[KeepingAndEndingCasualCloseAndBestFriendships]]
- [[EvolutionOfIndirectReciprocityBySocialInformationTheRoleOfTrustAndReputationInEvolutionOfAltruism]]
- [[SocialConnectivityInAmericaChangesInAdultFriendshipNetworkSizeFrom2002To2007]]
- [[SocialNetworksSupportCliquesAndKinship]]
- [[SocialNetworkSizeInHumans]]
- [[TargetArticleSelectiveInvestmentTheoryRecastingTheFunctionalSignificanceOfCloseRelationships]]
- [[TheEvolutionOfReciprocityInSizableGroups]]
- [[HumanSympathyGroups]]
- [[TheSocialBrainHypothesis]]
- [[TheDevelopmentOfCooperativeRelationshipsAnExperiment]]
- [[ThePromotionAndEvolutionOfCooperationThroughProjectionImplicationsForSocialDilemmasAndTrust]]
- [[TheNeedToBelongDesireForInterpersonalAttachmentsAsAFundamentalHumanMotivation]]
- [[ExploringVariationInActiveNetworkSizeConstraintsAndEgoCharacteristics]]
- [[SimulationForTheSocialScientist]]
- [[DevelopingTrustInLargeScalePeerToPeerSystems]]
- [[SocialCirclesASimpleStructureForAgentBasedSocialNetworkModels]]
- [[ReviewOnComputationalTrustAndReputationModels]]
- [[SizeMattersVariationInPersonalNetworkSizePersonalityAndEffectOnInformationTransmission]]
- [[SwarmIntelligence]]
- [[FriendshipMaintenanceAnAnalysisOfIndividualAndDyadBehaviors]]
- [[TheDayToDayFunctioningOfCloseVersusCasualFriendships]]
- [[SwarmIntelligenceFromNaturalToArtificialSystems]]
- [[UnresolvedReference6851E7E34AA3F635]]
- [[CoevolutionOfNeocorticalSizeGroupSizeAndLanguageInHumans]]
- [[VisualizingPersonalNetworksWorkingWithParticipantAidedSociograms]]
- [[EvolutionOfIndirectReciprocity]]
- [[DoesTheInternetIncreaseDecreaseOrSupplementSocialCapital]]
- [[UnresolvedReference2BF7D76339A07942]]
- [[UnresolvedReference94AD3BC704DA0AB6]]



## Audit Log
- Initial independent audit failed: the model summary omitted turn scheduling, partner selection probabilities/strategies, response and trust update order, operational tie-layer thresholds, and the global-defection limitation. Three bibliography identifiers remain unresolved (audit JSON, 2026-09-29).
- Expanded the mechanics and cited the source subsections and equations. Preserved reference links/order; bibliography title mapping remains incomplete. Re-audit pending.
- Independent re-audit found that the summary omitted the tested linear/log trust-waning variants and the best-fitting log-increase/linear-decrease combination. Added these, clarified cooperative/defection trust directions and update order, and added a source-specific footnote; references and order preserved. Awaiting final audit.

- Independent final check passed after correction. Bibliography limitations remain stated above.

## LLM Justification

[^r1]: Sutcliffe & di Wang (2012), Sections 1–2, motivation, model purpose, and Social Brain Hypothesis framing; https://www.jasss.org/15/1/3.html.
[^r2]: Sutcliffe & di Wang (2012), Sections 3.3–3.23 and 3.25, model-control algorithm, Equations (8)–(10), strategies, trust updates and controls; https://www.jasss.org/15/1/3.html.
[^r3]: Sutcliffe & di Wang (2012), Sections 3.26–3.27, 4 and 5.8, output definitions, findings, and global defection limitation; https://www.jasss.org/15/1/3.html.
[^r4]: Sutcliffe & di Wang (2012), Sections 1 and 4–5; model purpose and evaluation are described as computational exploration against SBH predictions; https://www.jasss.org/15/1/3.html.
[^r5]: Sutcliffe & di Wang (2012), Sections 4.5–4.10, comparing linear/log trust increase and linear/log waning and reporting the best-fitting log-increase/linear-decrease variant; Section 3.23 for the order of interaction update followed by trust waning; https://www.jasss.org/15/1/3.html.
