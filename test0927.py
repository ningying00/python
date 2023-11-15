"""
我们希望找到高于或等于1000的数字，即每四个连续数字的总和不能高于某个给定值。如果数字是num = d1d2d3d4d5d6，并且4个连续数字的最大和是max_sum，那么：

d1 + d2 + d3 + d4 <= max_sum
d2 + d3 + d4 + d5 <= max_sum
d3 + d4 + d5 + d6 <= max_sum
为此，我们需要创建一个函数max_sum_dig()，该函数接收n_max，作为研究间隔的最大值（范围（1000，n_max）），以及某个值max_sum ，即每连续四位数字应小于或等于的最大和。该函数应输出以下列表，其中包含详细信息：

[(1), (2), (3)]

(1) 满足上述约束的数字数量

(2) 最接近结果平均值的数字，如果有多个，则应选择最小的数字。

(3) 所有发现数字的总和

让我们看看一个包含所有细节的案例：

max_sum_dig(2000, 3) -------> [11, 1110, 12555]

(1) 总共找到11 个数字: 1000, 1001, 1002, 1010, 1011, 1020, 1100, 1101, 1110, 1200 和 2000

(2) 求得所有符合的数字的平均数为:
      (1000 + 1001 + 1002 + 1010 + 1011 + 1020 + 1100 + 1101 + 1110 + 1200 + 2000) /11 = 1141.36363,
      所以 1110 是最符合的数字.

(3) 所有符合的数字的总和为12555
      1000 + 1001 + 1002 + 1010 + 1011 + 1020 + 1100 + 1101 + 1110 + 1200 + 2000 = 12555
"""
def max_sum_dig(n_max: int, max_sum: int) -> list:
    lresult = []
    for i in range(1000, n_max + 1):
        ll = [int(a) for a in str(i)]
        for j in range(len(ll) - 3):
            if ll[j] + ll[j + 1] + ll[j + 2] + ll[j + 3] > max_sum:
                break
            else:
                lresult.append(i)
    countnum = len(lresult)
    sumunm = sum(lresult)
    avgnum = sumunm / countnum
    for i in range(len(lresult) - 1):
        if abs(avgnum - lresult[i]) < abs(avgnum - lresult[i + 1]):
            lresult[i], lresult[i + 1] = lresult[i + 1], lresult[i]
    minnum = lresult[-1]
    # return lresult
    return [countnum, minnum, sumunm]


assert max_sum_dig(2000, 3) == [11, 1110, 12555]
assert max_sum_dig(2000, 4) == [21, 1120, 23665]
assert max_sum_dig(2000, 7) == [85, 1200, 99986]
assert max_sum_dig(3000, 7) == [141, 1600, 220756]
assert max_sum_dig(4000, 4) == [35, 2000, 58331]
