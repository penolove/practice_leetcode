import unittest
import logging
from typing import Optional

LOG = logging.getLogger(__name__)


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    https://leetcode.com/problems/maximum-product-of-splitted-binary-tree/
    Given the root of a binary tree, split the binary tree into two subtrees by removing one edge such that the product of the sums of the subtrees is maximized.

    Return the maximum product of the sums of the two subtrees. Since the answer may be too large, return it modulo 109 + 7.

    Note that you need to maximize the answer before taking the mod and not after taking it.

    """

    def maxProduct(self, root: Optional[TreeNode]) -> int:
        self.subtree_sum_values = set()
        tree_sum = self.get_root_value(root)
        max_value = 0
        for i in self.subtree_sum_values:
            n = i * (tree_sum - i)
            if n > max_value:
                max_value = n
        return max_value % 1000000007

    def get_root_value(self, root):
        out = root.val
        if root.left:
            out += self.get_root_value(root.left)
        if root.right:
            out += self.get_root_value(root.right)
        self.subtree_sum_values.add(out)
        return out


def construct_tree_node(nums):
    len_nums = len(nums)
    idx = 0
    root = TreeNode(nums[idx])

    idx = 1
    current_node_pool = [root]
    while idx < len_nums and current_node_pool:
        current_node = current_node_pool.pop(0)

        left = nums[idx]
        idx += 1
        right = nums[idx]
        idx += 1
        if left is not None:
            current_node.left = TreeNode(left)
            current_node_pool.append(current_node.left)
        if right is not None:
            current_node.right = TreeNode(right)
            current_node_pool.append(current_node.right)
    return root


class TestSolution(unittest.TestCase):
    def test_1(self):
        nums = [1, 2, 3, 4, 5, 6, None]
        root = construct_tree_node(nums)
        assert Solution().maxProduct(root) == 110

    def test_2(self):
        nums = [1, None, 2, 3, 4, None, None, 5, 6]
        root = construct_tree_node(nums)
        assert Solution().maxProduct(root) == 90

    def test_3(self):
        nums = [2, 3, 9, 10, 7, 8, 6, 5, 4, 11, 1, None, None]
        root = construct_tree_node(nums)
        assert Solution().maxProduct(root) == 1025
