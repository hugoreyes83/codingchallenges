"""
Bubble sort funtion
"""
def bubble_sort(nums):
    """
    Bubble sort implementation to sort an unsorted list
    """
    idx = 1
    for _ in range(len(nums)):
        for j in range(len(nums) - idx):
            if nums[j] > nums[j + 1]:
                tmp = nums[j]
                nums[j] = nums[j + 1]
                nums[j + 1] = tmp
        idx += 1
    return nums
