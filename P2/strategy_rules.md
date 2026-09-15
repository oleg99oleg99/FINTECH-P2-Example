# strategy_rules.md — FINTECH-P2-Example

Pre-registration for Project 2, The Strategy Lab (FINA 4075/5075, Fall 2026). Locked at the
pre-registration commit; this file governs if the code and the file ever disagree.

STRATEGY: Intermediate momentum, months t-12 through t-7 ("months 7-12 only"; Strategy Menu,
  Section 4, item (i)). This is the instructor's demonstration strategy and sits outside the
  Fall 2026 menu on purpose, so that the example does not pre-empt any pair's menu choice.
  Pairs choose from Section 2 of the Strategy Menu (or one Section 3 combination).

UNIVERSE: The 200 stocks in P2_ticker_list_2026-08-31.csv, all of them, every month. No additions,
  no exclusions, no liquidity, price or sector screens. If the instructor's extension file marks a
  stock as delisted, it leaves the universe from the following month (Data Dictionary, Section 4).

DATA: panel_returns_2026-08-31.csv, simple monthly total returns, row 0 = January 2019, row 91 =
  August 2026, SHA-256 c9d3340eba3a3301a63bb788c87f1d6e9e55de58a3fec16b12a34b313cac076b, plus the
  instructor's dated extension files for September, October and November 2026 (each committed with
  its checkpoint entry). The posted files are authoritative; no rebuilt panel is used for any
  graded number.

SIGNAL: For the portfolio held during month t, the compounded total return over the SIX monthly
  returns of months t-12, t-11, t-10, t-9, t-8 and t-7 inclusive:
      signal_t = (1 + r_{t-12}) x (1 + r_{t-11}) x ... x (1 + r_{t-7}) - 1.
  Months t-6 through t-1 (the most recent six months) are excluded entirely and are not used
  anywhere in the rule. Compounded, not summed. In code the window is rets[t-12 : t-6]
  (Python slicing stops before t-6, so the slice holds rows t-12 .. t-7).
  MISSING DATA: if any of the six monthly returns in a stock's window is missing (the stock was not
  yet listed, or has delisted), the stock is ineligible for that month and is not ranked. The
  released panel has no missing values; this rule governs the live window only.

RANKING: Descending by signal (highest first).
TIE-BREAK: If two or more stocks tie at the 20th/21st rank boundary, fill the remaining slots with
  the alphabetically earliest tickers among the tied names (Python string order on the ticker
  symbol), up to exactly 20 holdings.

PORTFOLIO: The 20 highest-ranked stocks (the top decile of the 200), equal weights of 1/20 each,
  fully invested, long only. Weights are reset to 1/20 at every month-end rebalance.

REBALANCE: Monthly, at each month-end, using data through the prior month-end only. The portfolio
  held during month t is chosen from returns of months <= t-1 (in fact <= t-7, given the window).
  Signal computation and the rebalance trade are both assumed to happen at the month-end close;
  this is a simplification and is stated as such in the report. The first month with a complete
  window is January 2020 (row 12); the in-sample backtest runs January 2020 - August 2026
  (80 months).

COSTS: 10 basis points per side. One-way turnover in month t = (number of names in month t's
  portfolio that were not held in month t-1) / 20. Monthly cost = 2 x 0.0010 x turnover. The first
  month of any run (January 2020 in the backtest) counts as a full purchase (turnover = 1).
  Net monthly return = equal-weight mean of the 20 holdings' returns for month t - monthly cost.
  Turnover counts name replacement only. Rebalancing the weights of continuing holdings back to 1/20
  after they drift during the month is assumed costless; this is a stated simplification, fixed for
  both tracks and the placebo.

BENCHMARK: Equal-weighted average of the stocks active that month (all 200 until a name delists, the
  remaining active names thereafter), rebalanced monthly, no costs.

LIVE WINDOW: September, October and November 2026, scored month by month at the three checkpoints.
  The September 2026 portfolio is selected from the released panel (window = September 2025 -
  February 2026) and recorded in monitoring_log.md entry 0 inside the pre-registration commit.
  Each later month's portfolio is selected from the extended panel the day the extension file
  posts and recorded in that checkpoint's entry before the month it is scored on.

PLACEBO PLAN (pre-registered): 1,000 random portfolios. Each draws 20 distinct tickers without
  replacement from the stocks active at the start of the live window (numpy default_rng, seed 4075),
  then buys and holds them across the live months with the same cost formula (first month = full
  purchase; a holding that delists is dropped and its weight redistributed equally, matching the
  active-universe rule). For each track, report the gap versus the benchmark and its percentile in
  the placebo distribution of gaps. This is the buy-and-hold placebo the Instructor Guide describes.

REPORTING: All statistics follow Section 3 of the Detailed Student Instructions: CAGR, annualized
  volatility (sample standard deviation x sqrt 12), Sharpe with rf = 0, maximum drawdown of the
  growth path, annual one-way turnover (mean monthly turnover x 12).

NO: leverage, shorting, cash or T-bill positions, discretionary overrides, parameter changes
  (window, holding count, weights, cost rate), or edits to this file after the pre-registration
  commit. Any such change carries deduction code P0.
