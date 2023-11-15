import copy


def longest_lighting_time(operation: list) -> str:
    result = copy.deepcopy(operation)
    for i in range(1, len(operation)):
        result[i][1] = operation[i][1] - operation[i - 1][1]
    result = sorted(result, key=(lambda x: x[1]), reverse=True)
    char = [chr(i) for i in range(97, 123)]
    return char[result[0][0]]

assert longest_lighting_time([[0, 2], [1, 5], [0, 9], [2, 15]]) == 'c'
