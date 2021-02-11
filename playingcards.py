class Card():
    """A playing card."""
    RANKS = ["A", "2", "3", "4", "5", "6", 
            "7", "8", "9", "10", "J", "Q", "K"]
    SUITS = ["Plum", "Cube", "Heart", "Spades"]

    def __init__(self, rank, suit, face_up = True):
        self.rank = rank          
        self.suit = suit          
        self.is_face_up = face_up # 是否顯示牌的正面

    def __str__(self):
        if self.is_face_up:
            rep = self.suit + self.rank
        else:
            rep = 'XX'
        return rep
    
    # 牌的順序號
    def pic_order(self):
        if(self.rank == "A"):
            FaceNum = 1
        elif(self.rank == "J"):
            FaceNum = 11
        elif(self.rank == "Q"):
            FaceNum = 12
        elif(self.rank == "K"):
            FaceNum = 13
        else:
            FaceNum = int(self.rank)
        
        if(self.suit == "Plum"):
            Suit = 1
        elif(self.suit == "Cube"):
            Suit = 2
        elif(self.suit == "Heart"):
            Suit = 3       
        elif(self.suit == "Spades"):
            Suit = 4 
        return(Suit-1)*13 + FaceNum

    # 翻牌方法
    def flip(self):
        self.is_face_up = not(self.is_face_up)

class Hand():
    """A playing card."""
    def __init__(self):
        self.cards = []      # cards 清單變數儲存牌手的牌
    
    def __str__(self):
        if(self.cards):
            rep = ""
            for card in self.cards:
                rep += str(card) + "\t"
        else:
            rep = "no card"
        return rep

    # 清空手裡的牌    
    def clear(self):
        self.cards = []

    # 增加牌
    def add(self, card):
        self.cards.append(card)

    # 把一張牌給其他牌手
    def give(self, card, other_hand):
        self.cards.remove(card)
        other_hand.add(card)

class Poke(Hand):
    """A deck of playing cards."""
    # 產生一副牌
    def populate(self):
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self.add(Card(rank, suit))
    # 洗牌
    def shuffle(self):
        import random
        random.shuffle(self.cards)

    # 發牌，每人預設13張牌
    def deal(self, hands, per_hand = 13):
        for rounds in range(per_hand):
            for hand in hands:
                if(self.cards):
                    top_card = self.cards[0]
                    self.cards.remove(top_card)
                    hand.add(top_card)
                    # self.give(top_card, hand)
                else:
                    print("Finish")

if __name__ == "__main__":
    print("this is a moudle with classes for playing cards")
    players = [Hand(), Hand(), Hand(), Hand()]
    poke1 = Poke()
    poke1.populate()
    poke1.shuffle()
    poke1.deal(players, 13)

    # 顯示四位牌手的牌
    n = 1
    for hand in players:
        print("player", n, end=":")
        print(hand)
        n = n + 1
    input("\n Press the enter key to exit.")
    

