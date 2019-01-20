from card import *


def test_shuffle_deck():
    deck = create_deck()
    print("Before shuffling: ")
    print(deck)
    print("After shuffling: ")
    shuffle_deck(deck)
    print(deck)
    assert False
