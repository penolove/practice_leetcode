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
    653. Two Sum IV - Input is a BST
    Given the root of a Binary Search Tree and a target number k, return true if there exist two elements in the BST such that their sum is equal to the given target.

    """
    # a dfs + dp solution
    # the critical thinking is that in the worse case I will traverse all the nodes
    # k = node.val + remaining
    # let's assume remaining in the tree
    # if I meet k first, I don't know whether the remaining exists
    # but once I meet the remaining I know k exists -> return True
    def findTarget(self, root: 'TreeNode', k: 'int') -> 'bool':
        s = set()

        def helper(root, k):
            if not root:
                return False
            if k - root.val in s:
                return True
            s.add(root.val)
            return helper(root.left, k) or helper(root.right, k)

        return helper(root, k)


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
        nums = [5, 3, 6, 2, 4, None, 7]
        root = construct_tree_node(nums)
        assert Solution().findTarget(root, 9) == True

    def test_2(self):
        nums = [5, 3, 6, 2, 4, None, 7]
        root = construct_tree_node(nums)
        assert Solution().findTarget(root, 28) == False

    def test_3(self):
        nums = [2, 1, 3]
        root = construct_tree_node(nums)
        assert Solution().findTarget(root, 4) == True
