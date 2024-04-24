"""
Test function to test bubble_sort.py
"""
import pytest
from bubble_sort import bubble_sort

@pytest.mark.parametrize("nums,expected", (
    ([6,5,4,3,2,1], [1,2,3,4,5,6]),
    ([54,43,11,3,5,6],[3,5,6,11,43,54]),
))
def test_bubble_sort(nums, expected):
    """
    bubble_sort.py test function
    """
    assert bubble_sort(nums) == expected
