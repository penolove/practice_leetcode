import unittest
from typing import List


class TestMergeInterval(unittest.TestCase):
    """
    https://leetcode.com/problems/merge-intervals/
    Input: [[1,3],[2,6],[8,10],[15,18]]
    Output: [[1,6],[8,10],[15,18]]
    Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
    """
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        return [[1, 5]]

    def test_merge(self):
        self.assertListEqual(self.merge([[1, 4], [4, 5]]), [[1, 5]])
