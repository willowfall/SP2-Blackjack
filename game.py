from player import Player
from dealer import Dealer
from deck import Deck
from hand import Hand
import time


class BlackjackGame:
    def __init__(self):
        self.players = []
        self.dealer = Dealer()
        self.deck = Deck()
        self.round_number = 0
    
    def start(self):
        print("==============================")
        print("     WELCOME TO BLACKJACK!    ")       
        print("==============================")
        print("Rules:")
        print("- Try to get as close to 21 as possible.")
        print("- Face cards = 10, Ace = 1 or 11. In this version, aces can't be split.")
        print("- Dealer must hit until 17 or higher.")


        self.setup_players()
        while len(self.players) > 0: # Game continues while players have money
                self.deck = Deck()
                self.deck.shuffle()      # Reshuffle every round
                self.place_bets()
                self.initial_deal()
                self.run_player_turns()
                time.sleep(2)
                self.run_dealer_turn()
                time.sleep(3)
                self.resolve_round()
                time.sleep(2)
                self.eliminate_broke_players()

                if len(self.players) == 0:
                    print("No players remaining. Game Over!")
                    break

                if not self.ask_continue():
                    print("Thank you for playing! Hope you enjoyed ^^ ")
                    break

    def setup_players(self):

        while True: #asks number of players
            try: 
                num_of_players = int(input("How many players (1-7)? : "))
                if 0 < num_of_players < 8:
                    break
                print("Please enter at least one player or a number from 1 to 7.")
            except ValueError:
                print("Invalid input. Please enter an integer.")

        for i in range(num_of_players): #set up for each player
            print(f"\n --- Set up for Player {i+1} ---")
            name = input("Input Player Name: ")
        
            while True:
                try:
                    bal = int(input(f"Input Initial Balance for {name}: "))
                    if bal > 0:
                        break
                    print("Starting balance must be greater than 0.")
                except ValueError:
                    print("Invalid input. Please enter an integer.")

            new_player = Player(name, bal)
            self.players.append(new_player)

    def place_bets(self):
        for player in self.players:
            print(f"\n{player.name}'s Balance: ${player.balance}")
            
            while True:
                try:
                    amount = int(input(f"Enter bet for {player.name}: "))
                    if player.place_bet(amount): # Returns True if bet is valid, breaks and goes to next
                        break
                    print(f"Invalid amount! You only have ${player.balance}.")
                except ValueError:
                    print("Please enter a whole number.")

    def display_table(self, hide_dealer=True):
        print("\n" + "=" * 30)

        # dealer hand
        if hide_dealer:
            if self.dealer.hand.cards_hand:
                first_card = str(self.dealer.hand.cards_hand[0])
                print(f"Dealer: [{first_card}, ??]")
            else:
                print("Dealer: []")
        else:
            # remember that total is a @property, so no parentheses
            print(f"Dealer: {self.dealer.hand} (Total: {self.dealer.hand.total})")

        # player hands
        for player in self.players:
            print(f"{player.name}: {player.hand} (Total: {player.hand.total}) | Bet: ${player.bet}")

        print("=" * 30 + "\n")

    
    def initial_deal(self):
        for player in self.players:
            for _ in range(2):
                player.hand.add_card(self.deck.deal())

        for _ in range(2):
            self.dealer.hand.add_card(self.deck.deal())

        print(f"\n --- Initial Deals: ---")
        self.display_table(hide_dealer=True)
    
    def run_player_turns(self):
        for player in self.players:
            print(f"\n --- {player.name}'s Turn ---")

            if player.hand.is_blackjack():
                print(f"\n{player.name} has Blackjack! Skipping turn.")
                continue

            while player.hand.total <= 21:
                try:
                    choice = int(input("Input 1 to hit, 2 to stand: "))
                    if choice == 1:
                        player.hit(self.deck)
                        self.display_table(hide_dealer=True)

                    elif choice == 2:
                        player.stand()
                        self.display_table(hide_dealer=True)
                        break  # stop asking once they stand

                    else:
                        print("Invalid choice. Please enter 1 or 2.")
                except ValueError:
                    print("Invalid input. Please enter a 1 or a 2")
    
    def run_dealer_turn(self):
        print("--- Dealer's Turn ---")
        time.sleep(1)
        self.display_table(hide_dealer=False)  #reveal the cards
    
        while self.dealer.hand.total < 17:
            time.sleep(1.5) # i added a pause to build suspense
            print("Dealer hits...")
            self.dealer.play_turn(self.deck)
            self.display_table(hide_dealer=False)
        
        if self.dealer.hand.is_bust():
            print("Dealer BUSTS!")

    def resolve_round(self):
        dealer_total = self.dealer.hand.total
        dealer_bj = self.dealer.hand.is_blackjack()
        dealer_bust = self.dealer.hand.is_bust()

        print("\n" + "="*30)
        print(f"DEALER FINAL HAND: {self.dealer.hand} (Total: {dealer_total})")
        print("="*30)

        for player in self.players:
            time.sleep(2.5) # i added a pause for suspense again
            print(f"\n --- Processing {player.name}'s Result ---")
            
            p_total = player.hand.total
            p_bj = player.hand.is_blackjack()

            # Case: Both have Blackjack
            if p_bj and dealer_bj:
                 player.balance += player.bet
                 print(f"Tied! Both {player.name} and Dealer have Blackjack.")
            
            # Case: Only Dealer has Blackjack
            elif dealer_bj:
                 print(f"OUCH, Dealer has Blackjack! {player.name} loses.")

            elif player.hand.is_bust():
                print(f"{player.name} busts and loses their bet.")
            
            elif player.hand.is_blackjack():
                winnings = int(player.bet * 2.5) 
                player.balance += winnings
                print(f"{player.name} hits Blackjack! Wins ${winnings}.")

            elif dealer_bust or p_total > dealer_total:
                winnings = player.bet * 2
                player.balance += winnings
                print(f"{player.name} wins! Gains ${winnings}.")

            elif p_total == dealer_total:
                player.balance += player.bet
                print(f"{player.name} ties with Dealer. ${player.bet} is returned.")

            else:
                print(f"{player.name} loses. (Dealer: {dealer_total} vs {player.name}: {p_total})")
            

        time.sleep(2)

        # added End-Of-Round Summary
        print("\n" + "*"*30)
        print("    FINAL ROUND SUMMARY")
        for player in self.players:
            print(f" {player.name:15} | New Balance: ${player.balance}")
        print("*"*30 + "\n")

        # note to self: IMPORTANT! RESET HANDS FOR NEXT ROUND
        self.dealer.hand = Hand()
        for player in self.players:
            player.hand = Hand()
            player.bet = 0 # Clear the bet for the next round


    def eliminate_broke_players(self):
        for p in self.players[:] :  # i iterate over a copy
            print(f"\n --- Processing {p.name}'s Status ---")
            if p.balance <= 0:
                self.players.remove(p)
                print(f"{p.name} has been eliminated from the game, o7 bye bye!")
            else:
                print(f"{p.name} remains in the game with ${p.balance}.")
            time.sleep(1)


    def ask_continue(self):
        while True:
            choice = input("\nDo you want to play another round? (y/n): ").lower().strip()
            if choice == 'y':
                return True
            if choice == 'n':
                return False
            print("Invalid input. Please enter 'y' or 'n'.")
    
    
                




        


        


