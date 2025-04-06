def permuations(num: list, r: int) -> list[list]:
    '''
    para:
    num: a list of comparable objects
    r: an int denoting the length of a permuation
    return: 
    a list of list, representing all permutations with length r, with a total number of P(n, r)
    '''
    if r == 0:
        return [[]]

    result = []

    for i in range(len(num)):
        head = num[i]
        remain = num[:i]+num[i+1:]
        for lst in permuations(remain, r-1):
            result.append([head]+ lst)

    return result


print(permuations([1, 2, 3, 4], 2))
