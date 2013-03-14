def peak(values, index):
    """
    A plateau is defined as a number which is greater than both adjacent numbers (without wrapping around).

    Examples:
    >>> peak([], None)
    False
    >>> peak([1], None)
    False
    >>> peak([], 0)
    False
    >>> peak([0], 0)
    True
    >>> peak([-2, -1, 0], 0)
    False
    >>> peak([-1, 0, 1], 1)
    False
    >>> peak([0, 1, 2], 2)
    True
    >>> peak([0, 1, 2], -1)
    False
    >>> peak([0, 1, 0], 0)
    False
    >>> peak([-1, 0, -1], 1)
    True
    >>> peak([-2, -1, -2], 2)
    False
    >>> peak(range(1000000), 0)
    False
    >>> peak(range(1000000), 999999)
    True
    >>> peak([0] * 1000000, 0)
    False
    >>> peak([0] * 1000000, 999999)
    False
    >>> peak([0] * 1000000 + [1], 0)
    False
    >>> peak([0] * 1000000 + [1], 999999)
    False
    >>> peak([0] * 1000000 + [1], 1000000)
    True
    """
    if index is None: # Not a number, but comparable with number in Python 2
        return False
    elif index < 0:
        return False # Outside array
    elif index >= len(values):
        return False # Outside array
    else:
        return (index == 0 or values[index] > values[index - 1]) and (index == len(values) - 1 or values[index] > values[index + 1])

def plateau(values, index):
    """
    A plateau is defined as a number which is greater than or equal to both adjacent numbers (without wrapping around).

    Examples:
    >>> plateau([], None)
    False
    >>> plateau([1], None)
    False
    >>> plateau([], 0)
    False
    >>> plateau([0], 0)
    True
    >>> plateau([-2, -1, 0], 0)
    False
    >>> plateau([-1, 0, 1], 1)
    False
    >>> plateau([0, 1, 2], 2)
    True
    >>> plateau([0, 1, 2], -1)
    False
    >>> plateau([0, 1, 0], 0)
    False
    >>> plateau([-1, 0, -1], 1)
    True
    >>> plateau([-2, -1, -2], 2)
    False
    >>> plateau(range(1000000), 0)
    False
    >>> plateau(range(1000000), 999999)
    True
    >>> plateau([0] * 1000000, 0)
    True
    >>> plateau([0] * 1000000, 999999)
    True
    >>> plateau([0] * 1000000 + [1], 0)
    True
    >>> plateau([0] * 1000000 + [1], 999999)
    False
    >>> plateau([0] * 1000000 + [1], 1000000)
    True
    """
    if index is None: # Not a number, but comparable with number in Python 2
        return False
    elif index < 0:
        return False # Outside array
    elif index >= len(values):
        return False # Outside array
    else:
        return (index == 0 or values[index] >= values[index - 1]) and (index == len(values) - 1 or values[index] >= values[index + 1])

def linear_search(values):
    """
    Search through an integer array linearly and print the first index which is a plateau

    Examples:
    >>> linear_search([])
    False
    >>> linear_search([0])
    0
    >>> linear_search([-1, 0, -1])
    1
    >>> linear_search([0, -1, 0]) in [0, 2]
    True
    >>> linear_search([1, 1, 0, 1, -1]) in [0, 1, 3]
    True
    >>> linear_search([-1, 0, 1])
    2
    >>> linear_search(range(1000000))
    999999
    >>> linear_search([0] * 1000000) in range(1000000)
    True
    """
    for index in range(len(values)):
        if plateau(values, index):
            return index
    return False

def binary_search(values):
    """
    Search from the middle of the array for a plateau

    Examples:
    >>> binary_search([])
    False
    >>> binary_search([0])
    0
    >>> binary_search([-1, 0])
    1
    >>> binary_search([0, -1, 0]) in [0, 2]
    True
    >>> binary_search([0, 0, 0, 0, 0]) in range(5)
    True
    >>> binary_search([1, 1, 0, 1, -1]) in [0, 1, 3]
    True
    >>> binary_search([-1, 0, 1])
    2
    >>> binary_search(range(1000000))
    999999
    >>> binary_search([0] * 1000000) in range(1000000)
    True
    >>> binary_search([1, 0, -1, -2, -3, -4, -5])
    0
    >>> binary_search([-5, 1, 0, -1, -2, -3, -4])
    1
    >>> binary_search([-4, -5, 1, 0, -1, -2, -3]) in [0, 2]
    True
    >>> binary_search([-3, -4, -5, 1, 0, -1, -2]) in [0, 3]
    True
    >>> binary_search([-2, -3, -4, -5, 1, 0, -1]) in [0, 4]
    True
    >>> binary_search([-1, -2, -3, -4, -5, 1, 0]) in [0, 5]
    True
    >>> binary_search([0, -1, -2, -3, -4, -5, 1]) in [0, 6]
    True
    """
    if len(values) == 0:
        return False
    else:
        first = 0
        last = len(values) - 1
        while True:
            index = (first + last) / 2
            if first == last:
                return index;
            if index > 0 and values[index - 1] > values[index]:
                # Previous is larger
                last = index - 1
            elif index < len(values) - 1 and values[index + 1] > values[index]:
                # Next is larger
                first = index + 1
            else:
                # Match
                return index
    return False

if __name__ == '__main__':
    import doctest
    doctest.testmod()

