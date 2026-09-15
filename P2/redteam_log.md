# redteam_log.md — FINTECH-P2-Example

Red-team of strategy_rules.md before the pre-registration commit (Project 2, Step 6).
Second AI: Google Gemini (2.5 Pro), gemini.google.com, 9/15/2026. Route: pasted the full rules file
with the instruction "find every ambiguity that would let a dishonest researcher flex this backtest
later; quote the phrase, explain the exploit, propose exact replacement wording." Five findings; all
five were real and were fixed. The full exchange (prompt and verbatim reply) is in the AI Audit Note.

FINDING 1 — Missing data in the signal window is undefined.
  Quote: "The 200 stocks ... all of them, every month" together with the six-month signal product.
  Exploit: if any monthly return in a stock's t-12..t-7 window were missing, the file did not say
  whether to treat it as zero, skip the stock, or drop the month — a researcher could pick whichever
  helped. The released panel has no missing values, but an extension file could introduce one when a
  stock is acquired or delisted mid-window.
  FIX: added to SIGNAL — "If any of the six monthly returns in a stock's window is missing (the stock
  was not yet listed, or has delisted), the stock is ineligible for that month and is not ranked."

FINDING 2 — The tie-break covered only two stocks.
  Quote: "If two stocks have exactly equal signals at the 20th/21st boundary ..."
  Exploit: three or more stocks tied at the boundary fell outside the rule, leaving the last slots to
  discretion.
  FIX: rewrote TIE-BREAK — "If two or more stocks tie at the 20th/21st boundary, fill the remaining
  slots with the alphabetically earliest tickers among the tied names, up to exactly 20 holdings."

FINDING 3 — Turnover ignored the trades that reset drifted weights.
  Quote: "One-way turnover in month t = (number of names ... not held in month t-1) / 20."
  Exploit: continuing holdings drift away from 1/20 during the month; trading them back is real
  turnover the formula omits. A researcher could invoke the text when costs looked high and "correct
  the code" to full weight-drift turnover when they looked low.
  FIX: added to COSTS — "Turnover counts name replacement only. Rebalancing the weights of
  continuing holdings back to 1/20 is assumed costless; this is a stated simplification, fixed for
  both tracks and the placebo."

FINDING 4 — The benchmark denominator was undefined once a stock delists.
  Quote: "BENCHMARK: Equal-weighted average of all 200 stocks, rebalanced monthly ..."
  Exploit: after a delisting it was unclear whether the benchmark averaged over the static 200 or the
  active names, which moves the hurdle both tracks are judged against.
  FIX: rewrote BENCHMARK — "Equal-weighted average of the stocks active that month (all 200 until a
  name delists, the remaining active names thereafter), rebalanced monthly, no costs." The two tracks
  use the same active-universe rule.

FINDING 5 — The placebo draw mechanics were unspecified.
  Quote: "1,000 random 20-stock equal-weighted portfolios drawn from the same 200 stocks ..."
  Exploit: with or without replacement, and redrawn monthly versus drawn once and held, are different
  null distributions; leaving it open lets the placebo be shaped after the fact.
  FIX: rewrote PLACEBO PLAN — "Each of the 1,000 portfolios draws 20 distinct tickers without
  replacement from the stocks active at the start of the live window (numpy default_rng, seed 4075),
  then buys and holds them across the live months with the same cost formula (first month = full
  purchase). A holding that delists is dropped and its weight redistributed equally, matching the
  active-universe rule above." This is the buy-and-hold placebo the Instructor Guide describes.

Effect on the numbers: none of the five fixes change any in-sample result. The released panel has no
missing values, no two stocks share an identical six-month signal at the boundary (checked: the 20th
and 21st signals differ), and no stock delists in the January 2020 – August 2026 window, so findings
1, 2 and 4 are dormant on this data and findings 3 and 5 only pin down conventions the code already
followed. The value of the red-team is that the live window and any future rerun are now unambiguous.
