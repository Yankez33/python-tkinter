import os  # to access the assets folder
import random  # to shuffle the deck
import tkinter as tk

root = tk.Tk()

# used by multiple classes, so it gets defined outside the scope of a class
assets_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'assets/'))


# Card class
class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    # will change card display when we call print on it
    def __repr__(self):
        return " of ".join((self.value, self.suit))

    @classmethod
    def get_file_back(cls):
        cls.back = tk.PhotoImage(file=assets_folder + "/back.png")


# Deck class
class Deck:
    def __init__(self):
        self.cards = [Card(s, v) for s in ["Spades", "Clubs", "Hearts", "Diamonds"] for v in ["A", "2", "3", "4",
                                                                                              "5", "6", "7", "8",
                                                                                              "9", "10", "J", "Q",
                                                                                              "K"]]

    def shuffle(self):
        if len(self.cards) > 1:
            random.shuffle(self.cards)

    def deaf(self):
        if len(self.cards) > 1:
            return self.cards.pop(0)


# Hand class
class Hand:
    def __init__(self, dealer=False):
        self.dealer = dealer
        self.cards = []
        self.value = 0

    def add_card(self, card):
        self.cards.append(card)

    def calculate_value(self):
        self.value = 0
        has_ace = False
        for card in self.cards:
            if card.value.isnumeric():
                self.value += int(card.value)
            else:
                if card.value == "A":
                    has_ace = True
                    self.value += 11
                else:
                    self.value += 10

        if has_ace and self.value > 21:
            self.value -= 10

    def get_value(self):
        self.calculate_value()
        return self.value


# Game State class
class GameState:
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()

        self.player_hand = Hand()
        self.dealer_hand = Hand(dealer=True)

        for i in range(2):
            self.player_hand.add_card(self.deck.deal())
            self.dealer_hand.add_card((self.deck.deal()))

            self.has_winner = ' '

    def player_is_over(self):
        return self.player_hand.get_value() > 21
    has_won = True


root.mainloop()


