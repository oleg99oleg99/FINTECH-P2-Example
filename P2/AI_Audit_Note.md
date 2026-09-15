# AI Audit Note (individual) — FINTECH-P2-Example

Instructor's worked example of the individual AI Audit Note. This copy covers the AI used through the
9/20 pre-registration; the version submitted with the December final report adds the checkpoint and
report-writing AI use. Four standing elements (Semester Overview): tool log; most effective prompts;
AI errors caught with evidence; verification table. No student names appear in any AI-facing file
(AI Data Use Protocol); the panel is Level 1 public data.

## 1. Tool log
| Tool (model, route) | What it was used for | Level of data shown |
|---|---|---|
| Google Gemini 2.5 Pro, gemini.google.com | Red-team of strategy_rules.md (Step 6): find ambiguities a dishonest researcher could exploit | The rules file only (no returns) |
| Claude Fable 5.1 (effort "Max"), claude.ai | The frozen Track 2 analyst itself — the deliverable, not a coding aid; run once on the 8/31 briefing table | The standardized briefing table (Level 1 public returns) |
| Claude Fable 5.1, claude.ai | AI-assisted coding of the backtest and briefing generator (the course coding loop) | Panel rows (Level 1 public returns) |

The frozen analyst is a special case: its output is Track 2's data, so it is run under the contract in
llm_analyst_prompt.md (one run, verbatim paste, one logged retry only if malformed) and never treated
as a general assistant.

## 2. Most effective prompts (verbatim)
Red-team (Gemini): "I am a student in a finance course. Below is my pre-registration rules file ...
Find every ambiguity that would let a dishonest researcher flex this backtest later: any decision the
file leaves open, any wording two implementers could read differently, any parameter or convention
that is unstated, any place where the code could quietly differ from the text. For each finding, quote
the phrase, explain how it could be exploited, and propose exact replacement wording. Do not comment on
whether the strategy is a good idea, only on whether the file is unambiguous. Number the findings."
(Full rules file appended.) — Effective because it fixed the AI's job as adversarial editing of the
text, not strategy advice, and forced quotable finding → fix pairs that drop straight into
redteam_log.md.

Frozen analyst (Claude Fable 5.1 Max): the exact committed prompt in llm_analyst_prompt.md
("You are a portfolio manager. Below is a table of 200 U.S. mid-cap stocks ... Return exactly 20
tickers from the table as a single comma-separated list. No prose, no explanation, no ranking, no
other text."), followed by the briefing table. Effective because the hard format constraint made the
output machine-checkable (exactly 20 valid tickers) and parseable on the first try.

## 3. AI issues caught, with evidence
(1) Off-by-one in the signal window. An AI coding suggestion for "months t-12 through t-7" naturally
writes the slice rets[t-12:t-7], which in Python excludes the stop index and so drops month t-7 —
five months, not six. Caught by the hand-verification: recomputing August 2026's portfolio by hand
(mean of the 20 holdings' returns 6.215%, minus 2 x 0.0010 x 0.35 turnover = 6.145% net) matches the
engine to the cent only with the correct slice rets[t-12:t-6], and the September selection's window
prints as Sep 2025 – Feb 2026 (six months). The rules file and strategy.py both state the correct
form and note the Python subtlety.
(2) The frozen analyst did more than the prompt asked. Claude Fable 5.1 Max's own reasoning trace
(visible during the run: "Capping sector exposure and drafting an intact-trend filter",
"Comparing steadier candidates to swap into the sector slot") shows it imposed a sector cap and a
trend filter that the prompt never specified. The output still parsed to exactly 20 valid tickers, so
it was accepted verbatim under the contract — but the behavior is logged as a model-risk observation:
a "table-only" instruction does not stop the model from adding its own methodology, which is exactly
the run-to-run variability the graduate model-risk page will quantify with the double-run.

## 4. Verification table (key numbers → primary source, retrieval date)
| Number | Value | Primary source | Retrieved |
|---|---|---|---|
| Panel file integrity | SHA-256 c9d3340e… matches the Data Dictionary | Data Dictionary (D2L) + hashlib in the notebook | 9/15/2026 |
| Panel shape | 92 months × 200 stocks, no missing values | panel_returns_2026-08-31.csv (Yahoo Finance) | 9/15/2026 |
| In-sample CAGR, momentum vs EW | 20.3% vs 15.4% (Jan 2020–Aug 2026) | strategy.py on the posted panel | 9/15/2026 |
| Aug-2026 hand check | 6.145% net, matches engine to the cent | manual recompute vs panel_returns CSV | 9/15/2026 |
| Track 2 output | 20 valid distinct tickers, parsed first try | claude.ai Fable 5.1 Max run, screenshot in the Example folder | 9/15/2026 |

Note on this example's construction: the exemplar was assembled with Claude (Cowork) driving the code
and browser steps; a student's own Audit Note would name whichever tools they used. The discipline is
the same — every AI interaction that shaped a deliverable is logged, and every graded number is tied
back to the posted panel, not to anything an AI asserted.
