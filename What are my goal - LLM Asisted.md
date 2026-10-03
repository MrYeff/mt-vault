
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
	- ? compare coverage: ranked exposure, imperfect knowledge, directed ties, tie formation/decay, shared activities
	- ? extend the closest model for missing mechanisms

*>>> instrumental goal>>>*

- **G:** evaluate simulation
- **Q:** how to measure accuracy?
	- does the simulation predict the same thing as established models in their selected domain?
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
		- ? agreement with these models checks consistency; compare with held-out observations to test prediction[^validation]

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

[^happy]: [Diener & Seligman (2002), Very Happy People](https://www.psychologicalscience.org/journals/psychological-science/1467-9280.00415/): strong relationships characterized the happiest group. Association, not proof that adding ties causes happiness.
[^wellbeing]: [2024 meta-analysis](https://pubmed.ncbi.nlm.nih.gov/39233622/): higher support and lower loneliness were associated with life satisfaction in adults aged 65+. Check generalization to the app’s users. [Short Loneliness Scale](https://www.cmu.edu/common-cold-project/measures-by-study/psychological-and-social-constructs/social-relationships-loneliness-measures/loneliness.html): an established loneliness measure.
[^swls]: [Diener et al. (1985), SWLS](https://pubmed.ncbi.nlm.nih.gov/16367493/): measures global life satisfaction; a direct outcome measure, not a network metric.
[^integration]: [Cohen et al., Social Integration and Health](https://www.cmu.edu/joss/content/articles/volume1/cohen.html): involvement in social relationships/activities. [SNI documentation](https://www.cmu.edu/common-cold-project/measures-by-study/psychological-and-social-constructs/social-relationships-loneliness-measures/social-integration-network-size.html): counts roles with contact at least every two weeks; role diversity and network size are separate measures.
[^belonging]: [Lee, Draper & Lee (2001), SCS-R](https://www.mhpss.net/toolkit/mhpss-m-and-e-mov-toolkit/resource/social-connectedness-scale-revised): perceived connectedness. Belonging and observable participation are separate outcomes.
[^metrics]: Proposed operationalizations for this project. Define “active tie” and the observation interval before comparing algorithms. Graph measures alone do not establish happiness or relationship quality.
[^crossgroup]: [[Social capital II- determinants of economic connectedness]] separates exposure from friending bias. Applying that distinction to other groups is a proposed extension.
[^prod]: [PROD paper](https://arxiv.org/abs/2112.00626): people recommendations, network rewiring and opinion dynamics. A follow edge is not automatically a friendship.
[^trecs]: [T-RECS paper](https://arxiv.org/abs/2107.08959): configurable recommender feedback framework. The relationship mechanism would be an extension.
[^validation]: Proposed test: fit on one period, predict the next, compare tie changes/interactions with observations and no-change/random baselines. Model agreement tests consistency, not empirical accuracy.
