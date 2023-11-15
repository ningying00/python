"""
给定一个整数n，通过移除其中某一位数字，找出操作之后遗留的最大数字。
【示例】
输入：152
输出：52
解释：如果移除1，得到52；如果移除5，得到12；如果移除2，得到15。因此最大方案是移除1得到52。
"""
def solution(n: int)-> int:
    lresult=[]
    for i in range(len(str(n))):
        new_str = str(n).replace(str(n)[i], "", 1)
        lresult.append(int(new_str))
    return max(lresult)

assert solution(152) == 52
assert solution(1001) == 101
assert solution(10) == 1