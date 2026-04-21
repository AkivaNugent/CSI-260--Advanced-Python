"""
Bot: a single gambler.

Bankroll model (unchanged from blackjack version):
  - playing_pool: money actively being wagered
  - winnings: locked-away profits that never get bet
  - On WIN: stake returns to pool, profit goes to winnings
  - On LOSS: stake is already deducted, nothing returns
  - On PUSH: stake returns (shouldn't happen in simple roulette)

Bet determination order:
  1. Strategy picks a desired bet based on its logic.
  2. Bet is capped at table_max (the casino's rule).
  3. If the bot can't afford even the (capped) bet, it goes all-in with
     whatever's left in the pool.
  4. If pool is empty, the bot stops.

The strategy's record_result() sees the ACTUAL bet (after capping), so
martingale still "doubles on loss" even when it's actually been capped at
table max. This means after enough losses, current_bet tracks a number
higher than what's actually being bet - which is fine, it just means
martingale keeps trying to double whenever it wins and resets.
Actually, re-reading: on a WIN it resets, so the internal counter never
stays "stuck" above the cap for long.
"""
from strategies import make_strategy


class Bot:
    def __init__(self, name, strategy_name, base_bet, starting_pool,
                 table_max=50_000):
        self.name = name
        self.strategy_name = strategy_name
        self.base_bet = base_bet
        self.starting_pool = starting_pool
        self.table_max = table_max

        self.strategy = make_strategy(strategy_name, base_bet)
        self.playing_pool = starting_pool
        self.winnings = 0.0
        self.rounds_played = 0
        self.alive = True

    def total_money(self):
        return self.playing_pool + self.winnings

    def play_round(self, dealer):
        if not self.alive:
            return None

        # Check if the strategy has achieved its goal and wants to cash out
        if self.strategy.should_stop(self.playing_pool, self.winnings):
            self.alive = False
            return None

        desired_bet = self.strategy.next_bet(self.playing_pool, self.winnings)

        # Step 1: cap at table max (the casino rule - why martingale fails IRL)
        actual_bet = min(desired_bet, self.table_max)

        # Step 2: if still too big for pool, go all-in with what's left
        if actual_bet > self.playing_pool:
            actual_bet = self.playing_pool

        # Step 3: if nothing to bet, bot is done
        if actual_bet <= 0:
            self.alive = False
            return None

        # Wager: deduct from pool
        self.playing_pool -= actual_bet
        net = dealer.play_round(actual_bet)

        if net > 0:
            # Win: stake returns to pool, profit locked into winnings
            self.playing_pool += actual_bet
            self.winnings += net
            result = 'win'
            won = True
        elif net < 0:
            # Loss: stake gone
            result = 'loss'
            won = False
        else:
            # Push (shouldn't happen in simple roulette): stake returns
            self.playing_pool += actual_bet
            result = 'push'
            won = None

        self.strategy.record_result(won, net)
        self.rounds_played += 1

        return {
            'bot_name': self.name,
            'strategy': self.strategy_name,
            'round': self.rounds_played,
            'desired_bet': desired_bet,
            'actual_bet': actual_bet,
            'capped': desired_bet > actual_bet,  # was the bet reduced?
            'result': result,
            'net': net,
            'playing_pool': self.playing_pool,
            'winnings': self.winnings,
            'total_money': self.total_money(),
        }

    def play_until_broke(self, dealer, max_rounds=100_000):
        while self.alive and self.rounds_played < max_rounds:
            record = self.play_round(dealer)
            if record is None:
                break
            yield record
