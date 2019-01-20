from enum import Enum
import random


class Rank(Enum):
    def __str__(self):
        return str(self.value) if self.value <=10 else str(self.name)
    ace = 1
    two = 2
    three = 3
    four = 4
    five = 5
    six = 6
    seven = 7
    eight = 8
    nine = 9
    ten = 10
    jack = 11
    queen = 12
    king = 13


class Suit(Enum):
    def __str__(self):
        return str(self.name)
    club = 0
    diamond = 1
    heart = 2
    spade = 3


class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __hash__(self):
        return self.suit.value * 13 + self.rank.value

    def __eq__(self, other):
        return self.rank == other.rank and self.suit == other.suit

    def __str__(self):
        return "{rank}:{suit}".format(rank=self.rank, suit=self.suit)

    def __repr__(self):
        return "{rank}:{suit}".format(rank=self.rank, suit=self.suit)


def create_deck():
    deck = []
    for s in Suit:
        for r in Rank:
            deck.append(Card(r, s))
    return deck


def shuffle_deck(deck):
    random.shuffle(deck)


def rotation_incr(size, i):
    return 0 if i == size - 1 else i + 1


def deal_cards(deck, num_players):
    if len(deck) % num_players != 0:
        raise Exception('Cannot deal cards equally between players')
    hands = []
    for i in range(num_players):
        hands.append([])
    p = 0
    for c in deck:
        hands[p].append(c)
        p = rotation_incr(num_players, p)
    return hands


def main():
    print(Card(Rank.two, Suit.heart))


if __name__ == "__main__":
    main()
