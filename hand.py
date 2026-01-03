from card import Card
from deck import Deck

class Hand:
    def __init__(self):
        self.cards_hand = []
    
    @property
    def total(self):
        total = 0
        ace_count = 0

        for indiv_card in self.cards_hand:
            if indiv_card.rank == "A":
                ace_count += 1
                total += 11
            else:
                total += indiv_card.value

        while total > 21 and ace_count > 0:
            total -= 10
            ace_count -= 1
        
        return total

    def add_card(self, card):
        self.cards_hand.append(card)

    def is_bust(self):
        return self.total > 21
    
    def is_blackjack(self):
        return len(self.cards_hand) == 2 and self.total == 21
    
    def __str__(self):
    
        if not self.cards_hand:
            return "Empty"
    
        cards_str = ', '.join(str(card) for card in self.cards_hand)
        return f"[{cards_str}]"
    
    def __repr__(self):
        return f"Hand({self.cards_hand}, total={self.total})"
