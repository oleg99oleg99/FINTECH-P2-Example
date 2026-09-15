# monitoring_log.md — FINTECH-P2-Example

Paper-trading log for Project 2, The Strategy Lab (FINA 4075/5075, Fall 2026).
Track 1 = intermediate momentum, months t-12..t-7, top 20 EW, 10 bp/side (strategy_rules.md).
Track 2 = frozen prompt on Claude Fable 5.1 Max (llm_analyst_prompt.md).
One entry is committed with the pre-registration (entry 0) and one at each checkpoint. Track 2 picks
are pasted exactly as the model returned them; the log is Track 2's chain of custody.

================================================================================
ENTRY 0 — committed in the pre-registration commit (target: Sun 9/20/2026)
================================================================================
Data through 8/31/2026 (the released panel, panel_returns_2026-08-31.csv,
SHA-256 c9d3340eba3a3301a63bb788c87f1d6e9e55de58a3fec16b12a34b313cac076b).
Both tracks' September 2026 holdings are chosen from data through August 2026; neither is scored yet.
September is scored at checkpoint 1 (after the 9/30 extension file posts).

TRACK 1 (locked rule) — September 2026 holdings, 20 names, equal weight.
Selected by strategy.py from the released panel; signal window Sep 2025 – Feb 2026 (rows 80–85).
Alphabetical:
AMRX, AROC, BTU, CNX, DY, FLS, FORM, FRPT, GMED, HP, IONS, LUMN, MSGS, MTRN, NOV, OII, PSMT, PTEN, SLAB, VIAV

TRACK 2 (frozen prompt) — run once on the 8/31/2026 briefing table.
Model: Claude Fable 5.1 (effort "Max"), claude.ai, new empty chat, no tools/web/connectors, no files
beyond the pasted table. Run: 9/15/2026 (this instructor example was assembled 9/15; in a student
submission the run happens once in the 9/10–9/20 window and is committed by 9/20). Output parsed on
the first try (exactly 20 valid, distinct tickers; no prose); no retry needed. September picks pasted
verbatim, in the model's order:
PBF, DK, OII, PTEN, AMRX, HAE, LNTH, CHEF, PSMT, MSGS, STGW, CNK, ZD, MTRN, ASH, EAT, ETSY, AMG, AVT, SLAB

Overlap of the two September lists: 7 of 20 (AMRX, MSGS, MTRN, OII, PSMT, PTEN, SLAB). The frozen
analyst leaned harder into the strongest recent movers (energy and refiners — PBF, DK, OII, PTEN — and
high-3-month names like CHEF, EAT, ETSY) than the intermediate-momentum rule, which by construction
ignores the last six months; the divergence is itself a finding to revisit once the live months score.

Nothing is concluded from entry 0: three live months have not happened. The purpose of entry 0 is to
lock both portfolios under the commit hash before the evaluation window opens.

--------------------------------------------------------------------------------
CHECKPOINT 1 — target Sun 10/11/2026 — commit hash <9/20 hash> quoted   [TEMPLATE — not yet due]
--------------------------------------------------------------------------------
New month added: September 2026 (extension file panel_returns_2026-09-30.csv, posted within two days
of month-end; run that day; commit the dated file with this entry and confirm its SHA-256).
1. Rerun strategy.py unchanged on the extended panel; confirm its September holdings match entry 0's
   Track 1 list to the name (20/20). A mismatch means the code or the data vintage changed.
2. Score entry-0 holdings on September's return: Track 1 __%, Track 2 __%, EW benchmark __% (month).
3. Record October holdings, chosen from data through 9/30:
   TRACK 1 (locked rule): [20 tickers]
   TRACK 2 (frozen prompt) run once on the 9/30 briefing table (date/time): [20 tickers, verbatim]
4. Attribution, 3–5 sentences: which side led, whether the gap is inside the pre-registered placebo
   span, and what (if anything) the one month changes — which is almost always "nothing yet."

--------------------------------------------------------------------------------
CHECKPOINT 2 — target Sun 11/8/2026   [TEMPLATE — not yet due]
--------------------------------------------------------------------------------
New month: October 2026. Rerun; confirm October holdings match checkpoint 1's Track 1 list. Score
the checkpoint-1 holdings on October. Record November holdings for both tracks (LLM run once on the
10/31 table). Attribution.

--------------------------------------------------------------------------------
CHECKPOINT 3 — target Sun 12/6/2026   [TEMPLATE — not yet due]
--------------------------------------------------------------------------------
New month: November 2026. Rerun; confirm November holdings match checkpoint 2's Track 1 list. Score
the checkpoint-2 holdings on November. No new holdings are recorded (the live window ends). Attribution
plus a pointer to the final report's placebo test and verdict.
