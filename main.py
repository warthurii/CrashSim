import numpy as np
import hashlib
import string
import hmac

e = 2**52
salt = "0000000000000000000fa3b65e43e4240d71762a5bf397d5304b2596d116859c"
game_hash = "822960e79ac367834756e031ed88a5e3a55bd649eb4975e151beb43148711d4a"
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

results = []
count = 0
max = 0
cntTwo, cntTwoFive, cntThree, cntFour, cntFive, cntSix, cntSeven, cntEight, cntNine, cntTen= 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
cntTwoMax, cntTwoFiveMax, cntThreeMax, cntFourMax, cntFiveMax, cntSixMax, cntSevenMax, cntEightMax, cntNineMax, cntTenMax= 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
while game_hash != first_game:
    result = get_result(game_hash)

    if(result <= 2):
        cntTwo += 1
    else:
        if(cntTwo > cntTwoMax):
            cntTwoMax = cntTwo
            cntTwo = 0
    if(result <= 2.5):
        cntTwoFive += 1
    else:
        if(cntTwoFive > cntTwoFiveMax):
            cntTwoFiveMax = cntTwoFive
            cntTwoFive = 0
    if(result <= 3):
        cntThree += 1
    else:
        if(cntThree > cntThreeMax):
            cntThreeMax = cntThree
            cntThree = 0
    if(result <= 4):
        cntFour += 1
    else:
        if(cntFour > cntFourMax):
            cntFourMax = cntFour
            cntFour = 0
    if(result <= 5):
        cntFive += 1
    else:
        if(cntFive > cntFiveMax):
            cntFiveMax = cntFive
            cntFive = 0
    if(result <= 6):
        cntSix += 1
    else:
        if(cntSix > cntSixMax):
            cntSixMax = cntSix
            cntSix = 0
    if(result <= 7):
        cntSeven += 1
    else:
        if(cntSeven > cntSevenMax):
            cntSevenMax = cntSeven
            cntSeven = 0
    if(result <= 8):
        cntEight += 1
    else:
        if(cntEight > cntEightMax):
            cntEightMax = cntEight
            cntEight = 0
    if(result <= 9):
        cntNine += 1
    else:
        if(cntNine > cntNineMax):
            cntNineMax = cntNine
            cntNine = 0
    if(result <= 10):
        cntTen += 1
    else:
        if(cntTen > cntTenMax):
            cntTenMax = cntTen
            cntTen = 0
    if(result > max):
        max = result

    results.append(result)
    game_hash = get_prev_game(game_hash)

print(count)
with open("streaks.txt", 'w') as file_handler:
    file_handler.write("Longest streak <= 2: %d\n" % cntTwoMax)
    file_handler.write("Longest streak <= 2.5 %d\n" % cntTwoFiveMax)
    file_handler.write("Longest streak <= 3: %d\n" % cntThreeMax)
    file_handler.write("Longest streak <= 4: %d\n" % cntFourMax)
    file_handler.write("Longest streak <= 5: %d\n" % cntFiveMax)
    file_handler.write("Longest streak <= 6: %d\n" % cntSixMax)
    file_handler.write("Longest streak <= 7: %d\n" % cntSevenMax)
    file_handler.write("Longest streak <= 8: %d\n" % cntEightMax)
    file_handler.write("Longest streak <= 9: %d\n" % cntNineMax)
    file_handler.write("Longest streak <= 10: %d\n" % cntTenMax)
    file_handler.write("Largest Number: %f\n" % max)

results = np.array(results)

with open("results.txt", 'w') as file_handler:
    for x in results:
        file_handler.write("%f\n" % x)