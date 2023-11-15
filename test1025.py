"""已知一个包含唯一数字的列表，和一个指定的左闭右开区间[from, to)，我们的任务是：首先凑对，找出存在几对元素之和在区间内，然后将这些符合区间的和加总得到最终的和值。
备注：
所有凑对的元素必须是唯一的
凑对的和值只在区间内统计一次
示例：
已知列表是 [2, 4, 6, 10]，已知区间是[6， 10)
6：可以等于 2 + 4
7：无法凑对
8：可以等于 2 + 6
9：无法凑对
最终结果：6 + 8 = 14"""


def isadd(nums: list, num: int) -> bool:
    for i in range(len(nums)):
        if num - nums[i] in nums[i:]:
            return True
        else:
            return False


def solution(nums: list, target: range) -> int:
    lresult = []
    for i in target:
        if isadd(nums, i) == True:
            lresult.append(i)
    return sum(lresult)


assert solution([2, 4, 6, 10], range(6, 10)) == 14
