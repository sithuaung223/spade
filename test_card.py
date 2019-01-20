from card import *
import pytest

test_deck = [
    Card(Rank.two, Suit.heart),
    Card(Rank.three, Suit.club),
    Card(Rank.ace, Suit.spade),
    Card(Rank.king, Suit.diamond)]


def test_card_eq_twodifferentcards():
    two_heart = Card(Rank.two, Suit.heart)
    three_club = Card(Rank.three, Suit.club)
    assert two_heart != three_club

def test_card_eq_twosamecards():
    two_heart = Card(Rank.two, Suit.heart)
    another_two_heart = Card(Rank.two, Suit.heart)
    assert two_heart == another_two_heart


def test_create_deck__full52uniquecards():
    deck = create_deck()
    assert len(deck) == 52
    #test uniqueness of the cards
    s = set(deck)
    assert len(s) == 52


def test_deal_card_4cards2players_dealtevenly():
    hands = deal_cards(test_deck, num_players=2)

    assert hands[0][0] == test_deck[0]
    assert hands[0][1] == test_deck[2]

    assert hands[1][0] == test_deck[1]
    assert hands[1][1] == test_deck[3]


def test_deal_card_4cards3players_raiseexception():
    with pytest.raises(Exception):
        hands = deal_cards(test_deck, num_players=3)
