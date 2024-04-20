"""
Test functions to test binary_search.py
"""
import pytest
from binary_search import binary_search

@pytest.mark.parametrize("expected_input,item,expected",(
                         ([1,2,3,4,5], 5, 4),
                         ([1,2,3], 4, False),
                         ))
def test_binary_search(expected_input, item, expected):
    """
    Test function to test binay_search function
    """
    assert binary_search(expected_input,item) == expected
