class Cards:
    def __init__(self,card_type,number,flower):
        self.card_type = card_type
        self.number = number
        self.flower = flower

    def __str__(self):
        return f"{self.number}{self.card_type}[{self.flower}]"

    def __repr__(self):
        return f"{self.number}{self.card_type}{self.flower}"

class Player:
    def __init__(self,name,cards):
        self.name = name
        self.cards = cards