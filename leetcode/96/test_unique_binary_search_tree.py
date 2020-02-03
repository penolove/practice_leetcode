import unittest
import logging

LOG = logging.getLogger(__name__)


class TestUniqueBinarySearchTree(unittest.TestCase):
    def numTrees(self, n: int) -> int:
        # return self.sol_1(list(range(n)))
        query_map = {0: 1, 1: 1, 2: 2}
        # result = self.sol_2(n, query_map)
        result = self.sol_3(n, query_map)
        return result

    def sol_1(self, candidates):
        """
        this solution will timeout,
        seems recursive too much times,
        maybe I just need to use number instead of list of elements
        """
        result = 0
        for i in candidates:
            gt_candidates = [j for j in candidates if j > i]
            le_candidates = [j for j in candidates if j < i]
            if len(le_candidates) <= 1:
                left = 1
            else:
                left = self.sol_1(le_candidates)

            if len(gt_candidates) <= 1:
                right = 1
            else:
                right = self.sol_1(gt_candidates)

            result += right * left

        return result

    def sol_2(self, n: int, query_map: dict):
        """
        Runtime: 28 ms, faster than 59.44% of Python3 online submissions
        for Unique Binary Search Trees.
        """
        if n in query_map:
            return query_map[n]

        result = 0
        for i in range(n):
            gt_members = n - (i + 1)
            le_members = i
            if le_members <= 1:
                left = 1
            else:
                left = query_map.get(le_members, self.sol_2(le_members, query_map))

            if gt_members <= 1:
                right = 1
            else:
                right = query_map.get(gt_members, self.sol_2(gt_members, query_map))
            result += right * left
        query_map[n] = result
        return result

    def sol_3(self, n: int, query_map: dict):
        """
        Runtime: 24 ms, faster than 85.49% of Python3 online submissions
        for Unique Binary Search Trees.
        """

        if n in query_map:
            return query_map[n]

        result = 0
        for i in range(n // 2, n):
            gt_members = n - (i + 1)
            le_members = i

            left = query_map.get(le_members, self.sol_3(le_members, query_map))
            if gt_members == le_members:
                right = left
            else:
                right = query_map.get(gt_members, self.sol_3(gt_members, query_map))

            if i == n // 2 and n % 2 == 1:
                result += right * left
            else:
                result += right * left * 2

        query_map[n] = result
        return result

    def test_example(self):
        self.assertEqual(self.numTrees(3), 5)

    def test_example1(self):
        self.assertEqual(self.numTrees(6), 132)

    def test_example2(self):
        self.assertEqual(self.numTrees(19), 1767263190)
