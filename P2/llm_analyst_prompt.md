# llm_analyst_prompt.md — FINTECH-P2-Example

The frozen LLM analyst (Track 2) for Project 2, The Strategy Lab (FINA 4075/5075, Fall 2026).
Locked at the pre-registration commit. Any change to the model, the settings, the schedule or the
prompt text after that commit is a rule change (deduction code P0).

MODEL: Claude by Anthropic, model "Fable 5.1" with the effort setting "Max", exactly as shown in the
  claude.ai model picker ("Fable 5.1 Max"). Settings: a new, empty conversation for every run; no
  project, style or custom instructions; web search and every connector OFF; no files attached;
  no earlier picks, panel rows, backtest results or strategy rules shown to the model at any time.
  If Anthropic retires this model during the term, the forced switch is documented in the AI Audit
  Note and the nearest successor is used (Instructor Guide rule); the prompt text does not change.

RUN: once a month, on the briefing table as of the prior month-end, the day that table is generated.
  First run: the August-end (8/31/2026) table, inside the pre-registration commit
  (entry 0 = September picks, beside the locked rule's list). Then the day each monthly extension
  file posts: September-end table -> October picks (logged at checkpoint 1, Sun 10/11);
  October-end table -> November picks (logged at checkpoint 2, Sun 11/8). No run at checkpoint 3.
  Each run is one message in one new conversation; the first reply is the result.

MALFORMED OUTPUT: the output is malformed if it is not exactly 20 distinct tickers that all appear
  in the table, or if it contains any text besides the comma-separated list. One retry is permitted
  only for a malformed output, in a new conversation with the identical message; both outputs are
  logged either way. A disliked output earns nothing. If the retry is also malformed, both outputs
  are logged and the month is recorded as "no valid Track 2 picks" per the Instructor Guide.

INPUT: the standardized briefing table produced by the notebook's generator (Briefing-Table Format
  Specification): 200 rows sorted by ticker, one line each, Ticker | Company | Sector | 1M | 3M | 12M,
  trailing total returns in percent as of the stated month-end. The text block is pasted unedited
  directly beneath the prompt, in the same message. Nothing else is ever shown to the model.

OUTPUT HANDLING: the reply is pasted verbatim into monitoring_log.md (copy the model's text; do not
  retype, reorder or "clean" it). The log records the date and time of the run and whether the
  output parsed on the first try.

PROMPT (sent verbatim as one message; the briefing table is pasted directly beneath it, after one
blank line, in the same message):

You are a portfolio manager. Below is a table of 200 U.S. mid-cap stocks: ticker, company, sector, and trailing 1-, 3- and 12-month total returns in percent as of the stated month-end. Using only the information in this table, select the 20 stocks you would hold, equally weighted, for the next calendar month. Return exactly 20 tickers from the table as a single comma-separated list. No prose, no explanation, no ranking, no other text.

[BRIEFING TABLE pasted here, unedited — the output of the notebook's briefing generator for the month-end in question]
