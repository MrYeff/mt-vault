---
title: "Bounded Confidence Revisited: What We Overlooked, Underestimated, and Got Wrong"
tags:
  - model
  - simulation
authors:
  - "[[Literature/Authors/Rainer Hegselmann|Rainer Hegselmann]]"
publication date: 2023-10-31
source: https://www.jasss.org/26/4/11.html
doi: 10.18564/jasss.5257
read status: Todo
⚠️: []
---
## Abstract

In the bounded confidence model (BC-model) (Hegselmann and Krause 2002), period by period, all agents average over all opinions that are no further away from their actual opinion than a given distance ε, i.e., their ‘bound of confidence’. With the benefit of hindsight, it is clear that we completely overlooked a crucial feature of our model back in 2002. That is for increasing values of ε, our analysis suggested smooth transitions in model behaviour. However, the transitions are in fact wild, chaotic and non-monotonic—as described by Lorenz (2006). The most dramatic example of these effects is a consensus that breaks down for larger values of ε. The core of this article is a fundamentally new approach to the analysis of the BC-model. This new approach makes the non-monotonicities unmissable. To understand this approach, we start with the question: how many different BC-processes can we initiate with any given start distribution? The answer to this question is almost certainly for all possible start distributions and certainly in all cases analysed here, it is always a finite number of ε-values that make a difference for the processes we start. Moreover, there is an algorithm that finds, for any start distribution, the complete list of ε-values that make a difference. Using this list, we can then go directly through all the possible BC-processes given the start distribution. We can therefore check them for non-monotonicity of any kind, and will be able to find them all. This good news comes however with bad news. That is the algorithm that inevitably and without exception finds all the ε-values that matter requires exact arithmetics, without any rounding and without even the slightest rounding error. As a consequence, we have to abandon the usual floating-point arithmetic used in today’s computers and programming languages. What we need to use instead is absolutely exact fractional arithmetic with integers of arbitrary length. This numerical approach is feasible on all modern computers. The new analytical approach and results are likely to have implications for many applications of the BC-model.

## Research Questions
> Research Questions extracted via LLM
- For a fixed initial opinion distribution, which confidence-bound values produce distinct Hegselmann–Krause processes?[^r1]
- Do outcomes vary monotonically as the confidence bound increases?[^r2]

## Model
> Model extracted via LLM according to [[Model Notation]]

### What does it represent?
The paper analyses the Hegselmann–Krause (HK) bounded-confidence process, where opinions lie in [0,1] and agents update simultaneously. It studies how this process changes as ε varies for a fixed initial opinion profile. (Section 2, definition and Equation (4).)[^r1]

### How does it work?
- At time t, agent i's inclusive insider set is I(i,X(t),ε)={j:|x_i(t)−x_j(t)|≤ε}, including i. All agents synchronously replace their opinions with the arithmetic mean of opinions in their own insider sets: x_i(t+1)=|I|⁻¹∑_{j∈I}x_j(t). (Section 2, Equations (2)–(4).)[^r2]
- An ε-switch for process ⟨X(0),ε⟩ is the smallest larger ε* equal to the minimum distance, anywhere in that process, between an agent and one of its ε-outsiders; crossing it adds at least one link. The finite ordered switch list segments ε into intervals whose members generate identical processes.[^r3]
- The article proves primary switches are finite and reports that its search terminated with finite lists in all tested cases; finiteness of the complete list for every possible initial profile remains a conjecture, not a proved universal result. (Section 4; Appendix A, Analytical Notes 1, 5–7.)[^r3]
- Exact fractional arithmetic with arbitrary-length integers is required to locate every switch without rounding error. (Sections 1 and 3–4.)[^r4]

### What can it answer?
It can establish how bounded-confidence outcomes vary across ε for a specified initial distribution, including non-monotonic changes in consensus and fragmentation. (Sections 4–6.)[^r3]

### Where does it apply?
It applies to the bounded-confidence process under the stated initial conditions and exact-arithmetic analysis; it does not by itself model platform exposure or empirical social relationships. (Sections 2, 6.)[^r4]

## Metadata
### References
- [[PositiveDynamicalSystemsInDiscreteTime]]
- [[RationalConsensusInScienceAndSocietyAPhilosophicalAndMathematicalStudy]]
- [[NumericalComputingWithIeeeFloatingPointArithmetic]]
- [[ModellingAndSimulationInTheSocialSciencesFromThePhilosophyOfSciencePointOfView]]
- [[FourDecadesOfScientificExplanation]]
- [[MenOfIdeasSomeCreatorsOfContemporaryPhilosophy]]
- [[OpinionDynamicsDrivenByVariousWaysOfAveraging]]
- [[TheHegselmannKrauseDynamicsForTheContinuousAgentModelAndARegularOpinionFunctionDoNotAlwaysLeadToConsensus]]
- [[SocialConsensusAndRationalAgnoiology]]
- [[ExtendingTheHegselmannKrauseModelI]]
- [[AnExperimentalApplicationOfTheDelphiMethodToTheUseOfExperts]]
- [[ModelsAndTheLocusOfTheirTruth]]
- [[TruthApproximationSocialEpistemologyAndOpinionDynamics]]
- [[ConsensusThroughRespectAModelOfRationalGroupDecisionMaking]]
- [[Mixing beliefs among interacting agents]]
- [[SimulatingPeerDisagreements]]
- [[TheConsensusOfSubjectiveProbabilityDistributions]]
- [[OpinionDynamicsAndBoundedConfidenceModelsAnalysisAndSimulation]]
- [[AFormalTheoryOfSocialPower]]
- [[TheGhostInTheModelAndOtherEffectsOfFloatingPointArithmetic]]
- [[StanfordEncyclopediaOfPhilosophy]]
- [[WhatEveryAgentBasedModellerShouldKnowAboutFloatingPointArithmetic]]
- [[DeliberativeExchangeTruthAndCognitiveDivisionOfLabourALowResolutionModelingApproach]]
- [[OptimalOpinionControlTheCampaignProblem]]
- [[CeterisParibusConditionsMaterialityAndTheApplicationOfEconomicTheories]]
- [[ConsensusStrikesBackInTheHegselmannKrauseModelOfContinuousOpinionDynamicsUnderBoundedConfidence]]
- [[TruthAndCognitiveDivisionOfLabourFirstStepsTowardsAComputerAidedSocialEpistemology]]
- [[OpinionDynamicsTheEffectOfTheNumberOfPeersMetAtOnce]]
- [[WhatEveryComputerScientistShouldKnowAboutFloatingPointArithmetic]]
- [[ExplicationAsAMethodOfConceptualReEngineering]]
- [[InferenceToTheBestExplanationVersusBayesSRuleInASocialSetting]]
- [[WhenRationalDisagreementIsImpossible]]
- [[OpinionDynamicsModelsExtensionsAndExternalEffects]]
- [[EconomicsRulesWhyEconomicsWorksWhenItFailsAndHowToTellTheDifference]]
- [[OpinionDynamicsUnderTheInfluenceOfRadicalGroupsCharismaticLeadersAndOtherConstantSignalsASimpleUnifyingModel]]
- [[DimensionsOfObjectualUnderstanding]]
- [[ModelsOfSocialInfluenceTowardsTheNextFrontiers]]
- [[RepublicDividedDemocracyInTheAgeOfSocialMedia]]
- [[RightsAndWrongsOfEconomicModellingRefiningRodrik]]
- [[CommunicationInOnlineSocialNetworksFostersCulturalIsolation]]
- [[ExplainableMachineLearningForScientificInsightsAndDiscoveries]]
- [[RecentAdvancesInOpinionPropagationDynamicsA2020Survey]]
- [[LogicalFoundationsOfProbability]]
- [[ContinuousOpinionDynamicsUnderBoundedConfidenceASurvey]]
- [[UnresolvedReferenceC062E90E0D47FDC9]]
- [[MisAndDisinformationInABoundedConfidenceModel]]
- [[9PolarizationAndRadicalizationInTheBoundedConfidenceModelAComputerAidedSpeculation]]
- [[OnTheMethodOfIsolationInEconomics]]
- [[UnresolvedReference5427B980AB49B16A]]
- [[ARigorousFormulationOfAndPartialResultsOnLorenzSConsensusStrikesBackPhenomenonForTheHegselmannKrauseModel]]
- [[OpinionDynamicsInOnlineSocialMedia]]
- [[TheComplexLinkBetweenFilterBubblesAndOpinionPolarization]]
- [[NetworkEffectsInABoundedConfidenceModel]]
- [[IsYourModelSusceptibleToFloatingPointErrors]]
- [[AnalyzingTheEffectsOfConfidenceThresholdsOnOpinionClusteringInHomogeneousHegselmannKrauseModels]]
- [[DisciplinaryTrendsInTheUseOfTheDelphiMethodABibliometricAnalysis]]
- [[BoundedConfidenceOpinionDynamicsASurvey]]
- [[Bounded Confidence Revisited- What We Overlooked- Underestimated- and Got Wrong]]
- [[UnresolvedReference7043F37ACDCCF82D]]
- [[UnresolvedReference2DEC394F30F9018B]]
- [[UnresolvedReference49179B53D63C1FD7]]
- [[UnresolvedReference6D2B4D9C0376CB1A]]
- [[UnresolvedReferenceCF9B9A0705B0545C]]
- [[UnresolvedReferenceC628762875099F2C]]
- [[UnresolvedReference58DB6F5181AB9EC3]]
- [[UnresolvedReferenceCBC61EDAB19961EA]]
- [[UnresolvedReference887D3AE707A5A85A]]
- [[UnresolvedReference9FE1606A4741BD16]]
- [[UnresolvedReference1ED1545903DB7ACF]]
- [[UnresolvedReference1654C89ECEEECC15]]
- [[UnresolvedReference8337356AABBEF6CA]]
- [[UnresolvedReference65711AA662314725]]
- [[UnresolvedReference5D8BA921C2FADB46]]
- [[UnresolvedReference6E10414DDA6662EF]]
- [[UnresolvedReferenceD6F6AD097199D2E5]]
- [[UnresolvedReference1CFD8D7E151B8796]]
- [[UnresolvedReferenceFDAA0EF4ACF57821]]
- [[UnresolvedReference30099E339E4B0EFA]]
- [[UnresolvedReference04206A4F86654BB7]]
- [[UnresolvedReferenceE311AC9751A2CBE5]]
- [[UnresolvedReferenceCFBB701F7D3E54D9]]
- [[UnresolvedReference1AD5BD5733BF681A]]



## Audit Log
- Initial independent audit failed: omitted the formal HK update rule and switch definition, overstated the unqualified finiteness implication, and found unresolved bibliography identifiers (audit JSON, 2026-09-29).
- Corrected the model summary and retained the reference links/order. Bibliography remains incomplete because 26 identifiers are unresolved; do not treat the list as reconciled. Re-audit pending.
- Independent re-audit found duplicate [^r3]/[^r4] definitions and missing spaces in the imported abstract. Merged each footnote definition, removed duplicate labels, and restored readable sentence spacing and punctuation to the source abstract; references and order preserved. Awaiting final audit.

- Independent final check passed after correction. Bibliography limitations remain stated above.

## LLM Justification

[^r1]: Hegselmann (2023), Section 2, definition and Equation (4); primary article https://www.jasss.org/26/4/11.html.
[^r2]: Hegselmann (2023), Section 2, Equations (2)–(4); https://www.jasss.org/26/4/11.html.
[^r3]: Hegselmann (2023), Section 4 and Appendix A, Analytical Notes 1 and 5–7, for switch definition, finite primary switches, tested search results, and conjectured universal finiteness; Sections 4–6 for analyzed processes and outcome changes; https://www.jasss.org/26/4/11.html.
[^r4]: Hegselmann (2023), Sections 1 and 3–4 for exact arithmetic; Sections 2 and 6 for the BC-process definition and scope; https://www.jasss.org/26/4/11.html.
