def print_rank(rank):
    if (rank == 1):
        return "A"
    elif (rank == 2):
        return "2"
    elif (rank == 3):
        return "3"
    elif (rank == 4):
        return "4"
    elif (rank == 5):
        return "5"
    elif (rank == 6):
        return "6"
    elif (rank == 7):
        return "7"
    elif (rank == 8):
        return "8"
    elif (rank == 9):
        return "9"
    elif (rank == 10):
        return "10"
    elif (rank == 11):
        return "J"
    elif (rank == 12):
        return "Q"
    elif (rank == 13):
        return "K" 

class Card:
    def __init__(card, rank, suit):
        card.rank = rank
        card.suit = suit              

    def print_card(card):
        if (card.suit == 0):
            print("|♥ " + print_rank(card.rank) + "|")
        elif (card.suit == 1):
            print("|◆ " + print_rank(card.rank) + "|")
        elif (card.suit == 2):
            print("|♣ " + print_rank(card.rank) + "|")
        elif (card.suit == 3):
            print("|♠ " + print_rank(card.rank) + "|")
    
    def card_price(card):
        if ((card.rank == 13) or (card.rank == 12) or (card.rank == 11)):
            return 10
        elif (card.rank == 0):
            return 11
        else:
            return card.rank

#card = Card(1, 3)
#card.print_card()