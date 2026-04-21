"""
Analyze simulation output and produce plots.

Usage:
    python analyze.py                           # uses rounds.csv & summary.csv
    python analyze.py --rounds-csv r.csv --summary-csv s.csv --out-dir plots/

Produces:
  - total_money_over_time.png : the big pile of money shrinking
  - final_distribution.png    : histogram of final net profit per bot
  - sample_trajectories.png   : individual bot money-over-time (sample)
"""
import argparse
import csv
from collections import defaultdict
from pathlib import Path

import matplotlib
matplotlib.use('Agg')  # no display needed
import matplotlib.pyplot as plt


def load_rounds(path):
    """
    Load rounds CSV into a dict: bot_id -> list of (round_num, total_money).
    Also returns the base_bet and starting_pool for context (inferred).
    """
    by_bot = defaultdict(list)
    with open(path) as f:
        for row in csv.DictReader(f):
            bot_id = int(row['bot_id'])
            rnd = int(row['round'])
            total = float(row['total_money'])
            by_bot[bot_id].append((rnd, total))
    return by_bot


def load_summary(path):
    rows = []
    with open(path) as f:
        for row in csv.DictReader(f):
            rows.append({
                'bot_id': int(row['bot_id']),
                'bot_name': row['bot_name'],
                'strategy': row['strategy'],
                'base_bet': float(row['base_bet']),
                'starting_pool': float(row['starting_pool']),
                'rounds_played': int(row['rounds_played']),
                'final_total': float(row['final_total']),
                'net_profit': float(row['net_profit']),
            })
    return rows


def plot_total_money_over_time(by_bot, summary_rows, out_path):
    """
    The headline plot: total money across ALL bots, summed per round.

    Trick: different bots play different numbers of rounds. Once a bot
    goes bust, it contributes its final total (which is just its winnings,
    since playing_pool hit 0) to every subsequent round.
    """
    if not by_bot:
        print("No round data to plot.")
        return

    # Max round reached by any bot
    max_round = max(r for trajectories in by_bot.values() for r, _ in trajectories)

    # For each bot, build a full trajectory of length max_round.
    # After the bot busts, carry forward its final total_money.
    num_bots = len(by_bot)
    totals_per_round = [0.0] * (max_round + 1)  # index 0 = starting state

    # Starting pile: everyone starts with their starting_pool
    starting_pile = sum(r['starting_pool'] for r in summary_rows)
    totals_per_round[0] = starting_pile

    for bot_id, trajectory in by_bot.items():
        # trajectory is list of (round_num, total_money), sorted by round
        trajectory.sort(key=lambda x: x[0])
        last_total = None
        idx = 0
        for round_num in range(1, max_round + 1):
            # Advance through this bot's trajectory until we find round_num
            while idx < len(trajectory) and trajectory[idx][0] < round_num:
                last_total = trajectory[idx][1]
                idx += 1
            if idx < len(trajectory) and trajectory[idx][0] == round_num:
                last_total = trajectory[idx][1]
                idx += 1
            # If bot never reached this round, last_total is its last-seen value
            # (or None if it didn't play any rounds, which shouldn't happen)
            if last_total is None:
                # Fall back to the bot's starting pool
                for s in summary_rows:
                    if s['bot_id'] == bot_id:
                        last_total = s['starting_pool']
                        break
            totals_per_round[round_num] += last_total

    fig, ax = plt.subplots(figsize=(11, 6))
    ax.plot(range(len(totals_per_round)), totals_per_round,
            color='#2b7a3e', linewidth=2)
    ax.fill_between(range(len(totals_per_round)), 0, totals_per_round,
                    color='#2b7a3e', alpha=0.25)
    ax.axhline(y=starting_pile, color='gray', linestyle='--',
               linewidth=1, label=f'Starting pile: ${starting_pile:,.0f}')
    ax.set_xlabel('Round number')
    ax.set_ylabel('Total money across all bots ($)')
    strategy = summary_rows[0]['strategy'] if summary_rows else 'unknown'
    base_bet = summary_rows[0]['base_bet'] if summary_rows else 0
    ax.set_title(f'The Pile Shrinks: {num_bots} bots, {strategy} strategy, '
                 f'base bet ${base_bet:.0f}')
    ax.legend()
    ax.grid(True, alpha=0.3)
    ax.ticklabel_format(axis='y', style='plain')
    fig.tight_layout()
    fig.savefig(out_path, dpi=130)
    plt.close(fig)
    print(f"  Wrote {out_path}")


def plot_final_distribution(summary_rows, out_path):
    """Histogram of net profit per bot. Should be centered below 0 (house wins)."""
    if not summary_rows:
        return
    profits = [r['net_profit'] for r in summary_rows]
    mean_profit = sum(profits) / len(profits)

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.hist(profits, bins=50, color='#c43d3d', alpha=0.75, edgecolor='black', linewidth=0.4)
    ax.axvline(x=0, color='black', linestyle='-', linewidth=1, label='Break even')
    ax.axvline(x=mean_profit, color='blue', linestyle='--', linewidth=1.5,
               label=f'Mean: ${mean_profit:,.2f}')
    ax.set_xlabel('Net profit per bot ($)')
    ax.set_ylabel('Number of bots')
    strategy = summary_rows[0]['strategy']
    ax.set_title(f'Final outcomes distribution ({strategy} strategy, n={len(summary_rows)})')
    ax.legend()
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    fig.savefig(out_path, dpi=130)
    plt.close(fig)
    print(f"  Wrote {out_path}")


def plot_sample_trajectories(by_bot, summary_rows, out_path, sample_size=30):
    """Plot individual money-over-time for a random sample of bots."""
    import random
    if not by_bot:
        return
    bot_ids = list(by_bot.keys())
    sample = random.sample(bot_ids, min(sample_size, len(bot_ids)))

    fig, ax = plt.subplots(figsize=(11, 6))
    for bot_id in sample:
        traj = sorted(by_bot[bot_id], key=lambda x: x[0])
        rounds = [0] + [r for r, _ in traj]
        # Prepend starting pool
        starting = next(s['starting_pool'] for s in summary_rows if s['bot_id'] == bot_id)
        totals = [starting] + [t for _, t in traj]
        ax.plot(rounds, totals, alpha=0.45, linewidth=0.9)

    ax.set_xlabel('Round number')
    ax.set_ylabel('Bot total money ($)')
    strategy = summary_rows[0]['strategy']
    ax.set_title(f'Individual bot trajectories (sample of {len(sample)}, {strategy})')
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    fig.savefig(out_path, dpi=130)
    plt.close(fig)
    print(f"  Wrote {out_path}")


def print_stats(summary_rows):
    """Print quick summary statistics."""
    if not summary_rows:
        return
    n = len(summary_rows)
    profits = [r['net_profit'] for r in summary_rows]
    rounds = [r['rounds_played'] for r in summary_rows]
    mean_p = sum(profits) / n
    var_p = sum((p - mean_p) ** 2 for p in profits) / n
    std_p = var_p ** 0.5
    winners = sum(1 for p in profits if p > 0)
    losers = sum(1 for p in profits if p < 0)
    break_even = n - winners - losers

    print(f"\n--- Summary ({summary_rows[0]['strategy']}) ---")
    print(f"  Bots:                {n}")
    print(f"  Avg rounds played:   {sum(rounds)/n:.1f}")
    print(f"  Mean net profit:     ${mean_p:,.2f}")
    print(f"  Std dev of profit:   ${std_p:,.2f}")
    print(f"  Bots that won $:     {winners}  ({100*winners/n:.1f}%)")
    print(f"  Bots that lost $:    {losers}  ({100*losers/n:.1f}%)")
    print(f"  Bots at break-even:  {break_even}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--rounds-csv', default='rounds.csv')
    parser.add_argument('--summary-csv', default='summary.csv')
    parser.add_argument('--out-dir', default='plots')
    args = parser.parse_args()

    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    print("Loading data...")
    by_bot = load_rounds(args.rounds_csv)
    summary_rows = load_summary(args.summary_csv)

    print_stats(summary_rows)

    print("\nPlotting...")
    plot_total_money_over_time(by_bot, summary_rows, out_dir / 'total_money_over_time.png')
    plot_final_distribution(summary_rows, out_dir / 'final_distribution.png')
    plot_sample_trajectories(by_bot, summary_rows, out_dir / 'sample_trajectories.png')


if __name__ == '__main__':
    main()
