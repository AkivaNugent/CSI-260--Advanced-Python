"""Define the classes and main loop for the Go Fish game.

Author: Akiva Nugent
Class: CSI-260-01
Assignment: Week 3 Lab
Due Date: February 13, 2019 11:59 PM

Certification of Authenticity:
I certify that this is entirely my own work, except where I have given
fully-documented references to the work of others. I understand the definition
and consequences of plagiarism and acknowledge that the assessor of this
assignment may, for the purpose of assessing this assignment:
- Reproduce this assignment and provide a copy to another member of academic
- staff; and/or Communicate a copy of this assignment to a plagiarism checking
- service (which may then retain a copy of this assignment on its database for
- the purpose of future plagiarism checking)

AI Disclosure: I wrote this on my laptop in VSCode which has a heavy-handed
    autocomplete.
    It was often wrong in its assumptions on what I wanted to do, but it does
    represent some potion of the syntactic output.
    Still, t didn't understand the rules of GoFish so all game flow and thought
    came from me.
"""


import random


class Dealer:
    """Defines the dealer."""

    def __init__(self):
        """Initialize the dealer."""
        self.deck = ['ac', '2c', '3c', '4c', '5c', '6c', '7c', '8c', '9c',
                     '10c', 'jc', 'qc', 'kc',
                     'ad', '2d', '3d', '4d', '5d', '6d', '7d', '8d', '9d',
                     '10d', 'jd', 'qd', 'kd',
                     'ah', '2h', '3h', '4h', '5h', '6h', '7h', '8h', '9h',
                     '10h', 'jh', 'qh', 'kh',
                     'as', '2s', '3s', '4s', '5s', '6s', '7s', '8s', '9s',
                     '10s', 'js', 'qs', 'ks']

    def shuffle(self):
        """Shuffle the deck."""
        random.shuffle(self.deck)

    def deal(self, num_cards, player):
        """Deal cards to a player."""
        for _ in range(num_cards):
            if self.deck:
                card = self.deck.pop()
                player.hand.append(card)

    def is_empty(self):
        """Check if the deck is empty."""
        return len(self.deck) == 0


class Player:
    """Defines a player."""

    def __init__(self, name):
        """Initialize the player."""
        self.name = name
        self.hand = []
        self.books = []

    def show_hand(self):
        """Return a string representation of the player's hand."""
        return ', '.join(self.hand)

    def has_card(self, rank):
        """Check if the player has a card of the given rank."""
        return any(card.startswith(rank) for card in self.hand)

    def give_cards(self, rank, opponent):
        """Give all cards of the given rank to another player."""
        cards_to_give = [card for card in self.hand if card.startswith(rank)]
        for card in cards_to_give:
            self.hand.remove(card)
            opponent.hand.append(card)
        return cards_to_give

    def is_hand_empty(self):
        """Check if the player's hand is empty."""
        return len(self.hand) == 0

    def check_for_books(self):
        """Check for books in the player's hand."""
        rank_counts = {}
        for card in self.hand:
            rank = card[:-1]
            rank_counts[rank] = rank_counts.get(rank, 0) + 1

        for rank, count in rank_counts.items():
            if count == 4:
                self.books.append(rank)
                self.hand = [card for card in self.hand
                             if not card.startswith(rank)]

        print(f"{self.name} has {len(self.books)} book(s): "
              f"{', '.join(self.books)}")

    def ask_for_card(self, rank, opponent):
        """Ask another player for a card of the given rank."""
        if opponent.has_card(rank):
            return opponent.give_cards(rank, self)
        else:
            return []


def check_win_state(player1, player2):
    """Check conditions of the game for a winner."""
    win_state = False

    if len(player1.books) + len(player2.books) == 13:
        win_state = True
        if len(player1.books) > len(player2.books):
            print(f"{player1.name} wins with {len(player1.books)} books!")
        elif len(player2.books) > len(player1.books):
            print(f"{player2.name} wins with {len(player2.books)} books!")
        else:
            print("It's a tie!")

    return win_state


def main():
    """Define main driving function to run the Go Fish game."""
    player1_name = input("Enter the name of Player 1: ")
    player2_name = input("Enter the name of Player 2: ")

    dealer = Dealer()
    dealer.shuffle()

    player1 = Player(player1_name)
    player2 = Player(player2_name)

    dealer.deal(7, player1)
    dealer.deal(7, player2)

    current_player = player1
    opponent = player2

    while not check_win_state(player1, player2):
        print(f"\n{current_player.name}'s turn.")
        print(f"Your hand: {current_player.show_hand()}")
        rank = input("Enter the rank of the card you want to ask for "
                     "(e.g., 'A', '2', '3', ..., 'K'): ")
        if not current_player.has_card(rank):
            print("You must have at least one card of the rank you "
                  "are asking for.")
            continue
        cards_received = current_player.ask_for_card(rank, opponent)

        if cards_received:
            print(f"You received {len(cards_received)} card(s) "
                  f"from {opponent.name}.")
            print(f"Your hand: {current_player.show_hand()}")
        else:
            print(f"{opponent.name} says 'Go Fish!'")
            if not dealer.is_empty():
                dealer.deal(1, current_player)
                print("You drew a card from the deck.")
                print(f"Your hand: {current_player.show_hand()}")
            current_player, opponent = opponent, current_player

        player1.check_for_books()
        if player1.is_hand_empty() and not dealer.is_empty():
            print(f"{player1.name} has no cards left. Dealing 5 new "
                  f"cards to {player1.name}.")
            dealer.deal(5, player1)

        player2.check_for_books()
        if player2.is_hand_empty() and not dealer.is_empty():
            print(f"{player2.name} has no cards left. Dealing 5 new "
                  f"cards to {player2.name}.")
            dealer.deal(5, player2)


if __name__ == "__main__":
    main()
