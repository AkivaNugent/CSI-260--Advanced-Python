import bj_strat_tables
import random

deck = [
    'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', '10', '10', '10',
    'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', '10', '10', '10',
    'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', '10', '10', '10',
    'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', '10', '10', '10'
]

class GameLoop:
    def __init__(self, deck):
        self.deck = deck

        self.D_hand_1 = self.deal()
        self.D_hand_2 = self.deal()

        self.P_hand_1 = self.deal()
        self.P_hand_2 = self.deal()

        '''
        print(self.D_hand_1)
        print(self.D_hand_2)
        print(self.P_hand_1)
        print(self.P_hand_2)
        print(self.deck)
        '''

    def deal(self):
        item = random.choice(self.deck)
        deck.remove(item)
        
        return item

    def softplay(self):
        total = ""

    def hardplay(self):
        total = ""



    def house_play(self):
        total = 0
        state = ""
        back = False
        if self.D_hand_1 == 'A' and self.D_hand_2 == 'A':
            total = 12

        if (self.D_hand_1 == 'A' or self.D_hand_2 == 'A') and (self.D_hand_1 == '10' or self.D_hand_2 == '10'):
            return "W"

        if self.D_hand_1 == 'A':
            total += 11
            total += int(self.D_hand_2)
            back = True
        elif self.D_hand_2 == 'A':
            total += 11
            total += int(self.D_hand_1)
            back = True
        else:
            total += int(self.D_hand_1)
            total += int(self.D_hand_2)

        while total < 17:
            total += self.deal()

            if total > 21 and back == True:
                total -= 10

        if total > 21:
            return 'B'

        return total







s_cash = 1000 # starting cash for each bot
winnings = [] # bot's individual winnings for analysis

for i in range(1000):
    gl = GameLoop(deck)

    play = ''

    if gl.P_hand_1 == gl.P_hand_2:

    elif gl.P_hand_1 == 'A' or  gl.P_hand_2 == 'A':
        gl.softplay()
    else:
        gl.hardplay()

