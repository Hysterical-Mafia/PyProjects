#Card Game: War
import random

#Cards, Num and Suits || Handles individual cards
class Cards:
    def __init__(self, number, suit):
        self.number = number
        self.suit = suit

    def __str__(self):
        return f"{self.number} {self.suit}"

    def __repr__(self):
        return f"Cards(number='{self.number}', Suit='{self.suit}')"

#Full Deck, 52, Shuffle || concerns the entire deck all 52 cards
class Deck:
    def __init__(self):
        self.full_deck = []
        suits = ["Clubs", "Spades", "Diamonds", "Hearts"]
        numbers = ["Ace","2","3","4","5","6","7","8","9","10","J","Q","K"]
        
        for symbol in suits:
            for nums in numbers:
                full = self.full_deck.append(Cards(nums,symbol))
                
    def __repr__(self):
        return f"Deck({self.full_deck} cards)"
    
    def shuffle(self):
        random.shuffle(self.full_deck)
        
    def deal_cards(self):
        print    

    def show_full_deck(self): 
        print


#class Player:

class Players:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.score = 0

    def __repr__(self):
        return f"Players(name = '{self.name}' , hand = {self.hand} , score = {self.score})"
    
    def add_card(self, Cards):
        self.hand.append(Cards)

    def play_card(self):
        if self.hand:
            return self.hand.pop()
        else:
            return None


    def show_card(self):
        return self.hand
        
# Game Setu