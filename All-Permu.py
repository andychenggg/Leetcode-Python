def permu(num: list) -> list[list]:
    if len(num) == 0:
        return [[]]

    result = []

    for i in range(len(num)):
        head = num[i]
        remain = num[:i]+num[i+1:]
        for lst in permu(remain):
            result.append([head]+ lst)

    return result


print(permu([1, 2, 3]))
