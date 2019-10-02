import unittest
import timeit
from operator import itemgetter
from typing import List
import logging

from leetcode.cython_merge_56 import solution2 as cython_solution2

LOG = logging.getLogger(__name__)


class TestMergeInterval(unittest.TestCase):
    """
    https://leetcode.com/problems/merge-intervals/
    Input: [[1,3],[2,6],[8,10],[15,18]]
    Output: [[1,6],[8,10],[15,18]]
    Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
    """
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        return self.solution2(intervals)

    def solution1(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        keep a changable interval pool A, and looping over all intervals
        0. sorted the interval list with the interval start
        1. once the interval overlapped any one within A -> update the interval pool instance
        2. if the interval overlapped nobody -> add a new list to pool

        this solution is quite bad, which just faster than 6% python solution
        """
        def is_overlapped(a, b):
            overlapped = min(a[1], b[1]) - max(a[0], b[0])
            return overlapped >= 0

        interval_pool = []

        intervals.sort(key=lambda x: x[0])  # this can be faster with itemgetter
        for interval in intervals:
            if not interval_pool:
                interval_pool.append(interval)
            else:
                matched = 0
                for interval_pool_obj in interval_pool:
                    if is_overlapped(interval, interval_pool_obj):
                        interval_pool_obj[0] = min(interval[0], interval_pool_obj[0])
                        interval_pool_obj[1] = max(interval[1], interval_pool_obj[1])
                        matched = 1
                        break
                if not matched:
                    interval_pool.append(interval)
        return interval_pool

    def solution2(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        instead of keep the interval pool, we can use a pointer prev to reach our goal
        faster than 98% python solution
        """
        result = []
        prev = None

        intervals.sort(key=itemgetter(0))
        for interval in intervals:
            if prev is None:
                prev = interval
                result.append(prev)
            else:
                # overlapped
                if interval[0] <= prev[1]:
                    prev[1] = max(interval[1], prev[1])
                else:
                    prev = interval
                    result.append(prev)
        return result

    def test_merge1(self):
        self.assertListEqual(self.merge([[1, 4], [4, 5]]), [[1, 5]])

    def test_merge2(self):
        self.assertListEqual(
            self.merge([[1, 3], [2, 6], [8, 10], [15, 18]]), [[1, 6], [8, 10], [15, 18]])

    def test_merge3(self):
        self.assertListEqual(
            self.merge([[1, 4], [2, 3]]), [[1, 4]])

    def test_profiling(self):
        input_ = [[1, 3], [2, 6], [8, 10], [15, 18]]
        LOG.info("---profile solutions---")
        LOG.info("56. solution1: %s", timeit.timeit(lambda: self.solution1(input_), number=1000))
        LOG.info("56. solution2: %s", timeit.timeit(lambda: self.solution2(input_), number=1000))
        # cython implementation without code change shows 4 time faster
        LOG.info("56. cy_solution2: %s",
                 timeit.timeit(lambda: cython_solution2(input_), number=1000))
