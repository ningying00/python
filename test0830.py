'''如果 n 是分子，d 是分数的分母，当且仅当 GCD（n，d）==1，则该分数被定义为最简分数。
例如，5/16是一个最简分数，而不是6/16，因为 6 和 16 都可以被 2 整除，因此分数可以简化为3/8 。
现在，如果您考虑给定的数字d，那么使用d作为分母可以构建多少个最简分数？
例如，假设 d 是 15：你可以用它构建 0 和 1 之间总共 8 个不同的正确分数：1/15、2/15、4/15、7/15、8/15、11/15、13/15 和 14/15。
您将构建一个函数，该函数计算使用给定分母可以构建多少个最简分数：'''
 import time
# def prime_number(n):
#     lprime = [i for i in range(1, n)]
#     for i in range(2, n):
#         for j in range(2, i):
#             if i % j == 0 and i in lprime:
#                 lprime.remove(i)
#     return lprime
#没用

def prime_list(n):
    plist = []
    while n != 1:
        w = 0
        for i in range(1, n + 1):
            for j in range(1, i):
                if i % j == 0:
                    w = 1
            if w == 1:
                if n % i == 0:
                    plist.append(i)
                    n = n // i
    return plist


def proper_fractions(n):
    lrsult = [i for i in range(1, n)]
    lprime = prime_list(n)
    for i in range(1, n):
        for j in lprime:
            if i % j == 0 and i in lrsult:
                lrsult.remove(i)
                break
    ll = list((set(lrsult)))
    return len(ll)


#print(prime_list(15))
assert proper_fractions(1) == 0
#print(proper_fractions(15))
assert proper_fractions(2) == 1
assert proper_fractions(5) == 4
assert proper_fractions(15) == 8
assert proper_fractions(25) == 20
# assert proper_fractions(9999999) == 6637344
# assert proper_fractions(500000003) == 500000002
# assert proper_fractions(1532420) == 608256
# assert proper_fractions(123456789) == 82260072
# assert proper_fractions(9999999999) == 5890320000
