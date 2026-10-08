---

title: "How Does Facebook Retain Segregated Friendship? An Agent-Based Model Approach"
tags:
  - model
  - simulation
authors:
  - "[[Literature/Authors/Firman M. Firmansyah|Firman M. Firmansyah]]"
publication date: 2023-11-22
source:
  - https://arxiv.org/pdf/2109.08862v1
  - https://journals.sagepub.com/doi/10.1177/08944393231213960
doi: 10.1177/08944393231213960
read status: Todo
⚠️:
  - fulltext unavailable
---
## Abstract

Facebook, the largest social networking site in the world, has overcome the structural barriers that historically constrain individuals to reach out to different others. Through the platform, people from all walks of life and virtually any location can develop diverse friendships online. However, friendships on Facebook have been as segregated as friendships in real life. This research sought to understand why the leading social networking site intended to “bring the world closer together” retains segregated friendship. In doing so, I employed a series of agent-based simulations based on the Framework for Intergroup Relations and Multiple Affiliations Networks (FIRMAN). As demonstrated, Facebook has primarily enhanced users’ capacity to maintain a larger number of friendships (tie capacity), but it has done little to empower users’ ability to accept diversity and befriend different others (tie outreachability). Facebook must focus on the latter should they truly wish to contribute to the development of a more inclusive society. While in this study I focus on ethnically segregated friendship on Facebook, I argue that the same explanation might also hold for racially and ideologically segregated friendships on other bidirectional social networking sites.[^r0]

## Research Questions
> Research Questions extracted via LLM.[^aim]

- Given the same outreachability, do larger friendship pools and capacities reduce ethnic segregation?[^aim]
- Given different outreachability levels, how many cross-group friendships form?[^aim]

## Model
> Model extracted via LLM according to [[Model Notation]]. The rules below describe the accessible preprint; the published full text is unavailable.[^scope]

### What does it represent?

People, one binary ethnicity, and reciprocal friendships. Outreachability limits identity distance; capacity limits friend count. Tie length is identity distance, not relationship strength.[^state]

```yml
World:
  agents: [Agent]
  friendships: [Friendship]

Agent:
  ethnicity: Majority | Minority
  outreachability: 0 | 1
  capacity: int

Friendship:
  a: AgentId
  b: AgentId

Scenario:
  population: int
  mean_capacity: f64
  tolerant_share: 0..1
```

### How does it work?

Initialization and friendship formation follow Methods, Equations 1–2 and Figure 3. The notation uses Equation 2 for capacity; Figure 3 prints outreachability in that test instead.[^rules]

```
IDENTITY_WEIGHT = 1
MINORITY_SHARE = 0.22
CAPACITY_VARIANCE = 0.25
SATISFACTION_FRACTION = 0.5

sim_loop(
  mut world: World
):
  while exists_eligible_unlinked_pair(world):
    pair = next_pair_stochastically(world)
    sim_step(world, pair.a, pair.b)


sim_step(
  mut world: World,
  a: AgentId,
  b: AgentId
):
  if a != b and not friends(world, a, b):
    if eligible(world, a, b):
      world.friendships.push(Friendship(a, b))


eligible(
  world: World,
  a: AgentId,
  b: AgentId
) -> bool:

  x = world.agents[a]
  y = world.agents[b]
  distance = IDENTITY_WEIGHT * (x.ethnicity != y.ethnicity)

  out = distance <= min(x.outreachability, y.outreachability)
    and degree(world, a) < x.capacity
    and degree(world, b) < y.capacity


initialize(
  scenario: Scenario
) -> World:

  for i in 0..scenario.population:
    minority = Bernoulli(MINORITY_SHARE)
    agent.ethnicity = if minority: Minority else: Majority
    agent.outreachability = Bernoulli(scenario.tolerant_share)
    agent.capacity = discrete_normal(
      scenario.mean_capacity,
      CAPACITY_VARIANCE
    )
    agents.push(agent)

  out = World(agents, friendships = [])
```

- Agents contact people in their own population; an eligible invite cannot be declined.[^rules]
- There is no model of beliefs or imperfect information. Eligibility uses identity, outreachability and current friend counts directly.[^observation]
- Only friendships change; identities, outreachability and capacity remain fixed during formation.[^rules]
- The loop stops when no distinct, unlinked pair satisfies `eligible`. `next_pair_stochastically`: the selection distribution is unspecified. `discrete_normal`: the paper refers to code for discretization; rounding and negative-value handling are not given in the text.[^gaps]

### What can it answer?

Given a population, capacities and outreachability:[^design]

- How many same-group and cross-group friendships form?[^outcomes]
- What fraction of each person's friends belong to the same group?[^outcomes]
- How many people reach half their friend capacity?[^outcomes]

The experiment compares two settings at each outreachability level; constants follow Table 2.[^design]

```
OFFLINE_POPULATION = 30
OFFLINE_MEAN_CAPACITY = 3
FACEBOOK_POPULATION = 300
FACEBOOK_MEAN_CAPACITY = 30
TOLERANT_SHARE = 0.2 | 0.5 | 0.8
TRIALS_PER_CONDITION = 100
```

- Six conditions, 600 runs. Population and capacity change together, so the experiment does not separate their effects.[^design]
- Facebook-like runs produce more friendships but similar segregation; higher outreachability produces more cross-group friendships.[^results]
- Comparison data: Hofstra et al.'s offline and Facebook networks. The simulation collapses five minority groups into one; agreement of aggregate percentages does not validate every mechanism.[^validation]
- “Satisfied” means friend count ≥ `SATISFACTION_FRACTION * capacity`; it is a count threshold, not measured wellbeing. The text does not specify the same-group fraction for people with no friends.[^outcomes]
- The published supplement also measures satisfaction at thresholds `0.25` and `0.75`. Its code/data link could not be accessed; no additional implementation rules are inferred from it.[^supplement]
- Source conflicts: Methods/Table 2 use `0.2 | 0.5 | 0.8`; results prose uses `0.2 | 0.5 | 0.9`, and Table 4 uses `0.3` for the first case. Table 4's difference signs also contradict its stated subtraction order.[^conflicts]

### Where does it apply?

- Ethnic segregation in reciprocal friendship networks.[^limits]
- No tie strength, recommendation algorithm, feed, preference ranking, belief update or parasocial tie is simulated.[^limits]
- The author proposes extending the explanation to racial and ideological segregation; those extensions are not tested here.[^limits]

## Metadata
### References

Published bibliography: 59 entries, in publisher order. The accessible preprint has a different, shorter bibliography.[^bibliography]

- [[Gender and professional e-networks- Implications of gender heterophily on job search facilitation and outcomes|Gender and professional e-networks: Implications of gender heterophily on job search facilitation and outcomes]]
- [[Fostering diverse friendships- The role of beliefs about the value of diversity|Fostering diverse friendships: The role of beliefs about the value of diversity]]
- [[Tweeting from left to right- Is online political communication more than an echo chamber-|Tweeting from left to right: Is online political communication more than an echo chamber?]]
- [[Predicting international Facebook ties through cultural homophily and other factors|Predicting international Facebook ties through cultural homophily and other factors]]
- [[Manhattan distance|Manhattan distance]]
- [[Agent-based modeling- Methods and techniques for simulating human systems|Agent-based modeling: Methods and techniques for simulating human systems]]
- [[The socialbot network- When bots socialize for fame and money|The socialbot network: When bots socialize for fame and money]]
- [[Facebooking for good- Online contact to address offline conflict|Facebooking for good: Online contact to address offline conflict]]
- [[The social structure of political echo chambers- Variation in ideological homophily in online networks|The social structure of political echo chambers: Variation in ideological homophily in online networks]]
- [[School friendship networks, homophily and multiculturalism- Evidence from European countries|School friendship networks, homophily and multiculturalism: Evidence from European countries]]
- [[Expressing and challenging racist discourse on Facebook- How social media weaken the Spiral of Silence theory|Expressing and challenging racist discourse on Facebook: How social media weaken the Spiral of Silence theory]]
- [[The igraph software package for complex network research|The igraph software package for complex network research]]
- [[Purity homophily in social networks|Purity homophily in social networks]]
- [[Do online social media cut through the constraints that limit the size of offline social networks-|Do online social media cut through the constraints that limit the size of offline social networks?]]
- [[FAQs|FAQs]]
- [[The Focused Organization of Social Ties|The focused organization of social ties]]
- [[Dangerous speech, anti-Muslim violence, and Facebook in Myanmar|Dangerous speech, anti-Muslim violence, and Facebook in Myanmar]]
- [[Why do homogeneous friendships persist in a diverse population- Making sense of homophily|Why do homogeneous friendships persist in a diverse population? Making sense of homophily]]
- [[Interracial contact and changes in the racial attitudes of white college students|Interracial contact and changes in the racial attitudes of white college students]]
- [[Beyond the core- Who has larger social networks-|Beyond the core: Who has larger social networks?]]
- [[Sources of segregation in social networks- A novel approach using Facebook|Sources of segregation in social networks: A novel approach using Facebook]]
- [[The psychology of friendship|The psychology of friendship]]
- [[Political homophily in social relationships- Evidence from online dating behavior|Political homophily in social relationships: Evidence from online dating behavior]]
- [[The impact of diversity in informal social networks on tolerance in Japan|The impact of diversity in informal social networks on tolerance in Japan]]
- [[Similarity-attraction effects in friendship formation- Honest platoon-mates prefer each other but dishonest do not|Similarity-attraction effects in friendship formation: Honest platoon-mates prefer each other but dishonest do not]]
- [[Fear and loathing across party lines- New evidence on group polarization|Fear and loathing across party lines: New evidence on group polarization]]
- [[Agent-based modeling- A guide for social psychologists|Agent-based modeling: A guide for social psychologists]]
- [[School racial composition and adolescent racial homophily|School racial composition and adolescent racial homophily]]
- [[Homophily influences ranking of minorities in social networks|Homophily influences ranking of minorities in social networks]]
- [[A computational study of homophily and diffusion of common knowledge on social networks based on a model of Facebook|A computational study of homophily and diffusion of common knowledge on social networks based on a model of Facebook]]
- [[Gender homophily in online dyadic and triadic relationships|Gender homophily in online dyadic and triadic relationships]]
- [[On the cognitive benefits of cultural experience- Exploring the relationship between studying abroad and creative thinking|On the cognitive benefits of cultural experience: Exploring the relationship between studying abroad and creative thinking]]
- [[Teens, privacy and online social networks- How teens manage their online identities and personal information in the age of MySpace|Teens, privacy and online social networks: How teens manage their online identities and personal information in the age of MySpace]]
- [[A case study of international students’ social adjustment, friendship development, and physical activity|A case study of international students’ social adjustment, friendship development, and physical activity]]
- [[Homogeneity of personal values and personality traits in Facebook social networks|Homogeneity of personal values and personality traits in Facebook social networks]]
- [[Everything you need to know about agent-based modelling and simulation|Everything you need to know about agent-based modelling and simulation]]
- [[Me and my 400 friends- The anatomy of college students’ Facebook networks, their communication patterns, and well-being|Me and my 400 friends: The anatomy of college students’ Facebook networks, their communication patterns, and well-being]]
- [[Platformed racism- The mediation and circulation of an Australian race-based controversy on Twitter, Facebook and YouTube|Platformed racism: The mediation and circulation of an Australian race-based controversy on Twitter, Facebook and YouTube]]
- [[Worth the weight- Conceptualizing and measuring strong versus weak tie homophily|Worth the weight: Conceptualizing and measuring strong versus weak tie homophily]]
- [[Countering hate speech on Facebook- The case of the Roma Minority in Slovakia|Countering hate speech on Facebook: The case of the Roma Minority in Slovakia]]
- [[Residential segregation and interracial friendship in schools|Residential segregation and interracial friendship in schools]]
- [[Make new friends or keep the old- Gender and personality differences in social networking use|Make new friends or keep the old: Gender and personality differences in social networking use]]
- [[Personality homophily and geographic distance in Facebook|Personality homophily and geographic distance in Facebook]]
- [[Is having an educationally diverse social network good for health-|Is having an educationally diverse social network good for health?]]
- [[The filter bubbles- What the internet is hiding from you|The filter bubbles: What the internet is hiding from you]]
- [[Will you be my friend- Responses to friendship requests from strangers|Will you be my friend? Responses to friendship requests from strangers]]
- [[To befriend or not- A model of friend request acceptance on Facebook|To befriend or not? A model of friend request acceptance on Facebook]]
- [[The differential effects of racially homophilous sponsorship ties on job opportunities in an elite labor market- The case of NCAA basketball coaching|The differential effects of racially homophilous sponsorship ties on job opportunities in an elite labor market: The case of NCAA basketball coaching]]
- [[Social distance in the United States- Sex, race, religion, age, and education homophily among confidants, 1985 to 2004|Social distance in the United States: Sex, race, religion, age, and education homophily among confidants, 1985 to 2004]]
- [[Social simulation in the social sciences- A brief overview|Social simulation in the social sciences: A brief overview]]
- [[Why Facebook is losing the war on hate speech in Myanmar|Why Facebook is losing the war on hate speech in Myanmar]]
- [[Global social networks ranked by number of users 2021|Global social networks ranked by number of users 2021]]
- [[Change in friendship homophily- A German Israeli comparison of adolescent immigrants|Change in friendship homophily: A German Israeli comparison of adolescent immigrants]]
- [[Ethnic boundaries in core discussion networks- A multilevel social network study of Turks and Moroccans in The Netherlands|Ethnic boundaries in core discussion networks: A multilevel social network study of Turks and Moroccans in The Netherlands]]
- [[Facebook Oversight Board’s decision on the indefinite suspension of Donald Trump’s account|Facebook Oversight Board’s decision on the indefinite suspension of Donald Trump’s account]]
- [[Beyond and below racial homophily- ERG models of a friendship network documented on Facebook|Beyond and below racial homophily: ERG models of a friendship network documented on Facebook]]
- [[Preference effects on friendship choice- Evidence from an online field experiment|Preference effects on friendship choice: Evidence from an online field experiment]]
- [[The effects of direct and indirect contact on prejudice- 2007 and 2017 results among Greek Cypriots and Turkish Cypriots|The effects of direct and indirect contact on prejudice: 2007 and 2017 results among Greek Cypriots and Turkish Cypriots]]
- [[The role of inter-ethnic online friendships in prejudice reduction in post-conflict societies- Evidence from Serbia, Croatia and Cyprus|The role of inter-ethnic online friendships in prejudice reduction in post-conflict societies: Evidence from Serbia, Croatia and Cyprus]]

## Audit Log
- Independent source audit passed for the preprint model, published bibliography and bounded supplement captions. Published full text remains unavailable.[^repair]
- The initial audit found incorrect treatment of identity distance and friendship eligibility. The extraction now states source-version limits, explicit state and procedures, selection/discretization gaps, and contradictions in the source's diagram and parameters.[^repair]

## LLM Justification
[^r0]: Abstract copied from the publisher's public record; publication date is first online publication, 22 November 2023. https://journals.sagepub.com/doi/10.1177/08944393231213960
[^scope]: Full model source: arXiv 2109.08862v1, submitted 18 September 2021, all 23 pages. The publisher provides abstract and references but restricts full text. The published version's model rules have not been verified. https://arxiv.org/pdf/2109.08862v1
[^aim]: Preprint, Hypothesis, pp. 7–8, H1–H2; Simulation Design, pp. 8–9. Questions separate the platform comparison from changes in outreachability.
[^state]: Preprint, FIRMAN and Social Identity Distance, pp. 4–6, Equation 1, Figures 1–2; Tie Outreachability and Tie Capacity, pp. 6–7. The notation specializes the general identity space to this study's single binary dimension. Capacity's discrete draw is shown as int because the text does not specify handling of negative draws.
[^rules]: Preprint, Equation 2, p. 6; Simulation Design/Procedure, pp. 8–9; Figure 3 and note, p. 10. Equation 2 uses TC for capacity but Figure 3 prints TO in the friend-count test. The pseudocode displays the equation/prose rule explicitly, not an asserted correction to the diagram. Table 1's F-row lists F as its own friend, whereas Figure 2 and prose describe E–F; the procedure models friendships between different people. Identities and latent abilities are assigned initially; subsequent procedure only forms friendships.
[^observation]: Preprint, Simulation Procedure, p. 9 and Figure 3, p. 10. No observations, subjective estimates or learning state are defined. This describes an omission in this model, not a claim about real people.
[^gaps]: Preprint, Simulation Design, pp. 8–9: discrete capacity generation delegated to source code. Simulation Procedure, p. 9: stochastic initiation/target order without a probability law. Helpers mark these unavailable details; no uniform sampling or rounding rule is inferred.
[^design]: Preprint, Table 2 and trial description, p. 9. The two scenarios change N and mean TC together, leaving their individual effects unidentified; this follows directly from the design.
[^outcomes]: Preprint, Analytic Strategy, p. 10; Figures 5–9, pp. 11–16. Group dyads, individual same-group percentages, and the half-capacity satisfaction proxy are defined here. No zero-degree convention is provided.
[^results]: Preprint, Segregated Friendship Patterns, pp. 11–15, Figures 5–8, Tables 3–4. Increased population/capacity yields more ties, with broadly similar same-group proportions; raising q raises cross-group dyads. This is a simulation result, not evidence of a causal Facebook effect in real users.
[^validation]: Preprint, Hypothesis, p. 8; Simulation Design, p. 8; Validation Using Empirical Data, pp. 13–15. Hofstra et al. (2017) provides the comparison; the preprint explicitly notes its simplification from five minority groups to one. Aggregate agreement alone cannot distinguish competing formation mechanisms.
[^conflicts]: Preprint, Table 2, p. 9 (q=.2,.5,.8); results prose, p. 11 (q=.2,.5,.9); Table 4 and subsequent prose, pp. 14–15 (q=.3/.5/.8, later q=3). Table 4 defines Δ as simulated ratio minus .997, but .997 minus its displayed ratios gives its reported signs. Conflicts are retained; no undocumented code is used to resolve them.
[^limits]: Preprint, Discussion, pp. 16–18: capacity competition explanation; preferences not directly included; Study Limitations explicitly excludes relationship strength and friend suggestions. Conclusion, p. 18: racial/ideological extension proposed. Equations 1–2 and Figure 3 contain reciprocal ties only, no beliefs or feed.
[^bibliography]: Publisher's public References section, 59 entries, checked separately from the preprint's References, pp. 19–23. Links retain the publisher order and titles, with existing vault targets preferred. Published bibliography and abstract do not establish access to the published model text.
[^repair]: Initial audit and source correction described in the existing audit history; the current repair was checked against the complete accessible preprint and visible diagram. Process reports and source hashes are stored under vault/.automation.
[^supplement]: Published supplementary material, pp. 1–2, Figures 10–11 captions: satisfaction thresholds 0.25 and 0.75. Its “Simulation R Codes” section links an anonymous COMSES release that was inaccessible through the source reader. Figure outcomes were not inspected; this statement records the captioned measurement variants only. https://journals.sagepub.com/doi/suppl/10.1177/08944393231213960/suppl_file/sj-pdf-1-ssc-10.1177_08944393231213960.pdf
