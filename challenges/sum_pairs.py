'''
sum_pairs([4,2,10,5,1], 6) # [4,2]
sum_pairs([11,20,4,2,1,5], 100) # []
'''


def sum_pairs(lst, n):

    for i in lst:
        for j in lst:
            if i + j == n:
                return [i, j]
    return []


sum_pairs([4, 2, 10, 5, 1], 6)  # [4,2]
sum_pairs([11, 20, 4, 2, 1, 5], 100)  # []
