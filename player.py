from hand import Hand
from deck import Deck

class Player:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.hand = Hand()
        self.bet = 0

    def place_bet(self, bet):
        if 0 < bet <= self.balance:
            self.bet = bet
            self.balance -= bet
            return True
        return False #if unsuccessful

    def hit(self, deck):
        self.hand.add_card(deck.deal())

    def stand(self):
        pass