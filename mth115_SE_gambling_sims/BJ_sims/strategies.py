"""
Betting strategies. To add a new strategy:
  1. Subclass Strategy
  2. Implement next_bet(self, playing_pool, winnings)
  3. Implement record_result(self, won, net_amount) to update internal state
  4. Optionally override should_stop(self, playing_pool, winnings) if your
     strategy has a "cash out" condition (e.g. Paroli hitting a target)
  5. Register it in STRATEGIES at the bottom

The strategy only sees the bot's money state and the result of the last
hand. It decides bet size only - the dealer handles the game, and the Bot
handles table-max enforcement and all-in fallback.

IMPORTANT for martingale-family strategies: the strategy tracks its
*desired* bet based on its own logic. If the table max or pool forces a
smaller actual bet, the strategy still updates based on the RESULT
(win/loss), not on how much was actually wagered.
"""


class Strategy:
    """Base class for all betting strategies."""

    name = "base"

    def __init__(self, base_bet):
        self.base_bet = base_bet

    def next_bet(self, playing_pool, winnings):
        """Return desired bet (before table-max/pool clamping)."""
        raise NotImplementedError

    def record_result(self, won, net_amount):
        """
        Update internal state after a round.
          won: True/False/None (None = push)
          net_amount: signed net change from the round
        """
        pass

    def should_stop(self, playing_pool, winnings):
        """
        Return True if the strategy has achieved its goal and wants to stop.
        Default: never stop voluntarily. Paroli and Labouchere override this.
        """
        return False

    def reset(self):
        """Reset to initial state."""
        pass


# ---------------------------------------------------------------------------
# Flat
# ---------------------------------------------------------------------------

class FlatBet(Strategy):
    """Always bet the same base amount. The control case."""
    name = "flat"

    def next_bet(self, playing_pool, winnings):
        return self.base_bet


# ---------------------------------------------------------------------------
# Classic Martingale (double on loss, reset on win)
# ---------------------------------------------------------------------------

class Martingale(Strategy):
    """Double the bet after every loss, reset to base after any win."""
    name = "martingale"

    def __init__(self, base_bet):
        super().__init__(base_bet)
        self.current_bet = base_bet

    def next_bet(self, playing_pool, winnings):
        return self.current_bet

    def record_result(self, won, net_amount):
        if won is True:
            self.current_bet = self.base_bet
        elif won is False:
            self.current_bet *= 2

    def reset(self):
        self.current_bet = self.base_bet


# ---------------------------------------------------------------------------
# Paroli (reverse martingale): double on WIN, cash out at target or 3 wins
# ---------------------------------------------------------------------------

class Paroli(Strategy):
    """
    Reverse martingale. After a WIN, double the bet (riding the hot streak).
    After 3 consecutive wins, reset to base and "lock in" the profit from
    the streak. After a LOSS, reset to base.

    Stop condition: when total money (pool + winnings) reaches PAROLI_TARGET,
    the bot cashes out. Hardcoded to $200,000 (doubling a $100k start).
    """
    name = "paroli"

    PAROLI_TARGET = 200_000  # hardcoded per spec
    STREAK_RESET = 3         # reset to base after this many consecutive wins

    def __init__(self, base_bet):
        super().__init__(base_bet)
        self.current_bet = base_bet
        self.win_streak = 0

    def next_bet(self, playing_pool, winnings):
        return self.current_bet

    def record_result(self, won, net_amount):
        if won is True:
            self.win_streak += 1
            if self.win_streak >= self.STREAK_RESET:
                # Three wins in a row: take the profits, start over
                self.current_bet = self.base_bet
                self.win_streak = 0
            else:
                # Ride the streak: double up for the next bet
                self.current_bet *= 2
        elif won is False:
            # Streak broken, reset to base
            self.current_bet = self.base_bet
            self.win_streak = 0
        # Push: keep current bet and streak as-is

    def should_stop(self, playing_pool, winnings):
        return (playing_pool + winnings) >= self.PAROLI_TARGET

    def reset(self):
        self.current_bet = self.base_bet
        self.win_streak = 0


# ---------------------------------------------------------------------------
# Labouchère (cancellation system): graduated sequence, cash out when empty
# ---------------------------------------------------------------------------

class Labouchere(Strategy):
    """
    Cancellation betting system. Player writes down a sequence of numbers
    summing to their desired profit. Bet = first + last numbers.
      - On WIN: cross off both the first and last numbers.
      - On LOSS: append the lost amount (the bet) to the end.
    When the sequence is empty, the target profit has been achieved.

    We use the graduated textbook version: sequence = [1, 2, 3, ..., n].
    Sum of 1..n = n(n+1)/2. Each number represents `base_bet` dollars
    (the "unit size"), so profit target = base_bet * n(n+1)/2.

    With LABOUCHERE_N=14 and base_bet=$1000, sequence is
    [1000, 2000, ..., 14000] summing to $105,000 - roughly doubling
    a $100k starting pool.
    """
    name = "labouchere"

    LABOUCHERE_N = 14  # sequence [1, 2, ..., 14], sum = 105 units.
                       # With base_bet=$1000, target profit = $105,000.

    def __init__(self, base_bet):
        super().__init__(base_bet)
        self.sequence = list(range(1, self.LABOUCHERE_N + 1))

    def next_bet(self, playing_pool, winnings):
        if not self.sequence:
            return 0
        if len(self.sequence) == 1:
            return self.sequence[0] * self.base_bet
        return (self.sequence[0] + self.sequence[-1]) * self.base_bet

    def record_result(self, won, net_amount):
        if not self.sequence:
            return
        if won is True:
            # Cross off first and last
            if len(self.sequence) <= 2:
                self.sequence = []
            else:
                self.sequence = self.sequence[1:-1]
        elif won is False:
            # Append the lost amount (in units) to the end
            if len(self.sequence) == 1:
                lost_units = self.sequence[0]
            else:
                lost_units = self.sequence[0] + self.sequence[-1]
            self.sequence.append(lost_units)

    def should_stop(self, playing_pool, winnings):
        return not self.sequence

    def reset(self):
        self.sequence = list(range(1, self.LABOUCHERE_N + 1))


# ---------------------------------------------------------------------------
# Registry
# ---------------------------------------------------------------------------

STRATEGIES = {
    FlatBet.name: FlatBet,
    Martingale.name: Martingale,
    Paroli.name: Paroli,
    Labouchere.name: Labouchere,
}


def make_strategy(name, base_bet):
    """Factory. Raises KeyError on unknown strategy name."""
    if name not in STRATEGIES:
        raise KeyError(f"Unknown strategy '{name}'. Available: {list(STRATEGIES)}")
    return STRATEGIES[name](base_bet)
