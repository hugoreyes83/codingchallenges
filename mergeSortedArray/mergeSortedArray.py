from typing import List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        list_to_sort = mergeLists(nums1,m,nums2)
        return sort(list_to_sort)

def sort(list_to_sort):
    if len(list_to_sort) <= 1:
        return list_to_sort
    
    pivot = list_to_sort[0]
    first_half = [ i for i in list_to_sort[1:] if i <= pivot ]
    second_half = [ i for i in list_to_sort[1:] if i > pivot ]
    return sort(first_half) + [ pivot ] + sort(second_half)

def mergeLists(nums1,m,nums2):
    i = m
    for element in nums2:
        nums1[i] = element
        i += 1
    return nums1
