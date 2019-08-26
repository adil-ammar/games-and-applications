import random

suits = ('Spades', 'Diamonds', 'Hearts', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Ace', 'King', 'Queen', 'Jack')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Ace':11, 'King':10, 'Queen':10, 'Jack':10}

playing = True


#Card class
class Card:
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        
        return (self.rank + ' of ' + self.suit)


#Deck class
class Deck:
    
    def __init__(self):

        self.deck = []

        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))

    def __str__(self):
        
        deck_comp=''
        
        for card in self.deck:
            
            deck_comp += '\n' + card.__str__()
            
        return 'The Deck has: '+ deck_comp

    def shuffle(self):

        random.shuffle(self.deck)

    def deal(self):

        return self.deck.pop()

#Hand class
class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces
    
    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces+=1
    
    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.aces -= 1
            self.value -= 10

#Chips class
class Chips:
    
    def __init__(self, total = 100):
        self.total = total  # This can be set to a default value or supplied by a user input
        self.bet = 0
        
    def win_bet(self):
        self.total += self.bet
    
    def lose_bet(self):
        self.total -= self.bet



def take_bet(chip):
    while True:
        try:
            bet = int(input('enter the bet amount'))
    
        except ValueError:
            print('There is some error in your bet input')
    
        else:
            if chip.total >= bet:
                chip.bet = bet
                break
            else:
                print('Your bet exceeds the number of chips you have')


def hit(deck,hand):
    
    hand.add_card(deck.deal())
    hand.adjust_for_ace()
        
def hit_or_stand(deck,hand):
    
    global playing # to control an upcoming while loop
    
    while(True):
        playing = input('Do you want to hit?(True or False)').capitalize()
        if playing == 'True':
            hit(deck,hand)
        elif playing == 'False':
            playing = False
        else:
            print('Enter a valild input')
            continue
        break


def show_some(player,dealer):
    print('\nDealers cards')
    print('<Hidden Card>')
    print(*dealer.cards[1:])
    print('\nPlayers cards',*player.cards, sep = '\n')
def show_all(player,dealer):
    print("\nDealer's cards:", *dealer.cards, sep='\n ')
    print("Dealer's cards =",dealer.value)
    print("\nPlayer's cards:", *player.cards, sep='\n ')
    print("Player's cards =",player.value)


def player_busts(player,dealer,chips):
    print("Player busts!")
    chips.lose_bet()

def player_wins(player,dealer,chips):
    print("Player wins!")
    chips.win_bet()

def dealer_busts(player,dealer,chips):
    print("Dealer busts!")
    chips.win_bet()
    
def dealer_wins(player,dealer,chips):
    print("Dealer wins!")
    chips.lose_bet()
    
def push(player,dealer):
    print("Dealer and Player tie! It's a push.")


# Set up the Player's chips
print('Welcome to BlackJack')
chips = Chips(int(input('How many chips did you buy?')))

while(chips):
    

    while True:
        # Print an opening statement

    
        # Create & shuffle the deck, deal two cards to each player
        my_deck = Deck()
        my_deck.shuffle()
    
        player_hand = Hand()
        dealer_hand = Hand()
    
        player_hand.add_card(my_deck.deal())
        player_hand.add_card(my_deck.deal())
        
        dealer_hand.add_card(my_deck.deal())
        dealer_hand.add_card(my_deck.deal())
    
    
        # Prompt the Player for their bet
        take_bet(chips)
    
       # Show cards (but keep one dealer card hidden)
        show_some(player_hand, dealer_hand)
    
    
        while playing:# recall this variable from our hit_or_stand function
        
            # Prompt for Player to Hit or Stand
            hit_or_stand(my_deck, player_hand)
        
        
            # Show cards (but keep one dealer card hidden)
            show_some(player_hand, dealer_hand)
        
            # If player's hand exceeds 21, run player_busts() and break out of loop
            if player_hand.value > 21:
                player_busts(player_hand, dealer_hand, chips)
                break
        

            # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
        if player_hand.value <= 21:
        
            while(dealer_hand.value < 17):
                hit(my_deck, dealer_hand)
    
            # Show all cards
            show_all(player_hand, dealer_hand)
            
            # Run different winning scenario
            if (dealer_hand.value > 21):
                dealer_busts(player_hand, dealer_hand, chips)
                
            elif dealer_hand.value > player_hand.value:
                dealer_wins(player_hand, dealer_hand, chips)
            
            elif dealer_hand.value < player_hand.value:
                player_wins(player_hand, dealer_hand, chips)
                
            elif (player_hand.value == dealer_hand.value):
                push(player_hand, dealer_hand)
    
        # Inform Player of their chips total 
        print('Your Net amount of chips is : {}'.format(chips.total))
    
        # Ask to play again
        if (chips.total != 0 and input('Do you wanna play again? (y or n)').lower() == 'y'):
            playing = True
            continue
        
        else:
        	print('You have earned: {}'.format(chips.total))
        	print('Thank you for playing!!')
        	break
            
    if (input('Do you want to exit the game now?(y/n)').lower() == 'y'):
        print('Have a good day!!')
        break
