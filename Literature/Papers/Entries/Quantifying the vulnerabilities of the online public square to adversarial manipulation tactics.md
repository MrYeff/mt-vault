---
title: "Quantifying the vulnerabilities of the online public square to adversarial manipulation tactics"
authors:
  - "[[Literature/Authors/Bao Tran Truong|Bao Tran Truong]]"
  - "[[Literature/Authors/Xiaodan Lou|Xiaodan Lou]]"
  - "[[Literature/Authors/Alessandro Flammini|Alessandro Flammini]]"
  - "[[Literature/Authors/Filippo Menczer|Filippo Menczer]]"
source: "https://academic.oup.com/pnasnexus/article/3/7/pgae258/7701371"
doi: "10.1093/pnasnexus/pgae258"
publication date: "2024-06-29"
tags:
  - "model"
  - "simulation"
  - "social_media"
read status: Todo
⚠️:
  - audit failed
---

## Abstract

Social media, seen by some as the modern public square, is vulnerable to manipulation. By controlling inauthentic accounts impersonating humans, malicious actors can amplify disinformation within target communities. The consequences of such operations are difficult to evaluate due to the challenges posed by collecting data and carrying out ethical experiments that would influence online communities. Here we use a social media model that simulates information diffusion in an empirical network to quantify the impacts of adversarial manipulation tactics on the quality of content. We find that the presence of hub accounts, a hallmark of social media, exacerbates the vulnerabilities of online communities to manipulation. Among the explored tactics that bad actors can employ, infiltrating a community is the most likely to make low-quality content go viral. Such harm can be further compounded by inauthentic agents flooding the network with low-quality, yet appealing content, but is mitigated when bad actors focus on specific targets, such as influential or vulnerable individuals. These insights suggest countermeasures that platforms could employ to increase the resilience of social media users to manipulation.

## Research Questions
> Research Questions extracted via LLM

- Which adversarial tactics most effectively amplify low-quality content in a modeled online public square?[^r1]
- How do network hubs, infiltration, flooding, and targeting affect content diffusion and quality?[^r1]

## Model
> Model extracted via LLM according to [[Model Notation]]

### What does it represent?
- SimSoM models competing messages circulating through a static directed follower network with authentic accounts and an infiltrating inauthentic subnetwork.[^m1]

### How does it work?
The compact state distinguishes global message attributes from feed-specific engagement and age.[^m1]

```yml
World:
  accounts: [Account]
  messages: [Message]
  infiltration: 0..1
  deception: 0..1
  flooding: 1..64
  target: Random | Hubs | Misinformation | Partisanship | Liberal | Conservative

Account:
  kind: Authentic | Inauthentic
  follows: [AccountId]
  feed: [Entry]

Message:
  quality: 0..1
  appeal: 0..1

Entry:
  message: MessageId
  friend_shares: 0..
  first_seen: f64
```

The main diffusion/quality/convergence settings are fixed in the reported experiments.[^m1][^m2][^m3]

```
POST_PROBABILITY = 0.5
FEED_CAPACITY = 15
QUALITY_EXPONENT = 10
APPEAL_EXPONENT = 4
RECENCY_RATE = 0.4
RECENCY_POWER = 0.4
BAD_ACTOR_SHARE = 0.05
DEFAULT_INFILTRATION = 0.01
DEFAULT_DECEPTION = 0
DEFAULT_FLOODING = 1
QUALITY_SMOOTHING = 0.8
CONVERGENCE_THRESHOLD = 0.0001
REPLICATIONS = 10
```

- An activated account creates a new message with `POST_PROBABILITY`; otherwise it reshares one from its feed. Deliver to followers' feeds, retaining the most recent `FEED_CAPACITY` distinct messages. Follower links point follower→friend; messages move in the reverse direction.[^m1]
- Reshare weights are `appeal * friend_shares * exp(-RECENCY_RATE*age^RECENCY_POWER)`, normalized across the feed. Age is time since first arrival in that feed; engagement counts the posting/resharing by that account's friends. Flooding makes bad actors share θ times, boosting engagement.[^m1]
- Authentic new quality has density `τ*exp(τ*q)/(exp(τ)-1)` on `[0,1]`, τ=`QUALITY_EXPONENT`; appeal independently has density `(1+α)*(1-a)^α`, α=`APPEAL_EXPONENT`. Bad actors create quality zero; with probability ϕ set appeal one, otherwise draw authentic-style appeal.[^m2]
- Add βN bad actors, β=`BAD_ACTOR_SHARE`. Their directed random-walk growth starts with four fully connected nodes; each new node follows three others, using a random friend-of-friend with probability 0.5 for two of them. Bad actors neither follow nor reshare authentic content in this study.[^m4]
- Each authentic account follows each bad actor with probability γ; targeted variants weight this probability by followers, misinformation score, partisanship, or leaning, keeping expected authentic followers per bad actor γN fixed.[^m4]
- The empirical follower graph comes from a 10% random sample of public tweets (June 1–30, 2017), selecting accounts with at least 10 news links including one low-quality source and both partisanship and misinformation attributes. The retained graph has 10,006 accounts in its 94-core; edge sampling preserves the average in/out degree of the original graph and leaves 1,809,798 edges. The “hubs” shuffle preserves degree distribution but destroys clusters; the “clusters” shuffle rewires endpoints within clusters and destroys hubs; the random shuffle destroys both.[^m5]
- Measure the mean quality over all messages in authentic accounts’ feeds, smooth it with an exponential moving average, and stop when relative change falls below `CONVERGENCE_THRESHOLD`. Report end-state quality relative to a no-bad-actor baseline over `REPLICATIONS` random-start runs. Cascade-size distributions include extinct messages; exposure means a message is in an account’s feed when the account activates.[^m3]
- Results: hubs significantly lower relative quality (Mann–Whitney U, p<10⁻³), while clustering alone has no significant effect under random infiltration. At γ=0.1 infiltration alone drives quality below half the no-bad-actor baseline; θ=64 flooding or ϕ=1 deception alone lowers it below 70%. Combining γ=0.1 with either θ=64 or ϕ=1 lowers quality to about 40%, and all three together to 30%. Targeting hubs, misinformation sharers, or partisan groups is less harmful to whole-network quality than random targeting; hub targeting significantly raises average quality (p<10⁻⁴). Exposure cascades are about an order of magnitude larger than reshare cascades; fitted scaling exponents are ν=0.80±0.01 for low-quality and ν=0.56±0.01 for high-quality messages.[^m3][^m4][^m5]
- The model omits search, personalization, platform-specific recommendation algorithms, detailed cognitive behavior, and complex contagion; its results concern modeled feed quality, not opinion consensus or live-platform intervention effects.[^m6]

### What can it answer?
- It compares how infiltration, deception, flooding, targeting, and network structure affect feed quality and cascade reach.[^m3][^m4][^m5]

### Where does it apply?
- It studies modeled information-quality suppression on the sampled network; it does not directly estimate live-platform interventions or opinion consensus.[^m6]

## Metadata
### References
- [[Detectingandtrackingpoliticalabuseinsocialmedia|Detecting and tracking political abuse in social media]]
- [[Socialmediaandtheelections|Social media and the elections]]
- [[Examiningtrollsandpolarizationwitharetweetnetwork|Examining trolls and polarization with a retweet network]]
- [[ActingthepartexamininginformationoperationswithinBlackLivesMatterdiscourse|Acting the part: examining information operations within# BlackLivesMatter discourse]]
- [[Thescienceoffakenews|The science of fake news]]
- [[Anatomyofanonlinemisinformationnetwork|Anatomy of an online misinformation network]]
- [[FakenewsonTwitterduringthe2016USPresidentialelection|Fake news on Twitter during the 2016 U.S. Presidential election]]
- [[Thespreadoflowcredibilitycontentbysocialbots|The spread of low-credibility content by social bots]]
- [[Thespreadoftrueandfalsenewsonline|The spread of true and false news online]]
- [[Theexistentialthreatfromcyberenabledinformationwarfare|The existential threat from cyber-enabled information warfare]]
- [[Theattentioneconomy|The attention economy]]
- [[Howalgorithmicpopularitybiashindersorpromotesquality|How algorithmic popularity bias hinders or promotes quality]]
- [[Quantifyingbiasesinonlineinformationexposure|Quantifying biases in online information exposure]]
- [[UncoveringcoordinatednetworksonsocialmediaMethodsandcasestudies|Uncovering coordinated networks on social media: Methods and case studies]]
- [[Theriseofsocialbots|The rise of social bots]]
- [[Armingthepublicwithartificialintelligencetocountersocialbots|Arming the public with artificial intelligence to counter social bots]]
- [[Socialbotsdistortthe2016USPresidentialelectiononlinediscussion|Social bots distort the 2016 U.S. Presidential election online discussion]]
- [[Influenceofaugmentedhumansinonlineinteractionsduringvotingevents|Influence of augmented humans in online interactions during voting events]]
- [[Disinformationandsocialbotoperationsintherunuptothe2017FrenchPresidentialelection|Disinformation and social bot operations in the run up to the 2017 French Presidential election]]
- [[Identifyingandanalyzingcryptocurrencymanipulationsinsocialmedia|Identifying and analyzing cryptocurrency manipulations in social media]]
- [[Botsincreaseexposuretonegativeandinflammatorycontentinonlinesocialsystems|Bots increase exposure to negative and inflammatory content in online social systems]]
- [[TheroleofbotsquadsinthepoliticalpropagandaonTwitter|The role of bot squads in the political propaganda on Twitter]]
- [[Dissectingasocialbotnetgrowthcontentandinfluenceintwitter|Dissecting a social botnet: growth, content and influence in twitter]]
- [[OntheinfluenceofsocialbotsinonlineprotestspreliminaryfindingsofaMexicancasestudy|On the influence of social bots in online protests: preliminary findings of a Mexican case study]]
- [[Experimentalevidencefortippingpointsinsocialconvention|Experimental evidence for tipping points in social convention]]
- [[Evidenceofcomplexcontagionofinformationinsocialmediaanexperimentusingtwitterbots|Evidence of complex contagion of information in social media: an experiment using twitter bots]]
- [[Tacklingmisinformationwhatresearcherscoulddowithsocialmediadata|Tackling misinformation: what researchers could do with social media data]]
- [[Socialmediaandfakenewsinthe2016election|Social media and fake news in the 2016 election]]
- [[CyberwarhowRussianhackersandtrollshelpedelectapresident|Cyberwar: how Russian hackers and trolls helped elect a president]]
- [[Analyzingthedigitaltracesofpoliticalmanipulationthe2016RussianinterferenceTwittercampaign|Analyzing the digital traces of political manipulation: the 2016 Russian interference Twitter campaign]]
- [[LessthanyouthinkprevalenceandpredictorsoffakenewsdisseminationonFacebook|Less than you think: prevalence and predictors of fake news dissemination on Facebook]]
- [[SocialmediascontributiontopoliticalmisperceptionsinUSPresidentialelections|Social media’s contribution to political misperceptions in U.S. Presidential elections]]
- [[InternetResearchagencytwitteractivitypredicted2016USelectionpolls|Internet Research agency twitter activity predicted 2016 U.S. election polls]]
- [[AssessingtheRussianInternetResearchAgencysimpactonthepoliticalattitudesandbehaviorsofAmericanTwitterusersinlate2017|Assessing the Russian Internet Research Agency’s impact on the political attitudes and behaviors of American Twitter users in late 2017]]
- [[ExposuretotheRussianInternetResearchAgencyforeigninfluencecampaignonTwitterinthe2016USelectionanditsrelationshiptoattitudesandvotingbehavior|Exposure to the Russian Internet Research Agency foreign influence campaign on Twitter in the 2016 US election and its relationship to attitudes and voting behavior]]
- [[TheTacticsandTropesoftheInternetResearchAgency|The Tactics and Tropes of the Internet Research Agency]]
- [[AnatomyofanAIpoweredmalicioussocialbotnet|Anatomy of an AI-powered malicious social botnet]]
- [[ThemanufactureofpartisanechochambersbyfollowtrainabuseonTwitter|The manufacture of partisan echo chambers by follow train abuse on Twitter]]
- [[Measuringemotionalcontagioninsocialmedia|Measuring emotional contagion in social media]]
- [[Supersharersoffakenewsontwitter|Supersharers of fake news on twitter]]
- [[ManipulatingTwitterthroughdeletions|Manipulating Twitter through deletions]]
- [[Shiftingattentiontoaccuracycanreducemisinformationonline|Shifting attention to accuracy can reduce misinformation online]]
- [[Lazynotbiasedsusceptibilitytopartisanfakenewsisbetterexplainedbylackofreasoningthanbymotivatedreasoning|Lazy, not biased: susceptibility to partisan fake news is better explained by lack of reasoning than by motivated reasoning]]
- [[Twittersrecommendationalgorithm|Twitter’s recommendation algorithm]]
- [[Comparinginformationdiffusionmechanismsbymatchingoncascadesize|Comparing information diffusion mechanisms by matching on cascade size]]
- [[Misunderstandingtheharmsofonlinemisinformation|Misunderstanding the harms of online misinformation]]
- [[MeasuringuserinfluenceinTwitterthemillionfollowerfallacy|Measuring user influence in Twitter: the million follower fallacy]]
- [[Neutralbotsprobepoliticalbiasonsocialmedia|Neutral bots probe political bias on social media]]
- [[Designingorganizationsforaninformationrichworld|Designing organizations for an information-rich world]]
- [[Areopagitica|Areopagitica]]
- [[Thewisdomofcrowds|The wisdom of crowds]]
- [[Thedifferencehowthepowerofdiversitycreatesbettergroupsfirmsschoolsandsocieties|The difference: how the power of diversity creates better groups, firms, schools, and societies]]
- [[OntheorganizationoftheUSgovernmentforrespondingtoadversarialinformationwarfareandinfluenceoperations|On the organization of the U.S. government for responding to adversarial information warfare and influence operations]]
- [[Studyingfakenewsspreadingpolarisationdynamicsandmanipulationbybotsataleofnetworksandlanguage|Studying fake news spreading, polarisation dynamics, and manipulation by bots: a tale of networks and language]]
- [[Theproductionofinformationintheattentioneconomy|The production of information in the attention economy]]
- [[Experimentalstudyofinequalityandunpredictabilityinanartificialculturalmarket|Experimental study of inequality and unpredictability in an artificial cultural market]]
- [[Howsocialinfluencecanunderminethewisdomofcrowdeffect|How social influence can undermine the wisdom of crowd effect]]
- [[Networkdynamicsofsocialinfluenceinthewisdomofcrowds|Network dynamics of social influence in the wisdom of crowds]]
- [[Confirmationbiasaubiquitousphenomenoninmanyguises|Confirmation bias: a ubiquitous phenomenon in many guises]]
- [[Thedarksideofinformationproliferation|The dark side of information proliferation]]
- [[Informationgerrymanderingandundemocraticdecisions|Information gerrymandering and undemocratic decisions]]
- [[Friendshipparadoxbiasesperceptionsindirectednetworks|Friendship paradox biases perceptions in directed networks]]
- [[Robustdynamicclassesrevealedbymeasuringtheresponsefunctionofasocialsystem|Robust dynamic classes revealed by measuring the response function of a social system]]
- [[Characterizingandmodelingthedynamicsofonlinepopularity|Characterizing and modeling the dynamics of online popularity]]
- [[Fameemergesasaresultofsmallmemory|Fame emerges as a result of small memory]]
- [[Socialcomputingandtheattentioneconomy|Social computing and the attention economy]]
- [[Noveltyandcollectiveattention|Novelty and collective attention]]
- [[Howlimitedvisibilityanddividedattentionconstrainsocialcontagion|How limited visibility and divided attention constrain social contagion]]
- [[VIPincorporatinghumancognitivebiasesinaprobabilisticmodelofretweeting|VIP: incorporating human cognitive biases in a probabilistic model of retweeting]]
- [[Stardomandtalent|Stardom and talent]]
- [[Thespreadingofmisinformationonline|The spreading of misinformation online]]
- [[Competitionamongmemesinaworldwithlimitedattention|Competition among memes in a world with limited attention]]
- [[Competitioninducedcriticalityinamodelofmemepopularity|Competition-induced criticality in a model of meme popularity]]
- [[Effectsofnetworkstructurecompetitionandmemorytimeonsocialspreadingphenomena|Effects of network structure, competition and memory time on social spreading phenomena]]
- [[Analyticalstudyofqualitybiasedcompetitiondynamicsformemesinsocialmedia|Analytical study of quality-biased competition dynamics for memes in social media]]
- [[Simulatingsocialmediausinglargelanguagemodelstoevaluatealternativenewsfeedalgorithms|Simulating social media using large language models to evaluate alternative news feed algorithms]]
- [[Combininginterventionstoreducethespreadofviralmisinformation|Combining interventions to reduce the spread of viral misinformation]]
- [[Thesimplerulesofsocialcontagion|The simple rules of social contagion]]
- [[Theroleofinflexibleminoritiesinthebreakingofdemocraticopiniondynamics|The role of inflexible minorities in the breaking of democratic opinion dynamics]]
- [[Effectofzealotryinhighdimensionalopiniondynamicsmodels|Effect of zealotry in high-dimensional opinion dynamics models]]
- [[Socialconsensusthroughtheinfluenceofcommittedminorities|Social consensus through the influence of committed minorities]]
- [[Committedactivistsandthereshapingofstatusquosocialconsensus|Committed activists and the reshaping of status-quo social consensus]]
- [[Partisanasymmetriesinonlinepoliticalactivity|Partisan asymmetries in online political activity]]
- [[Rightandleftpartisanshippredictsasymmetricvulnerabilitytomisinformation|Right and left, partisanship predicts (asymmetric) vulnerability to misinformation]]
- [[Theechochambereffectonsocialmedia|The echo chamber effect on social media]]
- [[PoliticalpolarizationonTwitter|Political polarization on Twitter]]
- [[Viralitypredictionandcommunitystructureinsocialnetworks|Virality prediction and community structure in social networks]]
- [[Optimalnetworkmodularityforinformationdiffusion|Optimal network modularity for information diffusion]]
- [[Thedynamicsofnotunfollowingmisinformationspreaders|The dynamics of (not) unfollowing misinformation spreaders]]
- [[Learningthroughthegrapevineandtheimpactofthebreadthanddepthofsocialnetworks|Learning through the grapevine and the impact of the breadth and depth of social networks]]
- [[Mathematicalmodelingofdisinformationandeffectivenessofmitigationpolicies|Mathematical modeling of disinformation and effectiveness of mitigation policies]]
- [[ReconsideringTweetsinterveningduringtweetcreationdecreasesoffensivecontent|Reconsidering Tweets: intervening during tweet creation decreases offensive content]]
- [[FightingCOVID19misinformationonsocialmediaexperimentalevidenceforascalableaccuracynudgeintervention|Fighting COVID-19 misinformation on social media: experimental evidence for a scalable accuracy-nudge intervention]]
- [[Pausingtoconsiderwhyaheadlineistrueorfalsecanhelpreducethesharingoffalsenews|Pausing to consider why a headline is true or false can help reduce the sharing of false news]]
- [[AresponsetofakenewsasaresponsetoCitizensUnited|A response to fake news as a response to Citizens United]]
- [[Aninternetresearchprojectdrawsconservativeire|An internet research project draws conservative ire]]
- [[Epidemicsandrumours|Epidemics and rumours]]
- [[Thegrowingamplificationofsocialmediameasuringtemporalandsocialcontagiondynamicsforover150languagesonTwitterfor20092020|The growing amplification of social media: measuring temporal and social contagion dynamics for over 150 languages on Twitter for 2009–2020]]
- [[Exposuretosocialengagementmetricsincreasesvulnerabilitytomisinformation|Exposure to social engagement metrics increases vulnerability to misinformation]]
- [[ReplicationdataforRightandleftpartisanshippredictsvulnerabilitytomisinformation|Replication data for: Right and left, partisanship predicts vulnerability to misinformation]]
- [[Growingnetworkwithlocalrulespreferentialattachmentclusteringhierarchyanddegreecorrelations|Growing network with local rules: preferential attachment, clustering hierarchy, and degree correlations]]

## Audit Log
- 2026-10-03: Full publisher-source repair corrected publication date, expanded the sampled-network provenance and rewiring controls, added source-reported quality and cascade outcomes, and rebuilt References to all 101 publisher entries in source order. Replaced 43 opaque unresolved targets with verified title-derived links and removed 23 surplus imported items. Warning remains unchanged; independent re-audit pending.
- Audit invalidated (2026-09-30): auditor admitted relying on spot checks and previous reports before clearing flags. A full independent audit is still required.
- 2026-09-30: Full-source design audit found opaque source distributions concealed independent quality/appeal rules; feed-specific engagement/age state omitted; posting/feed/recency/convergence constants omitted; bad-actor growth and non-resharing of authentic messages omitted; targeting fixed-follower control omitted. Corrected against the source passages below; independent re-audit pending.[^design]
- Independent audit found the network/data construction and tactic mechanisms omitted. The note now specifies feed selection, message attributes, sampled follower network and reduction, γ/ϕ/θ tactics, targeting features, and exposure-quality outcomes. At that stage, independent re-audit remained pending.

- WITHDRAWN audit claim (2026-09-30): incomplete source checks; this audit does not establish a pass.

## LLM Justification
[^r1]: The research questions are a concise transformation of the primary source’s abstract and stated aims. Source location: Model and Results sections. Source: [Quantifying the vulnerabilities of the online public square to adversarial manipulation tactics](https://academic.oup.com/pnasnexus/article/3/7/pgae258/7701371).


[^m1]: Methods → Social media diffusion model: static follower→followed links, μ=.5, σ=15, normalized appeal×engagement×recency weights, recency exp(−0.4t^0.4), and θ flooding. New messages are continuously exogenous; diffusion is simple contagion. The paper describes θ as multiplying bad-actor activity/engagement; it does not specify platform ranking or a feed algorithm.

[^m2]: Methods → Quality and appeal supplies exact independent distributions, τ=10, α=4, q=0 bad-actor content and ϕ mixture setting a=1.

[^m3]: Methods → Overall quality, Cascade construction, Simulation framework and parameters; Results, Figures 3–6. Mean feed quality is exponentially smoothed (ρ=.8), stopping at relative change ε=.0001; report end-state relative to a no-bad-actor baseline across ten random-start runs. Cascade plots include extinct cascades; activated accounts with a message in-feed count as exposures. Results report network/tactic quality effects and exposure-vs-reshare scaling.

[^m4]: Methods → Bad-actor subnetwork and Bad-actor targeting tactics; Results/Figure 7. β=.05, four-node seed, outdegree 3, friend-of-friend probability .5, γ links, no authentic following/resharing by bad actors, targeted feature weighting with expected γN followers per bad actor. Results find less whole-network harm under preferential targeting; hub targeting significantly increases average quality (p<10⁻⁴).

[^m5]: Methods → Follower network and Simulation framework: news-sharing sample, 94-core 10006 nodes/1809798 sampled edges, degree/community/random rewiring controls.

[^m6]: Discussion → limitations: omitted search/personalization/cognition/complex contagion; focus is quality suppression rather than opinion consensus.

[^design]: Source audit checked the full text at https://academic.oup.com/pnasnexus/article/3/7/pgae258/7701371. Model footnotes identify the passages supporting the corrections.
