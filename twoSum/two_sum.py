"""
TwoSum function, Given an array 
of integers nums and an integer target, 
return indices of the two numbers such that 
they add up to target.
"""
def two_sum(nums, target):
    """
    two_sum function
    """
    num_dict = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_dict:
            return [num_dict[complement], i]
        num_dict[num] = i
    return []
