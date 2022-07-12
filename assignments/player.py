from deck import Deck

class Player:
    def __init__(player, deck, dealer):
        player.hand = []
        player.deck = deck
        player.dealer = dealer

    def deal_hand(player):
        player.hand.append(player.deck.draw_card())
        player.hand.append(player.deck.draw_card())
        if (player.dealer == False):
            player.print_hand()
        else:
            player.print_dealer_hand()

    def hit(player):
        player.hand.append(player.deck.draw_card())
        player.print_hand()

    def print_hand(player):
        print("Player hand:")
        for i in range(0, len(player.hand)):
            player.hand[i].print_card()

    def print_dealer_hand(player):
        print("Dealer hand:")
        player.hand[0].print_card()
        print("|   |")