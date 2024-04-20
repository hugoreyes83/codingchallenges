"""
Binary search function to perform binary search on an unordered list.
"""
def binary_search(lst, item):
    """
    Function to perfrom binary search on an ordered list
    """
    first = 0
    last = len(lst) - 1
    found = False
    middle = len(lst) // 2
    while (first <= last and not found):
        middle = (first + last) // 2
        if lst[middle] == item:
            found = True
            return middle
        if item < lst[middle]:
            last = middle - 1
        else:
            first = middle + 1

    if not found:
        return False
    return None
