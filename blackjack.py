import random
from unicodedata import name

ace_val = 0

suits = ('Spades', 'Hearts', 'Diamonds', 'Clubs')
cards = ('Ace','Two','Three', 'Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King')
values = {'Ace': ace_val, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10}

players = []
deck = []

class Card:
    def __init__(self,suit,card):
        self.suit = suit
        self.card = card
        self.value = values[card]

    def __str__(self):
        return self.card + ' of ' + self.suit

class Deck:

    def __init__(self):
        #self.deck = []
        global deck

    def create_deck(self):
        for suit in suits:
            for card in cards:
                deck.append(Card(suit,card))
                #print(card + ' of ' + suit, values[card])
        #return self.deck

    def shuffle_deck(self):
        random.shuffle(deck)
   
    def __str__(self):
        #self.new_deck()

        for i in self.deck:
            print(f'{i.card} of {i.suit}')

class Player:
    def __init__(self, name, chips):
        self.name = name
        self.chips = chips
        self.hand = []
        self.score = 0

    def hit(self):
        new_card = deck.pop(0)
        #print(new_card)
        self.hand.append(new_card)
        self.score += values[new_card.card]
        
    def check_score(self):
        if self.score <= 21:
            return True
        elif self.score >21:
            print('BUST!')
            return False

    def stand(self):
        pass

    def show_hand(self):
        print(f'\n---{self.name}---')
        for i in self.hand:
            print(f'{i.card} of {i.suit}')
            #self.score += values[i.card]
        print(f'\n{self.score} points\n')

class Dealer:
    def __init__(self, name = 'Dealer'):
        self.name = name
        self.hand = []
        self.score = 0

    def hit(self):
        new_card = deck.pop(0)
        #print(new_card)
        self.hand.append(new_card)
        self.score += values[new_card.card]

    def check_score(self):
        if self.score <= 21:
            return True
        elif self.score >21:
            return False

    def stand(self):
        pass

    def show_hand(self):
        print(f'\n---{self.name}---')
        for i in self.hand:
            print(f'{i.card} of {i.suit}')
            #self.score += values[i.card]
        print(f'\n{self.score} points\n')



def fill_table():
    table = ['Dealer']
    i = 1

    
    for i in range(1,9):
        seat = input('Seat ' + str(i) + ':')
        Player(seat)
        table.append(seat)
        i+=1

    print(table)



def run():
        
    new_deck = Deck()
    new_deck.create_deck()


    new_deck.shuffle_deck()

    dealer = Dealer()
    players.append(dealer)
    player1 = Player('Ryan', 500)
    players.append(player1)

    
    player1.hit()
    dealer.hit()
    player1.hit()
    dealer.hit()

    for i in players:
        i.show_hand()

    bet = int(input('Place your bet: '))

    while player1.check_score() == True:
        move = input('Hit or Stand: ')
        if move.lower() == 'hit':
            player1.hit()

            for i in players:
                i.show_hand()
            
        elif move.lower() == 'stand':
            player1.stand()

            for i in players:
                i.show_hand()

        else:
            move = input('Invalid Input. Hit or Stand: ')


        


run()

