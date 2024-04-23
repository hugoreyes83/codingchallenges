"""
Function can_partition.py
"""
def can_partition(nums):
    """
    Function to determine if you can partition 
    the array into two subsets such that the sum 
    of the elements in both subsets is equal or false otherwise
    """
    l = set()
    l.add(0)
    for element in nums:
        temp = set()
        for t in l:
            temp.add(t + element)
            temp.add(t)
        l = temp
    if sum(nums) // 2 in l:
        return True
    return False
