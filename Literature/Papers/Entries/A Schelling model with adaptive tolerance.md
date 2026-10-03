---
title: A Schelling model with adaptive tolerance
publication date: 2018-03-06
authors:
  - "[[Literature/Authors/Linda Urselmans|Linda Urselmans]]"
  - "[[Literature/Authors/Steve Phelps|Steve Phelps]]"
source: https://pmc.ncbi.nlm.nih.gov/articles/PMC5839580/
tags:
  - model
  - simulation
read status: Todo
doi: 10.1371/journal.pone.0193950
---
## Abstract

We introduce a Schelling model in which people are modelled as agents following simple behavioural rules which dictate their tolerance to others, their corresponding preference for particular locations, and in turn their movement through a geographic or social space. Our innovation over previous work is to allow agents to adapt their tolerance to others in response to their local environment, in line with contemporary theories from social psychology. We show that adaptive tolerance leads to a polarization in tolerance levels, with distinct modes at either extreme of the distribution. Moreover, agents self-organize into communities of like-tolerance, just as they congregate with those of same colour. Our results are robust not only to variations in free parameters, but also experimental treatments in which migrants are dynamically introduced into the native population. We argue that this model provides one possible parsimonious explanation of the political landscape circa 2016.

## Research Questions
> Research Questions extracted via LLM from the published full text.[^r1]

- Does locally adaptive tolerance produce polarized tolerance levels and spatial clustering by tolerance as well as group?[^r1]
- How do these outcomes vary with population composition, tolerance-change rate, and migration treatments?[^r2]
- Are these outcomes robust across the model's sampled parameter settings, after excluding ranges that often fail to converge within 20,000 ticks?[^r3]

## Model
> Model extracted via LLM according to [[Model Notation]] from §2.1, Eqs. 1–3 and Algorithms 1–2; §2.2, Tables 1–3; and §2.3 of the published paper.[^r4]

### What does it represent?

Agents of two groups occupy a toroidal 50 × 50 lattice with vacant sites. Each sees nearby agents and compares its own-group share with its threshold.[^r5]

```yml
World:
  lattice: Lattice
  agents: [Agent]
  parameters: Parameters

Lattice:
  width: LATTICE_WIDTH
  height: LATTICE_HEIGHT
  sites: [Site]

Site: ...

Agent:
  group: Native | Migrant
  position: SiteId
  tolerance: MIN_TOLERANCE..MAX_TOLERANCE

Parameters:
  tolerance_step: MIN_TOLERANCE_STEP..MAX_TOLERANCE_STEP  # uniform sample
  candidate_vacancies: MIN_CANDIDATE_VACANCIES..MAX_CANDIDATE_VACANCIES  # discrete uniform sample
  final_density: MIN_FINAL_DENSITY..MAX_FINAL_DENSITY  # uniform sample
  native_share: MIN_NATIVE_SHARE..MAX_NATIVE_SHARE  # uniform sample
  migration_waves: NO_MIGRATION | WAVES_1 | WAVES_4 | WAVES_15 | WAVES_100
```

```
LATTICE_WIDTH = 50
LATTICE_HEIGHT = 50
MIGRATION_WINDOW_TICKS = 1000
SIMULATION_TICKS = 20000

MIN_TOLERANCE = 0.05
MAX_TOLERANCE = 0.95
MIN_TOLERANCE_STEP = 0.00001
MAX_TOLERANCE_STEP = 0.001
MIN_CANDIDATE_VACANCIES = 25
MAX_CANDIDATE_VACANCIES = 125
MIN_FINAL_DENSITY = 0.75
MAX_FINAL_DENSITY = 0.98
MIN_NATIVE_SHARE = 0.02
MAX_NATIVE_SHARE = 0.98

NO_MIGRATION = 0
WAVES_1 = 1
WAVES_4 = 4
WAVES_15 = 15
WAVES_100 = 100
```

### How does it work?

- An agent is satisfied when its own-group share meets its threshold. A dissatisfied agent samples vacant sites, then randomly chooses among its **current site** and qualifying sampled sites.[^r6]
- Algorithm 1 requires a qualifying site to meet the threshold **and** have an out-group neighbor; the prose states only the threshold condition.[^r6]
- With out-group contact, a satisfied agent raises its threshold by the fixed step (up to 0.95), while a dissatisfied agent keeps it unchanged. With no out-group contact, it lowers the threshold (down to 0.05), regardless of satisfaction.[^r6][^r9]
- Algorithm 2 allows a satisfied agent with out-group contact to move randomly to a sampled vacancy with probability 0.01; the prose allows satisfied agents generally to do so. The prose also says tolerance stays unchanged if no new site is found, while Eq. 3 and Algorithm 2 do not include that exception.[^r6][^r9]
- At arrival, tolerance is drawn uniformly from 0.05 to 0.95. In the E=0 control, both groups start on the lattice.[^r7]
- In dynamic treatments, migrants arrive in 1, 4, 15, or 100 waves: first at tick 50, then at intervals of 900/E ticks, with each wave rounded to the target migrant count divided by E.[^r7]
- Each wave forms a cluster: choose a vacant focal site with the most migrant neighbors, or with the most total neighbors if no migrants exist yet (random tie break). The prose says further arrivals are placed at neighboring vacancies ranked first by nearby new migrants, then by density; Algorithm 4 ranks vacant neighbors by local density only. The two placement descriptions disagree.[^r10]
- Agents update sequentially in a new random order each tick. Each run lasts 20,000 ticks; the paper varies the sampled parameters above across runs.[^r11][^r7]
- The paper calls the neighborhood both a 5 × 5 Moore neighborhood and all sites at Euclidean distance at most two; these contain different sites (for example, offset (2,1) is inside the square but outside the radius). It also calls a higher required own-group share “increased tolerance,” although the satisfaction inequality makes it a stricter threshold.[^r5][^r12]
- The notation omits exact placement tie breaks, movement sampling details, and the outcome equations; use the cited algorithms and equations for replication.[^r5][^r12]

### What can it answer?

- Whether tolerance polarizes (final bimodality coefficient), whether groups and tolerance values cluster (adjacent-neighbor Moran's I), and how mean tolerance differs between groups.[^r8]
- How these measures vary by migration treatment and sampled parameters. The paper records outcomes every 10 ticks and restricts later analyses to native share 0.2–0.8 and tolerance step at least 0.0005, where about 97% of runs pass its convergence test.[^r2][^r3][^r8]

### Where does it apply?

A stylized two-group spatial model of movement and adaptation under local contact; its results are simulation outcomes, not estimates fitted to individual behavior.[^r4][^r7]

## Metadata
### References
- [[ExodusHowMigrationIsChangingOurWorld]]
- [[HandbookOfPrejudiceStereotypingAndDiscrimination]]
- [[TheRoleOfThreatInIntergroupRelations]]
- [[IntergroupThreatTheory]]
- [[DynamicModelsOfSegregation]]
- [[RecentAdvancesInIntergroupContactTheory]]
- [[PopulationSizePerceivedThreatAndExclusionAMultipleIndicatorsAnalysisOfAttitudesTowardForeignersInGermany]]
- [[NatureOfPrejudice]]
- [[A meta-analytic test of intergroup contact theory]]
- [[CombiningSegregationAndIntegrationSchellingModelDynamicsForHeterogeneousPopulation]]
- [[DirectAndIndirectIntergroupContactEffectsOnPrejudiceANormativeInterpretation]]
- [[TheSchellingModelOfEthnicResidentialDynamicsBeyondTheIntegratedSegregatedDichotomyOfPatterns]]
- [[WhatDeterminesAttitudesToImmigrationInEuropeanCountriesAnAnalysisAtTheRegionalLevel]]
- [[GoodThingsPeakInPairsANoteOnTheBimodalityCoefficient]]
- [[EPluribusUnumDiversityAndCommunityInTheTwentyFirstCenturyThe2006JohanSkyttePrizeLecture]]
- [[BowlingAloneTheCollapseAndRevivalOfAmericanCommunity]]
- [[EfficientTestsForAnAutoregressiveUnitRoot]]
- [[AgentBasedModelingMethodsAndTechniquesForSimulatingHumanSystems]]
- [[DoesDiversityErodeSocialCohesionConceptualAndMethodologicalIssues]]
- [[TheCulturalDivideInEuropeMigrationMulticulturalismAndPoliticalTrust]]
- [[DecisionMakingInAgentBasedModelsOfMigrationStateOfTheArtAndChallenges]]
- [[TrumpBrexitAndTheRiseOfPopulismEconomicHaveNotsAndCulturalBacklash]]
- [[The2016ReferendumBrexitAndTheLeftBehindAnAggregateLevelAnalysisOfTheResult]]
- [[ANationDivided]]
- [[SocialAndEconomicIdeologiesDifferentiallyPredictPrejudiceAcrossThePoliticalSpectrumButSocialIssuesAreMostDivisive]]
- [[MinorityMajorityRelationsInTheSchellingModelOfResidentialDynamics住宅动态迁移schelling模型中的少数多数关系]]
- [[A Schelling model with adaptive tolerance]]
- [[ASchellingModelWithImmigrationDynamics]]
- [[TheDiversityWaveAMetaAnalysisOfTheNativeBornWhiteResponseToEthnicDiversity]]
- [[UnresolvedReferenceF73AD8A491BE2319]]
- [[BowlingAlone]]
- [[UnresolvedReference47CB1472FA37A51F]]
- [[UnresolvedReference0230C0C827FA69AE]]
- [[UnresolvedReference9D83278CC8670619]]
- [[UnresolvedReference714813CE6944C83E]]
- [[PopulationSizePerceiveThreatAndExclusionAMultipleIndicatorsAnalysisOfAttitudesTowardForeignersInGermany]]
- [[FromPrejudiceToIntergroupEmotionsDifferentiatedReactionsToSocialGroups]]
- [[TheNatureOfPrejudice]]
- [[EPluribusUnumDiversityAndCommunityInTheTwentyFirstCentury]]
- [[TheDiversityWaveAMetaAnalysisOfEthnicDiversityPerceivedThreatAndNativeWhiteBacklash]]
- [[MigrationEconomicChangeSocialChallenge]]
- [[UnresolvedReferenceD39AC8E8B0561158]]


## Audit Log

- 2026-09-29: Independent Luna and Astra audits both failed the first extraction. Both identified an incorrect movement rule and omitted migration, outcomes, and convergence limits. Luna additionally identified a tolerance-update conflict; Astra identified neighborhood and threshold wording conflicts. These findings were checked against the published full text and corrected or explicitly flagged above.
- 2026-09-29: Luna re-audit found an additional prose/Algorithm 4 conflict in migrant placement and an incomplete description of the neighborhood conflict. Both were corrected above.
- 2026-09-29: Luna independently re-audited the corrected note against the published full text and found no remaining material defect. Audit passed.

## LLM Justification
[^r1]: Abstract and §3 report polarization in tolerance and self-assortment into like-tolerance communities as principal findings.
[^r2]: §§2.3 and 3 compare the dynamic migration treatments; Table 4 specifies 0, 1, 4, 15, and 100 waves.
[^r3]: §2.2 and Table 1 vary initial-condition parameters; §3.2 and Table 6 restrict later analyses to native share 0.2–0.8 and tolerance step at least 0.0005 after convergence tests.
[^r4]: §2 describes the agent-based simulation; §§2.1–2.4 define its rules, conditions, and measured outcomes.
[^r5]: §2.1 defines the 50 × 50 toroidal lattice, neighborhoods within Euclidean distance two, groups, vacancies, and state variables.
[^r6]: §2.1, Eqs. 1–3 and Algorithms 1–2 specify satisfaction, movement, random satisfied-agent moves, and tolerance adaptation.
[^r7]: §§2.1–2.3 and Tables 1–4 specify uniform initial tolerance, parameter ranges, E=0 initialization, dynamic wave counts, first arrival at tick 50, spacing, and rounded wave sizes.
[^r8]: §2.4, Table 5 and Eqs. 9–13 define the spatial segregation and tolerance distribution measures used in the analyses.
[^r9]: §2.1 prose after Algorithm 1 says failed relocation leaves tolerance unchanged; Eq. 3 and Algorithm 2 update it by satisfaction and out-group contact without that condition. The prose before Algorithm 2 permits random movement by satisfied agents generally; Algorithm 2 places that move inside the out-group-contact branch.
[^r10]: §2.1, Eq. 8 specifies the focal site. The paragraph following it says new-migrant count is the first placement criterion and local density the second; Algorithm 4 shows a density comparison but no new-migrant-count comparison.
[^r11]: §3 states agents update sequentially in a shuffled order each tick; Table 2 gives 20,000 ticks.
[^r12]: §2.1 describes H(p) as both a 5 × 5 Moore neighborhood and Euclidean radius two, and calls the threshold tolerance although Eq. 2 requires a larger own-group share at larger thresholds.
