from random import randint
from card import Card

class Deck:
    def __init__(deck):
        deck.cards = []

    def create_deck(deck):
        for i in range(1,14):
            for j in range(0,4):
                deck.cards.append(Card(i, j))

    def draw_card(deck):
        card = deck.cards[randint(0,51)]
        deck.cards.remove(card)
        return card

    def print_deck(deck):
        for i in range(0,52):
            deck.cards[i].print_card()
