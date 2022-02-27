import random

ace_val = ''

suits = ('Spades', 'Hearts', 'Diamonds', 'Clubs')
cards = ('Ace','Two','Three', 'Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King')
values = {'Ace': ace_val, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10}

players = ['Dealer']

class Card:
    def __init__(self,suit,card):
        self.suit = suit
        self.card = card
        self.value = values[card]


    def __str__(self):
        return self.card + ' of ' + self.suit


class Deck(Card):

    def __init__(self):
        self.deck = []

        for suit in suits:
            for card in cards:
                self.deck.append(Card(suit,card))

    def shuffle(self):

        random.shuffle(self.deck)

    def deal_one(self):
        
        return self.deck.pop()

    def __str__(self):
        return self.deck

class New_Player(Card):
    
    def __init__(self,name):
        self.name = name
        self.hand = []
    
        players.append(self.name)

    def add_card(self,card):
        self.card = card
        
        self.hand.append(self.card)
        

    def __iter__(self):
        return iter(self.hand)

    def __str__(self):
        return f'{self.name} is holding {self.hand.__iter__()}'
        




myDeck = Deck()

print(len(myDeck.deck))

myDeck.shuffle()
myCard = myDeck.deal_one()
print(myCard)

player1 = New_Player('Ryan')
player2 = New_Player('Annie')
print(players)


player1.add_card(myCard)
print(len(player1.hand))
print(player1)
