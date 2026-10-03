---
title: An Agent-Based Model of Social Identity Dynamics
authors:
- '[[Literature/Authors/Paul E. Smaldino|Paul E. Smaldino]]'
- '[[Literature/Authors/Cynthia L. Pickett|Cynthia L. Pickett]]'
- '[[Literature/Authors/Jeffrey W. Sherman|Jeffrey W. Sherman]]'
- '[[Literature/Authors/Jeffrey C. Schank|Jeffrey C. Schank]]'
publication date: 2012-10-31
tags:
- model
- simulation
source: https://www.jasss.org/15/4/7.html
doi: 10.18564/jasss.2030
read status: Todo
---
## Abstract

According to optimal distinctiveness theory (ODT; Brewer 1991), individuals prefer social groups that are relatively distinct compared to other groups in the individuals' social environment. Distinctive groups (i.e., groups of moderate relative size) are deemed "optimal" because they allow for feelings of inclusion and social connection while simultaneously providing a basis for differentiating the self from others. However, ODT is a theory about individual preferences and, as such, does not address the important question of what types of groups are actually formed as a function of these individual-level preferences for groups of a certain size. The goal of the current project was to address this gap and provide insight into how the nature of the social environment (e.g., the size of the social neighborhood) interacts with individual-level group size preferences to shape group formation. To do so, we developed an agent-based model in which agents adopted a social group based on an optimal group size preference (e.g., a group whose size represented 20% of the social neighborhood). We show that the assumptions of optimal distinctiveness theory do not lead to individually satisfactory outcomes when all individuals share the same social environment. We were able to produce results similar to those predicted by ODT when social neighborhoods were local and overlapping. These results suggest that the effectiveness of a social identity decision strategy is highly dependent on sociospatial structure.


## Research Questions
> Research Questions extracted via LLM

- How do preferences for optimally distinctive group sizes interact with social-neighborhood structure to shape group formation and identity dynamics?[^r1]
- Do well-mixed and spatially local populations differ in their ability to sustain groups with preferred relative sizes?[^r1][^r2]

## Model
> Model extracted via LLM according to [[Model Notation]]

### What does it represent?

- The model represents a population of N agents with one social identity (SID) each, drawn initially at random from k₀ available identities.[^r3][^r6]
- All agents share the same fixed preferred distinctiveness d*. Identities are orthogonal, cannot be created, and switching is instantaneous.[^r3][^r6]

### How does it work?

The following sketch separates the shared population settings from each agent's current identity and, in the spatial treatment, location.[^r3][^r4]

```yml
World:
  agents: [Agent]
  identities: [SocialIdentity]
  preferred_distinctiveness: 0..1  # shared and fixed across agents
  structure: WellMixed | Lattice(LatticeParameters)

LatticeParameters:
  side_length: 0..
  neighborhood_radius: 0..

SocialIdentity: ...
Site: ...

Agent:
  identity: SocialIdentityId
  location: SiteId?  # present only in the spatial condition
  observed_frequency: 0..1  # population share or local-neighborhood share
```

- At each time step, agents are stepped asynchronously in randomized order.[^r3][^r4]
- Agent i measures the frequency d_g of each identity and switches to the available SID minimizing |d_g−d*|.[^r3][^r4]
- If multiple identities tie, one is selected at random, except that a tied current SID is retained.[^r3][^r4]
- In the well-mixed model d_g=n_g/N uses the full population.[^r3][^r4]
- In the spatial model N=L² agents occupy one site each on an L×L lattice; each observes a square neighborhood of side 2r+1 centered on itself, including itself (r=1 gives a 3×3 neighborhood), and computes local SID frequencies.[^r3][^r4]

- The decision-error treatment chooses a random SID from the original nine with probability 0.01 per step for 4,500 steps; error is then disabled for 500 further steps.[^r5]
- The paper averages 30 runs per condition at t=5,000 for its systematic comparisons.[^r5]
- It varies d* and spatial radius r; the spatial model’s conclusions therefore depend on both preference and neighborhood size.[^r5]

- The model omits heterogeneous preferences, identity creation, similarity or nesting among identities, multiple simultaneous identities, and movement or changing social networks; the authors explicitly identify these as simplifications or possible extensions.[^r6]

### What can it answer?

- In the well-mixed model, the intuitive prediction k*=round(1/d*) is not generally obtained: for sufficiently large N and k₀>1/d*, the reported equilibrium relationship is k*(d*)=floor(1/(2d*))+1 (Eq. 2), so d*=0.2 gives three active SIDs rather than the intuitive five.[^r7]
- Spatially local observation can yield average distinctiveness close to optimal when d*<0.3.[^r7]
- Spatial structure also permits several locally majority identities to coexist when d*>0.5, but those patterns are vulnerable to decision error, especially at group boundaries; small neighborhoods are an exception to the tendency toward a single SID.[^r7]
- These are reported results, not rules imposed by the model.[^r7]

### Where does it apply?

- It addresses how global versus local information changes group formation under a shared optimal-distinctiveness rule.[^r1][^r6]
- The authors frame it as a deliberately simple initial model rather than a comprehensive account of social identity choice.[^r1][^r6]

## Metadata
### References
- [[PoliticalDistinctivenessAnIdentityOptimisingApproach]]
- [[SpatialBehaviorInGroupsAnAgentBasedApproach]]
- [[PositiveNegativeAsymmetryInSocialDiscriminationTheImpactOfStimulusValenceAndSizeAndStatusDifferentialsOnIntergroupEvaluations]]
- [[TheEvolutionOfReciprocityInSizableGroups]]
- [[TheSocialSelfOnBeingTheSameAndDifferentAtTheSameTime]]
- [[TakingTheSocialOriginsOfHumanNatureSeriouslyTowardAMoreImperialistSocialPsychology]]
- [[SelfEvaluationEffectsOfInterpersonalVersusIntergroupSocialComparison]]
- [[AloneInACrowdTheStructureAndSpreadOfLonelinessInALargeSocialNetwork]]
- [[SocialNetworkSensorsForEarlyDetectionOfContagiousOutbreaks]]
- [[OptimalVersusNaiveDiversificationHowInefficientIsThe1NPortfolioStrategy]]
- [[IdentityNeedsVersusSocialOpportunitiesTheUseOfGroupLevelAndIndividualLevelManagementStrategies]]
- [[GenerativeSocialScience]]
- [[CoupledContagionDynamicsOfFearAndDiseaseMathematicalAndComputationalExplorations]]
- [[StructuralEmbeddednessAndStabilityOfInterpersonalRelations]]
- [[KamaATemperatureDrivenModelOfMateChoiceUsingDynamicPartnerPreferences]]
- [[RationalityForMortalsHowPeopleCopeWithUncertainty]]
- [[HomoHeuristicusWhyBiasedMindsMakeTheBestInferences]]
- [[TheOutbreakOfCooperationAmongSuccessDrivenIndividualsUnderNoisyConditions]]
- [[PopulationHeterogeneityAndIndividualDifferencesInAnAssortativeAgentBasedMarriageAndDivorceModelMadamUsingSearchWithRelaxingExpectations]]
- [[UncertaintyIdentityTheoryInMPZannaEd]]
- [[StabilityInCompetition]]
- [[EvolutionaryGamesAndComputerSimulations]]
- [[DynamicalEvolutionaryPsychologyIndividualDecisionRulesAndEmergentSocialNorms]]
- [[TheSpatialSpreadOfAltruismVersusTheEvolutionaryResponseOfEgoists]]
- [[MinorityAndMajorityDiscriminationWhenAndWhy]]
- [[OptimalDistinctivenessTheoryAFrameworkForSocialIdentitySocialCognitionAndIntergroupRelationsInMZannaJOlsonEds]]
- [[MasonAMultiagentSimulationEnvironment]]
- [[SocialNetworksAndOrganizationalDynamics]]
- [[ComplexAdaptiveSystemsAnIntroductionToComputationalModelsOfSocialLife]]
- [[SegregationThatNoOneSeeks]]
- [[EvolutionaryGamesAndSpatialChaos]]
- [[ASimpleRuleForTheEvolutionOfCooperationOnGraphsAndNetworks]]
- [[TheLogicOfCollectiveAction]]
- [[CoevolutionaryGamesAMiniReview]]
- [[AgentBasedModelingAsAToolForStudyingSocialIdentityProcessesTheCaseOfOptimalDistinctivenessTheoryInRMKramerGJLeonardelliRWLivingstonEds]]
- [[AgentBasedAndIndividualBasedModelingAPracticalIntroduction]]
- [[RogersParadoxRecastAndResolvedPopulationStructureAndTheEvolutionOfSocialLearningStrategies]]
- [[DynamicModelsOfSegregation]]
- [[MicromotivesAndMacrobehavior]]
- [[PerceivedIntragroupHomogeneityInMinorityMajorityContexts]]
- [[SelfStereotypingAndSocialContextTheEffectsOfRelativeInGroupSizeAndInGroupStatus]]
- [[TheOriginsOfOptions]]
- [[MovementPatternsSocialDynamicsAndTheEvolutionOfCooperation]]
- [[ContextualizingPersonPerceptionsDistributedSocialCognition]]
- [[AgentBasedModelingANewApproachForTheoryBuildingInSocialPsychology]]
- [[Computational Modelling of Trust and Social Relationships]]
- [[AnIntegrativeTheoryOfIntergroupConflictInSWorchelGWAustinEds]]
- [[SelfAndCollectiveCognitionAndSocialContext]]
- [[ExponentialRandomGraphPModelsForAffiliationNetworks]]
- [[CollectiveDynamicsOfSmallWorldNetworks]]

## Audit Log
- Independent audit failed: initialization, local neighborhood definition, error schedule, and central well-mixed equilibrium result were missing or underspecified; robustness was stated too broadly. Revised against the model and results sections.[^r3][^r4][^r5][^r7]
- Independent re-audit passed after those corrections and verification of the published date, cited procedure sketch, and source-supported results.[^r3][^r4][^r5][^r7]

## LLM Justification
[^r1]: Smaldino et al., “An Agent-Based Model of Social Identity Dynamics,” Abstract and §§1.5–1.10 (aim and research questions): https://www.jasss.org/15/4/7.html
[^r2]: Ibid., §§3–6 (comparisons and results).
[^r3]: Ibid., §2.1–2.2 and §3.1 (one identity, available identity set, shared fixed d*, random initialization, randomized asynchronous stepping, distance rule, and tie handling).
[^r4]: Ibid., §§3.1–3.2 (well-mixed population frequency); §§4.1–4.2 (L×L lattice, local neighborhood dimensions including focal agent, radius, and local frequency rule).
[^r5]: Ibid., §5.11 and Figure 10 (error probability, original nine SIDs, 4,500-step error period, 500-step stabilization, 30-run averages at t=5,000); §5.8–5.10 (variation in d* and r).
[^r6]: Ibid., §§6.6–6.7 (simplifications and future extensions).
[^r7]: Ibid., §§3.2–3.4, Eq. 1 and Eq. 2 (intuitive expected count versus equilibrium relationship); §§5.8–5.11 and 6.2–6.3 (spatial outcomes and qualified error robustness).
