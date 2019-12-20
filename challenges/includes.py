'''
includes([1, 2, 3], 1) # True
includes([1, 2, 3], 1, 2) # False
includes({ 'a': 1, 'b': 2 }, 1) # True
includes({ 'a': 1, 'b': 2 }, 'a') # False
includes('abcd', 'b') # True
includes('abcd', 'e') # False
'''


def includes(col, val, start=None):
    if isinstance(col, dict):
        return val in col.values()
    if start is None:
        return val in col
    return val in col[start:]


includes([1, 2, 3], 1)  # True
includes([1, 2, 3], 1, 2)  # False
includes({'a': 1, 'b': 2}, 1)  # True
includes({'a': 1, 'b': 2}, 'a')  # False
includes('abcd', 'b')  # True
includes('abcd', 'e')  # False
