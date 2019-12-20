'''
list_check([[],[1],[2,3], (1,2)]) # False
list_check([1, True, [],[1],[2,3]]) # False
list_check([[],[1],[2,3]]) # True
'''


def list_check(lst):
    types = [isinstance(item, list) for item in lst]
    if all(types):
        return True
    else:
        return False


# list_check([[], [1], [2, 3], (1, 2)])  # False
# list_check([1, True, [],[1],[2,3]]) # False
# list_check([[],[1],[2,3]]) # True
