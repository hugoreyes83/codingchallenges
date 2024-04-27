"""
Test functions for trie.py
"""
import pytest
from trie import Trie

@pytest.fixture(name="words")
def fixture_words():
    """
    Words fixture
    """
    return ["apple", "banana", "grape", "orange", "grapefruit"]


def test_trie(words):
    """
    Test function for trie.py
    """
    trie = Trie()
    for word in words:
        trie.insert(word)
    assert trie.search("apple") is True
    assert trie.starts_with("app") is True
    assert trie.search("banana") is True
    assert trie.starts_with("bana") is True
    assert trie.search("grape") is True
    assert trie.starts_with("gr") is True
    assert trie.search("watermelon") is False
    assert trie.starts_with("water") is False
    assert trie.starts_with("pe") is False
