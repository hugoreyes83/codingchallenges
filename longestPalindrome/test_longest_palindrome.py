"""
Test function for longest_palindrome.py
"""
import pytest
from longest_palindrome import longest_palindrome

@pytest.mark.parametrize("s,expected", (
        ("tabbxx", "bb"),
        ("anitalavalatina", "anitalavalatina"),
))
def test_longest_palindrome(s,expected):
    """
    Test function to test longet_palindrome function
    """
    assert longest_palindrome(s) == expected
