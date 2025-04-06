def Combinations(num: list, r: int)-> list[list]:
    if r == 0:
        return [[]]
    
    result = [[]]

    for i in range(len(num)):
        head = num[i]
        remain = num[i+1:]
        for lst in Combinations(remain, r-1):
            result.append([head] + lst)
    return result

print(Combinations([1, 2, 3], 2))