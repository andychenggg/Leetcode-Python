def all_combinations(num: list)-> list[list]:
    """
    Calculate combinations of a list

    para:
    num: a list of comparable objects
    r: an int denoting the length of a combination

    return: 
    a list of list, representing all combinations, with a total number of 2^n
    """
    if len(num) == 0:
        return [[]]
    
    result = [[]]

    for i in range(len(num)):
        head = num[i]
        remain = num[i+1:]
        for lst in all_combinations(remain):
            result.append([head] + lst)
    return result


def combinations_r(num: list, r: int)-> list[list]:
    """
    Calculate combinations with length r of a list

    para:
    num: a list of comparable objects
    r: an int denoting the length of a combination

    return: 
    a list of list, representing all combination with length r, with a total number of C(n, r)
    """
    if r == 0:
        return [[]]
    
    result = []

    for i in range(len(num) - r + 1):
        head = num[i]
        remain = num[i+1:]
        for lst in combinations_r(remain, r-1):
            result.append([head] + lst)
    return result


print(combinations_r([1, 2, 3, 4], 2))
print(all_combinations([1, 2, 3]))