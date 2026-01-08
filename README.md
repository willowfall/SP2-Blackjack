## I. Flowchart 

The program logic is visually represented in the attached flowchart.

[Flowchart for SP2 Blackjack.pdf](https://github.com/user-attachments/files/24493588/Flowchart.for.SP2.Blackjack.pdf)


## II. Classes 

| Class | Description |
| :--- | :--- |
| **Class Card** | This Card class is the most “basic” class in this set-up. Its responsibility is to represent a card, by holding its attributes such as rank, suit, and value. It also has a method to display itself in a user-friendly manner that easily shows its rank and suit. |
| **Class Deck** | The Deck class is responsible for creating a standard deck of 52 cards for blackjack. It does so by managing a list of 52 card objects, shuffling, and dealing cards. |
| **Class Hand** | The Hand class is responsible for holding the cards that make up the hand. It holds the objects in a list to which cards can be added. It contains the logic that calculates the ace values, total of the hand, logic, and whether a hand is a bust or a blackjack. It also can present the hand. |
| **Class Player** | The Player Class is responsible to hold the data of the players. It holds attributes like name, balance, hand, and bet amount. It also contains actions/ methods for betting, hitting, and standing. |
| **Class Dealer** | The Dealer Class is of similar nature to the Player class however, is only able to hold hand data, and play turn (hit) and stand. |
| **Class BlackjackGame** | The BlackjackGame Class is the controller class in my structure that connects everything together and allows the game to run. It has attributes that track the players in the game, the dealer, the deck in play, and round number. It contains a start method that contains a loop that manages game flow through calling the functions in an order. It manages inputs/outputs, player setup, round actions/ events & round logic. It sets up players, collects the bets, runs player & dealer turns, decides & pays winners, eliminates broke players, presents a round summary, and prompts for continuation after the round. |

---

## III. 

Methods and Parameters 

Class Card 

* 
**`__init__(self, rank, suit, value)`**: Initializes rank (str), suit (str), and point value (int).


* 
**`__str__(self)`**: Returns a human-readable string like "Ace of Spades".



Class Deck 

* 
**`__init__(self)`**:Automatically creates a list with 52 Card objects by iterating through a nested loop for combinations of suits and ranks. It assigns values (10 for face cards, and initially 11 for Aces).



* 
**`shuffle(self)`**: Randomizes the order of the cards.


* 
**`deal(self)`**: Removes and returns the top card from the deck.



Class Hand 

* 
**`__init__(self)`**: Initializes an empty list for Card objects.


* 
**`total (property)`**: Calculates hand value; automatically changes Aces from 11 to 1 if total > 21.


* 
**`add(self, card)`**: Adds a Card object to the internal list.


* 
**`is_bust(self)`**: Returns True if hand total exceeds 21.


* 
**`is_blackjack(self)`**: Returns True if total is 21 with exactly two cards.


* 
**`__str__(self)`**: Returns a string showing all cards currently in the hand, separated by commas.




Class Player 

* 
**`__init__(self, name, balance)`**: Initializes name, starting funds, and a fresh Hand object.


* 
**`place_bet(self, bet)`**: Validates and subtracts the bet amount from the balance.


* 
**`hit(self, deck)`**: Deals a card from the deck and adds it to the player's hand.


* 
**`stand(self)`**: Signals the player is finished with their turn.



Class Dealer 

* 
**`__init__(self)`**: Initializes with a fresh Hand object.


* 
**`play_turn(self, deck)`**: Automates the dealer's hit action.


* 
**`stand(self)`**: Placeholder for when the dealer reaches 17 or higher.



Class BlackjackGame 

* 
**`start(self)`**: Main entry point; manages the round-by-round loop and delays.


* 
**`setup_players(self)`**: Handles input for player names and balances with validation.


* 
**`place_bets(self)`**: Prompts each player for their bet amount.


* 
**`display_table(self, hide_dealer)`**: Prints current cards; can hide the dealer's second card.


* 
**`run_player_turns(self)`**: Allows players to choose "Hit" or "Stand" until they bust or stay.


* 
**`run_dealer_turn(self)`**: Hits until 17 or more; reveals the hidden card.


* 
**`resolve_round(self)`**: Compares hands, updates balances, and resets for the next round.


* 
**`eliminate_broke_players(self)`**: Removes players with $0 or less.


* 
**`ask_continue(self)`**: Prompts user to play another round or exit.



---

## IV. 

Problems Encountered and Solutions 

* 
**Ace Value Logic**: I initially struggled with hands containing multiple Aces. At first, my logic only checked if there was an ace “A” in the hand when the value exceeded 21, and would change the value of the ace to a 1. However, I forgot to account that there are cases when a hand can have more than 1 ace at a time. I eventually solved this problem by realizing I can have a counter for the aces in the hand and decrement the ace count when I subtract 10 from the total as needed, instead of changing the value itself. 



* 
**Modular Coding**: This project was my first time dealing with multiple files for coding. So because of this new change, there were times where I misremembered the names of the methods/ attributes of the classes I’m calling (ex. deal() became deal_card(), the hand’s total(), I made it to be a property but I forgot this myself at times, etc.) Eventually,  I overcame confusion regarding method names through practice.

* 
**List Iteration**: I had an issue where removing players during a loop caused skipped entries. Fixed by using slicing (`self.players[:]`) to iterate over a copy of the list.


* 
**Readability**: I noticed the game initially printed results too quickly, resulting in a massive wall of text that can overwhelm the user and take away the smooth game feel. I solved this by implementing `time.sleep()` to create suspense and prevent "walls of text".
