import unittest
import logging


LOG = logging.getLogger(__name__)


class Trie:
    """
    https://leetcode.com/problems/implement-trie-prefix-tree/

    Trie is a tree-based data structure, which is used for efficient retrieval of a key in a
    large data-set of strings.
    Unlike a binary search tree, where node in the tree stores the key associated with that node,
    in trie node’s position in the tree defines the key with which it is associated and the key
    are only associated with the leaves.
    It is also known as prefix tree as all descendants of a node have a common prefix of the string
    associated with that node, and the root is associated with the empty string.
    """
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.mapping = {}
        self.located = False

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        cursor = self
        for w in word:
            mapping = cursor.mapping
            if w in mapping:
                cursor = mapping[w]
            else:
                mapping[w] = Trie()
                cursor = mapping[w]
        cursor.located = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        cursor = self
        for w in word:
            if w in cursor.mapping:
                cursor = cursor.mapping[w]
            else:
                return False
        return cursor.located

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        cursor = self
        for w in prefix:
            if w in cursor.mapping:
                cursor = cursor.mapping[w]
            else:
                return False
        return True


class TestTrieImplementation(unittest.TestCase):
    def test_insert(self):
        word_negative = 'loser_56'
        word_positive = 'winner_182'
        prefix_negative = 'loser'
        prefix_positive = 'winner'
        obj = Trie()
        obj.insert(word_negative)
        self.assertEqual(obj.search(word_negative), True)
        self.assertEqual(obj.search(prefix_negative), False)
        self.assertEqual(obj.startsWith(prefix_negative), True)
        self.assertEqual(obj.search(word_positive), False)
        # a loser is never able to reach any prefix of winner
        self.assertEqual(obj.startsWith(prefix_positive), False)
