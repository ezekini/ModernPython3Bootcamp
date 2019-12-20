'''
remove_every_other([1,2,3,4,5]) # [1,3,5]
remove_every_other([5,1,2,4,1]) # [5,2,1]
remove_every_other([1]) # [1]
'''


def remove_every_other(lst):
    new_lst = [c for i, c in enumerate(lst) if i % 2 == 0]
    return new_lst


remove_every_other([1, 2, 3, 4, 5])  # [1,3,5]
remove_every_other([5, 1, 2, 4, 1])  # [5,2,1]
remove_every_other([1])  # [1]
