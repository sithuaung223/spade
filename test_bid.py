from bidding import *


def test_bid():
    print("test_bid")
    assert is_valid_bid(3)
    assert is_valid_bid(10)
    assert is_valid_bid(-1) == False
    assert is_valid_bid(14) == False
