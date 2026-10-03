---

title: "How Does Facebook Retain Segregated Friendship? An Agent-Based Model Approach"
tags:
  - model
  - simulation
authors:
  - "[[Literature/Authors/Firman M. Firmansyah|Firman M. Firmansyah]]"
publication date: 2023-11-22
source:
  - https://doi.org/10.1177/08944393231213960
  - https://arxiv.org/abs/2109.08862
doi: 10.1177/08944393231213960
read status: Todo
⚠️: []
---
## Abstract

Facebook, the largest social networking site in the world, has overcome the structural barriers that historically constrain individuals to reach out to different others. Through the platform, people from all walks of life and virtually any location can develop diverse friendships online. However, friendships on Facebook have been as segregated as friendships in real life. This research sought to understand why the leading social networking site intended to “bring the world closer together” retains segregated friendship. In doing so, I employed a series of agent-based simulations based on the Framework for Intergroup Relations and Multiple Affiliations Networks (FIRMAN). As demonstrated, Facebook has primarily enhanced users’ capacity to maintain a larger number of friendships (tie capacity), but it has done little to empower users’ ability to accept diversity and befriend different others (tie outreachability). Facebook must focus on the latter should they truly wish to contribute to the development of a more inclusive society. While in this study I focus on ethnically segregated friendship on Facebook, I argue that the same explanation might also hold for racially and ideologically segregated friendships on other bidirectional social networking sites.[^r0]

## Research Questions
> Research questions distilled from the primary paper; phrasing is paraphrased.[^r0]
- Why do online friendships remain ethnically segregated despite Facebook reducing geographic and other structural barriers to contact?[^r0]
- How do increased tie capacity and tie outreachability affect segregation in FIRMAN simulations?[^r0]

## Model
> Model extracted via LLM according to [[Model Notation]].

### What does it represent?
- FIRMAN represents people as nodes in social-identity space and reciprocated friendships as ties.[^r1]
- In this study, identity is a binary ethnicity dimension (majority SI=0, minority SI=1; weight w=1). Social-identity distance (w_dist) is the required tie length (LT) in this geometric representation, not a measured friendship strength.[^r1]

### How does it work?
- A tie can form only when w_dist is no greater than the lower of the two agents’ tie-outreachability (TO) values and both agents remain below their tie-capacity (TC).[^r2]
- The stochastic procedure selects an initiator and target; the invitee cannot refuse when the bilateral eligibility and capacity constraints are satisfied. It repeats until no eligible tie can form.[^r2]
- The paper does not specify the probability distribution used to select initiator/target.[^r2]

### What can it answer?
- The design compares offline-like and Facebook-like settings: ethnicity is Bernoulli(p=.22); TO is Bernoulli(q); TC is drawn from a discrete normal distribution (variance .25; means 3 vs 30); and population is 30 vs 300.[^r3]
- Population and TC change together, so their separate effects are not identified. There are 100 trials per condition (600 total).[^r3]
- The methods specify q∈{.2,.5,.8}, while results prose reports {.2,.5,.9}, later uses q=.3, and Table 4 also includes q=.3; these internal inconsistencies are unresolved.[^r3]
- Outcomes include homogeneous/heterogeneous dyad counts, each agent’s share of same-ethnicity friends, and a satisfaction indicator (friends at least half of TC).[^r3]
- The Facebook-like scenarios yield more total ties but no higher cross-group share; increasing outreachability raises that share.[^r3]
- Comparison with Hofstra et al. is the paper’s validation exercise.[^r3]

### Where does it apply?
- The model examines ethnic segregation in reciprocal Facebook friendships.[^r4]
- Extension to racial or ideological segregation on other reciprocal platforms is proposed by the author, not independently tested.[^r4]
- The model abstracts away recommendation/feed mechanisms and represents platform influence through capacity and outreachability parameters.[^r4]

## Metadata
### References
Publisher page lists 59 references; title-based Obsidian links below follow its displayed order. The list is publisher-page-derived; verify aliases against the full paper before treating it as complete.

- [[GenderandprofessionalenetworksImplicationsofgenderheterophilyonjobsearchfacilitationandoutcomes|Gender and professional e-networks: Implications of gender heterophily on job search facilitation and outcomes]]
- [[FosteringdiversefriendshipsTheroleofbeliefsaboutthevalueofdiversity|Fostering diverse friendships: The role of beliefs about the value of diversity]]
- [[TweetingfromlefttorightIsonlinepoliticalcommunicationmorethananechochamber|Tweeting from left to right: Is online political communication more than an echo chamber?]]
- [[PredictinginternationalFacebooktiesthroughculturalhomophilyandotherfactors|Predicting international Facebook ties through cultural homophily and other factors]]
- [[Manhattandistance|Manhattan distance]]
- [[AgentbasedmodelingMethodsandtechniquesforsimulatinghumansystems|Agent-based modeling: Methods and techniques for simulating human systems]]
- [[ThesocialbotnetworkWhenbotssocializeforfameandmoney|The socialbot network: When bots socialize for fame and money]]
- [[FacebookingforgoodOnlinecontacttoaddressofflineconflict|Facebooking for good: Online contact to address offline conflict]]
- [[ThesocialstructureofpoliticalechochambersVariationinideologicalhomophilyinonlinenetworks|The social structure of political echo chambers: Variation in ideological homophily in online networks]]
- [[SchoolfriendshipnetworkshomophilyandmulticulturalismEvidencefromEuropeancountries|School friendship networks, homophily and multiculturalism: Evidence from European countries]]
- [[ExpressingandchallengingracistdiscourseonFacebookHowsocialmediaweakentheSpiralofSilencetheory|Expressing and challenging racist discourse on Facebook: How social media weaken the Spiral of Silence theory]]
- [[Theigraphsoftwarepackageforcomplexnetworkresearch|The igraph software package for complex network research]]
- [[Purityhomophilyinsocialnetworks|Purity homophily in social networks]]
- [[Doonlinesocialmediacutthroughtheconstraintsthatlimitthesizeofofflinesocialnetworks|Do online social media cut through the constraints that limit the size of offline social networks?]]
- [[FAQs|FAQs]]
- [[The Focused Organization of Social Ties|The focused organization of social ties]]
- [[DangerousspeechantiMuslimviolenceandFacebookinMyanmar|Dangerous speech, anti-Muslim violence, and Facebook in Myanmar]]
- [[WhydohomogeneousfriendshipspersistinadiversepopulationMakingsenseofhomophily|Why do homogeneous friendships persist in a diverse population? Making sense of homophily]]
- [[Interracialcontactandchangesintheracialattitudesofwhitecollegestudents|Interracial contact and changes in the racial attitudes of white college students]]
- [[BeyondthecoreWhohaslargersocialnetworks|Beyond the core: Who has larger social networks?]]
- [[SourcesofsegregationinsocialnetworksAnovelapproachusingFacebook|Sources of segregation in social networks: A novel approach using Facebook]]
- [[Thepsychologyoffriendship|The psychology of friendship]]
- [[PoliticalhomophilyinsocialrelationshipsEvidencefromonlinedatingbehavior|Political homophily in social relationships: Evidence from online dating behavior]]
- [[TheimpactofdiversityininformalsocialnetworksontoleranceinJapan|The impact of diversity in informal social networks on tolerance in Japan]]
- [[SimilarityattractioneffectsinfriendshipformationHonestplatoonmatesprefereachotherbutdishonestdonot|Similarity-attraction effects in friendship formation: Honest platoon-mates prefer each other but dishonest do not]]
- [[FearandloathingacrosspartylinesNewevidenceongrouppolarization|Fear and loathing across party lines: New evidence on group polarization]]
- [[AgentbasedmodelingAguideforsocialpsychologists|Agent-based modeling: A guide for social psychologists]]
- [[Schoolracialcompositionandadolescentracialhomophily|School racial composition and adolescent racial homophily]]
- [[Homophilyinfluencesrankingofminoritiesinsocialnetworks|Homophily influences ranking of minorities in social networks]]
- [[AcomputationalstudyofhomophilyanddiffusionofcommonknowledgeonsocialnetworksbasedonamodelofFacebook|A computational study of homophily and diffusion of common knowledge on social networks based on a model of Facebook]]
- [[Genderhomophilyinonlinedyadicandtriadicrelationships|Gender homophily in online dyadic and triadic relationships]]
- [[OnthecognitivebenefitsofculturalexperienceExploringtherelationshipbetweenstudyingabroadandcreativethinking|On the cognitive benefits of cultural experience: Exploring the relationship between studying abroad and creative thinking]]
- [[TeensprivacyandonlinesocialnetworksHowteensmanagetheironlineidentitiesandpersonalinformationintheageofMySpace|Teens, privacy and online social networks: How teens manage their online identities and personal information in the age of MySpace]]
- [[Acasestudyofinternationalstudentssocialadjustmentfriendshipdevelopmentandphysicalactivity|A case study of international students’ social adjustment, friendship development, and physical activity]]
- [[HomogeneityofpersonalvaluesandpersonalitytraitsinFacebooksocialnetworks|Homogeneity of personal values and personality traits in Facebook social networks]]
- [[Everythingyouneedtoknowaboutagentbasedmodellingandsimulation|Everything you need to know about agent-based modelling and simulation]]
- [[Meandmy400friendsTheanatomyofcollegestudentsFacebooknetworkstheircommunicationpatternsandwellbeing|Me and my 400 friends: The anatomy of college students’ Facebook networks, their communication patterns, and well-being]]
- [[PlatformedracismThemediationandcirculationofanAustralianracebasedcontroversyonTwitterFacebookandYouTube|Platformed racism: The mediation and circulation of an Australian race-based controversy on Twitter, Facebook and YouTube]]
- [[WorththeweightConceptualizingandmeasuringstrongversusweaktiehomophily|Worth the weight: Conceptualizing and measuring strong versus weak tie homophily]]
- [[CounteringhatespeechonFacebookThecaseoftheRomaMinorityinSlovakia|Countering hate speech on Facebook: The case of the Roma Minority in Slovakia]]
- [[Residentialsegregationandinterracialfriendshipinschools|Residential segregation and interracial friendship in schools]]
- [[MakenewfriendsorkeeptheoldGenderandpersonalitydifferencesinsocialnetworkinguse|Make new friends or keep the old: Gender and personality differences in social networking use]]
- [[PersonalityhomophilyandgeographicdistanceinFacebook|Personality homophily and geographic distance in Facebook]]
- [[Ishavinganeducationallydiversesocialnetworkgoodforhealth|Is having an educationally diverse social network good for health?]]
- [[ThefilterbubblesWhattheinternetishidingfromyou|The filter bubbles: What the internet is hiding from you]]
- [[WillyoubemyfriendResponsestofriendshiprequestsfromstrangers|Will you be my friend? Responses to friendship requests from strangers]]
- [[TobefriendornotAmodeloffriendrequestacceptanceonFacebook|To befriend or not? A model of friend request acceptance on Facebook]]
- [[ThedifferentialeffectsofraciallyhomophiloussponsorshiptiesonjobopportunitiesinanelitelabormarketThecaseofNCAAbasketballcoaching|The differential effects of racially homophilous sponsorship ties on job opportunities in an elite labor market: The case of NCAA basketball coaching]]
- [[SocialdistanceintheUnitedStatesSexracereligionageandeducationhomophilyamongconfidants1985to2004|Social distance in the United States: Sex, race, religion, age, and education homophily among confidants, 1985 to 2004]]
- [[SocialsimulationinthesocialsciencesAbriefoverview|Social simulation in the social sciences: A brief overview]]
- [[WhyFacebookislosingthewaronhatespeechinMyanmar|Why Facebook is losing the war on hate speech in Myanmar]]
- [[Globalsocialnetworksrankedbynumberofusers2021|Global social networks ranked by number of users 2021]]
- [[ChangeinfriendshiphomophilyAGermanIsraelicomparisonofadolescentimmigrants|Change in friendship homophily: A German Israeli comparison of adolescent immigrants]]
- [[EthnicboundariesincorediscussionnetworksAmultilevelsocialnetworkstudyofTurksandMoroccansinTheNetherlands|Ethnic boundaries in core discussion networks: A multilevel social network study of Turks and Moroccans in The Netherlands]]
- [[FacebookOversightBoardsdecisionontheindefinitesuspensionofDonaldTrumpsaccount|Facebook Oversight Board’s decision on the indefinite suspension of Donald Trump’s account]]
- [[BeyondandbelowracialhomophilyERGmodelsofafriendshipnetworkdocumentedonFacebook|Beyond and below racial homophily: ERG models of a friendship network documented on Facebook]]
- [[PreferenceeffectsonfriendshipchoiceEvidencefromanonlinefieldexperiment|Preference effects on friendship choice: Evidence from an online field experiment]]
- [[Theeffectsofdirectandindirectcontactonprejudice2007and2017resultsamongGreekCypriotsandTurkishCypriots|The effects of direct and indirect contact on prejudice: 2007 and 2017 results among Greek Cypriots and Turkish Cypriots]]
- [[TheroleofinterethniconlinefriendshipsinprejudicereductioninpostconflictsocietiesEvidencefromSerbiaCroatiaandCyprus|The role of inter-ethnic online friendships in prejudice reduction in post-conflict societies: Evidence from Serbia, Croatia and Cyprus]]

## Audit Log
- Initial independent audit failed on 2026-09-30. Corrected weighted social-identity distance versus tie length, the bilateral eligibility/capacity mechanism, and the undisclosed initiator/target selection distribution; documented the q-value discrepancy across methods, results, and Table 4. The publisher bibliography is now represented as source-ordered title links, but alias matching/completeness against the full paper’s reference list remains a limitation. See `vault/.automation/audit/next-fifteen-31-35-initial-2026-09-30.json`.[^r5]

## LLM Justification
[^r0]: Abstract copied verbatim from the publisher record. Research questions are concise paraphrases of the paper’s stated aims/questions. Publisher references were converted to title-based Obsidian links in publisher-page order; alias matching remains to be checked.
[^r1]: Firmansyah, “How Does Facebook Retain Segregated Friendship?,” “FIRMAN,” pp. 4–5, Equation 1. https://arxiv.org/pdf/2109.08862
[^r2]: Firmansyah, “How Does Facebook Retain Segregated Friendship?,” “Reciprocated Friendship Formation,” Equation 2, and “Simulation Procedure,” pp. 5–9. https://arxiv.org/pdf/2109.08862
[^r4]: Firmansyah, “How Does Facebook Retain Segregated Friendship?,” conclusion and discussion, pp. 16–18. https://arxiv.org/pdf/2109.08862
[^r3]: Firmansyah, “How Does Facebook Retain Segregated Friendship?,” “Simulation Design,” Table 2 and “Analytic Strategy,” pp. 8–9; Results, pp. 11–15. https://arxiv.org/pdf/2109.08862
[^r5]: Process log based on the initial audit record and publisher reference list; this is not an independent re-audit.
