import random


class Player:

    def get_bid(self):
        return self.bid

    def set_bid(self, bid):
        self.bid = bid


def bid_round(players):
    for p in players:
        b = int(raw_input("Enter your bid: "))
        while not is_valid_bid(b):
            b = int(raw_input("Invalid bid. Reenter your bid: "))
        p.set_bid(b)


def is_valid_bid(bid):
    return True if bid >= 0 and bid <= 13 else False


def main():
    players = [Player() for i in range(4)]
    bid_round(players)
    for p in players:
        print(p.get_bid())


if __name__ == "__main__":
    main()
