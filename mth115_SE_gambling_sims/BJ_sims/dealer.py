"""
Roulette dealer. European wheel: 0-36, where 0 is green (house win on
red/black bets), 1-36 split evenly between red and black.

We simulate a simple "bet on red" strategy - pays 1:1 on a red number,
loses on black or green. House edge: 1/37 ≈ 2.70%.

The bot only makes betting decisions (amount). The dealer handles the spin
and payout. Interface matches the old blackjack Dealer: play_round(bet)
returns +bet on win, -bet on loss, 0 on push (roulette has no pushes on
simple red/black bets, but we keep the return type for compatibility).
"""
import random

# European roulette: 18 red, 18 black, 1 green (the 0).
# Red numbers (standard European wheel):
RED_NUMBERS = {1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36}


class Dealer:
    """Spins a European roulette wheel. Bot always bets on red."""

    def __init__(self, rng=None):
        self.rng = rng or random.Random()

    def play_round(self, bet):
        """
        Spin the wheel. Returns:
            +bet on red (win)
            -bet on black or green (loss)

        No pushes in simple red/black roulette.
        """
        spin = self.rng.randint(0, 36)
        if spin in RED_NUMBERS:
            return bet  # 1:1 payout on red
        return -bet
