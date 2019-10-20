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

    Runtime: 128 ms, faster than 98.99% of Python3 online submissions
    """
    def __init__(self):
        """
        Initialize your data structure here.
        """
        # use None as the finish point
        self.end_up_key = None
        self.mapping = {}

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        mapping = self.mapping
        for w in word:
            if w not in mapping:
                mapping[w] = {}
            mapping = mapping[w]
        mapping[self.end_up_key] = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        mapping = self.mapping
        for w in word:
            if w not in mapping:
                return False
            mapping = mapping[w]
        return mapping.get(self.end_up_key, False)

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        mapping = self.mapping
        for w in prefix:
            if w not in mapping:
                return False
            mapping = mapping[w]
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
