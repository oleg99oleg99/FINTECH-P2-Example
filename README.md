# FINTECH-P2-Example

Worked example for **Project 2 — The Strategy Lab** (FINA 4075/5075, FinTech Foundations & Applications, Fall 2026). This repo is the pre-registration a pair commits by **Sunday 9/20** (and, below it, the checkpoint entries that follow): a mechanical strategy and a frozen LLM analyst, locked in one timestamped commit so neither can be quietly changed once the live window opens.

- **Track 1 (mechanical):** intermediate momentum, months t-12 through t-7 — top 20 of 200, equal weights, 10 bp per side. See `P2/strategy_rules.md` and `P2/strategy.py`.
- **Track 2 (AI analyst):** a frozen prompt run once a month on a standardized briefing table. Model: **Claude Fable 5.1 Max**. See `P2/llm_analyst_prompt.md`.

## Files in `P2/`
| File | What it is |
|---|---|
| `strategy_rules.md` | The locked rule, in words a stranger could implement identically. Governs if the code and the text ever disagree. |
| `strategy.py` | The locked strategy code (Track 1). Read-only after 9/20; rerun unchanged at each checkpoint. |
| `llm_analyst_prompt.md` | The frozen Track 2 prompt: model, settings, run schedule, output format, one-retry rule. |
| `redteam_log.md` | Five ambiguities a second AI (Gemini) found in the rules file, and the fixes. |
| `monitoring_log.md` | Entry 0 (both tracks' September holdings), then one entry per checkpoint. Track 2 picks are pasted verbatim. |
| `AI_Audit_Note.md` | Individual AI audit note (tool log, prompts, errors caught, verification table). |
| `FINA4075_P2_StrategyLab.ipynb` | The Colab notebook that produces every number: hash check, backtest exhibit, hand check, briefing generator, entry-0 selection. |
| `FINA4075_P2_StrategyLab_executed.ipynb` | The same notebook with its outputs, run in Colab on the pinned runtime (9/22). |
| `FINA4075_P2_StrategyLab_2026-09-30.ipynb` | **Checkpoint 1 (10/5):** the 9/20 notebook pointed at the extension file, plus the checkpoint cells (rerun check, September scored, October holdings, placebo preview, Track 2 paste). Diff it against the original: the strategy code is unchanged. |
| `FINA4075_P2_StrategyLab_executed_2026-09-30.ipynb` | The checkpoint-1 notebook with its outputs (pinned package versions). |
| `panel_returns_2026-09-30.csv` | **Checkpoint 1 extension file:** the 92 released rows unchanged + September 2026 (93 x 200). SHA-256 `d9417fdf2892769b1662aeb6a82b13d6f96199416ae8b082977b5d3f43e8acea`, matching the Data Dictionary. |
| `panel_returns_2026-08-31.csv` | The returns panel (committed with its exact bytes preserved — the walkthrough uses **Add file → Upload files** for a data CSV; SHA-256 `c9d3340eba3a3301a63bb788c87f1d6e9e55de58a3fec16b12a34b313cac076b`, matching the Data Dictionary). At each checkpoint the dated extension file is committed here too. |

## Checkpoint 1 (committed 10/5/2026, due Sun 10/11)
September 2026 scored on the entry-0 holdings: **Track 1 −3.63% net · Track 2 −0.84% net · EW benchmark −5.78%.** The locked code rerun on the extension file reproduced entry 0's September list 20/20. October holdings — Track 1 (locked rule): `CWEN, FORM, GMED, HCC, HP, IRDM, KEX, LNTH, MSGS, MTDR, MUR, NOV, NYT, OII, PBF, PTEN, SLAB, TDW, VIAV, WLK`; Track 2 (frozen prompt, run once 10/5, verbatim): `PBF, DK, PTEN, WHD, TDW, SM, HAE, AMRX, RGEN, BIO, BRKR, ICUI, CHEF, EAT, QLYS, AVT, HCC, STGW, ZD, AMG`. Details and attribution in `P2/monitoring_log.md`.

One live month concludes nothing about the strategy — the pre-registered placebo band for a single month is about −3 to +3 percentage points around the benchmark. The point of the commits is to lock each month's portfolios before they can be scored.
