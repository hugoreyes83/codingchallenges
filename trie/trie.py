"""
Class implementation of a trie data sctructure
"""

class TrieNode: # pylint: disable=too-few-public-methods
    """
    TrieNode class
    """
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie: # pylint: disable=too-few-public-methods
    """
    Trie class implementation
    """
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        insert function
        """
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word):
        """
        search function
        """
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def starts_with(self, prefix):
        """
        starts_with function
        """
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True
