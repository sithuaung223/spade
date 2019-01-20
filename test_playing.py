from playing import *
from card import *
from bidding import *

test_hand = [
    Card(Rank.two, Suit.heart),
    Card(Rank.three, Suit.club),
    Card(Rank.ace, Suit.spade),
    Card(Rank.king, Suit.diamond)]

def test_play_acard_twoheart_losetwoheartfromhand():
    result_hand = play_acard(test_hand, Card(Rank.two, Suit.heart))
    assert len(result_hand) == 3
    assert Card(Rank.two, Suit.heart) not in result_hand

def test_decide_winner_samesuits_highestrankwins():
    playing_cards = [
        Card(Rank.two, Suit.heart),
        Card(Rank.three, Suit.heart),
        Card(Rank.four, Suit.heart),
        Card(Rank.five, Suit.heart)]
    winning_card = decide_winner(playing_cards)
    assert winning_card == Card(Rank.five, Suit.heart)

def test_decide_winner_offsuitswithoutspade_highestrankofleadingsuitwins():
    playing_cards = [
        Card(Rank.two, Suit.heart),
        Card(Rank.three, Suit.diamond),
        Card(Rank.four, Suit.heart),
        Card(Rank.five, Suit.club)]
    winning_card = decide_winner(playing_cards)
    assert winning_card == Card(Rank.four, Suit.heart)

def test_decide_winner_offsuitswithaspade_highestspadewins():
    playing_cards = [
        Card(Rank.two, Suit.heart),
        Card(Rank.three, Suit.spade),
        Card(Rank.four, Suit.spade),
        Card(Rank.five, Suit.club)]
    winning_card = decide_winner(playing_cards)
    assert winning_card == Card(Rank.four, Suit.spade)
