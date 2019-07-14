import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

class Card:
    def __init__(self,suits,ranks):
        self.suits=suits
        self.ranks=ranks
        self.values=values[self.ranks]
        
    def __str__(self):
        return (self.suits+" "+self.ranks)

class Deck:
    def __init__(self):
        self.deck=[]
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))
    def show(self):
         print("Deck has:")
         for card in self.deck:
             print(card)
    def shuffle(self):
        random.shuffle(self.deck)
             
class Hand:
    def __init__(self):
        self.cards=[]
        self.value=0
    def add_card(self,card):
        self.cards.append(card)
        self.value+=card.values


class Chip:
    def __init__(self,total):
        self.total=total
        self.bet=0
    def win_bet(self):
        self.total+=self.bet
    def lose_bet(self):
        self.total-=self.bet
    def set_bet(self):
        while True:
            bet=int(input('Enter bet amount'))
            if(bet>self.total):
                print('You dont have that much chips')
            else:
                self.bet=bet
                break;
        
class Player:
    def __init__(self,Hand,Chip):
        self.Hand=Hand
        self.Chip=Chip
    def hit(self,Deck):
        card=Deck.deck.pop()
        print(card)
        self.Hand.add_card(card)
    def isBusted(self):
        return (self.Hand.value>21)

class Dealer:
    def __init__(self,Hand,Chip):
        self.Hand=Hand
        self.Chip=Chip
    def hit(self,Deck):
        card=Deck.deck.pop()
        print(card)
        self.Hand.add_card(card)
    def isBusted(self):
        return (self.Hand.value>21)


def hit_or_stand(player):
    while True:
        if(player.isBusted()):
            print('You Busted')
            return 'busted'
        else:
            play_deck.shuffle()
            s=input('DO you want to hit or stand? Enter h for hit and s for stand')
            if(s.lower()=='h'):
                player.hit(play_deck)
            if(s.lower()=='s'):
                break;


print("WELCOME TO BLACK JACK!!! HAVE FUN")
chip_amount=int(input('Enter chip amount'))
player_chip=Chip(chip_amount)
dealer_chip=Chip(chip_amount)
player_chip.set_bet()
dealer_chip.bet=player_chip.bet
player_Hand=Hand()
dealer_Hand=Hand()
player=Player(player_Hand,player_chip)
dealer=Dealer(dealer_Hand,dealer_chip)
play_deck=Deck()
play_deck.shuffle()

for i in range(2):
    card=play_deck.deck.pop()
    player.Hand.add_card(card)
    card=play_deck.deck.pop()
    dealer.Hand.add_card(card)

print('Player has')
for card in player.Hand.cards:
    print(card)

print('Dealer has')    
print(dealer.Hand.cards[1])

status=hit_or_stand(player)
if(status=='busted'):
    print('Dealer won!!!')
else:
    while(dealer.Hand.value<17):
        play_deck.shuffle()
        dealer.hit(play_deck)
    print('Dealers second card is')
    print(dealer.Hand.cards[0])
    print('Player value'+str(player.Hand.value))
    print('Dealer value'+str(dealer.Hand.value))
    if(player.Hand.value>dealer.Hand.value):
        player.Chip.win_bet()
        dealer.Chip.lose_bet()
        print('Player has '+ str(player.Chip.total))
        print('Dealer has '+ str(dealer.Chip.total))
        print('Player won!!!')
    elif(player.Hand.value==dealer.Hand.value):
        print('Player has '+ str(player.Chip.total))
        print('Dealer has '+ str(dealer.Chip.total))
        print('Draw!!!')
    else:
        dealer.Chip.win_bet()
        player.Chip.lose_bet()
        print('Player has '+ str(player.Chip.total))
        print('Dealer has '+ str(dealer.Chip.total))
        print('Dealer won!!!')

        
        
    
    
