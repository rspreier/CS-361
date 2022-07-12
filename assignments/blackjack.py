from player import Player
from deck import Deck

class Blackjack:
    def __init__(self):
        self.deck = Deck()
        self.deck.create_deck()
        self.player = Player(self.deck, False)
        self.dealer = Player(self.deck, True)

    def play_blackjack(self):
        cur_score = 50
        play = True
        while(play):
            print("\nPlayer score: " + str(cur_score))
            self.dealer.deal_hand()
            self.player.deal_hand()
            hit = ""
            while (hit != "s"):
                hit = input("Would you like to hit or stand? h/s: ")
                if (hit == "h"):
                    print("\n")
                    self.player.hit()
                elif (hit == "s"):
                    print("Temporary")
                    play = False
                else:
                    print("Not an option, please enter valid input")

# deck = Deck()
# deck.create_deck()
# player = Player(deck)
# player.deal_hand()
# player.print_hand()
# player.hit()
# player.print_hand()

start = ""
while (start != "1"):
    start = input("\n-------------------\nWelcome to Blackjack!\n-------------------\nIf you would like to start the game, press 1. If you need a refresher of the rules, press 2. If you would like to quit the program press [control][c]: ")
    if (start == "1"):
        break
    elif (start == "2"):
        print("\n------------------\nRules of Blackjack\n------------------")
        print("The play begins when the dealers draws two cards for the player and the dealer.\nThe goal of the game is to have all of the cards in your hand add up to 21 or as close to that value as possible\n")
        print("Only one of the dealer's cards are shown at the beginning of the turn, while both of the player cards are shown.")
        print("Based on the user hand, and the dealer hand, the user has the option to hit or stand. If the user selects hit, the dealer draws another card for the player.\n")
        print("If the player goes over a total of 21, they bust and the dealer wins the hand. If the user selects to stand, they keep their current hand total and are betting that they will end up closer to 21 compared to the dealer. Face cards are worth 10, and Ace card can be counted as either 11 or 1\n")
        print("Once the player stands, the second dealer card is revealed, and cards are drawn until the dealer's hand either 1) Goes over 17 2) Is closer to 21 compared to the player hand 3) Goes over 21\n")
        print("If the first or third option occurs, the player wins the hand. If the second option occurs, the dealer wins. If at any point the player gets 21, they win the hand. If it ends in a tie, the hand results in a push, and the points carry over to the next hand.\n")
        print("If the player start with a face card and an Ace, the player gets a blackjack, meaning they win the hand and earn more points\n")
        print("Play continues until the user runs out of points or they decide to cash out")
        start_game = ""
        start_game = input("Press 1 to return back to the menu: ")
        if (start_game == 1):
            break
blackjack = Blackjack()
blackjack.play_blackjack()

