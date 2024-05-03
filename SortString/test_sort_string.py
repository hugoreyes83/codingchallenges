"""
Test function for sort_string.py
"""
import pytest
from sort_string import sort_string

@pytest.mark.parametrize("s,expected", (
                         ("Zbajsdfhsahq", "aabdfhhjqssZ"),
                         ))
def test_sort_string(s,expected):
    """
    Test function for sort_string.py
    """
    assert sort_string(s) == expected
