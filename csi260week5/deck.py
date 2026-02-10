'''
Suits:
    s = Spades
    d = Diamonds
    h = Hearts
    c = Clubs
'''
class Deck:
    def __init__(self):
        self.card_lst1 = ['2s', '3s', '4s', '5s', '6s', '7s', '8s', '9s', '10s', 'Js', 'Qs', 'Ks', 'As']
        self.card_lst2 = ['2d', '3d', '4d', '5d', '6d', '7d', '8d', '9d', '10d', 'Jd', 'Qd', 'Kd', 'Ad']




class Player:
    def __init__(self, player_1, player_2):
        self.player_1 = player_1
        self.player_2 = player_2

player_1 = []
player_2 = []
