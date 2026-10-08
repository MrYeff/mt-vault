
- **G:** build a social media app that makes people more socialy connected  
- **Q:** what parts of the app does this research focus on
	- information algorithms - what does each user get to see
- **Q:** what makes algortihms good?
	- key social metrics go up
	- **Q:** what are key social metrics?
		- ? increase social connectedness
		- ? reduce solo screen time
		- ? increase positive steriotypes
		- metrics correlating with happines
		- **Q:** what are established metrics that positively correlate with happines?
			- quality of close relationships[^happy]
			- perceived social support; lower loneliness[^wellbeing]
			- measure life satisfaction directly with SWLS[^swls]
		- metrics correlating with social integration 
		- **Q:**  what metrics correlating with social integration ?
			- regular contact across different social roles: Social Network Index (SNI)[^integration]
			- ? participation in shared activities: frequency and repeat attendance
			- ? perceived belonging: Social Connectedness Scale–Revised (SCS-R)[^belonging]
		- **Q:** what is social integration?
			- participation in social relationships, groups and shared activities[^integration]
- **Q:** How do we decide if algorithm is good - pre deploy?
	- Build a simulation

*>>> instrumental goal>>>*

- **G:** Use simulation to predict change in *social network metrics* based on *information enviroment* accurately 
- **Q:** what are relevant social network metrics?
	- ? active reciprocal contacts per agent[^metrics]
	- ? fraction of agents with no active reciprocal contacts[^metrics]
	- ? number of social roles with regular contact per agent[^integration]
	- ? cross-group tie share, accounting for opportunities to meet[^crossgroup]
	- ? tie persistence over a fixed interval[^metrics]
	- ? distribution of contacts across agents; report the least connected agents separately[^metrics]
	- ? directed tie reciprocity; keep one-sided ties visible[^metrics]
- **Q:** do simulations exist that model this?
	- **Q:** what simulations exist modeling social behaviour?
		- Selection, not exhaustive. Priority reading order: [[Simulation Reading List]].
		- PROD: opinions and a changing follow network — [[The Effect of People Recommenders on Echo Chambers and Polarization]]
		- T-RECS: recommendation and user feedback — [[T-RECS- A Simulation Tool to Study the Societal Impact of Recommender Systems]]
		- HUMAT: motives, choices and social influence — [[HUMAT- An Integrated Framework for Modelling Individual Motivations- Social Exchange and Network Dynamics]]
		- Sutcliffe et al.: interaction, trust and relationship formation/decay — [[Social Relationships and the Emergence of Social Networks]]
		- FIRMAN: friendship formation under capacity and identity constraints — [[How Does Facebook Retain Segregated Friendship- An Agent-Based Model Approach]]
	- **Q:** wich of these can model the impact of information on social networks?
		- PROD directly models people recommendations changing follow ties and opinions[^prod]
		- T-RECS models content recommendations and feedback; friendship updates need an added mechanism[^trecs]
		- HUMAT models information exchange and choices; this alone does not specify changing friendships
		- FIRMAN varies platform-like capacity/outreachability; it does not implement a ranked feed
	- **Q:** what are limitations of these simulations?
		- PROD: one opinion per agent; fixed follow count; no friendship quality or shared activities.[^limits_prod]
		- T-RECS: user behavior must be configured; friendship changes need an added mechanism.[^limits_trecs]
		- HUMAT: core models choices between A and B; ranked exposure and friendship changes need additional rules.[^limits_humat]
		- Sutcliffe: no message content or ranked exposure; exact trust/search rules partly unspecified.[^limits_sutcliffe]
		- FIRMAN: reciprocal ties only; eligible invitations cannot be refused; no ranked exposure.[^limits_firman]
		- Validation: PROD has no direct quantitative test against real data; T-RECS demonstrates conceptual replications.[^limits_prod][^limits_trecs]
		- Outcomes: less polarization or more ties do not establish belonging or better relationships.[^limits_metrics]
	- ? compare coverage: ranked exposure, imperfect knowledge, directed ties, tie formation/decay, shared activities
	- ? extend the closest model for missing mechanisms

*>>> instrumental goal>>>*

- **G:** evaluate simulation
- **Q:** how to measure accuracy?
	- does the simulation predict the same thing as established models in their selected domain?
	- ? test prediction against held-out tie changes and interactions; model agreement checks consistency[^validation]
	- **Q:** what established models exists
		- bounded confidence — [[Mixing beliefs among interacting agents]]
		- adaptive Schelling — [[A Schelling model with adaptive tolerance]]
		- FIRMAN — [[How Does Facebook Retain Segregated Friendship- An Agent-Based Model Approach]]
		- SAOM — [[Stochastic Actor-Oriented Models for Network Dynamics]]
		- relational event models — [[4. A Relational Event Framework for Social Action]]
		- cognitive social structures — [[Cognitive social structures]]
	- **Q:** what parts of the domain do they model?
		- bounded confidence: opinion change after encounters; consensus and clustering
		- adaptive Schelling: relocation, neighborhood segregation and changing thresholds
		- FIRMAN: reciprocal friendship formation subject to identity distance and capacity
		- SAOM: changes in observed networks over time
		- relational event models: order/timing of directed actions
		- cognitive social structures: who believes which ties exist; measurement, not a temporal simulator
		
*>>> instrumental goal (if not exist)>>>*

- **G:** build simulation
	- **Q:** how is information represented?
		- **Q:** how to represent psychological / social effects?
			- **Q:** what effects do exist?
				- ? habbits
				- ? asymetric relationships
				- ? moral judgement
				- ? steriotypes
				- ? misunderstanding
				- ? introverted / extroverted
				- ? social anxiety
				- ? hypocrite
				- ? topic memory difficulty
				- ? homophily: preferential interaction with similar people
				- ? reciprocity: responding to received attention or support
				- ? repeated contact: familiarity and tie maintenance
				- ? limited time/attention: competing relationships and activities
				- ? perceived group norms: choices influenced by what peers seem to do
		- ? see [[Model]]
		- ? separate actual ties/events from each agent’s beliefs about them
		- ? keep what I believe separate from what I believe another agent believes
		- ? record source, time and confidence of an observation
		- ? restrict observations to encounters, shown content and received messages
	- **Q:** what drives change in the system?
		- ? agent - agent influence
		- ? enviroment - agent influence
		- ? agent internal processes
		- ? actions connect beliefs to network changes: follow, message, invite, attend, withdraw
		- ? feed ranking changes which people, claims and events agents encounter
		- ? tie maintenance uses time/attention; neglect permits ties to weaken
		- **Q:** how do agents influence each other?
			- ? when they meet they inform each other about their opinions
			- **Q:** when do agents meet?
				- ? random encounters at events
		- **Q:** how does the enviroment influence an agent?
			- ? ground truth correlation e.g. `techno ~ loud`
		- **Q:** what agent internal processes do exist?
			- ? agents reflect about their believes
			- ? information decays over time

## Sources / reasoning

[^happy]: [[Very Happy People]]: strong relationships characterized the happiest group. Association, not proof that adding ties causes happiness.
[^wellbeing]: [[A Systematic Review and Meta-Analysis of the Association Between Physical Capability, Social Support, Loneliness, Depression, Anxiety, and Life Satisfaction in Older Adults]]: higher support and lower loneliness were associated with life satisfaction in adults aged 65+. Check generalization to the app’s users. [Short Loneliness Scale](https://www.cmu.edu/common-cold-project/measures-by-study/psychological-and-social-constructs/social-relationships-loneliness-measures/loneliness.html): an established loneliness measure.
[^crossgroup]: [[Social capital II- determinants of economic connectedness]] separates exposure from friending bias. Applying that distinction to other groups is a proposed extension.
[^swls]: [[The Satisfaction With Life Scale]]: measures global life satisfaction; a direct outcome measure, not a network metric.
[^integration]: [[Social Integration and Health- The Case of the Common Cold]]: involvement in social relationships/activities. [SNI documentation](https://www.cmu.edu/common-cold-project/measures-by-study/psychological-and-social-constructs/social-relationships-loneliness-measures/social-integration-network-size.html): counts roles with contact at least every two weeks; role diversity and network size are separate measures.
[^belonging]: [[Social connectedness, dysfunctional interpersonal behaviors, and psychological distress- Testing a mediator model]]: perceived connectedness. Belonging and observable participation are separate outcomes.
[^metrics]: Proposed operationalizations for this project. Define “active tie” and the observation interval before comparing algorithms. Graph measures alone do not establish happiness or relationship quality.
[^prod]: [[The Effect of People Recommenders on Echo Chambers and Polarization]]: people recommendations, network rewiring and opinion dynamics. A follow edge is not automatically a friendship.
[^trecs]: [[T-RECS- A Simulation Tool to Study the Societal Impact of Recommender Systems]]: configurable recommender feedback framework. The relationship mechanism would be an extension.
[^validation]: Proposed test: fit on one period, predict the next, compare tie changes/interactions with observations and no-change/random baselines. Model agreement tests consistency, not empirical accuracy.

[^limits_metrics]: Project limitation: the desired outcomes above include belonging and relationship quality. PROD §4.2 measures neighbor-opinion correlation and random-walk separation; these do not measure those outcomes.
[^limits_prod]: [[The Effect of People Recommenders on Echo Chambers and Polarization]], §§3–4 and §6: scalar opinions, directed follow rewiring, fixed population/contact budget, no direct quantitative comparison with real data. Missing feed/activity/nested-belief mechanisms follow from its stated state and updates.
[^limits_scope]: Scope comparison of the models listed immediately above, not a claim about every possible extension. Bounded confidence: opinion updates; Schelling: relocation; FIRMAN: friendship formation; SAOM/relational events: configured effects on tie/action rates; cognitive social structures: perceived-network measurement.

[^limits_trecs]: [[T-RECS- A Simulation Tool to Study the Societal Impact of Recommender Systems]], §§4.1–4.4: researcher-configured user behavior and feedback; friendship formation is not supplied by the core feedback loop. §§5.1–5.2: conceptual replications, with differences in operationalization; these do not validate behavior for this app.
[^limits_humat]: [[HUMAT- An Integrated Framework for Modelling Individual Motivations- Social Exchange and Network Dynamics]], §2 and Appendix A: A/B choices, dissonance and signalling/inquiring among alters. Ranked exposure and friendship-change rules are additions to this core, not claims that the framework forbids extensions.
[^limits_sutcliffe]: [[Social Relationships and the Emergence of Social Networks]], §§2.1–2.6: partner selection and cooperation/defection update directed trust; messages have no modeled content and no recommendation ranking. Exact inherited search functions are omitted, and trust prose/control rules conflict; see the note’s source-located disclosures.
[^limits_firman]: [[How Does Facebook Retain Segregated Friendship- An Agent-Based Model Approach]], model procedure and design: reciprocated ties, bilateral capacity/outreachability constraints, no refusal after eligibility. Platform effects are represented by these parameters, not a recommendation/feed procedure.
