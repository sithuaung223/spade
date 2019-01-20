from playing import *
from card import *
from bidding import *

test_hand = [
    Card(Rank.two, Suit.heart),
    Card(Rank.three, Suit.club),
    Card(Rank.ace, Suit.spade),
    Card(Rank.king, Suit.diamond)]

def test_play_acard_handlostonecard():
    result_hand = play_acard(test_hand, Card(Rank.two, Suit.heart))

    assert len(result_hand) == 3
    assert Card(Rank.two, Suit.heart) not in result_hand
