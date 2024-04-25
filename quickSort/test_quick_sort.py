"""
Test function for quick_sort.py
"""
import pytest
from quick_sort import quick_sort

@pytest.mark.parametrize("nums,expected", (
        ([9,8,7,6,5,4,3,2,1], [1,2,3,4,5,6,7,8,9]),
))
def test_quick_sort(nums, expected):
    """
    Test function for quicksort
    """
    assert quick_sort(nums) == expected
