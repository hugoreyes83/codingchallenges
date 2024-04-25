"""
Function to perform quick and sort on an unsorted array
"""
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
