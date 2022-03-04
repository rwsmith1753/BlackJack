import random


suits = ('Spades', 'Hearts', 'Diamonds', 'Clubs')
cards = ('Ace','Two','Three', 'Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King')
values = {'Ace': 0, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10}

table = []
deck = []
buyin = 50
bet = 0

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
                deck.append(Card(suit,card))  #use two decks
                #print(card + ' of ' + suit, values[card])
        for i in deck:                      
            return f'{i.card} of {i.suit}'

    def shuffle_deck(self):
        random.shuffle(deck)
   
    #def __str__(self):
        

        #for i in self.deck:                      
           # return f'{i.card} of {i.suit}'


class Player:
    def __init__(self, name, chips):
        self.name = name
        self.chips = int(chips)
        self.hand = []
        self.score = 0
        self.bet = 0

    def hit(self):
        new_card = deck.pop(0)
        #print(new_card)
        self.hand.append(new_card)
        self.score += values[new_card.card]
    '''        ---probably can delete---
    def check_score(self):
        if self.score <= 21:
            return True
        elif self.score >21:
            print('BUST!')
            return False
    '''            
    def stand(self):
        pass

    def show_hand(self):

        print(f'\n---{self.name}---Chips: {self.chips}')
        for i in self.hand:
            if values[i.card] == 0:
                if self.score + 11 <= 21:
                    values[i] = 11
                else:
                    values[i] = 1
            
            print(f'{i.card} of {i.suit}')
            #self.score += values[i.card]


        print(f'\n{self.score} points\n')

    def bust(self):
        print(f'{self.name} busted!')
        print(Player)

    def win(self):
        winnings = (buyin + bet) * 2
        self.chips += winnings
        print(f'{self.name} has won {winnings}!')
        print(Player)

    def lose(self):
        print(f'{self.name} lost!')
        print(Player)

    def push(self):
        self.chips += buyin
        print(f'{self.name} pushes!')
        print(Player)
        
    def __str__(self):
        return str('{} has {} chips'.format(self.name, self.chips))

class Dealer:
    def __init__(self, name = 'Dealer'):
        self.name = name
        self.hand = []
        self.score = 0

    def hit(self):
        if self.score >= 17:
            pass
        else:
            #new_card = deck.pop(0)
            new_card = Card('Spades','Ace')   #Ace points test
            #print(new_card)
            self.hand.append(new_card)
            self.score += values[new_card.card]

    def check_score(self):
        if self.score <= 21:
            return True
        elif self.score >21:
            print('BUST')

    def stand(self):
        pass

    def show_hand(self):

        face_up = self.hand[0].card
        print(f'\n---{self.name}---')
        print(f'{self.hand[0]}')
        print('********')
        
        if face_up == 'Ace':
            if self.score + 11 <= 21:
                values[face_up] = 11
                #return ace_val
            else:
                values[face_up] = 1
                #return ace_val
        
        print(f'\n{values[face_up]} points\n')


    def show_hole(self):

        print(f'\n---{self.name}---')
        for i in self.hand:
            if values[i.card] == 0:
                if self.score + 11 <= 21:
                    values[i] = 11
            else:
                values[i] = 1
                               
            print(f'{i.card} of {i.suit}')
            #self.score += values[i.card]

                
        print(f'\n{self.score} points\n')
    

    def __repr__(self):
        return str(self.name)


def fill_table():
    global buyin
    global table
    dealer = Dealer()
 
    
    for i in range(1,2):
        seat = input('Seat ' + str(i) + ':')
        chips = input('Starting Chips: ')

        if seat == '' or chips == '':
            pass
        else:
            player = Player(seat,chips)
            table.append(player)
            player.chips -= buyin
            i+=1

    table.insert(0,dealer)



def buy_in():
    global pot
    global bet
    for i in table[1::]:
        buyin = 50
        i.chips -= int(buyin)
        bet = input(f'{i.name} -- Bet: ')
        i.chips -= int(bet)
 
    
def deal():
    for i in table:
        i.hit()
        i.hit()

def show_table():
    for i in table:
        i.show_hand()

def run():
    game_over = False
    hit_stand = {}
    new_deck = Deck()
    new_deck.create_deck()
    new_deck.shuffle_deck()

    fill_table()
    buy_in()
    deal()

    show_table()

    while game_over == False:
        for i in table[1::]:
            move = input(f'{i.name} -- Hit or Stand? ')
            if move.lower() == 'hit':
                i.hit()
                hit_stand.update({i:'hit'})
            elif move.lower() == 'stand':
                i.stand()
                hit_stand.update({i:'stand'})
        if 'hit' in hit_stand.values():
            for i in table[1::]:
                if hit_stand[i] == 'hit':
                    i.hit()
                else:
                    pass
            show_table()
        else:
            for i in table:
                if i.score >21:
                    i.bust()
                elif i.score <= 21:
                    if i == table[0]:
                        pass
                    elif i.score > table[0].score:
                        i.win()
                    elif i.score < table[0].score:
                        i.lose()
                    elif i.score == table[0].score:
                        i.push()               
            game_over = True
        show_table()
        

if __name__ == '__main__':
    run()


