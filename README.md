# FINTECH-P2-Example

Worked example for **Project 2 — The Strategy Lab** (FINA 4075/5075, FinTech Foundations & Applications, Fall 2026). This private repo is the pre-registration a pair commits by **Sunday 9/20**: a mechanical strategy and a frozen LLM analyst, locked in one timestamped commit so neither can be quietly changed once the live window opens.

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
| `panel_returns_2026-08-31.csv` | The returns panel (added via **Add file → Upload files** to preserve its exact bytes; SHA-256 `c9d3340eba3a3301a63bb788c87f1d6e9e55de58a3fec16b12a34b313cac076b`, matching the Data Dictionary). At each checkpoint the dated extension file is committed here too. |

Nothing here concludes anything about the strategy — three live months have not happened yet. The point of the commit is to lock both portfolios before they can be scored.
