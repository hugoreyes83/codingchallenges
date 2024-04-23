"""
Test functions to test can_partition.py
"""
import pytest
from can_partition import can_partition

@pytest.mark.parametrize("nums,expected", (([1,5,11,5], True),))
def test_can_partition(nums,expected):
    """
    Test function for can_partition.py
    """
    assert can_partition(nums) == expected
