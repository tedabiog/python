

import random

class Card:
    def __init__(self, suit, rank):
        # extra parameters
        self.suit = suit
        self.rank = rank
    def __str__(self): #string method used when print is called. #so you don't get that wierd object code notation.
        # return self.rank["rank"] + ' of ' + self.suit
        return f"{self.rank['rank']} of {self.suit}"
class Deck:
    def __init__(self):  #self represents class object or instance
        #self is needed in all the functions in the init funciton
        suits = ['spades', 'clubs', 'hearts', 'diamonds']  
        # ranks = ["A", '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        ranks = [
                {"rank": "A", "value" : 11},
                {"rank" : '2', 'value' : 2},
                {"rank" : '3', 'value' : 3},
                {"rank" : '4', 'value': 4},
                {"rank" : '5', 'value': 5},
                {"rank" : '6', 'value': 6},
                {"rank" : '7', 'value': 7},
                {"rank" : '8', 'value': 8},
                {"rank" : '9', 'value': 9},
                {"rank" : '10', 'value': 10},
                {"rank" : 'Q', 'value': 10},
                {"rank" : 'K', 'value': 10},
                {"rank" : 'J', 'value': 10},
            ]
        #each element in list is a dictionary key value pair. 2 keys in each dictionary. "rank " and "value" each with their corresonding values.
      
        self.cards = [] #52 items in self. list
        for suit in suits:
            for rank in ranks:
                # print([suit, rank])  # all 52 cards printed as 2 item lists
                self.cards.append(Card(suit, rank)) #add all items pairs as 2 item list to card list append only takes one argument

    #shuffle cards so cards arent in order
    def shuffle(self):
        if len(self.cards) > 1:
           random.shuffle(self.cards)

    #rank is Q, J, 6 etc.
    def deal(self, number):
        cards_dealt = []
        
        card = self.cards.pop(number)  #randomly removes cards and deals them. RETURNS them
        for i in range(number):
            if len(self.cards) > 0:
                card = self.cards.pop(number)
                cards_dealt.append(card)
        
        return cards_dealt
    
# deck1 = Deck() #create an instance (object) of class
# print(deck1.cards) #should be 52 cards. lists suit rank and value

class Hand:
    def __init__(self, dealer = False): #parameters can have default values (set has false)
        self.cards = []
        self.value = 0
        self.dealer = dealer
        #self.cards is part of Deck class function. Accessing that object from deck class in Hand class.
    def add_card(self, card_list):
        self.cards.extend(card_list)
    
    def calculate_value(self):
        self.value = 0 #defined in init
        has_ace = False #only used inside method. #no ace by default
        for card in self.cards:
            card_value = int(card.rank['value']) #ace value is 1 or 11
            self.value += card_value
            if card.rank["rank"] == 'A':
               has_ace = True
        if has_ace and self.value > 21:
           self.value -= 10

    def get_value(self):
        self.calculate_value() #instance of calculate_value method. calls funct
        return self.value
    
    def is_blackjack(self):
        return self.get_value == 21 #returns True or false. == is evaluator
    
    def display(self, show_all_dealer_cards = False):
        print(f'''{"Dealer's" if self.dealer else "Your"} hand:''')
        
        for index, card in enumerate(self.cards):
            if index == 0 and self.dealer \
            and not show_all_dealer_cards and not self.is_blackjack:
                print('hidden')
            else:
                print(card)
        if not self.dealer:
            print('Value:', self.get_value())
        print()
    
        
class Game:
    def play(self):
        game_number = 0
        games_to_play = 0
        while games_to_play <= 0: 
            try:
                games_to_play = int(input('How many games do you want to play? '))
            except:
                print('Use must enter a number')
        
        while game_number < games_to_play:
              game_number += 1
              deck = Deck()
              deck.shuffle()
              player_hand = Hand()
              dealer_hand = Hand(dealer = True)
              for i in range(2):
                  player_hand.add_card(deck.deal(1))
                  dealer_hand.add_card(deck.deal(1))
              print()
              print('*' * 30)
              print(f"Game {game_number} of {games_to_play}")
              print('*' * 30)  #asterisks are just visual dividers
              player_hand.display()
              dealer_hand.display()
              if self.check_winner(player_hand, dealer_hand):
                 continue
              
              choice = ''
              while player_hand.get_value() < 21 and choice not in ['s', 'stand']:
                   choice = input('Please choose "Hit" or "Stand": ').lower()
                   print() #just new line separator
                   while choice not in ['h', 's', 'hit', 'stand']:
                       choice = input('Please enter "Hit" or "Stand" (or H/S ") ').lower()
                       print()
                   if choice in ['hit', 'h']:
                       player_hand.add_card(deck.deal(1))
                       player_hand.display()
              if self.check_winner(player_hand, dealer_hand):
                  continue
              player_hand_value = player_hand.get_value()
              dealer_hand_value = dealer_hand.get_value()

              while dealer_hand_value < 17:
                   dealer_hand.add_card(deck.deal(1))
                   dealer_hand_value = dealer_hand.get_value()    
              
              dealer_hand.display(show_all_dealer_cards = True)
              if self.check_winner(player_hand, dealer_hand):
                 continue
              print("final results")
              print('Your hand:', player_hand_value)
              print("Dealer's hand:", dealer_hand_value)

              self.check_winner(player_hand, dealer_hand, True)

        print("\nThanks for playing!")

    



    def check_winner(self, player_hand, dealer_hand, game_over = False):
        if not game_over:
            if player_hand.get_value() > 21:
                print('You busted. Dealer wins!')
                return True
            elif dealer_hand.get_value() > 21:
                print('Dealer busted. You win!')
                return True
            
            elif dealer_hand.is_blackjack() and player_hand.is_blackjack():
                print('Both players have blackjack! Tie!')
                return True
            
            elif player_hand.is_blackjack():
                print('You have blackjack. You win!')
                return True
            
            elif dealer_hand.is_blackjack():
                print('Dealer has blackjack. Dealer wins!')
                return True
            
        else: 
            if player_hand.get_value() > dealer_hand.get_value():
                print('You win!')
            elif player_hand.get_value() == dealer_hand.get_value():
                print('Tie')
            else:
                print('Dealer wins.')
            return True





g = Game()
g.play()

    


