---

title: "LLM Agents Grounded in Self-Reports Enable General-Purpose Simulation of Individuals"
tags:
  - model
  - simulation
authors:
  - "[[Literature/Authors/Joon Sung Park|Joon Sung Park]]"
  - "[[Literature/Authors/Zou, Carolyn Q.|Zou, Carolyn Q.]]"
  - "[[Literature/Authors/Kamphorst, Jonne|Kamphorst, Jonne]]"
  - "[[Literature/Authors/Egan, Niles|Egan, Niles]]"
  - "[[Literature/Authors/Aaron Shaw|Aaron Shaw]]"
  - "[[Literature/Authors/Benjamin Mako Hill|Benjamin Mako Hill]]"
  - "[[Literature/Authors/Carrie Jun Cai|Carrie Jun Cai]]"
  - "[[Literature/Authors/Meredith Ringel Morris|Meredith Ringel Morris]]"
  - "[[Literature/Authors/Percy Liang|Percy Liang]]"
  - "[[Literature/Authors/Robb Willer|Robb Willer]]"
  - "[[Literature/Authors/Michael S. Bernstein|Michael S. Bernstein]]"
publication date: "2024-11-15"
source:
  - https://doi.org/10.48550/arXiv.2411.10109
  - https://arxiv.org/pdf/2411.10109
doi: "10.48550/arXiv.2411.10109"
read status: Todo
⚠️: []
---
## Abstract

Machine learning can predict human behavior well when substantial structured data are available for well-defined outcomes. Such models are typically outcome-specific, however, requiring training data for each target outcome, limiting their applicability to new domains. We test whether large language models (LLMs) can relax these requirements by using self-report data to build attitudinal and behavioral simulations, or “generative agents,” that can predict responses across outcomes without outcome-specific training data. Using data from a diverse national sample of 1,052 Americans, we built agents from (i) two-hour, semi-structured interviews elicited using the American Voices Project interview schedule, (ii) structured surveys including General Social Survey items and the Big Five personality inventory, or (iii) both sources combined. On held-out General Social Survey items, interview-only, survey-only, and combined agents achieved accuracies equal to 83%, 82%, and 86% of participants’ own two-week test-retest consistency benchmark, respectively, compared with 74% for demographics-only agents. Combining interviews and surveys produced the highest accuracy, though gains over either source alone were modest, suggesting that predictive benefits from data begin to asymptote once the model has observed sufficient evidence within a domain. We find that these agents also predict personality traits, economic-game behavior, and experimental responses, while reducing accuracy disparities across racial and ideological groups relative to demographics-only agents. Together, these results show that LLM agents grounded in qualitative or quantitative self-reports can support general-purpose simulation of individuals across outcomes, without requiring task-specific training data.[^r1]

## Research Questions
> Research Questions extracted via LLM

- How accurately can self-report-grounded LLM agents reproduce individuals’ held-out attitudes and behavior across outcomes without outcome-specific training data?[^r2]
- How do interview, survey, combined, and demographics-only grounding compare in prediction accuracy and group disparities?[^r2]

## Model
> Model extracted via LLM according to [[Model Notation]]

### What does it represent?
An LLM-based proxy for a sampled individual, grounded in that person’s interview, survey responses, or both, used to predict responses to held-out and cross-domain questions; this is an empirical evaluation of an agent construction procedure, not a theory of social interaction.[^r3]

### How does it work?
- For each participant, interview-only, survey-only, and combined agents receive the relevant self-report data in their prompt. Each agent also stores model-generated expert reflections from four perspectives—psychologist, behavioral economist, political scientist, and demographer—which infer implications beyond what the participant stated directly; at prediction time, the most relevant expert reflections are appended to the self-report input.[^r3]
- GPT-4o produces the agent predictions.[^r3]
- Survey-agent inputs exclude the target GSS question and, for Big Five predictions, all question-answer pairs in the target question’s category; overlapping or near-duplicate GSS evaluation items were also screened out.[^r3]
- Participants completed the surveys and experiments again two weeks later, supplying a test-retest benchmark. Main evaluations cover 150 core GSS questions, Big Five items, five incentivized economic games, and five experimental studies.[^r3]
- Normalized accuracy is an agent’s accuracy divided by that participant’s own two-week replication accuracy; a value of 1 matches the person’s own retest consistency. For continuous outcomes, the analogous metric is normalized correlation.[^r3]
- The paper reports GSS normalized accuracies of 0.83 (interview), 0.82 (survey), 0.86 (combined), and 0.74 (demographics-only). This concise account omits prompt templates, exact settings, and secondary analyses.[^r3]

### What can it answer?
It evaluates how well these agent instances reproduce individual self-reports across GSS items, personality, economic games and experiments relative to test-retest consistency and demographic-only baselines; reported accuracy does not establish reliable forecasts for arbitrary new outcomes.[^r3]

### Where does it apply?
The demonstrated scope is a diverse national sample of 1,052 Americans and the listed held-out outcomes; transfer beyond those tasks and population remains an empirical question.[^r3]

## Metadata
### References
- [[Predicting Results of Social Science Experiments Using Large Language Models]]
- [[Out of one, many: Using language models to simulate human samples]]
- [[Twin-2K-500: A data set for building digital twins of over 2,000 people based on their answers to over 500 questions]]
- [[The Book of Life approach: Enabling richness and scale for life course research]]
- [[Determining the validity of large language models for automated perceptual analysis]]
- [[Using cognitive psychology to understand GPT-3]]
- [[A large-scale replication of scenario-based experiments in psychology and management using large language models]]
- [[LLM social simulations are a promising research method]]
- [[Can Generative AI improve social science?]]
- [[Designing AI-agents with personalities: A Psychometric Approach]]
- [[Measuring the predictability of life outcomes with a scientific mass collaboration]]
- [[Finetuning LLMs for Human Behavior Prediction in Social Science Experiments]]
- [[Specializing Large Language Models to Simulate Survey Response Distributions for Global Populations]]
- [[The Book of Life approach: Enabling richness and scale for life course research]]
- [[Computational social science: past, present, and future]]
- [[Reasoning models generate societies of thought]]
- [[Generative agents: Interactive simulacra of human behavior]]
- [[Large language models cannot replace human participants because they cannot portray identity groups]]
- [[Performance and biases of large language models in public opinion simulation]]
- [[Machine bias: How do generative language models answer opinion polls?]]
- [[Who’s to blame for survey instability: Respondents with nonexistent preferences or researchers with flawed measures?]]
- [[The Mixed Subjects Design: Treating large language models as potentially informative observations]]
- [[The origins of unpredictability in life outcome prediction tasks]]
- [[Listening to People: A Practical Guide to Interviewing, Participant Observation, Data Analysis, and Writing It All Up]]
- [[Learning From Strangers: The Art and Method of Qualitative Interview Studies]]
- [[American Voices Project]]
- [[General Social Survey, 2023]]
- [[The Big Five trait taxonomy: History, measurement, and theoretical perspectives]]
- [[Fairness in simple bargaining experiments]]
- [[Trust, reciprocity, and social history]]
- [[UnresolvedReference31]]
- [[Prisoner’s Dilemma: A Study in Conflict and Cooperation]]
- [[Perceived intent motivates people to magnify observed harms]]
- [[When fairness matters less than we expect]]
- [[Selfish third parties act as peacemakers by transforming conflicts and promoting cooperation]]
- [[Dehumanization increases instrumental violence, but not moral violence]]
- [[Power decreases trust in social exchange]]
- [[Mechanical Turk Replication Project]]
- [[Social Simulacra- Creating Populated Prototypes for Social Computing Systems]]
- [[The Strength of Issues: Using Multiple Measures to Gauge Preference Stability, Ideological Constraint, and Issue Voting]]
- [[Artificial intelligence and illusions of understanding in scientific research]]
- [[CoMPosT: Characterizing and Evaluating Caricature in LLM Simulations]]
- [[UnresolvedReference43]]
- [[Equality of opportunity in supervised learning]]
- [[Fairness and Machine Learning]]
- [[Take caution in using LLMs as human surrogates]]
- [[Questioning the Survey Responses of Large Language Models]]
- [[SimBench: Benchmarking the Ability of Large Language Models to Simulate Human Behaviors]]
- [[Synthetic Replacements for Human Survey Data? The Perils of Large Language Models]]
- [[Which Humans?]]
- [[Representativeness versus Response Quality: Assessing Nine Opt-In Online Survey Samples]]
- [[Agent-Based Models in Empirical Social Research]]
- [[Dynamic models of segregation]]
- [[Growing Artificial Societies: Social Science from the Bottom Up]]
- [[Why agents? On the varied motivations for agent computing in the social sciences]]
- [[Organizational learning and personnel turnover]]
- [[PS-I: A user-friendly agent-based modeling platform for testing theories of political identity and political stability]]
- [[Micromotives and Macrobehavior]]
- [[Agent-based modeling: Methods and techniques for simulating human systems]]
- [[From Factors to Actors: Computational Sociology and Agent-Based Modeling]]
- [[Theory of Games and Economic Behavior]]
- [[Conditional logit analysis of qualitative choice behavior]]
- [[Large language models as simulated economic agents: What can we learn from homo silicus?]]
- [[General Social Surveys, 1972-2020: Cumulative Codebook]]
- [[Survey Methodology]]
- [[InterViews: Learning the Craft of Qualitative Research Interviewing]]
- [[Lost in the middle: How language models use long contexts]]
- [[The Media Equation: How People Treat Computers, Television, and New Media Like Real People and Places]]
- [[Text to speech guide]]
- [[Whisper]]
- [[GPT-4]]
- [[Tracking US Social Change Over a Half-Century: The General Social Survey at Fifty]]
- [[General Social Surveys, 1972-2022: Cumulative Codebook]]
- [[The Big Five Across Time, Space, and Method: A Systematic Review]]
- [[Toward a synthesis of personality, temperament, motivation, emotion and mental health models within the Circumplex of Personality Metatraits]]
- [[Behavioral Game Theory: Experiments in Strategic Interaction]]
- [[Promoting an open research culture]]
- [[Cochrane Handbook for Systematic Reviews of Interventions]]
- [[Averaging correlation coefficients: Should Fisher’s z transformation be used?]]
- [[ChatGPT outperforms crowd workers for text-annotation tasks.]]

All 80 numbered entries in the arXiv v3 bibliography are represented in source order. The source omits a work title for items 31 and 43; these use unresolved links, with raw citations recorded in automation metadata.[^r4]
## Audit Log
Initial independent audit failed because the model account omitted expert reflections and GPT-4o, held-out-input masking, and the normalized test-retest benchmark. These methodological details and the main task set have now been added from the article and supplementary materials. All 80 numbered source references are now represented; two citations lack titles in the source and remain unresolved. Pending independent re-audit.

## LLM Justification
[^r1]: Exact abstract copied from arXiv v3, Abstract, submitted 15 Nov 2024 and revised 28 Jun 2026, [arXiv record](https://arxiv.org/abs/2411.10109).
[^r2]: Questions paraphrase the stated research aim and evaluation comparisons in Abstract and Introduction, [arXiv v3 full text](https://arxiv.org/pdf/2411.10109).
[^r3]: Agent architecture, expert reflections, model, held-out masking, task set, and normalized benchmark from main text pp. 3–6 (Methods and Results); two-week retest schedule from Supplementary Materials §1, pp. 19–20. [arXiv v3 full text](https://arxiv.org/pdf/2411.10109).
[^r4]: Links transcribed in printed order from the arXiv v3 References, pp. 13–17. Items 31 and 43 lack work titles in the source; raw citations are retained in the import automation metadata. [arXiv v3 full text](https://arxiv.org/pdf/2411.10109).
