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
    98. Validate Binary Search Tree
    https://leetcode.com/problems/validate-binary-search-tree/submissions/
    """
    def isValidBST(self, root: TreeNode, min_value=None, max_value=None) -> bool:
        # root check
        if root is None:
            return True

        # check self bigger than left
        if root.left is not None and root.val <= root.left.val:
            return False

        if root.right is not None and root.val >= root.right.val:
            return False

        if min_value is not None and root.val <= min_value:
            return False

        if max_value is not None and root.val >= max_value:
            return False

        # # subtree check
        if not self.isValidBST(root.left, min_value=min_value, max_value=root.val):
            return False
        return self.isValidBST(root.right, min_value=root.val, max_value=max_value)


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
        nums = [3, 1, 5, 0, 2, 4, 6, None, None, None, 3]

        root = construct_tree_node(nums)
        assert Solution().isValidBST(root) == False

    def test_2(self):
        nums = [2, 1, 3]
        root = construct_tree_node(nums)
        assert Solution().isValidBST(root) == True

    def test_3(self):
        nums = [5, 1, 4, None, None, 3, 6]
        root = construct_tree_node(nums)
        assert Solution().isValidBST(root) == False
