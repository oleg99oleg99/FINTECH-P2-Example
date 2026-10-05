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
CHECKPOINT 1 — committed Mon 10/5/2026 (due Sun 10/11/2026) — pre-registration commit 293cd99 quoted
--------------------------------------------------------------------------------
(293cd99 is the commit that locked the rules, code, prompt, red-team log and entry 0 on 9/15; the panel
file was added in 111e4f8 and the last pre-deadline commit is 0e9a61c. A student pair quotes its single
9/20 hash here.)

New month added: September 2026. Extension file panel_returns_2026-09-30.csv — 93 rows, the 92 released
rows unchanged plus 2026-09-30; posted 10/5/2026; SHA-256
d9417fdf2892769b1662aeb6a82b13d6f96199416ae8b082977b5d3f43e8acea (matches the Data Dictionary) —
committed with this entry. Rerun the same day the file posted.

1. Rerun check. strategy.py is byte-identical to the 9/20 commit. Run unchanged on the extended panel, it
   selects the same September 2026 portfolio as entry 0: 20/20 names match (window Sep 2025 – Feb 2026,
   rows 80–85). Code and data vintage are intact.

2. Entry-0 holdings scored on September 2026 (equal weights; the first live month counts as a full
   purchase for both tracks, cost = 2 x 0.0010 x 1.0 = 0.20%; benchmark = equal-weighted panel, no costs):
   Mechanical (Track 1): gross -3.43%, net -3.63%, gap vs benchmark +2.15pp  |  LLM (Track 2): gross
   -0.64%, net -0.84%, gap vs benchmark +4.94pp  |  Benchmark (EW, 200 names): -5.78% (month).
   Biggest movers inside the lists: FORM +48.4%, VIAV +15.5%, AMRX +15.3%, MTRN +14.2% up; IONS -26.0%,
   BTU -17.9%, FRPT -17.6%, OII -15.7%, EAT -15.3%, HP -14.8% down.

3. October 2026 holdings, chosen from data through 9/30/2026:
   TRACK 1 (locked rule) — signal window Oct 2025 – Mar 2026 (rows 81–86); 20 names, equal weight,
   alphabetical:
   CWEN, FORM, GMED, HCC, HP, IRDM, KEX, LNTH, MSGS, MTDR, MUR, NOV, NYT, OII, PBF, PTEN, SLAB, TDW, VIAV, WLK
   11 of 20 names replaced versus September (October one-way turnover 0.55; cost 0.11%, charged when
   October is scored). Dropped: AMRX, AROC, BTU, CNX, DY, FLS, FRPT, IONS, LUMN, MTRN, PSMT.
   TRACK 2 (frozen prompt) — run once on the 9/30/2026 briefing table: Mon 10/5/2026, 12:55 AM Central.
   Claude Fable 5.1 (effort "Max"), claude.ai, new empty chat, web search and memory off, no files beyond
   the pasted table; the message was the committed prompt, one blank line, the table unedited. Output
   parsed on the first try (exactly 20 valid, distinct tickers; no prose); no retry. October picks pasted
   verbatim, in the model's order:
   PBF, DK, PTEN, WHD, TDW, SM, HAE, AMRX, RGEN, BIO, BRKR, ICUI, CHEF, EAT, QLYS, AVT, HCC, STGW, ZD, AMG
   Overlap of the two October lists: 4 of 20 (HCC, PBF, PTEN, TDW).

4. Attribution. Both tracks beat the equal-weighted panel in a month when the panel itself fell 5.8%,
   and the frozen analyst beat the rule. The rule's energy names (BTU, CNX, HP, NOV, OII, PTEN) led its
   losses while FORM, VIAV, AMRX and MTRN offset most of them; the analyst had skipped the coal and gas
   names, held AMRX, MTRN and AVT, and its refiners (PBF, DK) held up. Run on September alone, the
   pre-registered placebo (1,000 random 20-stock portfolios, same costs) puts Track 1's +2.15pp at the
   90th percentile and Track 2's +4.94pp at the 99.6th — an unusual month for the analyst, but the 5th to
   95th percentile band of one-month gaps is -2.8pp to +3.1pp, so one month distinguishes nothing; the
   three-month test in December is the evidence, and nothing in the rules, the code or the prompt changes.

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
