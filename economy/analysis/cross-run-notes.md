# Cross-run notes — economy series (r1–r5)

All numbers are from the five scorecards, the three 1,000-run dice-only files in `economy/model/`, and the replays saved in this folder (`a-…`, `b-…`, `c-…`, `d-…`, `scorecard-extract.json`). "Adults in work" means the share of all adults who have a job. It is a better measure than the unemployment rate, which only counts people who are still looking.

## Jobs, and the Jevons effect

**Count of jobs.** More jobs were created than destroyed in two games (r1: 47.9m against 37.6m; r3: 22.9m against 19.8m), the two were level in two (r4: 29.6m against 29.5m; r5: 14.2m each), and fewer were created in one (r2: 44.9m against 53.5m).

**Adults in work (2026: 59.1%).** r1 62.7%, r3 60.2%, r5 59.1%, r4 59.0%, r2 56.1%. Unemployment ended between 2.9% and 4.3% everywhere and never rose above 5.3%.

**Where the people in r2 went.** r2 lost 8.6m more jobs than it created, yet unemployment was 4.3%. The scorecard shows why. The number of adults grew by 11.2m. The number in work fell by 2.1m. The number unemployed and looking barely moved (7.0m to 7.2m). The number neither working nor looking rose by 13.1m, from 105.4m to 118.5m. Had the 2026 share still been working there would be 8.7m more people in jobs; essentially all of them are outside the workforce, not on the unemployment count. That happened because employers shrank by hiring freezes and not replacing leavers (only 25–40% of removed jobs became layoffs), and because people who stay unemployed gradually stop looking. Those still in work also worked less: the average week fell from 34.3 to 31.5 hours, so total paid hours fell 9% while the adult population grew 4%. Population growth did not cause the gap; it hid part of it in the raw job count. The model has no ages, so this is not a retirement wave. With hands-off behaviour on the same hand, the same economy shows 10.3% unemployment and 51.0% of adults in work.

**Was it Jevons?** The textbook Jevons effect is: cheaper prices, so people buy more, so there is more work in the same trade. That channel produced 17.7m jobs in r1 and 13.3m in r2, where prices of professional services fell about 12–13%. It produced almost nothing in r3, r4 and r5 (0.03m, 0.03m, 0.07m), because prices did not fall: pay absorbed the savings and AI firms held their prices. In those three games the economy found new work, but the Jevons effect did not operate. Even in r1, office work lost 19.3m jobs and regained 16.1m. In every game office employment fell (by 1.3m to 8.9m) and the growth was in new industries, care and building. New kinds of work supplied 53–85% of all jobs created.

Verdict: held for the whole economy in r1 only, and even there not for office workers; "the economy found new work without Jevons" in r3, r4 and r5; failed in r2.

## Living standards

Typical (median) household income after prices rose in all five: +35%, +21%, +27%, +30%, +16% (the no-AI trend is about +9%). The poorest fifth: +33%, +19%, +22%, +36%, +15%. Poverty fell from 12.9% to 6.9–9.7%. Homelessness fell from 22 per 10,000 to 12–15. Housing got 8–24% cheaper in every game; health care did not get cheaper in any; goods and professional services got cheaper only in r1 and r2.

The split moved towards owners in every game. Workers' share of national income fell from 52.8% to between 50.7% (r5) and 38.8% (r2). The top 1% share rose from 20% to between 20.8% and 25.8%. Federal deficits ended between 4.0% and 6.0% of GDP (6.0% at the start); debt ended between 90% and 118% of GDP. In r2 revenue slid from 17.3% to 16.0% of GDP as the wage tax base shrank.

## Luck, choices, structure

**The hands were kind.** The condition that matters most for jobs, how much new human work appears, was drawn in the upper part of its range in four of five games and never low (45th to 87th percentile). Housing was easy to build in four of five. Lost wages snowballed in only one. Against the 1,000 dice-only runs with default behaviour, the played games' share of adults in work sits at the 100th, 20th, 98th, 81st and 83rd percentile; typical income at the 83rd or higher in all five; homelessness in the best 6% in all five. In dice-only runs, jobs created exceed jobs destroyed in about 16% (default), 14% (hands-off) and 55% (active policy); typical income ends below 2026 in 10%, 20% and under 1%; unemployment ends above 8% in 2%, 15% and under 1%. (The model README's "9%" for the hands-off case does not match its own file; 15% is what the file gives.)

**What choices added on the same hand.** Replaying each hand with hands-off behaviour and the same events: adults in work 62.7 / 51.0 / 56.4 / 58.6 / 58.2% (played: 62.7 / 56.1 / 60.2 / 59.0 / 59.1); typical income 129 / 99 / 116 / 132 / 110 (played 135 / 121 / 127 / 130 / 116); homelessness 16–21 per 10,000 (played 12–15). Choices mattered little on the kindest hands and a great deal on the hardest.

**The same decisions on a harsher hand.** With the economy's response at about its 20th percentile and each game's own technology speed, the players' actual decisions give: adults in work 50.5–55.3% (a fall of four to nine points), 0.5–0.7 jobs created per job destroyed, unemployment 4.8–6.2%, typical income between 11% lower and level with 2026, top 1% share 25–28%. Hands-off behaviour on that hand gives 9–14% unemployment, 45–52% of adults in work and typical income 14–28% lower. On an all-median hand the players' decisions give 58.0–61.3% in work and typical income +15–21%.

**What separates good from bad runs:** new kinds of work (jobs), how freely housing can be built (living standards and homelessness), then how fast desk-work AI improves and is adopted.

## How much to trust this

The model is a simple accounting model with stated assumptions; it has no regions, ages, finance or trade. Five games is a small sample and they were lucky. All players were AI agents from one model family and were unusually cooperative: no mass layoffs, no strikes, AI firms accepting levies. Rapid AI progress was assumed, not tested. The replays hold decisions fixed, which real players would not do. Treat the direction of the findings as suggestive and the numbers as illustrations.
