"""
Compute the average amount wagered per bot from rounds.csv in the
current directory. Prints the result to console.

Usage: put this script in the same folder as a rounds.csv, then run:
    python avg_wagered.py
"""
import csv
from collections import defaultdict


def main():
    wagered = defaultdict(float)
    with open('../flat_100/rounds.csv') as f:
        for row in csv.DictReader(f):
            bot_id = int(row['bot_id'])
            wagered[bot_id] += float(row['actual_bet'])

    if not wagered:
        print("No data found in rounds.csv")
        return

    total = sum(wagered.values())
    num_bots = len(wagered)
    avg = total / num_bots

    print(f"Bots:              {num_bots:,}")
    print(f"Total wagered:     ${total:,.2f}")
    print(f"Avg wagered/bot:   ${avg:,.2f}")


if __name__ == '__main__':
    main()
