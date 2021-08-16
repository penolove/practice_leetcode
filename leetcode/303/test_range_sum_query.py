# Minimum Window Substring
import unittest
import logging
from typing import List
LOG = logging.getLogger(__name__)


class NumArray:
    """
    https://leetcode.com/problems/range-sum-query-immutable/
    init with O(n)
    query with O(1)
    """
    def __init__(self, nums: List[int]):
        acc_sum = []
        for idx, i in enumerate(nums):
            if idx == 0:
                acc_sum.append(i)
            else:
                acc_sum.append(i + acc_sum[idx-1])
        self.acc_sum = acc_sum

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.acc_sum[right]
        else:
            return self.acc_sum[right] - self.acc_sum[left-1]


class TestSolution(unittest.TestCase):
    def test_1(self):
        actions = ["NumArray", "sumRange", "sumRange", "sumRange"]
        values = [[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
        ans = [None, 1, -1, -3]
        out = None
        for action, value, ans in zip(actions, values, ans):
            if action == "NumArray":
                out = NumArray(value[0])
                assert ans is None
            else:
                result = out.sumRange(left=value[0], right=value[1])
                assert result == ans
