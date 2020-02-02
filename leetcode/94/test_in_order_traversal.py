import unittest
import logging
from typing import List

LOG = logging.getLogger(__name__)


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class TestInOrderTraversal(unittest.TestCase):
    def in_order_traversal(self, root: TreeNode) -> List[int]:
        """
        in order traversal is to traverse

        left node -> root -> right node
        """
        return self.in_order_traversal_sol1(root)

    def in_order_traversal_sol1(self, root: TreeNode) -> List[int]:
        """
        Runtime: 24 ms, faster than 87.66% of Python3 online submissions for Binary Tree Inorder Traversal.

        """
        result = []
        if root is not None:
            if root.left is not None:
                result += self.in_order_traversal_sol1(root.left)

            result += [root.val]

            if root.right is not None:
                result += self.in_order_traversal_sol1(root.right)
        return result

    def test_example_tree(self):
        tree = TreeNode(1)
        tree.right = TreeNode(2)
        tree.right.left = TreeNode(3)
        self.assertEqual(self.in_order_traversal(tree), [1, 3, 2])
