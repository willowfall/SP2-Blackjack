from card import Card
import random

ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
suits = ["Clubs", "Spades", "Hearts", "Diamonds"]
face_cards = ["J", "Q", "K"]

class Deck:
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                if rank in face_cards:
                    value = 10
                elif rank == "A":
                    value = 11
                else:
                    value = int(rank)

                card_obj = Card(rank, suit, value)
                self.deck.append(card_obj)
    
    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        if self.deck:
            return self.deck.pop()
        else: #if empty list nothing happens
            return None