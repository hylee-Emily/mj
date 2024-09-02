from helper import create_all_cards
#from player import Player
from status import Cards,Player
import random

class Player:
    def __init__(self,name,cards):
        self.name = name
        self.cards = cards

def generate_cards(flower_or_not):
    card = create_all_cards(flower_or_not)
    random.shuffle(card)
    """
    deck1 = card[0:3],card[16:19],card[32:35],card[48]+card[52]
    deck2 = card[4:7]#+cards[20:23]+cards[36:39]+cards[49]
    deck3 = card[8:11]#+cards[24:27]+cards[40:43]+cards[50]
    deck4 = card[12:15]#+cards[28:31]+cards[44:47]+cards[51]
    """

    return card[0:13],card[14:26],card[27:39],card[40:52]


a,b,c,d = generate_cards(False)
player1 = Player("PlayerA",a)
player2 = Player("PlayerB",b)
player3 = Player("playerC",c)
player4 = Player("PlayerD",d)

print(player1.cards)
print(player2.cards)
print(player3.cards)
print(player4.cards)
