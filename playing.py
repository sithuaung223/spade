from card import *


def play_acard(hand, card):
    hand.remove(card)
    return hand


def decide_winner(playing_cards):
    winning_card = playing_cards[0]

    for c in playing_cards:
        if (c.suit == winning_card.suit):
            if (c.rank.value > winning_card.rank.value):
                winning_card = c
        elif (c.suit == Suit.spade):
            winning_card = c

    return winning_card
