# AI Audit Note (individual) — FINTECH-P2-Example

Instructor's worked example of the individual AI Audit Note. This copy covers the AI used through the
9/20 pre-registration and checkpoint 1 (10/5/2026); the version submitted with the December final report
adds checkpoints 2 and 3 and the report-writing AI use. Four standing elements (Semester Overview): tool log; most effective prompts;
AI errors caught with evidence; verification table. No student names appear in any AI-facing file
(AI Data Use Protocol); the panel is Level 1 public data.

## 1. Tool log
| Tool (model, route) | What it was used for | Level of data shown |
|---|---|---|
| Google Gemini 2.5 Pro, gemini.google.com | Red-team of strategy_rules.md (Step 6): find ambiguities a dishonest researcher could exploit | The rules file only (no returns) |
| Claude Fable 5.1 (effort "Max"), claude.ai | The frozen Track 2 analyst itself — the deliverable, not a coding aid; run once on the 8/31 briefing table | The standardized briefing table (Level 1 public returns) |
| Claude Fable 5.1 (effort "Max"), claude.ai | Checkpoint 1: the same frozen analyst, run once on the 9/30 briefing table (Mon 10/5/2026, 12:55 AM Central; new empty chat, web search and memory off) | The 9/30 briefing table only |
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
(3) Checkpoint 1 — the same behavior, second run. The 10/5 run's visible reasoning labels were
"Continuing to tally adjusted momentum across more candidates", "Swapping lower-ranked sector picks for
diversified alternatives" and "Verifying sector assignments and finalizing the twenty-stock selection":
again a self-imposed sector rule the prompt never asked for. The output was well-formed (20 valid,
distinct tickers, first try) and was pasted verbatim; the picks landed 6 Energy, 6 Health Care, 2
Communication Services, 2 Information Technology and one each in four other sectors, so the "cap" is the
model's own. No prompt wording was changed in response — the time for that was the red-team step (P0).
(4) Data integrity, not an AI error but caught the same way. Rebuilding August 2026 from the fresh Yahoo
pull before appending September reproduced the released panel's August row for 195 of 200 names
exactly; five names (SM, SLGN, REXR, KRG, IRT) differed by 0.000001 in the last decimal because Yahoo
had re-adjusted those series for a later dividend. The released rows were left untouched (the posted
file is authoritative); only the September row was appended, and its hash is in the Data Dictionary.

## 4. Verification table (key numbers → primary source, retrieval date)
| Number | Value | Primary source | Retrieved |
|---|---|---|---|
| Panel file integrity | SHA-256 c9d3340e… matches the Data Dictionary | Data Dictionary (D2L) + hashlib in the notebook | 9/15/2026 |
| Panel shape | 92 months × 200 stocks, no missing values | panel_returns_2026-08-31.csv (Yahoo Finance) | 9/15/2026 |
| In-sample CAGR, momentum vs EW | 20.3% vs 15.4% (Jan 2020–Aug 2026) | strategy.py on the posted panel | 9/15/2026 |
| Aug-2026 hand check | 6.145% net, matches engine to the cent | manual recompute vs panel_returns CSV | 9/15/2026 |
| Track 2 output | 20 valid distinct tickers, parsed first try | claude.ai Fable 5.1 Max run, screenshot in the Example folder | 9/15/2026 |
| Extension file integrity | SHA-256 d9417fdf… matches the Data Dictionary; 93 x 200, no missing values | panel_returns_2026-09-30.csv (Yahoo Finance, pulled 10/5/2026) + hashlib in the notebook | 10/5/2026 |
| Rerun check (checkpoint 1) | strategy.py unchanged; September holdings = entry 0, 20/20 | FINA4075_P2_StrategyLab_2026-09-30.ipynb, Cell 12 | 10/5/2026 |
| September 2026 scores | Track 1 −3.63% net, Track 2 −0.84% net, EW benchmark −5.78% | notebook Cell 13 on the posted extension file | 10/5/2026 |
| Track 2 October picks | 20 valid distinct tickers, parsed first try; overlap with Track 1 4/20 | claude.ai Fable 5.1 Max run 10/5/2026, outputs/track2_run_2026-09-30_screenshot.jpg | 10/5/2026 |

Note on this example's construction: the exemplar was assembled with Claude (Cowork) driving the code
and browser steps; a student's own Audit Note would name whichever tools they used. The discipline is
the same — every AI interaction that shaped a deliverable is logged, and every graded number is tied
back to the posted panel, not to anything an AI asserted.
