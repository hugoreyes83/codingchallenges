"""
Sort string function
"""
import string

def quick_sort(nums):
    """
    quick sort implementation
    """
    if len(nums) <= 1:
        return nums

    pivot = nums[0]

    left = [ i for i in nums[1:] if i <= pivot ]
    right = [ i for i in nums[1:] if i > pivot ]

    return quick_sort(left) + [pivot] + quick_sort(right)


def sort_string(s):
    """
    Function sorts an unsorted string
    """
    alphabets = list(string.ascii_letters)
    temp = []
    for element in s:
        temp.append(alphabets.index(element))

    sorted_list = quick_sort(temp)
    temp = []
    for element in sorted_list:
        temp.append(alphabets[element])
    return "".join(temp)
