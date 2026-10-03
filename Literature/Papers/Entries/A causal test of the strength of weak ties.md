---
title: A causal test of the strength of weak ties
tags:
authors:
  - "[[Literature/Authors/Karthik Rajkumar|Karthik Rajkumar]]"
  - "[[Literature/Authors/Guillaume Saint-Jacques|Guillaume Saint-Jacques]]"
  - "[[Literature/Authors/Iavor Bojinov|Iavor Bojinov]]"
  - "[[Literature/Authors/Erik Brynjolfsson|Erik Brynjolfsson]]"
  - "[[Literature/Authors/Sinan Aral|Sinan Aral]]"
publication date: 2022-09-15
source: https://gwern.net/doc/sociology/technology/2022-rajkumar.pdf
doi: 10.1126/science.abl4476
read status: Todo
---
## Abstract

The authors analyzed data from multiple large-scale randomized experiments on LinkedIn's People You May Know algorithm, which recommends new connections to LinkedIn members, to test the extent to which weak ties increased job mobility in the world's largest professional social network. The experiments randomly varied the prevalence of weak ties in the networks of over 20 million people over a 5-year period, during which 2 billion new ties and 600,000 new jobs were created. The results provided experimental causal evidence supporting the strength of weak ties and suggested three revisions to the theory. First, the strength of weak ties was nonlinear. Statistical analysis found an inverted U-shaped relationship between tie strength and job transmission such that weaker ties increased job transmission but only to a point, after which there were diminishing marginal returns to tie weakness. Second, weak ties measured by interaction intensity and the number of mutual connections displayed varying effects. Moderately weak ties (measured by mutual connections) and the weakest ties (measured by interaction intensity) created the most job mobility. Third, the strength of weak ties varied by industry. Whereas weak ties increased job mobility in more digital industries, strong ties increased job mobility in less digital industries.


## Research Questions
> Research Questions extracted via LLM

- Does experimentally increasing the share of weak ties in professional networks increase job transmission, and how does the effect vary with tie strength?[^r1]
- Do effects differ when tie strength is measured by interaction intensity versus mutual connections, and across industries with different digital intensity?[^r2]

## Model
> Model extracted via LLM according to [[Model Notation]]

### What does it represent?
The study tests whether randomized recommendation variants that shift tie formation change subsequent job mobility. Members received randomized PYMK variants; the 2015 experiment provides observations per newly formed tie, while the 2019 experiments provide observations per member.[^r3]

### How does it work?
```yml
Member: ...

Experiment:
  members: [Member]
  randomized_variant: ...
  observations_2015: [TieId -> JobTransmission]
  observations_2019: [MemberId -> MemberObservation]

Tie:
  bilateral_message_count: 0..
  mutual_connections: 0..
  degree_i: 0..
  degree_j: 0..
  structural_strength: mutual_connections / (degree_i + degree_j - mutual_connections - SELF_EXCLUSION)
  is_sequential_job_tie: bool

JobTransmission: ...
MemberObservation: ...
```

```
SELF_EXCLUSION = 2
```
- The PYMK variants altered recommendations to induce different weak/strong tie mixes.[^r4]
- Interaction intensity counts bilateral messages **after** a new tie forms; structural strength uses the formula above, measured **before** treatment.[^r4]
- A new tie was classified as structurally strong or weak by whether its pretreatment strength was above or below the pretreatment network median.[^r4]
- A sequential job tie required two members to report jobs at the same company at least a year apart and to have been connected at least a year before the later job.[^r4]
- This sketch omits treatment variants, regression and instrumental-variable estimation, covariates, and exact outcome specifications.[^r5]

### What can it answer?
The analyses estimate effects of randomized recommendation assignments and marginal tie additions on job transmission, including nonlinear effects and heterogeneity by tie metric and industry.[^r6]

### Where does it apply?
The evidence concerns LinkedIn members and professional job mobility in the studied recommendation experiments.[^r7]

## Metadata
### References
- [[TheSourcesAndConsequencesOfEmbeddednessForTheEconomicPerformanceOfOrganizationsTheNetworkEffect]]
- [[SocialNetworksAndLaborMarketOutcomesTowardAnEconomicAnalysis]]
- [[StatisticsAndCausalInferenceCommentWhichIfsHaveCausalAnswers]]
- [[SocialNetworksAndCooperationInHunterGatherers]]
- [[TechnologyBrokeringAndInnovationInAProductDevelopmentFirm]]
- [[SocialCapitalStructuralHolesAndTheFormationOfAnIndustryNetwork]]
- [[NetworkDiversityAndEconomicDevelopment]]
- [[NetworksDiversityAndProductivityTheSocialCapitalOfCorporateRDTeams]]
- [[StructuralHolesAndGoodIdeas]]
- [[EmergenceOfScalingInRandomNetworks]]
- [[TheRoleOfSocialNetworksInInformationDiffusion]]
- [[A61MillionPersonExperimentInSocialInfluenceAndPoliticalMobilization]]
- [[MaximizingTheSpreadOfInfluenceThroughASocialNetwork]]
- [[TieStrengthEmbeddednessAndSocialInfluenceALargeScaleNetworkedExperiment]]
- [[TheNetworkStructureOfExplorationAndExploitation]]
- [[IdentificationAndEstimationOfLocalAverageTreatmentEffects]]
- [[TheStrengthOfWeakTies]]
- [[CollectiveDynamicsOfSmallWorldNetworks]]
- [[Birds of a Feather- Homophily in Social Networks]]
- [[ComplexContagionsAndTheWeaknessOfLongTies]]
- [[DynamicSocialNetworksPromoteCooperationInExperimentsWithHumans]]
- [[TheSpreadOfBehaviorInAnOnlineSocialNetworkExperiment]]
- [[GraphClusterRandomization]]
- [[StructuralDiversityInSocialContagion]]
- [[SocialNetworksAndLaborMarketsHowStrongTiesRelateToJobFindingOnFacebookSSocialNetwork]]
- [[RandomizationAnalysisOfExperimentalDataTheFisherRandomizationTestComment]]
- [[TheEconometricsOfRandomizedExperiments]]
- [[TheParadoxOfWeakTiesIn55Countries]]
- [[AnalyzingTwoStageExperimentsInThePresenceOfInterference]]
- [[EstimatingAverageCausalEffectsUnderGeneralInterferenceWithApplicationToASocialNetworkExperiment]]
- [[LfeLinearGroupFixedEffects]]
- [[WhatCanMachinesLearnAndWhatDoesItMeanForOccupationsAndTheEconomy]]
- [[TheStrengthOfLongRangeTiesInPopulationScaleSocialNetworks]]
- [[TheImpactOfArtificialIntelligenceOnTheLaborMarket]]
- [[TrustworthyOnlineControlledExperiments]]
- [[HowManyJobsCanBeDoneAtHome]]
- [[UnresolvedReference55BD08C38BAE0677]]
- [[UnresolvedReference868744863AF9E526]]
- [[InstrumentalVariablesAndTheSearchForIdentificationFromSupplyAndDemandToNaturalExperiments]]
- [[TheDiversityBandwidthTradeOff]]
- [[IdentificationOfCausalEffectsUsingInstrumentalVariables]]
- [[UnresolvedReference2F741B815FFE98D3]]
- [[UnresolvedReferenceCF1D75CA7DE346FC]]
- [[MostlyHarmlessEconometrics]]
- [[StructuralHoles]]

## Audit Log

- 2026-09-29: Independent audit found that the extraction conflated randomized member assignment with observation units, and omitted the structural tie-strength formula and measurement timing. Corrected from the published paper, pp. 1–2.
- 2026-09-29: Independent re-audit passed. Verified the 2015 edge-level and 2019 node-level observations, the structural tie-strength formula and pretreatment timing, the median split for strong/weak structural ties, and post-formation interaction measurement against the published paper, PDF pp. 1–2. Source: https://gwern.net/doc/sociology/technology/2022-rajkumar.pdf.

## LLM Justification
[^r1]: Rajkumar et al., “A causal test of the strength of weak ties,” introduction and abstract, PDF pp. 1–2; https://gwern.net/doc/sociology/technology/2022-rajkumar.pdf.
[^r2]: Same paper, abstract and Results/Discussion, PDF pp. 1, 3–6; same URL.
[^r3]: Same paper, experiment and analysis design, PDF pp. 1–2; same URL.
[^r4]: Same paper, operational definitions of job transmission and tie strength, PDF p. 2; same URL.
[^r5]: Same paper, “The experiments” and “Results,” PDF pp. 1–4; same URL.
[^r6]: Same paper, Results and Discussion, PDF pp. 2–6; same URL.
[^r7]: Same paper, study design and job-transmission outcome, PDF pp. 1–2; same URL.
