# Research brief: AI, robotics, jobs and distribution (for economic wargame design)

Date of research: 2026-10-03.

**Sourcing.** Figures for 2025–26 come from web searches run today; most were read through search summaries, not primary PDFs. The older academic literature is cited from memory and is well established, but I did not re-check exact figures today. Items marked **[U]** are unverified or single-sourced and should be checked before becoming ground truth.

**Guardrails.** Academic authors are named as citations only. Forecasters are described by role where possible.

---

## A. Jevons paradox and labour

**What it claims.** Jevons (1865) observed that more efficient steam engines raised total coal use, because cheaper effective energy expanded demand more than efficiency cut use per unit. For labour, the analogue is that automation cuts labour per unit of output, so sector employment rises only if output grows by more than labour per unit falls.

**The condition.** Employment in the automating sector rises only if price elasticity of demand for its output is above 1, assuming cost savings pass through to prices. It is a condition, not a law.

**Bessen's inverted U** (Bessen 2019, *Economic Policy*, "Automation and jobs: when technology boosts employment"; NBER w24235, https://www.nber.org/papers/w24235):
- US cotton textiles, steel and autos each saw employment grow for many decades alongside very large productivity gains, then decline.
- In textiles, labour per yard fell by roughly 98% over the 19th century while weaver employment grew.
- Early on, demand was highly elastic because of large unmet need. Once consumption saturated, elasticity fell below 1 and further productivity gains cut jobs.
- Textile and steel employment peaked around the mid-20th century and fell about 90% afterwards (trade also contributed).

**ATMs and bank tellers** (Bessen 2015, *Learning by Doing*):
- Tellers per branch fell from about 20 to about 13 between 1988 and 2004.
- Cheaper branches led to about 43% more urban branches, and teller employment rose from about 500k in 1980 to about 550–600k in 2010.
- The reversal came after 2010 with mobile banking: tellers are now about 350k, and BLS projects further double-digit decline **[U exact figures]**.
- Design lesson: the "Jevons" phase lasted about 30 years and then reversed when a more complete substitute arrived.

**Radiologists.** A 2016 prediction held that they would be obsolete within five years. Instead:
- Residency positions hit a record 1,208 in 2025, vacancy rates are at highs, and average pay is about $520–571k.
- The mechanisms are cheaper and faster reads raising imaging volume, plus regulatory and liability bottlenecks and tasks outside image reading.
- Sources: https://www.understandingai.org/p/ai-isnt-replacing-radiologists and https://fortune.com/2026/05/04/godfather-of-ai-geoffrey-hinton-radiologists-future-of-work-tech-ai-job-anxiety/
- Caveat: supply is licence-restricted, so the wage data partly reflect rationing.

**Translators.** This is a mixed case, and the closest to a counter-example.
- Frey & Llanos-Paredes (2025) find that each 1 pp rise in Google Translate use is associated with 0.71 pp slower translator employment growth, about 28,000 fewer translator jobs over 2010–23. Demand for foreign-language skills fell across occupations. https://www.oxfordmartin.ox.ac.uk/publications/lost-in-translation-artificial-intelligence-and-the-demand-for-foreign-language-skills
- Headline translator employment was still roughly flat or rising through 2023 (NPR Planet Money, 2024).
- Rates and freelance earnings fell **[U magnitude]**.

**Software developers, 2023–26.** This is the live test.
- Indeed software postings are still about 27% below the pre-pandemic baseline and about 69% below the 2022 peak.
- Postings are up about 15% since early 2025, while all postings fell 7%.
- 71% of the May 2025 to May 2026 increase is senior roles, and 37% mention AI in the title. Entry-level postings have not recovered.
- BLS "computer programmers" fell 27.5% over 2023–25, while "software developers" fell 0.3%.
- Source: Indeed Hiring Lab, https://www.hiringlab.org/?p=20708 **[U: read via search summary]**
- Reading: possible early Jevons rebound for senior and AI-complementary work, with the entry rung displaced.

**When it reverses.** Four conditions end the Jevons phase:
1. Demand saturates (food, textiles, eventually cars).
2. The technology moves from partial to complete substitute, so there is no residual human bottleneck task.
3. Savings are kept as margin, not passed to prices (market power).
4. Demand shifts to other sectors, so economy-wide employment depends on new sectors, not the automated one.

The economy-wide version is weaker than the sectoral one. Historically, aggregate employment-to-population did not fall over 150 years of automation, but that relied on humans keeping a comparative advantage in something (see B).

---

## B. Task-based models and the theoretical range

**Acemoglu & Restrepo framework** (JEP 2019, "Automation and New Tasks"). Automation has three effects:
- A displacement effect: tasks shift from labour to capital, cutting the labour share and possibly wages.
- A productivity effect: lower costs raise demand for all inputs.
- A reinstatement effect: new tasks appear where labour has comparative advantage.

Their decomposition finds displacement accelerated and reinstatement slowed after about 1987 compared with 1947–87. "So-so automation" (small productivity gain, full displacement) is the worst case for workers.

**Robots and jobs** (Acemoglu & Restrepo, JPE 2020; US commuting zones, 1990–2007):
- One more robot per 1,000 workers cuts the employment-to-population ratio by about 0.2 pp and wages by about 0.42%.
- That is about 3.3 jobs lost per robot nationally (about 6 locally).
- Contrast: Graetz & Michaels (2018) find productivity gains with no aggregate employment loss across 17 countries. Dauth et al. (2021, Germany) find no net job loss, but fewer manufacturing entry jobs and lower wages for incumbents.

Acemoglu & Restrepo (Econometrica 2022) attribute 50–70% of the change in US wage structure since 1980 to automation of routine tasks.

**"New Frontiers"** (Autor, Chin, Salomons & Seegmiller, QJE 2024):
- About 60% of 2018 US employment was in job titles that did not exist in 1940.
- New work arises from augmenting innovations and demand shocks.
- Since 1980, new work has polarised: high-paid professional and low-paid service, with a hollowed middle. Automation's erosive effect intensified.
- https://www.nber.org/papers/w30389

**Small-effects view** (Acemoglu 2024, "The Simple Macroeconomics of AI"):
- About 20% of tasks are exposed; about 23% of those are profitably automatable in 10 years, giving about 4.6% of tasks; cost savings are about 27%.
- Result: TFP gain of at most 0.66% over a decade (about 0.07 pp a year) and GDP gain of about 1–1.5%.
- No wage gain for low-education workers, and a wider capital–labour gap.
- https://www.nber.org/papers/w32487
- Critics (Aghion & Bunel 2024) get about 0.7–1.3 pp a year with different inputs. Goldman Sachs (2023) projects about 7% on global GDP over a decade and about 1.5 pp a year on US productivity.

**Explosive-growth view.**
- Davidson (Open Philanthropy, 2021/2023), Trammell & Korinek (https://globalprioritiesinstitute.org/philip-trammell-and-anton-korinek-economic-growth-under-transformative-ai) and Erdil & Besiroglu (2023) argue that if AI substitutes for labour in all tasks including R&D, capital accumulation and idea production become self-reinforcing.
- Growth above 30% a year is possible in these models, with the labour share heading towards zero.
- Aghion, Jones & Jones (2019) give the counterweight: with Baumol-style complementarity, growth is limited by the slowest-improving essential tasks.

**Korinek & Suh** (NBER w32255, 2024, "Scenarios for the Transition to AGI"; https://www.nber.org/papers/w32255):
- If the complexity of tasks humans can do is bounded and automation reaches the bound, wages collapse to the cost of the machine substitute.
- If task complexity has an unbounded thick tail, wages can rise indefinitely.
- Wages typically rise and then fall as the last tasks are automated. This is the scarcity-to-abundance switch, and the most useful mechanic for a game.

**"Turing Trap"** (Brynjolfsson, *Daedalus* 2022). Human-like AI substitutes for workers and shifts bargaining power to capital owners; augmenting AI does not. Technologists, firms and tax policy all lean towards substitution.

**Baumol cost disease.** Sectors with slow productivity growth (care, education, health, live services, construction) take a rising share of spending and employment as other things get cheap. This is the main mechanism behind "jobs move to what machines can't do", and behind living costs concentrating in the unautomated basket.

**Comparative-advantage argument and its limits.**
- The claim: even if AI is absolutely better at everything, scarce compute is allocated to its highest-value uses, leaving humans tasks where their relative disadvantage is smallest.
- Limit 1: comparative advantage guarantees some positive market-clearing wage, not a wage above subsistence. Horses kept a comparative advantage, yet the US horse population fell from about 26 million (1915) to about 3 million (1960).
- Limit 2: if compute and robots become abundant and cheap, the human wage is capped at the machine rental cost for the same task.
- Limit 3: humans compete with AI for land and energy.
- Limit 4: transaction, minimum-wage and liability costs can make employing humans not worthwhile.

---

## C. Evidence 2023–2026

**Macro snapshot (US).**
- Unemployment was 4.1% in August 2026, with payrolls up 162k. Participation was 61.6% (down 0.5 pp since January) and employment-to-population was 59.1%. https://thebiggamehunter.us/employment-situation-summary-september-4-2026/ **[U: secondary site; verify against bls.gov]**
- The September report was due on 2 October; I could not retrieve it.
- For reference, September 2025 unemployment was 4.4%.
- Recent graduates (22–27): 5.6% unemployment in March 2026, above the overall rate, which is a historical inversion. Underemployment is about 41.5–42.5% (NY Fed).
- Labour share (nonfarm business) hit a record low of 52.8% in Q2 2026, down from 53.8% in Q3 2025; the series starts in 1947. https://www.bls.gov/opub/ted/2026/labor-share-at-its-lowest-level-52-8-percent-in-second-quarter-2026.htm
- Corporate profit margins are at a record high: about 14.9% of GDP **[U: secondary source]**.
- Productivity grew 1.4% annualised in Q2 2026 and 0.8% in Q1. There is no boom in the aggregate data yet.

**Entry-level effects** (Brynjolfsson, Chandar & Chen, "Canaries in the Coal Mine", ADP payroll data):
- The original (August 2025) found a 13% relative employment decline for 22–25-year-olds in the most AI-exposed occupations.
- The August 2026 update, with data through June 2026, puts the gap at 19%.
- It works through reduced hiring, not separations. Experienced workers are unaffected, and the effect is concentrated where AI use is automating, not augmenting.
- https://digitaleconomy.stanford.edu/app/uploads/2026/08/Canaries_August2026.pdf

**The sceptical counter-evidence.**
- Yale Budget Lab / Brookings tracker: occupational-mix change is within historical range and pre-dates ChatGPT. Exposure measures are unrelated to unemployment changes through March 2026. https://budgetlab.yale.edu/node/1419/pdf
- NY Fed: the hiring divergence by AI exposure began before late 2022.
- Humlum & Vestergaard (2025, Danish administrative data; "Large Language Models, Small Labor Market Effects"): precise zeros on earnings and hours, ruling out effects above 1–2%. Average time saving is about 3%. https://bfi.uchicago.edu/working-paper/large-language-models-small-labor-market-effects/

**Layoffs attributed to AI** (Challenger, Gray & Christmas):
- 54,836 AI-attributed cuts in all of 2025, and 101,743 through June 2026.
- AI was the most-cited reason by May 2026, at about 40% of that month's announced cuts, up from 7% in January.
- https://www.hcamag.com/au/news/general/ai-emerges-as-most-cited-reason-for-job-cuts/578361
- Caveats: Yale Budget Lab flags "AI-washing" (https://fortune.com/2026/02/02/ai-labor-market-yale-budget-lab-ai-washing/). Also, 100k is small against about 1.7 million monthly US layoffs and discharges.

**Freelancers.**
- Hui, Reshef & Zhou (2024): about 2% fewer jobs and about 5% lower earnings for exposed Upwork freelancers after ChatGPT.
- Demirci, Hannane & Zhu (2024): about 21% fewer postings for writing and coding gigs and about 17% fewer for image creation.

**Call centres and productivity studies.**
- Brynjolfsson, Li & Raymond (QJE 2025): about 15% more issues resolved per hour, and about 30% or more for novices (skill compression).
- Noy & Zhang (Science 2023): 40% less time and 18% higher quality on writing tasks.
- Dell'Acqua et al. (2023, consultants): 25% faster and 40% higher quality inside the "jagged frontier", worse outside it.
- Peng et al. (2023): Copilot users 56% faster on a coding task.
- METR (2025) RCT: experienced open-source developers were 19% slower with AI tools while believing they were faster.
- One fintech publicly replaced about 700 agents' worth of support work with AI in 2024 and later partly re-hired humans **[U details]**.

**Adoption.**
- Census BTOS: 17–20% of firms used AI between December 2025 and May 2026. Wording was broadened in November 2025; under the old wording it was about 9–10%.
- By size: 37% of firms with 250+ employees, under 20% of the smallest. https://census.gov/library/stories/2026/05/ai-use-businesses.html
- St. Louis Fed Real-Time Population Survey: generative AI assisted about 6.3% of all work hours in Q2 2026, with self-reported time savings of about 1.4% of total hours. https://fred.stlouisfed.org/series/RPSGENAIASSISTWRKHRSALL
- Anthropic Economic Index: enterprise API use is about 77% automation-pattern, against roughly 50/50 on the consumer app.

**New job categories.** The share of software postings with AI in the title is rising. Roles include AI trainer and evaluator, data labelling, robot teleoperation, data-centre construction and electrical trades, and "forward-deployed" engineers. There is no reliable count **[U]**. WEF (2025) projects 170 million jobs created against 92 million displaced globally by 2030, which is a survey of employers, not a forecast model.

**Net reading.** Aggregate employment is undisturbed. There is a clear and widening hole at the entry rung of exposed occupations. The labour share is falling to records, and productivity is only modestly up. This is consistent with early "displacement at the hiring margin" and with "macro noise plus AI-washing". The game should let either be true.

---

## D. Robotics, state and pace (late 2026)

**Industrial baseline.** IFR reports about 540k industrial robot installations a year and about 4.6 million in operation, with China taking about half of installs **[U: 2024–25 figures from memory]**.

**Humanoids.**
- Unitree shipped more than 5,500 humanoids in 2025 and targets 10–20k in 2026. Its G1 is priced from about $16k.
- Unitree plus AgiBot are projected to take about 80% of 2026 global shipments. One bank projects about 90k units industry-wide in 2026, which looks high against company targets, and about 1.2 million a year later in the decade. https://www.itiger.com/news/1186298418 **[U]**
- Tesla has about 1,000–1,200 Optimus units internally, described by the company as mainly for learning and data collection. There are zero external sales. The claim of 1,000 a week by late 2026 is unverified. https://liveinthefuture.org/stories/humanoid-deployment-gap.html **[U]**
- Figure: two units completed an 11-month BMW pilot (1,250 operating hours, 90k parts). Figure 03 is now doing logistics sequencing.
- Agility Digit: 65,000 cumulative operating hours across nine customer facilities as of May 2026. That is the labour of about 30 full-time workers for a year, in total. https://humanoid.guide/humanoid-deployments-in-2026-favor-figure-and-agility/
- Reading: hardware is cheap and shipping in the low tens of thousands, mostly to labs, for data collection or as demos. Productive commercial humanoid labour is still measured in tens of FTE-equivalents.
- The binding constraints are dexterity, reliability (uptime and MTBF are unpublished), battery life of 2–4 hours, training data for manipulation, safety certification around people, and actuator and rare-earth supply chains.

**Warehouses.**
- Amazon has more than 1 million robots, close to its count of human warehouse workers. Its Vulcan tactile picker handles about 75% of item types.
- Leaked plans reported in 2025 aim to automate about 75% of operations and avoid about 160k US hires by 2027 and about 600k by 2033. That is hires avoided, not layoffs. https://fortune.com/2025/10/22/amazon-just-might-replace-500000-humans-with-robots
- This is the most credible large-scale physical-automation datapoint.

**Autonomous vehicles.**
- Waymo: about 500k paid rides a week (March 2026), about 3,500 vehicles and 10–11 US metros. It targets 1 million rides a week by end-2026 and has announced London and Tokyo. https://www.automotiveworld.com/news/waymos-metric-for-2026-success-one-million-weekly-rides/
- Baidu Apollo Go: a peak of about 350k rides a week across 27 cities, with per-vehicle break-even claimed in its largest city.
- Tesla: about 40 verified unsupervised robotaxis as of June 2026. https://www.electrive.com/2026/06/02/tesla-robotaxi-fleet-in-texas-reaches-only-42-vehicles/
- Scale check: the US has about 3.5 million truck drivers and about 1.5 million or more taxi, rideshare and delivery drivers. Total US ride-hail is on the order of 200–250 million rides a week **[U]**, so robotaxis are under 1% of trips. Growth is about 2–3× a year.
- Driverless trucking (Aurora, Texas) is commercial but tiny.

**Realistic timelines** (my synthesis, for the adjudicator's priors):

| Domain | Timeline |
|---|---|
| Warehouses, structured manufacturing | Substantial labour substitution 2026–2032 |
| Driving | City-by-city; meaningful driver displacement in major metros 2028–2035 |
| Construction | Partial only (layout, drywall finishing, bricklaying, 3D printing, prefab microfactories); general site work unlikely before the mid-2030s |
| Care work | Assistive, not substitutive, through 2035 (safety, liability, acceptance) |
| Skilled trades (electrician, plumber) | Last to go; unstructured environments plus licensing |

The key swing variable is whether "robot foundation models" give a step change in general manipulation, which is high-variance.

---

## E. Distribution

**Labour share.**
- US nonfarm business labour share was about 63–65% from 1947 to 2000, about 56–57% in the 2010s, and 52.8% in Q2 2026.
- Karabarbounis & Neiman (QJE 2014) find a global decline of about 5 pp since 1980, tied to cheaper investment goods.
- Measurement debates over housing, depreciation and proprietors' income shrink the decline but do not erase it.

**Superstar firms.** Autor, Dorn, Katz, Patterson & Van Reenen (QJE 2020) find the labour-share decline is mainly reallocation towards high-markup, low-labour-share firms, with rising concentration in most industries. De Loecker, Eeckhout & Unger (2020) find markups rose from about 1.21 to about 1.61 over 1980–2016 (contested).

**Who owns capital** (Fed Distributional Financial Accounts, Q1 2026):

| Wealth group | Share of corporate equities and mutual funds |
|---|---|
| Top 1% | 50.2% |
| Top 10% | 87.4% |
| 50th–90th percentile | about 11.6% |
| Bottom 50% | about 1.1% |

Source: https://fred.stlouisfed.org/series/WFRBSN09149 (summary via https://pennycalc.com/stock-market-ownership/history/). Implication: if AI shifts 10 pp of national income from labour to capital, almost none of it reaches the bottom half without redistribution. Pension and Social Security claims are the main exception.

**Price declines and real incomes.**
- Roughly, over 2000–2022: TV prices fell about 97%, and toys, software and clothing fell in real terms. Hospital services rose about 200% or more, college tuition about 170–180%, and childcare and housing rose faster than wages (BLS CPI, the "chart of the century") **[U exact]**.
- Low-income households spend about 40% or more of their budget on housing and much of the rest on food, transport and health.
- AI deflation in goods and digital services raises measured real income but does not fix the housing, care or health basket unless those sectors are themselves automated or deregulated. This is Baumol plus supply restriction.

**Engels' pause** (Allen 2009, *Explorations in Economic History*):
- In Britain from about 1800 to 1840, output per worker rose 46% while real wages rose about 12%. The profit share roughly doubled.
- Wages caught up only after about 1840. That means some 40–60 years of flat living standards for workers, amid rapid growth.
- Handloom weavers numbered about 240k around 1820. They saw real earnings fall by more than half over decades and were essentially gone by the 1860s. Adjustment came largely through cohort replacement.

**Other adjustment episodes.**
- US agriculture went from 41% of employment in 1900 to 2% in 2000. It was absorbed over generations, helped by the high-school movement.
- China shock (Autor, Dorn & Hanson): about 1–2.4 million jobs lost, with local employment and income depressed for more than a decade and little out-migration.
- Displaced-worker literature (Jacobson, LaLonde & Sullivan; Davis & von Wachter): long-tenured workers displaced in recessions lose about 15–25% of lifetime earnings.
- Rule of thumb: local adjustment takes 10–20 years, and for mid-career individuals often never.

---

## F. Homelessness and poverty

**Drivers.** Colburn & Aldern (2022, *Homelessness Is a Housing Problem*) show that variation across US metros is explained by rents and vacancy rates. Rates of poverty, addiction, mental illness, weather or benefit generosity do not explain it. Those factors determine who becomes homeless within a tight market, not how many. Supporting evidence: GAO (2020) finds a $100 rise in median rent is associated with about 9% higher homelessness. Glynn & Fox find inflection points where rent exceeds about 32% of income.

**Counts** (HUD point-in-time, one night in January):

| Year | Count | Note |
|---|---|---|
| 2023 | 653,104 | |
| 2024 | 771,480 | +18%, a record |
| 2025 | 745,652 | −3.4%, first fall since 2016 |

- In 2025, 479,332 were sheltered and 266,320 unsheltered.
- Family homelessness fell 11.2%, partly as the migrant-shelter surge unwound. Individual and chronic homelessness were at record highs. About 20% are aged 55 or over.
- Source: https://nlihc.org/resource/hud-2025-annual-homelessness-assessment-report-finds-first-reduction-overall-homelessness
- January 2026 local counts are mixed: Clark County NV up 12% on 2024, Nashville up 5.4%, Chicago shelter counts down but unsheltered up about 25%, Utah down. There is no national 2026 figure yet.

**Poverty.** In 2024 the official rate was about 10.6% and the Supplemental Poverty Measure about 12.9% **[U; the 2025 figures were released in September 2026 and I did not retrieve them]**. The natural experiment: the expanded Child Tax Credit cut SPM child poverty to 5.2% in 2021, and it rebounded to 12.4% in 2022 on expiry. Cash works immediately and reverses immediately.

**What works.**
- Housing First: about 80–90% housing retention at 12–24 months (At Home/Chez Soi RCT in Canada; the Denver supportive-housing RCT, about 77% housed at three years with fewer jail stays). There is little effect on substance use or employment. It needs units to place people in.
- Cash: Vancouver's New Leaf RCT gave a C$7,500 lump sum, producing about 99 fewer days homeless and net savings to the shelter system. The Denver Basic Income Project showed gains in all arms including the low-payment arm, so it is ambiguous.
- Supply: metros that build (Houston, Austin, Minneapolis) show lower rents and lower homelessness for a given level of poverty.
- Federal policy shifted away from Housing First in 2025–26 **[U details]**.

**Could robots and AI cut housing costs?**
- US construction productivity fell about 40% over 1970–2020 while economy-wide productivity roughly doubled or more (Goolsbee & Syverson 2023). Regulation and site fragmentation are implicated (D'Amico, Glaeser et al. 2024).
- Structure cost is about 50–60% of a new home's price nationally, but land plus the regulatory premium dominates in the coastal metros where homelessness concentrates. Gyourko & Krimmel estimate "zoning taxes" of hundreds of thousands of dollars per lot in San Francisco, Los Angeles and Seattle.
- Robotic prefab and 3D printing claim savings of about 20–35% on structure **[U; vendor claims]**.
- So even a 50% cut in construction cost lowers prices by perhaps 25–30% in elastic-supply metros and much less in supply-constrained ones, where savings are capitalised into land values.
- Blockers: zoning and permitting, land, local veto, building codes, trades licensing, financing, and infrastructure hookups.
- A second-order risk: AI wealth concentrates in a few metros and bids up land there.

---

## G. Policy levers and evidence

**Unconditional cash and UBI.**
- OpenResearch (Vivalt, Rhodes, Bartik, Broockman, Miller; NBER w32719, 2024): $1,000 a month for three years to 1,000 low-income adults, against $50 a month for 2,000 controls. Employment fell 2.0 pp and hours fell 1.3 a week (see correction note below). There was no gain in job quality or human capital. Stress fell in year one and the effect faded. Spending rose on basics and on helping others. https://www.nber.org/papers/w32719
- **Correction note:** the search summary reported "3.9 pp" and "$1,800 a year". My memory of the paper is about 2.0 pp and about $1,500 a year. **[U — check the PDF]**
- Alaska Permanent Fund Dividend (about $1–2k per person a year): Jones & Marinescu (2022) find no fall in aggregate employment and part-time work up 1.8 pp.
- Other pilots: Finland 2017–18 (small positive employment effect), Stockton SEED (full-time work up), GiveDirectly Kenya (no labour reduction, with local multipliers of about 2.5).
- Caveat for the game: no pilot tests UBI as wage replacement in a labour market with falling demand, or its fiscal and inflation effects at scale. A $12k-a-year UBI for US adults costs about $3.1 trillion gross, roughly 10% of GDP.

**Wage insurance.** Hyman, Kovak & Leive (2024), on the Trade Adjustment Assistance wage-insurance programme, find faster re-employment and higher cumulative earnings, roughly self-financing. It is effective for a one-step-down transition and useless if there is no next job.

**Retraining.**
- The generic programmes are weak. The WIA Gold Standard evaluation found about zero earnings impact from training vouchers at 30 months. TAA training gains fade after about 10 years (Hyman 2018).
- Sectoral programmes with employer ties (Year Up, Per Scholas, Project QUEST) raise earnings 14–39% in RCTs (Katz, Roth, Hendra & Schaberg 2022). They are small and selective, and their target occupations (IT support, for example) are now AI-exposed.
- Retraining is nonetheless the consensus pick: about 72% of economists in the Forecasting Research Institute survey chose it.

**Job guarantees.**
- Gramatneusiedl, Austria (Kasy & Lehner): eliminated long-term unemployment and produced large wellbeing gains at a cost similar to benefits.
- India's NREGA raised rural wages.
- No large rich-country test exists.

**Shorter working week.** The four-day-week pilots (UK 2022, 61 firms, about 92% continued) are self-selected and uncontrolled. France's 35-hour law showed no clear employment gain (Chemin & Wasmer 2009). It spreads work only if hourly productivity or wage adjustments allow.

**Taxing capital and AI.**
- Acemoglu, Manera & Restrepo (2020): the US taxes labour at about 25–28% effective, against about 5% for equipment and software capital, which biases firms towards automation. Levelling this is the first-best step before any "robot tax".
- Guerreiro, Rebelo & Teles (REStud 2022) and Costinot & Werning (2023): the optimal robot tax is small (low single digits) and transitional.
- South Korea trimmed automation tax credits in 2017. No jurisdiction has a real robot tax.
- Compute and token taxes and windfall clauses are proposals only. Their base is mobile and concentrated in a handful of firms.

**Sovereign funds and dividends.** The Alaska fund is about $80 billion and pays about $1–1.7k a year. Norway's fund is about $1.8–2 trillion, roughly $340k per citizen **[U]**. Proposals for public equity stakes in AI firms follow the same logic.

**Fiscal exposure.**
- Federal receipts in FY2024–25 were about 49–50% individual income tax, about 35% payroll tax and about 10–11% corporate tax.
- Wages are about two-thirds of the individual income tax base, so roughly 65–75% of federal revenue rests on labour income (my estimate **[U]**).
- Social Security and Medicare are funded directly by payroll, so a falling labour share hits them first. Corporate and capital-gains receipts offset this only partly, given lower effective rates and deferral.
- States get about 35–40% of tax revenue from personal income tax and about 30% from sales tax. Local governments get about 70% from property tax. States have balanced-budget rules, so cuts are pro-cyclical.
- Unemployment insurance replaces about 40% of wages for 26 weeks, and trust funds are thin in many states.

---

## H. Expert disagreement and simulation parameters

**Forecast range for about 2030–2036 (US):**

| Camp | Growth | Unemployment / employment | Wages and labour share |
|---|---|---|---|
| Official baselines (CBO-type) | about 1.8–2% | about 4.3–4.5% | Labour share flat |
| Sceptic (Acemoglu 2024) | +0.1 pp a year | Unchanged | Slight rise in inequality |
| Mainstream bank (Goldman Sachs) | +0.3–1.5 pp a year in productivity over a decade | 6–7% of jobs displaced over the adoption period; peak unemployment up about 0.5 pp (about 1 million people) if spread over 10 years, more if front-loaded | Mean wages up; entry-level squeezed |
| Forecasting Research Institute survey, "rapid AI" scenario (economists' median; about 560 respondents, Oct 2025–Feb 2026) | 3.3% by 2030; 3.5% by 2050 | Participation falls from 62% to 54% by 2050 (about 10 million jobs attributed to AI) | — |
| Frontier-lab leadership (public statement, May 2025) | High | 10–20% unemployment within 1–5 years; half of entry-level white-collar jobs gone | — |
| Explosive-growth modellers (Davidson; Trammell & Korinek; Korinek & Suh's AGI scenarios) | 10–30% or more a year in the 2030s | Employment undefined | Wages rise then collapse towards machine cost; labour share heads to zero |

Sources: FRI survey, https://forecastingresearch.substack.com/p/forecasting-the-economic-effects-of-ai; Goldman, https://www.fortune.com/2026/01/13/humans-could-go-the-way-of-horses-goldman-ai-job-apocalypse-unemployment. The unconditional median growth forecast across FRI expert groups was 2.5%. The IMF (2026) has global growth at 3.3% with up to +0.3 pp from AI.

Even inside the economists' "rapid" scenario the adjustment shows up as lower participation, not headline unemployment. The game should track employment-to-population, not only the unemployment rate.

**Parameters to randomise:**

| # | Parameter | Plausible range | Low-end evidence | High-end evidence |
|---|---|---|---|---|
| 1 | Cognitive task automation by 2032 (share of wage bill profitably automatable) | 5% to 60% | Acemoglu's 4.6%; Humlum's null results; METR's slowdown | 77% automation-pattern enterprise use; the Canaries gap widening from 13% to 19% in a year; rapid capability growth |
| 2 | Physical automation lag (years by which general manipulation trails cognitive AI) | 2 to 15+ years | Unitree volumes; $16k hardware; the Amazon plan | About 30 FTE-years of total commercial humanoid work to date; 15 years from AV demos to under 1% of trips |
| 3 | Demand elasticity and saturation in automated sectors | 0.3 to 2.0 by sector, decaying | Bessen post-saturation; translators; tellers after 2010 | Radiology; senior software rebound; early textiles |
| 4 | Reinstatement rate (new-task creation per unit of displacement) | 0.2 to 1.2 | Acemoglu & Restrepo's post-1987 slowdown; AI can also do the new tasks | Autor's 60% new work; WEF net +78 million |
| 5 | Diffusion speed (years from capability to 50% firm adoption) | 3 to 20 | Entrant firms and agent deployment; AI share of layoff announcements rising from 7% to 40% within 2026 | Firm use only 17–20%; electrification took about 30 years |
| 6 | Price pass-through versus margin capture | 20% to 90% of cost savings reach prices | Record margins; superstar concentration; few frontier labs | Fast-falling token prices; open-weight competition |
| 7 | Capital–labour elasticity and labour-share path (2035 labour share) | 30% to 55% | Full-automation models | Baumol bottlenecks keep humans essential; measurement sceptics |
| 8 | Housing and essentials supply response | Real housing cost −30% to +20% by 2035 | Zoning and land capitalisation; construction productivity down 40% over 50 years | Prefab and robotic microfactories plus state pre-emption of zoning |
| 9 | Policy response lag and scale (years from visible displacement to major transfer programme; size as % of GDP) | 1 to 10+ years; 0 to 10% of GDP | The 2020 CARES Act passed in weeks | CTC expiry in 2022; the China shock saw no real response for 15 years |
| 10 | Aggregate-demand feedback (consumption response when income shifts from wage earners to low-spending capital owners) | Multiplier 0.5 to 1.5 on lost wages | The investment boom (data-centre capex) offsets | Top 10% own 87% of equities; states' balanced-budget cuts amplify |

**Optional 11th parameter:** AI-washing share, meaning the fraction of announced "AI layoffs" that are really macro or interest-rate driven (20–80%). It drives how actors misread signals.

**Design implications.**
- The current data fit both a "slow, Jevons-ish" world and an "early-displacement" world. Ground truth should be hidden and drawn from parameters 1–5.
- Outcomes for ordinary people depend at least as much on parameters 6, 8 and 9 (pass-through, housing supply, policy lag) as on technology.
- The Engels' pause precedent makes "strong growth, record profits, flat or falling median living standards for a decade or more" a historically grounded central scenario, not a tail.
- Fiscal stress arrives through payroll-funded programmes and state budgets before it shows in headline GDP.

**Items most in need of primary-source verification:** the August and September 2026 BLS figures; the OpenResearch employment effect (2.0 or 3.9 pp); the 2026 humanoid shipment projections and Tesla production claims; the 2025 poverty rates; total US ride-hail volume; the teller counts; the labour-income share of federal revenue.
