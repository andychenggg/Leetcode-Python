def Combinations(num: list)-> list[list]:
    if len(num) == 0:
        return [[]]
    
    result = [[]]

    for i in range(len(num)):
        head = num[i]
        remain = num[i+1:]
        for lst in Combinations(remain):
            result.append([head] + lst)
    return result

print(Combinations([1, 2, 3]))