"""
strategy.py — LOCKED STRATEGY CODE (Track 1)   ·   FINTECH-P2-Example   ·   FINA 4075/5075, Fall 2026

Rule (see strategy_rules.md, which governs if the two ever disagree):
  Intermediate momentum, months t-12 through t-7.  For the portfolio held in month t, rank the 200
  stocks by their compounded total return over the SIX monthly returns t-12, t-11, ..., t-7
  (the most recent six months, t-6 .. t-1, are skipped entirely).  Hold the top 20, equal weights,
  rebalanced at every month-end from data through the prior month-end only.  10 bp per side.

CODE RULE: this file is read-only after the 9/20/2026 pre-registration commit.  At each checkpoint
the panel is extended by one month and this code is rerun unchanged.
"""
import numpy as np
import pandas as pd

PER_SIDE = 0.0010        # transaction cost, 10 basis points per side
N_HOLD = 20              # holding count (the top decile of the 200-stock panel)
WINDOW_START = 12        # window starts WINDOW_START months before month t  (t-12)
WINDOW_END = 7           # window ends   WINDOW_END   months before month t  (t-7), inclusive
FIRST_TRADEABLE = WINDOW_START   # the first month t whose window exists is row 12 (January 2020)


def load_panel(panel_path, ticker_path):
    """Read the course packet.  Returns (rets, dates, tickers, info).

    rets    : numpy array, T x N, simple monthly total returns (row 0 = January 2019)
    dates   : the month-end dates of the rows
    tickers : list of the N ticker symbols, in the column order of the panel
    info    : the company list (ticker, company, sector, ...) indexed by ticker
    """
    panel = pd.read_csv(panel_path, index_col=0, parse_dates=True)
    info = pd.read_csv(ticker_path).set_index("Ticker")
    tickers = list(panel.columns)
    assert list(info.index) == tickers, "ticker list and panel columns differ"
    assert not panel.isna().any().any(), "panel has missing values"
    return panel.to_numpy(), panel.index, tickers, info


def signal(t, rets):
    """Compounded return over rows t-12 .. t-7 inclusive (six monthly returns).

    Python slicing excludes the stop index, so rows t-12 .. t-7 are rets[t-12 : t-6].
    """
    window = rets[t - WINDOW_START : t - WINDOW_END + 1]
    assert window.shape[0] == WINDOW_START - WINDOW_END + 1 == 6
    return np.prod(1 + window, axis=0) - 1


def select_holdings(t, rets, tickers):
    """The 20 stocks held during month t: highest signal first; ties broken by alphabetical ticker.

    A stock with any missing return in its t-12..t-7 window is ineligible for month t (rules: MISSING
    DATA). The released panel has no gaps, so every stock is eligible in-sample; this guard governs
    the live window, where an extension file could carry a delisted name's partial history.
    """
    window = rets[t - WINDOW_START : t - WINDOW_END + 1]
    eligible = ~np.isnan(window).any(axis=0)
    sig = signal(t, rets)
    cand = [i for i in range(len(tickers)) if eligible[i]]
    order = sorted(cand, key=lambda i: (-sig[i], tickers[i]))
    return set(order[:N_HOLD])


def run_track(select_fn, rets, t0, t1, per_side=PER_SIDE):
    """Paper-trade a selection rule from month t0 to month t1 (row indices, inclusive).

    Course conventions: equal weights; one-way turnover = names replaced / 20 (the first month
    counts as a full purchase); monthly cost = 2 x per_side x turnover; growth path starts at 1.0.
    Returns (values, turnovers, holdings) with len(values) == months + 1.
    """
    prev, vals, turns, holdings = set(), [1.0], [], []
    for t in range(t0, t1 + 1):
        hold = select_fn(t, rets)
        turn = 1.0 if not prev else len(hold - prev) / N_HOLD
        gross = rets[t, sorted(hold)].mean()
        vals.append(vals[-1] * (1 + gross - 2 * per_side * turn))
        prev = hold
        turns.append(turn)
        holdings.append(hold)
    return np.array(vals), np.array(turns), holdings


def bench(rets, t0, t1):
    """Equal-weighted average of all 200 stocks, rebalanced monthly, no costs."""
    vals = [1.0]
    for t in range(t0, t1 + 1):
        vals.append(vals[-1] * (1 + rets[t].mean()))
    return np.array(vals)


def stats(vals, turns=None):
    """CAGR, annualized volatility, Sharpe (rf = 0), maximum drawdown, annual one-way turnover."""
    months = len(vals) - 1
    monthly = vals[1:] / vals[:-1] - 1
    cagr = vals[-1] ** (12 / months) - 1
    vol = monthly.std(ddof=1) * np.sqrt(12)
    maxdd = (vals / np.maximum.accumulate(vals) - 1).min()
    out = {"CAGR": cagr, "Annualized volatility": vol, "Sharpe (rf = 0)": cagr / vol,
           "Maximum drawdown": maxdd, "Growth of $10,000": 10000 * vals[-1]}
    if turns is not None:
        out["Annual one-way turnover"] = turns.mean() * 12
        out["Cost drag per year"] = 2 * PER_SIDE * turns.mean() * 12
    return out
