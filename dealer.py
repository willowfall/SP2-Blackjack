from hand import Hand
from deck import Deck

class Dealer:
    def __init__(self):
        self.hand = Hand()

    def play_turn(self, deck):
        self.hand.add_card(deck.deal())
        
    def stand(self):
        pass