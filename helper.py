from status import Cards

def create_all_cards(flow):
    deck = []
    for _ in range(4):
        for card_type in ["索","萬","筒"]:
            for num in range(1,10):
                deck.append(Cards(card_type,num,False))
        for number in ["東","南","西","北","中","發","白"]:
            deck.append(Cards("字",number,False))
        if flow == True:
            deck.append(Cards("梅",1,True))
            deck.append(Cards("蘭",2,True))
            deck.append(Cards("菊",3,True))
            deck.append(Cards("竹",4,True))
            deck.append(Cards("春","一",True))
            deck.append(Cards("夏","二",True))
            deck.append(Cards("秋","三",True))
            deck.append(Cards("冬","四",True))
    return deck


             
