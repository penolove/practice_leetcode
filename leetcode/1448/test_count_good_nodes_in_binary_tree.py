# Minimum Window Substring
import unittest
import logging

LOG = logging.getLogger(__name__)


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    https://leetcode.com/problems/count-good-nodes-in-binary-tree/
    Given a binary tree root, a node X in the tree is named good
    if in the path from root to X there are no nodes with a value greater than X.

    Return the number of good nodes in the binary tree.
    """

    def goodNodes(self, root: TreeNode) -> int:
        return self.get_good_nodes(root, -10001)

    def get_good_nodes(self, node, max_value):
        count = 0
        if node.val >= max_value:
            count += 1

        max_value = max(node.val, max_value)
        if node.left is not None:
            count += self.get_good_nodes(node.left, max_value)
        if node.right is not None:
            count += self.get_good_nodes(node.right, max_value)
        return count


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
        nums = [3, 1, 4, 3, None, 1, 5]
        root = construct_tree_node(nums)
        assert Solution().goodNodes(root) == 4

    def test_2(self):
        nums = [3, 3, None, 4, 2]
        root = construct_tree_node(nums)
        assert Solution().goodNodes(root) == 3

    def test_3(self):
        nums = [1]
        root = construct_tree_node(nums)
        assert Solution().goodNodes(root) == 1
