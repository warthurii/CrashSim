#import numpy as np
import hashlib
import string
import hmac

e = 2**52
salt = "0000000000000000000fa3b65e43e4240d71762a5bf397d5304b2596d116859c"
game_hash = "725e21f12b1312c91be9e4d0ce59ec4cdbbd6df05b39fafc85978a61077ee2cb"
first_game = "77b271fe12fca03c618f63dfb79d4105726ba9d4a25bb3f1964e435ccf9cb209"

def get_result(game_hash):
    hm = hmac.new(str.encode(game_hash), b'', hashlib.sha256)
    hm.update(salt.encode("utf-8"))
    h = hm.hexdigest()
    if (int(h, 16) % 33 == 0):
        return 1
    h = int(h[:13], 16)
    e = 2**52
    return (((100 * e - h) / (e-h)) // 1) / 100.0

def get_prev_game(hash_code):
    m = hashlib.sha256()
    m.update(hash_code.encode("utf-8"))
    return m.hexdigest()

def longestRun(multi):
    cnt = 0
    cntMax = 0
    game_hash = "725e21f12b1312c91be9e4d0ce59ec4cdbbd6df05b39fafc85978a61077ee2cb"

    while game_hash != first_game:
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
    i = 0
    result = 100.0
    while i < num:
        result = result/2
        i += 1
    return result

print(optimalPercentage(17))
print(optimalPercentage(30))
print(optimalPercentage(42))
print(optimalPercentage(63))