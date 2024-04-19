"""
This class is meant to merge two lists of different sizes and then merge them into one.
"""
from typing import List
class Solution: # pylint: disable=too-few-public-methods
    """
    Solution class, merge method will return merged and sorted list
    """
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        list_to_sort = merge_lists(nums1, m, nums2, n)
        return sort(list_to_sort)

def sort(list_to_sort):
    """
    Function to sort a list

    Input: unsorted list

    Output: sorted list
    """
    if len(list_to_sort) <= 1:
        return list_to_sort

    pivot = list_to_sort[0]
    first_half = [ i for i in list_to_sort[1:] if i <= pivot ]
    second_half = [ i for i in list_to_sort[1:] if i > pivot ]
    return sort(first_half) + [ pivot ] + sort(second_half)

def merge_lists(nums1, m, nums2, n):
    """
    Function that returns one list after merging two lists of different sizes

    Input: nums1, m and nums2

    Output: sorted list
    """
    if any([n, m]):
        i = m
        for element in nums2:
            nums1[i] = element
            i += 1
    return nums1
