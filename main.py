# import numpy as np
import hashlib
import string
import hmac
import time

e = 2**52
salt = "0000000000000000000fa3b65e43e4240d71762a5bf397d5304b2596d116859c"
game_hash = "cf4b7cd4824de8e19609b748d5718e276d17f9f4e367232c1635308ee266c09c"
first_game = "77b271fe12fca03c618f63dfb79d4105726ba9d4a25bb3f1964e435ccf9cb209"

games = []


def get_result(game_hash):
    hm = hmac.new(str.encode(game_hash), b"", hashlib.sha256)
    hm.update(salt.encode("utf-8"))
    h = hm.hexdigest()
    if int(h, 16) % 33 == 0:
        return 1
    h = int(h[:13], 16)
    e = 2**52
    return (((100 * e - h) / (e - h)) // 1) / 100.0


def get_prev_game(hash_code):
    m = hashlib.sha256()
    m.update(hash_code.encode("utf-8"))
    return m.hexdigest()


def longestRun(multi):
    cnt = 0
    cntMax = 0
    game_hash = "cf4b7cd4824de8e19609b748d5718e276d17f9f4e367232c1635308ee266c09c"

    while game_hash != first_game:
        print(game_hash)
        result = get_result(game_hash)

        # Conditions to count and find the longest streak less than each multiplier.
        if result <= multi:
            cnt += 1
            if cnt > cntMax:
                cntMax = cnt
        else:
            cnt = 0

        game_hash = get_prev_game(game_hash)

    return cntMax


def optimalPercentage(num):
    return 100 / 2**num


def testOptimalPercentage(perc, num, multi):
    lossy = perc
    losses = perc
    i = 1

    while i < num:
        lossy *= 2
        losses += lossy
        i += 1

    print()
    print("final losses: " + str(losses))
    print("final lossy: " + str(lossy))

    profit = (lossy * multi) - (losses + perc)
    print("profit: " + str(profit))


def getResults():
    game_hash = "cf4b7cd4824de8e19609b748d5718e276d17f9f4e367232c1635308ee266c09c"
    games = []
    while game_hash != first_game:
        print(game_hash)
        # result = get_result(game_hash)
        # games.insert(0, result)

        game_hash = get_prev_game(game_hash)


def determineProfit(multi, perc):
    bankroll = 100

    bet = perc

    while game_hash != first_game:
        result = get_result(game_hash)

        if result <= multi:
            bankroll = bankroll - bet
            bet = bet * 2
        else:
            bankroll = bankroll + (bet * multi)
            bet = perc

    return bankroll - 100


if __name__ == "__main__":
    # print(determineProfit(2, optimalPercentage(18)))
    # print(longestRun(2))
    # print(longestRun(2.5))
    # print(longestRun(3))
    # print(longestRun(4))
    # print(longestRun(5))
    # num = 63
    # multi = 5
    # print(optimalPercentage(num))
    # print()
    # print(testOptimalPercentage(optimalPercentage(num), num, multi))
    getResults()
    print(len(games))
