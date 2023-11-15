from typing import Union


def isdivisor(num):
    lresult = []
    for i in range(1, num // 2 + 1):
        if num % i == 0:
            lresult.append(i)
    return lresult


def buddy(start: int, limit: int) -> Union[list, str]:
    for i in range(start, limit):
        lresult1 = isdivisor(i)
        lsum = sum(lresult1) - 1
        lresult2 = isdivisor(lsum)
        if sum(lresult2) - 1 == i and i < lsum:
            return [i, lsum]
    return "Nothing"


assert buddy(10, 50) == [48, 75]
assert buddy(2177, 4357) == "Nothing"
assert buddy(57345, 90061) == [62744, 75495]
assert buddy(1071625, 1103735) == [1081184, 1331967]
