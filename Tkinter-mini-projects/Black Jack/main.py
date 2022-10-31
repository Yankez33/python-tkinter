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