#!/usr/bin/env python3
"""Economy Games model: plain accounting of jobs, incomes, prices, housing and
public finances under rapidly improving AI and robotics (US, 2026-2036).

Every constant below is documented in economy/model/README.md with its source
in economy/research/econ-brief.md (or flagged as the author's assumption).
Python 3 standard library only.

  econ.py init --run <RUN> --seed <N>
  econ.py step --run <RUN> --levers <file.json> --years <1|2> --label <period>
  econ.py montecarlo --n 1000 --policy <default|laissez|active> --out <csv>
  econ.py sensitivity [--n 600]
  econ.py selftest
"""
import argparse
import csv
import json
import math
import os
import random
import sys

# ----------------------------------------------------------------------------
# 1. Fixed structure (see README "Fixed constants")
# ----------------------------------------------------------------------------
SECTORS = ["office", "care", "retail", "manuf", "logistics", "construction", "neweco"]
SECTOR_NAMES = {
    "office": "office and professional work",
    "care": "health, care and education",
    "retail": "retail and hospitality",
    "manuf": "manufacturing",
    "logistics": "logistics and transport",
    "construction": "construction and trades",
    "neweco": "new-economy and other work",
}
# Employment, millions, late 2026 (sums to 162.4 = 59.1% of 274.8m adults).
EMP0 = {"office": 48.0, "care": 38.0, "retail": 34.0, "manuf": 12.8,
        "logistics": 11.0, "construction": 14.0, "neweco": 4.6}
# Share of each sector's work that is cognitive / physical (rest is in-person
# human contact that the model never automates).
COG = {"office": 0.80, "care": 0.30, "retail": 0.25, "manuf": 0.25,
       "logistics": 0.20, "construction": 0.15, "neweco": 0.50}
PHY = {"office": 0.02, "care": 0.35, "retail": 0.50, "manuf": 0.65,
       "logistics": 0.70, "construction": 0.75, "neweco": 0.20}
# How much of the automatable frontier applies in the sector (licensing,
# liability, unstructured environments). Brief section D timeline table.
COG_EASE = {"office": 1.0, "care": 0.6, "retail": 0.9, "manuf": 1.0,
            "logistics": 1.0, "construction": 0.8, "neweco": 0.8}
PHY_EASE = {"office": 0.5, "care": 0.2, "retail": 0.6, "manuf": 1.0,
            "logistics": 0.9, "construction": 0.35, "neweco": 0.5}
# Relative pay per worker (economy average about 1).
WAGE_REL = {"office": 1.35, "care": 0.95, "retail": 0.55, "manuf": 1.05,
            "logistics": 0.90, "construction": 1.05, "neweco": 1.30}
# Labour's share of each sector's costs.
LS_SEC = {"office": 0.70, "care": 0.75, "retail": 0.55, "manuf": 0.45,
          "logistics": 0.55, "construction": 0.55, "neweco": 0.45}
# Sector multiplier on the demand-response (Jevons) parameter.
ELAS_F = {"office": 1.0, "care": 1.1, "retail": 0.7, "manuf": 0.6,
          "logistics": 0.8, "construction": 1.2, "neweco": 1.3}
# Where spending freed by cheaper things goes (Baumol: mostly services).
SPILL_W = {"office": 0.12, "care": 0.28, "retail": 0.25, "manuf": 0.08,
           "logistics": 0.05, "construction": 0.12, "neweco": 0.10}
# Where genuinely new kinds of work appear.
NEW_W = {"office": 0.15, "care": 0.20, "retail": 0.12, "manuf": 0.04,
         "logistics": 0.04, "construction": 0.10, "neweco": 0.35}
# Where slack labour is slowly re-absorbed at lower pay.
ABSORB_W = {"office": 0.0, "care": 0.30, "retail": 0.40, "manuf": 0.0,
            "logistics": 0.0, "construction": 0.15, "neweco": 0.15}
# Where public-employment jobs sit.
PUBLIC_W = {"office": 0.2, "care": 0.5, "retail": 0.0, "manuf": 0.0,
            "logistics": 0.0, "construction": 0.3, "neweco": 0.0}
# Sensitivity of sector jobs to swings in total spending.
DSENS = {"office": 0.8, "care": 0.5, "retail": 1.5, "manuf": 1.2,
         "logistics": 1.1, "construction": 1.3, "neweco": 1.0}

START_YEAR = 2026
A_C0, A_P0 = 0.06, 0.03          # automatable shares, late 2026
AUTO_C0, AUTO_P0 = 0.015, 0.010  # actually automated shares, late 2026
A_PRE_SLOPE = 0.015              # pre-2026 cognitive frontier growth per year
A_MAX = 0.90                     # ceiling on automatable share
ROBOT_DIFFUSION = 0.8            # hardware rolls out slower than software
COST_SAVING = 0.60               # machine does the task for 40% of the wage
SATURATION = 1.0                 # demand response halves per 50% price fall
LEAK = 0.7                       # share of unspent savings that makes no jobs (land, saving, dearer services)
LEAK_BUILD = 0.5                 # share of leaked spending that becomes building where supply allows
LEAK_RENT = 0.5                  # how strongly that leak bids up rents
HOUSING_SPEND_SHARE = 0.15       # housing as share of total spending
CARE_PT = 0.5                    # care passes on half as much of its savings
NEW_TASK_SMOOTH = 0.5            # new work follows displacement with ~2y lag
EROSION_EXP = 0.2                # new work gets scarcer as machines can do more
ABSORB_RATE = 0.08               # slack re-absorbed per year (10-20y adjustment)
DISCOURAGE = 0.15                # excess unemployed leaving labour force / yr (cyclical history ~0.08-0.10)
UI_REPLACE = 0.25                # share of lost wages covered automatically
POP_GROWTH = 0.004               # adults, per year
TREND = 0.010                    # non-AI productivity and wage growth per year
EP0 = 0.591                      # employment-to-population, Aug 2026
U_RATE0 = 0.041                  # unemployment rate, Aug 2026
U_FLOOR = 0.03                   # frictional floor
RESERVE = 0.03                   # adults who would work if jobs appeared
HOURS0 = 34.3                    # average weekly hours
LS0 = 0.528                      # labour share, Q2 2026
PROFIT0 = 14.9                   # corporate profits % GDP
WAGE_PER_EP_PP = 0.021           # wage level lost per pp of E/P lost
TOP1_OF_LABOUR, TOP1_OF_CAPITAL = 0.08, 0.335   # gives 20.0% at baseline
TOP1_OF_NEW_CAPITAL = 0.50       # top 1% hold 50.2% of equities
MED_MIX = {"labour": 0.78, "transfers": 0.15, "capital": 0.07}
B20_MIX = {"labour": 0.45, "transfers": 0.50, "capital": 0.05}
MED_GDP_SHARE, B20_GDP_SHARE = 0.105, 0.040  # group income as share of GDP
BASKET_MED = {"goods": 0.30, "digital": 0.10, "health": 0.15, "housing": 0.33, "other": 0.12}
BASKET_B20 = {"goods": 0.33, "digital": 0.05, "health": 0.08, "housing": 0.42, "other": 0.12}
POVERTY0, POVERTY_ELAS = 12.9, 2.0
HOMELESS0 = 22.0                 # per 10,000 people
REV_LABOUR0, REV_CAPITAL0 = 12.1, 5.2   # federal revenue % GDP (sum 17.3)
SPEND0 = 23.3
DEBT0 = 100.0
SPEND_GDP_EXP = 0.5
CAPTAX_COLLECT = 0.6
TRANSFER_EXIT = 0.002            # share of adults leaving work per 1% GDP
WORKTIME_JOBS = 0.2              # jobs gained per unit of hours cut
UNREST0 = 35.0

# ----------------------------------------------------------------------------
# 2. Hidden parameters sampled once per run
# ----------------------------------------------------------------------------
# name: (low, high, distribution, plain description)
PARAM_SPEC = {
    "cog_auto_2032": (0.25, 0.60, "uniform",
                      "share of desk-work pay that machines could profitably do by 2032"),
    "robot_lag_years": (2.0, 8.0, "uniform",
                        "years by which general-purpose robots trail desk-work AI"),
    "jevons": (0.3, 2.0, "uniform",
               "how strongly cheaper goods and services make people buy more of them"),
    "new_task_rate": (0.2, 1.2, "uniform",
                      "new kinds of human jobs appearing per job automated away"),
    "diffusion_t50": (3.0, 20.0, "loguniform",
                      "years for half of firms to adopt what the technology can do"),
    "passthrough": (0.2, 0.9, "uniform",
                    "share of cost savings that reaches customers as lower prices"),
    "wage_share": (-0.3, 0.6, "uniform",
                   "share of the automation cost saving that goes to pay (0.6 = all of it; negative: pay of remaining workers is bid down)"),
    "housing_supply": (0.0, 1.0, "uniform",
                       "how freely housing supply can expand (0 blocked, 1 builds freely)"),
    "demand_mult": (0.5, 1.5, "uniform",
                    "spending lost per dollar of wages lost"),
    "policy_lag_years": (1.0, 10.0, "loguniform",
                         "years between visible job losses and a major federal response"),
    "policy_scale_pct": (0.0, 10.0, "triangular:3",
                         "size of that eventual response, % of GDP (dice-only runs)"),
}
CAPABILITY_PARAMS = ["cog_auto_2032", "robot_lag_years"]


def sample_params(seed):
    rng = random.Random(seed)
    p = {"seed": seed, "noise": 1.0}
    for name, (lo, hi, dist, _) in PARAM_SPEC.items():
        if dist == "uniform":
            v = rng.uniform(lo, hi)
        elif dist == "loguniform":
            v = math.exp(rng.uniform(math.log(lo), math.log(hi)))
        else:
            v = rng.triangular(lo, hi, float(dist.split(":")[1]))
        p[name] = round(v, 4)
    return p


def mid_params():
    """Mid-range value of every parameter (used by selftest and sensitivity)."""
    p = {"seed": 0, "noise": 0.0}
    for name, (lo, hi, dist, _) in PARAM_SPEC.items():
        if dist == "loguniform":
            p[name] = math.sqrt(lo * hi)
        elif dist.startswith("triangular"):
            p[name] = float(dist.split(":")[1])
        else:
            p[name] = (lo + hi) / 2
    return p


def band(name, v):
    lo, hi, dist, _ = PARAM_SPEC[name]
    if dist == "loguniform":
        f = (math.log(v) - math.log(lo)) / (math.log(hi) - math.log(lo))
    else:
        f = (v - lo) / (hi - lo)
    return "low" if f < 1 / 3 else "middle" if f < 2 / 3 else "high"


def politics_label(p):
    lag = p["policy_lag_years"]
    if lag < 2.5:
        return "responsive"
    if lag < 5.5:
        return "divided"
    return "gridlocked"


def describe_params(p):
    words = {
        "cog_auto_2032": {"low": "desk-work AI is fast", "middle": "desk-work AI is very fast",
                          "high": "desk-work AI is extremely fast"},
        "robot_lag_years": {"low": "robots arrive early (2-4 years behind desk AI)",
                            "middle": "robots arrive mid-period (4-6 years behind)",
                            "high": "robots arrive late (6-8 years behind)"},
        "jevons": {"low": "people do NOT buy much more when things get cheaper (weak Jevons)",
                   "middle": "people buy moderately more when things get cheaper",
                   "high": "cheaper things unlock a lot of new demand (strong Jevons)"},
        "new_task_rate": {"low": "few new kinds of human work appear",
                          "middle": "some new kinds of human work appear",
                          "high": "many new kinds of human work appear"},
        "diffusion_t50": {"low": "firms adopt quickly", "middle": "firms adopt at a moderate pace",
                          "high": "firms adopt slowly"},
        "passthrough": {"low": "firms keep most savings as profit",
                        "middle": "savings are split between prices and profit",
                        "high": "competition passes most savings to customers"},
        "wage_share": {"low": "pay barely shares in productivity gains",
                       "middle": "pay shares partly in productivity gains",
                       "high": "pay shares well in productivity gains"},
        "housing_supply": {"low": "housing supply is blocked (zoning, land)",
                           "middle": "housing supply responds partly",
                           "high": "housing can be built freely and cheaply"},
        "demand_mult": {"low": "investment booms cushion lost wages",
                        "middle": "lost wages reduce spending roughly one for one",
                        "high": "lost wages snowball into wider spending cuts"},
        "policy_lag_years": {"low": "Washington can act within a couple of years",
                             "middle": "Washington is divided and slow",
                             "high": "Washington is gridlocked"},
        "policy_scale_pct": {"low": "any federal response would be small",
                             "middle": "a federal response would be medium-sized",
                             "high": "a federal response could be very large"},
    }
    lines = []
    for name in PARAM_SPEC:
        b = band(name, p[name])
        lines.append(f"- {words[name][b]}  [{name} = {p[name]:.3g}, {b} third of range]")
    lines.append(f"- starting political configuration: {politics_label(p)}")
    return "\n".join(lines)


# ----------------------------------------------------------------------------
# 3. Levers set by the referee each round
# ----------------------------------------------------------------------------
# name: (low, high, default, kind, who, meaning)   kind: level | shock
LEVER_SPEC = {
    "deploy_pace": (0.7, 1.3, 1.0, "level", "ai-firms",
                    "speed at which AI and robot makers release and scale new capability (1 = baseline)"),
    "ai_pricing": (-1.0, 1.0, 0.0, "level", "ai-firms",
                   "-1 = price for maximum margin, +1 = price war; moves pass-through by 0.15"),
    "adoption_speed": (0.5, 1.6, 1.0, "level", "employers",
                       "how hard employers push automation into their operations (1 = baseline)"),
    "layoff_share": (0.2, 0.9, 0.6, "level", "employers",
                     "share of removed jobs done by layoff (rest by not replacing leavers / not hiring)"),
    "hours_share": (0.0, 0.5, 0.1, "level", "employers",
                    "share of labour saving taken as shorter hours instead of fewer jobs"),
    "wage_sharing": (-0.1, 0.3, 0.0, "level", "employers",
                     "extra share of productivity gains paid out as wages"),
    "new_business": (0.75, 1.3, 1.0, "level", "entrepreneurs",
                     "rate of new-business and new-job-type formation (1 = baseline)"),
    "union_pressure": (0.0, 1.0, 0.0, "level", "households",
                       "organised worker pressure: lifts pay share by up to 0.15, slows adoption by up to 15%"),
    "household_saving": (-0.03, 0.05, 0.0, "level", "households",
                         "change in household saving rate vs 2026 (precaution cuts spending)"),
    "transfers_pct_gdp": (0.0, 10.0, 0.0, "level", "federal-gov",
                          "new cash transfers / basic income, % of GDP per year"),
    "transfer_target": (0.0, 1.0, 0.0, "level", "federal-gov",
                        "0 = same cheque for everyone, 1 = aimed at the bottom two-fifths"),
    "capital_tax_pct": (0.0, 30.0, 0.0, "level", "federal-gov",
                        "extra tax on capital / AI profits, percentage points"),
    "retraining_pct_gdp": (0.0, 1.0, 0.0, "level", "federal-gov",
                           "NEW retraining and wage-insurance spending beyond 2026 programmes, % of GDP"),
    "public_jobs_m": (0.0, 8.0, 0.0, "level", "federal-gov",
                      "public employment / job guarantee, millions of jobs"),
    "worktime_cut_pct": (0.0, 15.0, 0.0, "level", "federal-gov",
                         "legislated cut in the standard working week, %"),
    "deploy_regulation": (0.0, 1.0, 0.0, "level", "federal-gov",
                          "restrictions on deployment (licensing, human-in-the-loop); 1 halves adoption speed"),
    "competition_policy": (0.0, 1.0, 0.0, "level", "federal-gov",
                           "antitrust / open-access enforcement; 1 adds 0.15 to pass-through"),
    "housing_policy": (0.0, 1.0, 0.0, "level", "federal-gov+states",
                       "zoning pre-emption, building programme, Housing First; 1 adds 0.4 to housing supply"),
    "shock_frontier_cog": (-0.05, 0.05, 0.0, "shock", "events",
                           "one-off jump in automatable desk-work share"),
    "shock_robot_lag_years": (-2.0, 2.0, 0.0, "shock", "events",
                              "one-off change in how far robots trail (negative = sooner)"),
    "shock_adoption": (0.6, 1.4, 1.0, "shock", "events",
                       "multiplier on adoption speed this round only"),
    "shock_demand_pct": (-4.0, 2.0, 0.0, "shock", "events",
                         "outside swing in total spending this round, % of GDP"),
    "shock_housing_pct": (-5.0, 5.0, 0.0, "shock", "events",
                          "one-off change in real housing costs, %"),
    "shock_new_task": (0.6, 1.6, 1.0, "shock", "events",
                       "multiplier on new-work creation this round only"),
}


def default_levers():
    return {k: v[2] for k, v in LEVER_SPEC.items()}


def validate_levers(given, prev):
    """Return (levers, notes). Missing level levers carry over; shocks reset."""
    out, notes = {}, []
    for k in given:
        if k not in LEVER_SPEC:
            raise ValueError(f"unknown lever '{k}'. Valid: {', '.join(LEVER_SPEC)}")
    for k, (lo, hi, dflt, kind, _, _) in LEVER_SPEC.items():
        if k in given:
            v = float(given[k])
            if not (lo - 1e-9 <= v <= hi + 1e-9):
                raise ValueError(f"lever '{k}'={v} outside allowed range [{lo}, {hi}]")
            out[k] = v
        elif kind == "level":
            out[k] = prev.get(k, dflt)
            if out[k] != dflt:
                notes.append(f"{k} carried over at {out[k]}")
        else:
            out[k] = dflt
    return out, notes


# ----------------------------------------------------------------------------
# 4. State
# ----------------------------------------------------------------------------
def clip(x, lo, hi):
    return max(lo, min(hi, x))


def sector_u(a_c, a_p, s):
    return COG[s] * COG_EASE[s] * a_c + PHY[s] * PHY_EASE[s] * a_p


def a_hist(st, t):
    """Automatable desk-work share at (possibly fractional, possibly past) year t."""
    if t <= START_YEAR:
        return max(0.0, A_C0 - A_PRE_SLOPE * (START_YEAR - t))
    lo = int(math.floor(t))
    hi = lo + 1
    h = st["A_hist"]
    a_lo = h.get(str(lo), a_hist(st, lo) if lo <= START_YEAR else st["A_c"])
    a_hi = h.get(str(hi), st["A_c"])
    return a_lo + (a_hi - a_lo) * (t - lo)


def new_state(p):
    total = sum(EMP0.values())
    pop = total / EP0
    lf = total / (1 - U_RATE0)
    prod = {s: WAGE_REL[s] / LS_SEC[s] for s in SECTORS}
    y_raw = sum(EMP0[s] * prod[s] for s in SECTORS)
    prod = {s: prod[s] * 100.0 / y_raw for s in SECTORS}
    st = {
        "year": START_YEAR, "rounds": 0,
        "A_c": A_C0, "A_p": A_P0, "a_c": AUTO_C0, "a_p": AUTO_P0,
        "A_hist": {str(START_YEAR): A_C0},
        "lag": p["robot_lag_years"],
        "A_floor": max(0.0, A_C0 - A_PRE_SLOPE * p["robot_lag_years"]),
        "emp": dict(EMP0),
        "u": {s: sector_u(AUTO_C0, AUTO_P0, s) for s in SECTORS},
        "prod": prod,
        "cumx": {s: 0.0 for s in SECTORS},
        "price": {s: 1.0 for s in SECTORS},
        "rent": 1.0,
        "pop": pop, "U": lf - total, "disc": 0.0, "reserve": RESERVE * pop,
        "w_core": 1.0, "wage": 1.0, "hours": HOURS0,
        "D_smooth": 0.0, "cum_destroyed": 0.0, "cum_created": 0.0,
        "Y": 100.0, "debt": DEBT0, "unrest": UNREST0,
        "prev_levers": default_levers(),
        "wagebill0": sum(EMP0[s] * WAGE_REL[s] for s in SECTORS),
        "ls": LS0,
        "pop0": pop,
    }
    return st


def blank_flows():
    f = {"destroyed": {s: 0.0 for s in SECTORS}, "created": {s: 0.0 for s in SECTORS},
         "trend": 0.0, "vol_exit": 0.0, "unfilled": 0.0}
    for ch in ("d_automation", "d_demand", "d_shift", "d_policy",
               "c_price", "c_shift", "c_newwork", "c_absorb", "c_demand", "c_policy"):
        f[ch] = 0.0
    return f


def hire(st, n):
    """Fill n jobs from the unemployed, the discouraged and the reserve. Returns filled."""
    if n <= 0:
        return 0.0
    lf = sum(st["emp"].values()) + st["U"]
    pools = {"U": max(0.0, st["U"] - U_FLOOR * lf), "disc": st["disc"], "reserve": st["reserve"]}
    weight = {"U": 2.0, "disc": 1.0, "reserve": 0.5}
    need, filled = n, 0.0
    for _ in range(4):
        tot = sum(weight[k] * pools[k] for k in pools)
        if tot <= 1e-12 or need <= 1e-12:
            break
        take_total = 0.0
        for k in pools:
            take = min(pools[k], need * weight[k] * pools[k] / tot)
            pools[k] -= take
            st[k] -= take
            take_total += take
        need -= take_total
        filled += take_total
    return filled


# ----------------------------------------------------------------------------
# 5. One year of accounting
# ----------------------------------------------------------------------------
def step_year(st, p, lv, prev, rng, first, fl):
    nscale = p.get("noise", 1.0)

    def nz(sd):
        return math.exp(rng.gauss(0.0, sd * nscale)) if nscale > 0 else 1.0

    def delta(k):  # change in a level lever, applied once at the start of a round
        return (lv[k] - prev[k]) if first else 0.0

    year = st["year"] + 1
    # --- 5.0 population trend: everything scales, E/P unchanged ---
    g = POP_GROWTH
    for s in SECTORS:
        add = st["emp"][s] * g
        st["emp"][s] += add
        fl["trend"] += add
    for k in ("U", "disc", "reserve", "pop"):
        st[k] *= 1 + g

    # --- 5.1 what machines CAN do (premise: keeps improving rapidly) ---
    slope = (p["cog_auto_2032"] - A_C0) / 6.0
    dA = slope * lv["deploy_pace"] + (lv["shock_frontier_cog"] if first else 0.0)
    st["A_c"] = clip(st["A_c"] + dA, st["a_c"], A_MAX)
    st["A_hist"][str(year)] = st["A_c"]
    if first:
        st["lag"] = clip(st["lag"] + lv["shock_robot_lag_years"], 1.0, 12.0)
    st["A_p"] = max(st["A_p"], min(A_MAX, A_P0 + max(0.0, a_hist(st, year - st["lag"]) - st["A_floor"])))

    # --- 5.2 what firms actually automate (diffusion) ---
    rate = (math.log(2) / p["diffusion_t50"]) * lv["adoption_speed"] \
        * (1 - 0.5 * lv["deploy_regulation"]) * (1 - 0.005 * lv["capital_tax_pct"]) \
        * (1 - 0.15 * lv["union_pressure"]) * lv["shock_adoption"] * nz(0.05)
    st["a_c"] += (st["A_c"] - st["a_c"]) * (1 - math.exp(-rate))
    st["a_p"] += (st["A_p"] - st["a_p"]) * (1 - math.exp(-ROBOT_DIFFUSION * rate))

    # --- 5.3 displacement, cost savings, prices, demand response by sector ---
    Y = sum(st["emp"][s] * st["prod"][s] for s in SECTORS)
    wagebill = sum(st["emp"][s] * WAGE_REL[s] for s in SECTORS)
    emp_total0 = sum(st["emp"].values())
    pt = clip(p["passthrough"] + 0.15 * lv["ai_pricing"] + 0.15 * lv["competition_policy"], 0.05, 0.95)
    # pay's share of the saving: at most the whole saving (COST_SAVING); negative = pay bid down
    beta = clip(p["wage_share"] + lv["wage_sharing"] + 0.15 * lv["union_pressure"], -0.4, COST_SAVING)
    h_eff = clip(p["housing_supply"] + 0.4 * lv["housing_policy"], 0.0, 1.2)
    destroyed = {s: 0.0 for s in SECTORS}
    created = {s: 0.0 for s in SECTORS}
    x = {}
    frac = {}
    pool, leak, hours_saved, g_ai = 0.0, 0.0, 0.0, 0.0
    for s in SECTORS:
        u_old = st["u"][s]
        u_new = clip(sector_u(st["a_c"], st["a_p"], s), u_old, 0.95)
        frac[s] = (u_new - u_old) / (1 - u_old)        # labour no longer needed per unit of output
        saving = st["emp"][s] * frac[s]
        d_auto = saving * (1 - lv["hours_share"])
        hours_saved += saving * lv["hours_share"]
        destroyed[s] += d_auto
        fl["d_automation"] += d_auto
        g_ai += frac[s] * st["emp"][s] * WAGE_REL[s] / wagebill
        # The saving (COST_SAVING per unit of labour removed) is split three ways. Pay takes beta,
        # out of profit first; customers get pass-through of the rest; a wage cut (beta < 0) adds
        # to what can be passed on. Pay and price cuts together can never exceed the saving.
        price_share = max(0.0, min(pt * (COST_SAVING - min(beta, 0.0)), COST_SAVING - beta))
        x[s] = (CARE_PT if s == "care" else 1.0) * LS_SEC[s] * frac[s] * price_share   # fall in price
        eps = p["jevons"] * ELAS_F[s] * math.exp(-SATURATION * st["cumx"][s])
        if s == "construction":
            eps *= 0.5 + 0.5 * min(1.0, h_eff)           # land limits building
        c_price = (st["emp"][s] - d_auto) * eps * x[s]   # more output needs more of the remaining human tasks
        created[s] += c_price
        fl["c_price"] += c_price
        v_share = st["emp"][s] * st["prod"][s] / Y
        sp = (1 - eps) * x[s] * v_share                  # spending freed (or pulled in), share of GDP
        if sp >= 0:
            leak += LEAK * sp
            pool += (1 - LEAK) * sp
        else:
            pool += (1 - LEAK) * sp                      # 30% pulled from other sectors, 70% is new demand
        st["cumx"][s] += x[s]
        st["u"][s] = u_new
    # freed spending lands in other sectors (mostly labour-heavy services)
    for s in SECTORS:
        v_share = st["emp"][s] * st["prod"][s] / Y
        j = pool * SPILL_W[s] / v_share * st["emp"][s]
        if j >= 0:
            created[s] += j
            fl["c_shift"] += j
        else:
            destroyed[s] += -j
            fl["d_shift"] += -j
    # leaked spending: builds homes where supply allows, bids up rents where it does not
    vc = st["emp"]["construction"] * st["prod"]["construction"] / Y
    j = LEAK_BUILD * leak * min(1.0, h_eff) / vc * st["emp"]["construction"]
    created["construction"] += j
    fl["c_shift"] += j
    rent_push = LEAK_RENT * leak * (1 - min(1.0, h_eff)) / HOUSING_SPEND_SHARE

    # --- 5.4 new kinds of work (reinstatement), with a lag ---
    d_auto_total = sum(st["emp"][s] * frac[s] * (1 - lv["hours_share"]) for s in SECTORS)
    st["D_smooth"] = NEW_TASK_SMOOTH * st["D_smooth"] + (1 - NEW_TASK_SMOOTH) * d_auto_total
    retrain = min(1.0, lv["retraining_pct_gdp"] / 0.5)
    erosion = ((1 - st["A_c"]) / (1 - A_C0)) ** EROSION_EXP   # machines can do more of the new tasks too
    new_total = p["new_task_rate"] * st["D_smooth"] * erosion * lv["new_business"] \
        * (1 + 0.1 * retrain) * lv["shock_new_task"] * nz(0.08)
    for s in SECTORS:
        created[s] += new_total * NEW_W[s]
    fl["c_newwork"] += new_total

    # --- 5.5 slow re-absorption of slack labour at lower pay ---
    lf = emp_total0 + st["U"]
    slack = max(0.0, st["U"] - U_RATE0 * lf) + st["disc"]
    absorb = ABSORB_RATE * slack * (1 - st["A_c"])
    for s in SECTORS:
        created[s] += absorb * ABSORB_W[s]
    fl["c_absorb"] += absorb

    # --- 5.6 direct policy jobs: public employment, shorter legal week ---
    dpj = delta("public_jobs_m")
    dcut = delta("worktime_cut_pct") / 100.0
    pol = {s: dpj * PUBLIC_W[s] + WORKTIME_JOBS * dcut * st["emp"][s] for s in SECTORS}
    for s in SECTORS:
        if pol[s] >= 0:
            created[s] += pol[s]
            fl["c_policy"] += pol[s]
        else:
            destroyed[s] += -pol[s]
            fl["d_policy"] += -pol[s]

    # --- 5.7 spending feedback: lost wages, fiscal changes, outside shocks ---
    # "lost wages" (share of GDP) = pay lost with the net jobs lost so far this year, minus (plus)
    # pay rates running ahead of (behind) their old trend. One pass: demand_mult is the total multiplier.
    net_loss = (sum((destroyed[s] - created[s]) * WAGE_REL[s] for s in SECTORS) / wagebill
                - beta * g_ai) * st["ls"]
    hh_loss = max(0.0, net_loss) * (1 - UI_REPLACE)   # gains show up as income, not as extra jobs
    profit_base = PROFIT0 + (LS0 - st["ls"]) * 100
    cost_now = fiscal_cost(lv, st, emp_total0)
    cost_prev = fiscal_cost(prev, st, emp_total0)
    rev_now = lv["capital_tax_pct"] / 100 * profit_base * CAPTAX_COLLECT
    rev_prev = prev["capital_tax_pct"] / 100 * profit_base * CAPTAX_COLLECT
    impulse = ((cost_now - cost_prev) * 0.9 - (rev_now - rev_prev) * 0.3) / 100 if first else 0.0
    demand = -p["demand_mult"] * hh_loss + impulse + delta("shock_demand_pct") / 100 \
        - delta("household_saving") * 0.7
    demand *= nz(0.10) if demand < 0 else 1.0
    if demand > 0:   # extra spending only makes jobs while there are people to hire
        demand = min(demand, slack / emp_total0)
    norm = sum(DSENS[s] * st["emp"][s] for s in SECTORS) / emp_total0
    for s in SECTORS:
        j = demand * st["emp"][s] * DSENS[s] / norm
        if j >= 0:
            created[s] += j
            fl["c_demand"] += j
        else:
            destroyed[s] += -j
            fl["d_demand"] += -j

    # --- 5.8 apply flows to people ---
    for s in SECTORS:
        destroyed[s] = min(destroyed[s], st["emp"][s] * 0.9)
    d_tot = sum(destroyed.values())
    c_tot = sum(created.values())
    for s in SECTORS:
        st["emp"][s] -= destroyed[s]
    st["U"] += lv["layoff_share"] * d_tot
    st["disc"] += (1 - lv["layoff_share"]) * d_tot
    filled = hire(st, c_tot)
    scale = filled / c_tot if c_tot > 0 else 1.0
    fl["unfilled"] += c_tot - filled
    # (channel totals are reported before the labour-shortage cap; see c_unfilled_m)
    for s in SECTORS:
        created[s] *= scale
        st["emp"][s] += created[s]
        fl["destroyed"][s] += destroyed[s]
        fl["created"][s] += created[s]
    # long-term unemployed give up looking
    lf = sum(st["emp"].values()) + st["U"]
    excess = max(0.0, st["U"] - U_RATE0 * lf)
    move = DISCOURAGE * (1 - 0.3 * retrain) * excess
    st["U"] -= move
    st["disc"] += move
    # cash transfers let some people stop working (OpenResearch: -2pp at ~10% of GDP)
    exits = delta("transfers_pct_gdp") * TRANSFER_EXIT * st["pop"]
    if exits > 0:
        lf = sum(st["emp"].values()) + st["U"]
        from_u = min(exits, max(0.0, st["U"] - U_RATE0 * lf))
        st["U"] -= from_u
        rest = exits - from_u
        tot = sum(st["emp"].values())
        for s in SECTORS:
            st["emp"][s] -= rest * st["emp"][s] / tot
        st["reserve"] += exits
        fl["vol_exit"] += rest
    elif exits < 0:
        back = min(-exits, st["reserve"])
        st["reserve"] -= back
        st["U"] += back

    # --- 5.9 hours, pay, productivity, output ---
    emp_total = sum(st["emp"].values())
    st["hours"] *= (1 - hours_saved / emp_total0) * (1 - dcut)
    st["w_core"] *= math.exp(TREND + beta * g_ai) * (1 + 0.5 * dcut)
    ep = emp_total / st["pop"]
    old_wage = st["wage"]
    st["wage"] = st["w_core"] * clip(1 - WAGE_PER_EP_PP * (EP0 - ep) * 100, 0.6, 1.05)
    dlnw = math.log(st["wage"] / old_wage)
    ls_avg = sum(LS_SEC[s] * st["emp"][s] * st["prod"][s] for s in SECTORS) / Y
    for s in SECTORS:
        # output per worker rises as tasks are automated; shorter hours give some of it back
        st["prod"][s] *= math.exp(TREND) / (1 - frac[s]) * (1 - lv["hours_share"] * frac[s]) * (1 - 0.8 * dcut)
        # prices: labour-heavy services get relatively dearer when pay rises (Baumol), minus passed-on savings
        st["price"][s] *= math.exp((LS_SEC[s] - ls_avg) * (dlnw - TREND) - x[s])
    st["Y"] = sum(st["emp"][s] * st["prod"][s] for s in SECTORS)
    # labour share is pay over output AT CURRENT PRICES: savings passed to customers are not profit
    y_nom = sum(st["emp"][s] * st["prod"][s] * st["price"][s] for s in SECTORS)
    wb = sum(st["emp"][s] * WAGE_REL[s] for s in SECTORS) * st["wage"] * st["hours"] / HOURS0
    st["ls"] = clip(LS0 * (wb / st["wagebill0"]) / (y_nom / 100.0), 0.05, 0.80)

    # --- 5.10 housing ---
    constr = clip(0.6 + 2.0 * st["u"]["construction"], 0.6, 1.4)
    drent = (1 - min(1.0, h_eff)) * 0.02 - h_eff * 0.035 * constr + rent_push + 0.3 * (dlnw - TREND)
    drent += (lv["shock_housing_pct"] / 100 if first else 0.0)
    st["rent"] *= math.exp(drent) * nz(0.005)

    st["year"] = year
    return fl


def fiscal_cost(lv, st, emp_total):
    """New programme spending, % of GDP."""
    return (lv["transfers_pct_gdp"] + lv["retraining_pct_gdp"] + 0.3 * lv["housing_policy"]
            + lv["public_jobs_m"] / emp_total * st["ls"] * 100 * 0.7)


# ----------------------------------------------------------------------------
# 6. Derived indicators (the scorecard row)
# ----------------------------------------------------------------------------
def indicators(st, lv, fl, label, years, y_prev):
    emp = sum(st["emp"].values())
    lf = emp + st["U"]
    ep = emp / st["pop"]
    t = st["year"] - START_YEAR
    pr = st["price"]
    cat = {
        "goods": pr["manuf"] ** 0.5 * pr["logistics"] ** 0.2 * pr["retail"] ** 0.3,
        "digital": pr["office"] ** 0.7 * pr["neweco"] ** 0.3,
        "health": pr["care"],
        "housing": st["rent"],
        "other": pr["retail"],
    }
    cpi_med = math.prod(cat[k] ** w for k, w in BASKET_MED.items())
    cpi_b20 = math.prod(cat[k] ** w for k, w in BASKET_B20.items())
    y_pc = (st["Y"] / 100.0) / (st["pop"] / st["pop0"])
    weekly = st["wage"] * st["hours"] / HOURS0
    ep_rel = (EP0 - ep) / EP0
    lab_med = weekly * clip(1 - 1.0 * ep_rel, 0.3, 1.3)
    lab_b20 = weekly * clip(1 - 2.0 * ep_rel, 0.2, 1.4)
    t_base = 1.0   # existing benefits hold their 2026 value (price-indexed, not wage-indexed)
    cap = ((1 - st["ls"]) * y_pc) / (1 - LS0)
    tr = lv["transfers_pct_gdp"] / 100.0 * y_pc
    tg = lv["transfer_target"]
    med_nom = (MED_MIX["labour"] * lab_med + MED_MIX["transfers"] * t_base + MED_MIX["capital"] * cap
               + tr * (0.2 - 0.1 * tg) / MED_GDP_SHARE)
    b20_nom = (B20_MIX["labour"] * lab_b20 + B20_MIX["transfers"] * t_base + B20_MIX["capital"] * cap
               + tr * (0.2 + 0.3 * tg) / B20_GDP_SHARE)
    med_real = 100 * med_nom / cpi_med
    b20_real = 100 * b20_nom / cpi_b20
    # distribution of all income after the new tax and transfers
    profit_base = PROFIT0 + (LS0 - st["ls"]) * 100
    captax = lv["capital_tax_pct"] / 100 * profit_base * CAPTAX_COLLECT       # % GDP
    k_after = (1 - st["ls"]) - captax / 100
    k_new = (LS0 - st["ls"]) - captax / 100           # capital income beyond its 2026 share, after the new tax
    top1 = (TOP1_OF_LABOUR * st["ls"] + TOP1_OF_CAPITAL * (1 - LS0) + TOP1_OF_NEW_CAPITAL * k_new) \
        / (st["ls"] + k_after + lv["transfers_pct_gdp"] / 100) * 100
    poverty = clip(POVERTY0 * (b20_real / 100) ** (-POVERTY_ELAS), 2.0, 45.0)
    burden = st["rent"] / b20_nom
    homeless = HOMELESS0 * burden * max(1.0, burden / 1.1) ** 0.5 * (1 - 0.2 * lv["housing_policy"])
    # federal budget, % of GDP
    y_trend = 100 * math.exp((TREND + POP_GROWTH) * t)
    rev = REV_LABOUR0 * st["ls"] / LS0 + REV_CAPITAL0 * (1 - st["ls"]) / (1 - LS0) + captax
    ui = max(0.0, st["U"] - U_RATE0 * lf) / emp * st["ls"] * 100 * 0.4 * 0.5
    spend = SPEND0 * (y_trend / st["Y"]) ** SPEND_GDP_EXP + ui + fiscal_cost(lv, st, emp)
    deficit = spend - rev
    growth = (st["Y"] / y_prev) ** (1.0 / years) - 1
    for _ in range(years):
        st["debt"] = st["debt"] / (1 + growth + 0.02) + deficit
    u_rate = st["U"] / lf * 100
    target = UNREST0 + 4 * (u_rate - 4.1) + 2 * (EP0 - ep) * 100 + 0.5 * max(0, 100 - med_real) \
        - 0.3 * max(0, med_real - 100) + 1.0 * (top1 - 20) + 0.3 * (homeless - HOMELESS0) \
        - 2 * lv["transfers_pct_gdp"]
    st["unrest"] = clip(0.5 * st["unrest"] + 0.5 * target, 0, 100)
    d_tot = sum(fl["destroyed"].values())
    c_tot = sum(fl["created"].values())
    st["cum_destroyed"] += d_tot
    st["cum_created"] += c_tot
    row = {
        "period": label, "end_date": f"{st['year']}-12-31", "years": years,
        "ai_capability_index": round(100 * st["A_c"] / A_C0),
        "robot_capability_index": round(100 * st["A_p"] / A_P0),
        "cog_automatable_pct": round(100 * st["A_c"], 1),
        "cog_automated_pct": round(100 * st["a_c"], 1),
        "phys_automatable_pct": round(100 * st["A_p"], 1),
        "phys_automated_pct": round(100 * st["a_p"], 1),
        "employment_m": round(emp, 2),
    }
    for s in SECTORS:
        row[f"emp_{s}_m"] = round(st["emp"][s], 2)
    row.update({
        "jobs_destroyed_m": round(d_tot, 2),
        "jobs_created_m": round(c_tot, 2),
        "jobs_net_m": round(c_tot - d_tot, 2),
        "jobs_from_population_growth_m": round(fl["trend"], 2),
        "voluntary_exits_m": round(fl["vol_exit"], 2),
        "cum_jobs_destroyed_m": round(st["cum_destroyed"], 2),
        "cum_jobs_created_m": round(st["cum_created"], 2),
    })
    for s in SECTORS:
        row[f"destroyed_{s}_m"] = round(fl["destroyed"][s], 2)
    for s in SECTORS:
        row[f"created_{s}_m"] = round(fl["created"][s], 2)
    for ch in ("d_automation", "d_demand", "d_shift", "d_policy",
               "c_price", "c_shift", "c_newwork", "c_absorb", "c_demand", "c_policy"):
        row[f"{ch}_m"] = round(fl[ch], 2)
    row["c_unfilled_m"] = round(fl["unfilled"], 2)
    row.update({
        "unemployment_rate": round(u_rate, 2),
        "participation_rate": round(lf / st["pop"] * 100, 2),
        "employment_to_population": round(ep * 100, 2),
        "avg_weekly_hours": round(st["hours"], 2),
        "real_wage_index": round(100 * st["wage"] / cpi_med, 1),
        "median_real_income_index": round(med_real, 1),
        "bottom20_real_income_index": round(b20_real, 1),
        "top1_income_share": round(top1, 1),
        "labour_share": round(st["ls"] * 100, 1),
        "real_gdp_index": round(st["Y"], 1),
        "gdp_growth_pct": round(growth * 100, 2),
        "price_goods": round(100 * cat["goods"], 1),
        "price_digital_services": round(100 * cat["digital"], 1),
        "price_health": round(100 * cat["health"], 1),
        "price_housing": round(100 * cat["housing"], 1),
        "cost_of_living_median": round(100 * cpi_med, 1),
        "poverty_rate": round(poverty, 1),
        "homeless_per_10k": round(homeless, 1),
        "fed_revenue_pct_gdp": round(rev, 1),
        "fed_spending_pct_gdp": round(spend, 1),
        "fed_deficit_pct_gdp": round(deficit, 1),
        "fed_debt_pct_gdp": round(st["debt"], 1),
        "new_transfers_pct_gdp": round(lv["transfers_pct_gdp"], 2),
        "unrest_index": round(st["unrest"], 1),
    })
    return row


def step(st, p, lv, rng, years=1, label=None):
    """Advance the economy by `years` (1 or 2). Mutates st; returns the scorecard row."""
    prev = st["prev_levers"]
    fl = blank_flows()
    y_prev = st["Y"]
    for i in range(years):
        step_year(st, p, lv, prev, rng, i == 0, fl)
    st["rounds"] += 1
    row = indicators(st, lv, fl, label or str(st["year"]), years, y_prev)
    st["prev_levers"] = dict(lv)
    return row


def baseline_row(st):
    row = indicators(st, default_levers(), blank_flows(), "2026 baseline", 1, st["Y"])
    st["debt"], st["unrest"] = DEBT0, UNREST0
    row["fed_debt_pct_gdp"] = DEBT0
    row["gdp_growth_pct"] = ""
    return row


# ----------------------------------------------------------------------------
# 7. Policy presets for dice-only runs
# ----------------------------------------------------------------------------
ROUNDS = [("2027", 1), ("2028", 1), ("2029", 1), ("2030", 1),
          ("2031-32", 2), ("2033-34", 2), ("2035-36", 2)]


def preset_levers(policy, st, p, row, mem):
    lv = default_levers()
    if policy == "laissez":
        lv.update(adoption_speed=1.15, layoff_share=0.7, deploy_pace=1.1)
    elif policy == "active":
        slack_m = max(0.0, (EP0 * 100 - row["employment_to_population"]) / 100 * st["pop"])
        lv.update(transfers_pct_gdp=3.0 if st["year"] >= 2027 else 0.0, transfer_target=0.5,
                  capital_tax_pct=10.0, retraining_pct_gdp=0.4, housing_policy=0.7,
                  competition_policy=0.6, hours_share=0.3, new_business=1.2,
                  public_jobs_m=min(3.0, round(0.3 * slack_m, 1)))
    else:  # default: politics reacts to visible damage, after this run's lag, at this run's scale
        if mem.get("seen") is None and (row["unemployment_rate"] >= 6.0
                                        or row["employment_to_population"] <= EP0 * 100 - 1.5
                                        or row["unrest_index"] >= 55):
            mem["seen"] = st["year"]
        if mem.get("seen") is not None and st["year"] - mem["seen"] >= p["policy_lag_years"] - 1:
            sc = p["policy_scale_pct"]
            lv.update(transfers_pct_gdp=sc, transfer_target=0.5, capital_tax_pct=min(20.0, 2.5 * sc),
                      retraining_pct_gdp=min(0.5, 0.05 * sc), housing_policy=min(0.5, 0.05 * sc))
    return lv


def no_ai_benchmark():
    """2036 outcomes if automation simply stopped at its 2026 level (the 'old normal' trend)."""
    q = mid_params()
    q["cog_auto_2032"] = A_C0
    st = new_state(q)
    st["a_c"], st["a_p"] = A_C0, A_P0
    st["u"] = {s: sector_u(A_C0, A_P0, s) for s in SECTORS}
    st["A_floor"] = 1.0
    baseline_row(st)
    rng = random.Random(1)
    rows = [step(st, q, default_levers(), rng, yrs, label) for label, yrs in ROUNDS]
    return rows[-1]


def run_once(p, policy, seed=None):
    st = new_state(p)
    rng = random.Random((seed if seed is not None else p["seed"]) * 7919 + 13)
    row = baseline_row(st)
    rows, mem = [row], {}
    for label, yrs in ROUNDS:
        lv = preset_levers(policy, st, p, row, mem)
        row = step(st, p, lv, rng, yrs, label)
        rows.append(row)
    return rows


def summarise(rows):
    last = rows[-1]
    return {
        "unemployment_2036": last["unemployment_rate"],
        "peak_unemployment": max(r["unemployment_rate"] for r in rows),
        "participation_2036": last["participation_rate"],
        "emp_pop_2036": last["employment_to_population"],
        "min_emp_pop": min(r["employment_to_population"] for r in rows),
        "jobs_destroyed_total": last["cum_jobs_destroyed_m"],
        "jobs_created_total": last["cum_jobs_created_m"],
        "created_per_destroyed": round(last["cum_jobs_created_m"] / max(0.01, last["cum_jobs_destroyed_m"]), 3),
        "median_income_2036": last["median_real_income_index"],
        "bottom20_income_2036": last["bottom20_real_income_index"],
        "top1_share_2036": last["top1_income_share"],
        "labour_share_2036": last["labour_share"],
        "gdp_index_2036": last["real_gdp_index"],
        "poverty_2036": last["poverty_rate"],
        "homeless_2036": last["homeless_per_10k"],
        "housing_cost_2036": last["price_housing"],
        "deficit_2036": last["fed_deficit_pct_gdp"],
        "debt_2036": last["fed_debt_pct_gdp"],
        "unrest_2036": last["unrest_index"],
        "peak_unrest": max(r["unrest_index"] for r in rows),
    }


def pct(xs, q):
    xs = sorted(xs)
    k = (len(xs) - 1) * q
    lo, hi = int(math.floor(k)), int(math.ceil(k))
    return xs[lo] + (xs[hi] - xs[lo]) * (k - lo)


def montecarlo(n, policy, out=None, seed0=1000, quiet=False):
    recs = []
    for i in range(n):
        p = sample_params(seed0 + i)
        s = summarise(run_once(p, policy))
        rec = {"seed": seed0 + i, "policy": policy}
        rec.update({k: p[k] for k in PARAM_SPEC})
        rec.update(s)
        recs.append(rec)
    if out:
        with open(out, "w", newline="") as f:
            w = csv.DictWriter(f, fieldnames=list(recs[0].keys()))
            w.writeheader()
            w.writerows(recs)
    if not quiet:
        print(f"Monte Carlo: {n} dice-only runs, policy preset '{policy}'")
        for k in ("unemployment_2036", "peak_unemployment", "participation_2036", "emp_pop_2036",
                  "jobs_destroyed_total", "jobs_created_total", "created_per_destroyed", "median_income_2036", "bottom20_income_2036",
                  "top1_share_2036", "labour_share_2036", "gdp_index_2036", "poverty_2036",
                  "homeless_2036", "housing_cost_2036", "deficit_2036"):
            xs = [r[k] for r in recs]
            print(f"  {k:24s} p10 {pct(xs, .1):7.2f}   p50 {pct(xs, .5):7.2f}   p90 {pct(xs, .9):7.2f}")
        more = sum(1 for r in recs if r["created_per_destroyed"] >= 1) / n
        ep_ok = sum(1 for r in recs if r["emp_pop_2036"] >= EP0 * 100 - 0.5) / n
        trend = no_ai_benchmark()["median_real_income_index"]
        better = sum(1 for r in recs if r["median_income_2036"] > trend) / n
        worse = sum(1 for r in recs if r["median_income_2036"] < 100) / n
        print(f"  share of runs with more jobs created than destroyed: {more:.0%}")
        print(f"  share with 2036 employment rate within 0.5pt of 2026 or higher: {ep_ok:.0%}")
        print(f"  share with median income above the no-AI trend ({trend}): {better:.0%}; below 2026 level: {worse:.0%}")
    return recs


def rank(xs):
    order = sorted(range(len(xs)), key=lambda i: xs[i])
    r = [0.0] * len(xs)
    for pos, i in enumerate(order):
        r[i] = pos
    return r


def corr(a, b):
    n = len(a)
    ma, mb = sum(a) / n, sum(b) / n
    va = sum((x - ma) ** 2 for x in a)
    vb = sum((y - mb) ** 2 for y in b)
    if va == 0 or vb == 0:
        return 0.0
    return sum((x - ma) * (y - mb) for x, y in zip(a, b)) / math.sqrt(va * vb)


def sensitivity(n):
    outs = ["emp_pop_2036", "unemployment_2036", "created_per_destroyed", "median_income_2036",
            "bottom20_income_2036", "homeless_2036"]
    recs = montecarlo(n, "default", quiet=True)
    print(f"A. Hidden parameters: rank correlation with 2036 outcomes ({n} runs, default preset)")
    print("| parameter | " + " | ".join(outs) + " |")
    print("|---|" + "---|" * len(outs))
    for k in PARAM_SPEC:
        cells = [f"{corr(rank([r[k] for r in recs]), rank([r[o] for r in recs])):+.2f}" for o in outs]
        print(f"| {k} | " + " | ".join(cells) + " |")
    print()
    print("B. Hidden parameters one at a time: low end -> high end, others mid-range, default levers, no noise")
    print("| parameter | " + " | ".join(outs) + " |")
    print("|---|" + "---|" * len(outs))

    def fixed(p, lv_over):
        st = new_state(p)
        rng = random.Random(1)
        baseline_row(st)
        rows = []
        for label, yrs in ROUNDS:
            lv = default_levers()
            lv.update(lv_over)
            rows.append(step(st, p, lv, rng, yrs, label))
        return summarise(rows)

    for k, (lo, hi, _, _) in PARAM_SPEC.items():
        if k.startswith("policy_"):
            continue
        a = dict(mid_params()); a[k] = lo
        b = dict(mid_params()); b[k] = hi
        ra, rb = fixed(a, {}), fixed(b, {})
        print(f"| {k} {lo:g}->{hi:g} | " + " | ".join(f"{ra[o]:.1f} -> {rb[o]:.1f}" for o in outs) + " |")
    print()
    print("C. Levers one at a time: default -> strong setting held 2027-36, parameters mid-range, no noise")
    print("| lever | " + " | ".join(outs) + " |")
    print("|---|" + "---|" * len(outs))
    base = fixed(mid_params(), {})
    print("| (all defaults) | " + " | ".join(f"{base[o]:.1f}" for o in outs) + " |")
    tests = [("deploy_pace", 0.7), ("deploy_pace", 1.3), ("ai_pricing", 1.0), ("ai_pricing", -1.0),
             ("adoption_speed", 0.5), ("adoption_speed", 1.6), ("layoff_share", 0.2),
             ("hours_share", 0.5), ("wage_sharing", 0.3), ("new_business", 1.3), ("new_business", 0.75),
             ("union_pressure", 1.0), ("household_saving", 0.05), ("transfers_pct_gdp", 5.0),
             ("capital_tax_pct", 20.0), ("retraining_pct_gdp", 0.5), ("public_jobs_m", 4.0),
             ("worktime_cut_pct", 10.0), ("deploy_regulation", 1.0), ("competition_policy", 1.0),
             ("housing_policy", 1.0)]
    for k, v in tests:
        r = fixed(mid_params(), {k: v})
        print(f"| {k} = {v:g} | " + " | ".join(f"{r[o]:.1f} ({r[o] - base[o]:+.1f})" for o in outs) + " |")


# ----------------------------------------------------------------------------
# 8. Self-test
# ----------------------------------------------------------------------------
def selftest():
    fails = []

    def check(name, ok, detail=""):
        print(("PASS " if ok else "FAIL ") + name + (f"  [{detail}]" if detail else ""))
        if not ok:
            fails.append(name)

    p = mid_params()
    st = new_state(p)
    b = baseline_row(st)
    check("baseline unemployment 4.1", abs(b["unemployment_rate"] - 4.1) < 0.01, b["unemployment_rate"])
    check("baseline participation 61.6", abs(b["participation_rate"] - 61.6) < 0.05, b["participation_rate"])
    check("baseline E/P 59.1", abs(b["employment_to_population"] - 59.1) < 0.01)
    check("baseline labour share 52.8", abs(b["labour_share"] - 52.8) < 0.01)
    check("baseline indices 100", b["median_real_income_index"] == 100 and b["bottom20_real_income_index"] == 100
          and b["real_gdp_index"] == 100 and b["price_housing"] == 100)
    check("baseline poverty 12.9, homeless 22, top1 20", b["poverty_rate"] == 12.9 and b["homeless_per_10k"] == 22.0
          and abs(b["top1_income_share"] - 20.0) < 0.05, f"{b['poverty_rate']} {b['homeless_per_10k']} {b['top1_income_share']}")
    check("baseline budget 17.3 / 23.3 / 6.0", b["fed_revenue_pct_gdp"] == 17.3 and b["fed_spending_pct_gdp"] == 23.3
          and b["fed_deficit_pct_gdp"] == 6.0)
    check("basket and mix weights sum to 1", all(abs(sum(d.values()) - 1) < 1e-9 for d in
          (BASKET_MED, BASKET_B20, MED_MIX, B20_MIX, SPILL_W, NEW_W, ABSORB_W, PUBLIC_W)))

    # no-AI counterfactual: nothing more automated -> steady state on trend
    r = no_ai_benchmark()
    check("no-AI world: unemployment stays 4.1%, labour share 52.8%, incomes on the slow old trend",
          abs(r["unemployment_rate"] - 4.1) < 0.05 and 107 < r["median_real_income_index"] < 111
          and abs(r["labour_share"] - 52.8) < 0.1, f"{r['unemployment_rate']} {r['median_real_income_index']}")

    # accounting identities, bounds, NaNs across random runs and presets
    ok_id = ok_bounds = ok_nan = ok_people = True
    for policy in ("default", "laissez", "active"):
        for seed in range(150):
            pp = sample_params(seed)
            st = new_state(pp)
            rng = random.Random(seed)
            row = baseline_row(st)
            mem = {}
            prev_emp = row["employment_m"]
            for label, yrs in ROUNDS:
                lv = preset_levers(policy, st, pp, row, mem)
                e0 = sum(st["emp"].values())
                row = step(st, pp, lv, rng, yrs, label)
                e1 = sum(st["emp"].values())
                net = row["jobs_created_m"] - row["jobs_destroyed_m"] + row["jobs_from_population_growth_m"] \
                    - row["voluntary_exits_m"]
                if abs((e1 - e0) - net) > 0.06:
                    ok_id = False
                if abs(sum(st["emp"].values()) - row["employment_m"]) > 0.02:
                    ok_id = False
                for k, v in row.items():
                    if isinstance(v, float) and (math.isnan(v) or math.isinf(v)):
                        ok_nan = False
                if not (0 <= row["unemployment_rate"] <= 60 and 20 <= row["participation_rate"] <= 75
                        and 0 < row["labour_share"] <= 80 and 0 <= row["top1_income_share"] <= 60
                        and 0 <= row["unrest_index"] <= 100 and row["homeless_per_10k"] > 0
                        and row["cog_automated_pct"] <= row["cog_automatable_pct"] + 1e-6
                        and all(st["emp"][s] > 0 for s in SECTORS)):
                    ok_bounds = False
                if st["U"] < -1e-9 or st["disc"] < -1e-9 or st["reserve"] < -1e-9 \
                        or sum(st["emp"].values()) + st["U"] > st["pop"]:
                    ok_people = False
    check("employment change = created - destroyed + population growth - voluntary exits", ok_id)
    check("no NaN or infinite values", ok_nan)
    check("rates and shares stay in bounds", ok_bounds)
    check("stocks of people never negative", ok_people)

    # a 2-year step equals two 1-year steps (noise off)
    sa, sb = new_state(p), new_state(p)
    baseline_row(sa); baseline_row(sb)
    ra = step(sa, p, default_levers(), random.Random(1), 2)
    step(sb, p, default_levers(), random.Random(1), 1)
    rb = step(sb, p, default_levers(), random.Random(1), 1)
    check("one 2-year step = two 1-year steps", abs(ra["employment_m"] - rb["employment_m"]) < 0.01
          and abs(ra["median_real_income_index"] - rb["median_real_income_index"]) < 0.1)

    def run(over=None, lv_over=None):
        pp = dict(mid_params())
        pp.update(over or {})
        st = new_state(pp)
        baseline_row(st)
        rng = random.Random(1)
        rows = []
        for label, yrs in ROUNDS:
            lv = default_levers()
            lv.update(lv_over or {})
            rows.append(step(st, pp, lv, rng, yrs, label))
        return summarise(rows)

    lo, hi = run({"jevons": 0.3}), run({"jevons": 2.0})
    check("stronger demand response -> more jobs created", hi["jobs_created_total"] > lo["jobs_created_total"]
          and hi["emp_pop_2036"] > lo["emp_pop_2036"], f"{lo['jobs_created_total']} -> {hi['jobs_created_total']}")
    lo, hi = run({"new_task_rate": 0.2}), run({"new_task_rate": 1.2})
    check("more new kinds of work -> higher employment", hi["emp_pop_2036"] > lo["emp_pop_2036"])
    lo, hi = run({"diffusion_t50": 3}), run({"diffusion_t50": 20})
    check("slower adoption -> fewer jobs destroyed", hi["jobs_destroyed_total"] < lo["jobs_destroyed_total"])
    lo, hi = run({"cog_auto_2032": 0.25}), run({"cog_auto_2032": 0.60})
    check("faster AI -> more jobs destroyed and more output", hi["jobs_destroyed_total"] > lo["jobs_destroyed_total"]
          and hi["gdp_index_2036"] > lo["gdp_index_2036"])
    lo, hi = run({"robot_lag_years": 8}), run({"robot_lag_years": 2})
    check("earlier robots -> more jobs destroyed", hi["jobs_destroyed_total"] > lo["jobs_destroyed_total"])
    lo, hi = run({"passthrough": 0.2}), run({"passthrough": 0.9})
    check("more pass-through -> higher median real income", hi["median_income_2036"] > lo["median_income_2036"])
    lo, hi = run({"wage_share": -0.3}), run({"wage_share": 0.6})
    check("pay sharing in gains -> higher labour share, lower top-1% share",
          hi["labour_share_2036"] > lo["labour_share_2036"] and hi["top1_share_2036"] < lo["top1_share_2036"])
    lo, hi = run({"housing_supply": 0.0}), run({"housing_supply": 1.0})
    check("freer housing supply -> cheaper housing, less homelessness",
          hi["housing_cost_2036"] < lo["housing_cost_2036"] and hi["homeless_2036"] < lo["homeless_2036"],
          f"housing {lo['housing_cost_2036']} -> {hi['housing_cost_2036']}")
    check("housing cost range roughly +20% to -30% (brief H8)", 110 <= lo["housing_cost_2036"] <= 135
          and 60 <= hi["housing_cost_2036"] <= 85, f"{lo['housing_cost_2036']} / {hi['housing_cost_2036']}")
    lo, hi = run({"demand_mult": 0.5, "new_task_rate": 0.4}), run({"demand_mult": 1.5, "new_task_rate": 0.4})
    check("stronger spending feedback -> lower employment when jobs are being lost",
          hi["emp_pop_2036"] < lo["emp_pop_2036"])
    base = run()
    tr = run(lv_over={"transfers_pct_gdp": 4.0, "transfer_target": 1.0})
    check("targeted transfers cut poverty and homelessness", tr["poverty_2036"] < base["poverty_2036"]
          and tr["homeless_2036"] < base["homeless_2036"])
    check("transfers cost money", tr["deficit_2036"] > base["deficit_2036"])
    tx = run(lv_over={"capital_tax_pct": 20.0})
    check("capital tax lowers deficit and top-1% share", tx["deficit_2036"] < base["deficit_2036"]
          and tx["top1_share_2036"] < base["top1_share_2036"])
    rg = run(lv_over={"deploy_regulation": 1.0})
    check("deployment restrictions -> fewer jobs destroyed and less output",
          rg["jobs_destroyed_total"] < base["jobs_destroyed_total"] and rg["gdp_index_2036"] < base["gdp_index_2036"])

    # both answers reachable on both questions
    good = run({"jevons": 2.0, "new_task_rate": 1.2, "passthrough": 0.9, "wage_share": 0.3,
                "housing_supply": 1.0, "demand_mult": 0.5})
    bad = run({"jevons": 0.3, "new_task_rate": 0.2, "passthrough": 0.2, "wage_share": -0.3,
               "housing_supply": 0.0, "demand_mult": 1.5, "diffusion_t50": 3.0})
    check("optimist's world: more jobs created than destroyed, employment rate not lower",
          good["created_per_destroyed"] > 1 and good["emp_pop_2036"] >= 59.0,
          f"ratio {good['created_per_destroyed']}, E/P {good['emp_pop_2036']}, u {good['unemployment_2036']}")
    check("optimist's world: median income well above trend, homelessness falls",
          good["median_income_2036"] > 120 and good["homeless_2036"] < 22,
          f"{good['median_income_2036']} / {good['homeless_2036']}")
    check("pessimist's world: far fewer jobs created than destroyed, mass joblessness",
          bad["created_per_destroyed"] < 0.6 and bad["emp_pop_2036"] < 52,
          f"ratio {bad['created_per_destroyed']}, E/P {bad['emp_pop_2036']}, u {bad['unemployment_2036']}")
    check("pessimist's world: median income below 2026, homelessness rises",
          bad["median_income_2036"] < 100 and bad["homeless_2036"] > 22,
          f"{bad['median_income_2036']} / {bad['homeless_2036']}")

    # lever validation
    try:
        validate_levers({"nonsense": 1}, default_levers()); ok = False
    except ValueError:
        ok = True
    try:
        validate_levers({"transfers_pct_gdp": 50}, default_levers()); ok = False
    except ValueError:
        pass
    check("lever names and ranges are validated", ok)
    print()
    print("SELFTEST " + ("OK" if not fails else f"FAILED ({len(fails)}): " + "; ".join(fails)))
    return 0 if not fails else 1


# ----------------------------------------------------------------------------
# 9. Command line
# ----------------------------------------------------------------------------
def write_row(path, row, new=False):
    with open(path, "w" if new else "a", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(row.keys()))
        if new:
            w.writeheader()
        w.writerow(row)


def key_numbers(row):
    return (
        f"Period {row['period']} (to {row['end_date']})\n"
        f"  Jobs: {row['jobs_destroyed_m']}m destroyed, {row['jobs_created_m']}m created "
        f"(net {row['jobs_net_m']:+}m, plus {row['jobs_from_population_growth_m']}m from population growth); "
        f"employment {row['employment_m']}m\n"
        f"  Unemployment {row['unemployment_rate']}%  participation {row['participation_rate']}%  "
        f"employment-to-population {row['employment_to_population']}%  weekly hours {row['avg_weekly_hours']}\n"
        f"  Median real household income {row['median_real_income_index']} (2026=100)  "
        f"bottom fifth {row['bottom20_real_income_index']}  top-1% share {row['top1_income_share']}%  "
        f"labour share {row['labour_share']}%\n"
        f"  GDP index {row['real_gdp_index']} (growth {row['gdp_growth_pct']}%/yr)  prices: goods {row['price_goods']}, "
        f"digital/professional {row['price_digital_services']}, health {row['price_health']}, housing {row['price_housing']}\n"
        f"  Poverty {row['poverty_rate']}%  homeless {row['homeless_per_10k']} per 10k  "
        f"federal deficit {row['fed_deficit_pct_gdp']}% GDP (debt {row['fed_debt_pct_gdp']}%)  unrest {row['unrest_index']}/100\n"
        f"  Automation: desk work {row['cog_automated_pct']}% done by machines of {row['cog_automatable_pct']}% possible; "
        f"physical work {row['phys_automated_pct']}% of {row['phys_automatable_pct']}%"
    )


def cmd_init(a):
    sd = os.path.join(a.run, "state")
    os.makedirs(sd, exist_ok=True)
    if os.path.exists(os.path.join(sd, "state.json")) and not a.force:
        sys.exit(f"{sd}/state.json already exists; use --force to overwrite")
    p = sample_params(a.seed)
    st = new_state(p)
    row = baseline_row(st)
    json.dump(p, open(os.path.join(sd, "params.json"), "w"), indent=1)
    json.dump(st, open(os.path.join(sd, "state.json"), "w"), indent=1)
    write_row(os.path.join(sd, "scorecard.csv"), row, new=True)
    print(f"Initialised {a.run} with seed {a.seed}.")
    print("HIDDEN CONDITIONS (referee only - never show players):")
    print(describe_params(p))
    print()
    print(key_numbers(row))


def cmd_step(a):
    sd = os.path.join(a.run, "state")
    p = json.load(open(os.path.join(sd, "params.json")))
    st = json.load(open(os.path.join(sd, "state.json")))
    sc = os.path.join(sd, "scorecard.csv")
    labels = [r["period"] for r in csv.DictReader(open(sc))]
    if a.label in labels:
        sys.exit(f"period '{a.label}' is already in the scorecard; refusing to step twice")
    try:
        lv, notes = validate_levers(json.load(open(a.levers)), st["prev_levers"])
    except ValueError as e:
        sys.exit(f"LEVER ERROR: {e}")
    json.dump(st, open(os.path.join(sd, f"state-before-{a.label}.json"), "w"))
    rng = random.Random(p["seed"] * 1000 + st["rounds"] + 1)
    row = step(st, p, lv, rng, a.years, a.label)
    json.dump(st, open(os.path.join(sd, "state.json"), "w"), indent=1)
    write_row(sc, row)
    for n in notes:
        print("note:", n)
    print(key_numbers(row))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("init"); s.add_argument("--run", required=True); s.add_argument("--seed", type=int, required=True)
    s.add_argument("--force", action="store_true")
    s = sub.add_parser("step"); s.add_argument("--run", required=True); s.add_argument("--levers", required=True)
    s.add_argument("--years", type=int, choices=[1, 2], required=True); s.add_argument("--label", required=True)
    s = sub.add_parser("montecarlo"); s.add_argument("--n", type=int, default=1000)
    s.add_argument("--policy", choices=["default", "laissez", "active"], default="default")
    s.add_argument("--out", default=None); s.add_argument("--seed0", type=int, default=1000)
    s = sub.add_parser("sensitivity"); s.add_argument("--n", type=int, default=600)
    sub.add_parser("selftest")
    sub.add_parser("levers")
    a = ap.parse_args()
    if a.cmd == "init":
        cmd_init(a)
    elif a.cmd == "step":
        cmd_step(a)
    elif a.cmd == "montecarlo":
        montecarlo(a.n, a.policy, a.out, a.seed0)
    elif a.cmd == "sensitivity":
        sensitivity(a.n)
    elif a.cmd == "selftest":
        sys.exit(selftest())
    elif a.cmd == "levers":
        for k, (lo, hi, d, kind, who, txt) in LEVER_SPEC.items():
            print(f"{k:24s} [{lo:g}, {hi:g}] default {d:g}  ({kind}; {who})  {txt}")


if __name__ == "__main__":
    main()
