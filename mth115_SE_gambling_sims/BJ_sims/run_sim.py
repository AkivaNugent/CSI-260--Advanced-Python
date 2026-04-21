"""
Run the roulette simulation.

Usage (from roulette_sim/ directory):
    python run_sim.py --bots 10000 --strategy flat --base-bet 100 --pool 10000
    python run_sim.py --bots 10000 --strategy martingale --base-bet 100 \
        --pool 10000 --table-max 50000

Two CSVs are written:
  - rounds.csv: one row per round per bot (good for time-series plots)
  - summary.csv: one row per bot (good for distribution plots)

Names file: one name per line. If the file has fewer names than bots,
they wrap around. Use --skip-header if the first line is a CSV header.
"""
import argparse
import csv
import random
import sys
import time
from pathlib import Path

from bot import Bot
from dealer import Dealer
from strategies import STRATEGIES


def load_names(path, num_bots, skip_header=False):
    """Load names from a file, one per line. Wraps if not enough names."""
    if path is None:
        return [f"Bot_{i+1:04d}" for i in range(num_bots)]
    lines = [line.strip() for line in Path(path).read_text().splitlines() if line.strip()]
    if skip_header and lines:
        lines = lines[1:]
    if not lines:
        return [f"Bot_{i+1:04d}" for i in range(num_bots)]
    return [lines[i % len(lines)] for i in range(num_bots)]


def run_simulation(
    num_bots,
    strategy_name,
    base_bet,
    starting_pool,
    table_max=50_000,
    names_file=None,
    skip_header=False,
    rounds_csv='rounds.csv',
    summary_csv='summary.csv',
    seed=None,
    max_rounds_per_bot=100_000,
    progress_every=500,
):
    """Run num_bots bots sequentially and write both CSVs."""
    if seed is not None:
        master_rng = random.Random(seed)
    else:
        master_rng = random.Random()

    names = load_names(names_file, num_bots, skip_header=skip_header)

    rounds_fields = [
        'bot_id', 'bot_name', 'strategy', 'round',
        'desired_bet', 'actual_bet', 'capped',
        'result', 'net', 'playing_pool', 'winnings', 'total_money',
    ]
    summary_fields = [
        'bot_id', 'bot_name', 'strategy', 'base_bet', 'starting_pool',
        'table_max', 'rounds_played', 'rounds_capped',
        'final_playing_pool', 'final_winnings',
        'final_total', 'net_profit',
    ]

    start_time = time.time()

    with open(rounds_csv, 'w', newline='') as rf, \
         open(summary_csv, 'w', newline='') as sf:
        rounds_writer = csv.DictWriter(rf, fieldnames=rounds_fields)
        rounds_writer.writeheader()
        summary_writer = csv.DictWriter(sf, fieldnames=summary_fields)
        summary_writer.writeheader()

        for i in range(num_bots):
            bot_rng = random.Random(master_rng.random())
            dealer = Dealer(rng=bot_rng)
            bot = Bot(
                name=names[i],
                strategy_name=strategy_name,
                base_bet=base_bet,
                starting_pool=starting_pool,
                table_max=table_max,
            )

            rounds_capped = 0
            for record in bot.play_until_broke(dealer, max_rounds=max_rounds_per_bot):
                record['bot_id'] = i + 1
                if record['capped']:
                    rounds_capped += 1
                rounds_writer.writerow(record)

            summary_writer.writerow({
                'bot_id': i + 1,
                'bot_name': bot.name,
                'strategy': bot.strategy_name,
                'base_bet': bot.base_bet,
                'starting_pool': bot.starting_pool,
                'table_max': bot.table_max,
                'rounds_played': bot.rounds_played,
                'rounds_capped': rounds_capped,
                'final_playing_pool': bot.playing_pool,
                'final_winnings': bot.winnings,
                'final_total': bot.total_money(),
                'net_profit': bot.total_money() - bot.starting_pool,
            })

            if progress_every and (i + 1) % progress_every == 0:
                elapsed = time.time() - start_time
                print(f"  {i+1}/{num_bots} bots done ({elapsed:.1f}s)",
                      file=sys.stderr)

    elapsed = time.time() - start_time
    print(f"\nSimulation complete: {num_bots} bots, {elapsed:.1f}s", file=sys.stderr)
    print(f"  Rounds CSV:  {rounds_csv}", file=sys.stderr)
    print(f"  Summary CSV: {summary_csv}", file=sys.stderr)


def main():
    parser = argparse.ArgumentParser(description="Roulette bot simulation")
    parser.add_argument('--bots', type=int, default=10000)
    parser.add_argument('--strategy', choices=list(STRATEGIES), default='paroli')
    parser.add_argument('--base-bet', type=float, default=100.0)
    parser.add_argument('--pool', type=float, default=100000.0,
                        help='starting playing pool per bot')
    parser.add_argument('--table-max', type=float, default=50_000.0,
                        help='maximum bet allowed at the table (default $50k)')
    parser.add_argument('--names-file', type=str, default="BOTNAMES.csv",
                        help='one name per line; wraps if too short')
    parser.add_argument('--skip-header', action='store_true',
                        help='skip the first line of the names file')
    parser.add_argument('--rounds-csv', type=str, default='rounds.csv')
    parser.add_argument('--summary-csv', type=str, default='summary.csv')
    parser.add_argument('--seed', type=int, default=None)
    parser.add_argument('--max-rounds', type=int, default=100_000,
                        help='safety cap on rounds per bot')
    args = parser.parse_args()

    run_simulation(
        num_bots=args.bots,
        strategy_name=args.strategy,
        base_bet=args.base_bet,
        starting_pool=args.pool,
        table_max=args.table_max,
        names_file=args.names_file,
        skip_header=args.skip_header,
        rounds_csv=args.rounds_csv,
        summary_csv=args.summary_csv,
        seed=args.seed,
        max_rounds_per_bot=args.max_rounds,
    )


if __name__ == '__main__':
    main()
