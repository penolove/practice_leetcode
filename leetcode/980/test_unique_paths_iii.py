import unittest
import logging
from typing import List


LOG = logging.getLogger(__name__)


class UniquePath:
    """
    https://leetcode.com/problems/unique-paths-iii/

    On a 2-dimensional grid, there are 4 types of squares:

    1 represents the starting square.  There is exactly one starting square.
    2 represents the ending square.  There is exactly one ending square.
    0 represents empty squares we can walk over.
    -1 represents obstacles that we cannot walk over.
    Return the number of 4-directional walks from the starting square to the ending square,
    that walk over every non-obstacle square exactly once.

    Example 1:

    Input: [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
    Output: 2
    Explanation: We have the following two paths:
    1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2)
    2. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2)

    Backtracking brute force, not a smart solution. 2020-05-31
    Runtime: 52 ms, faster than 88.89% of Python3 online submissions for Unique Paths III.

    """

    def unique_paths_iii(self, grid: List[List[int]]) -> int:
        n_row = len(grid)
        n_col = len(grid[0])
        # get the start position

        (start_x, start_y), n_zero = self.find_start_and_get_zero_count(
            grid, n_row, n_col
        )

        return get_paths(grid, n_row, n_col, start_x, start_y, n_zero + 1)

    def find_start_and_get_zero_count(self, grid, n_row, n_col):
        start = None
        n_zero = 0
        for i in range(n_row):
            for j in range(n_col):
                if grid[i][j] == 1:
                    start = (i, j)
                if grid[i][j] == 0:
                    n_zero += 1
        return start, n_zero


def get_paths(grid, n_row, n_col, cx, cy, n_zero):
    if cx < 0 or cx > (n_row - 1):
        return 0
    if cy < 0 or cy > (n_col - 1):
        return 0

    target_value = grid[cx][cy]
    if target_value == 2:
        if n_zero == 0:
            return 1
        else:
            return 0
    elif target_value == -1:
        return 0
    elif target_value == 0 or target_value == 1:
        grid[cx][cy] = -1
        count = get_paths(grid, n_row, n_col, cx + 1, cy, n_zero - 1)
        count += get_paths(grid, n_row, n_col, cx, cy + 1, n_zero - 1)
        count += get_paths(grid, n_row, n_col, cx - 1, cy, n_zero - 1)
        count += get_paths(grid, n_row, n_col, cx, cy - 1, n_zero - 1)
        grid[cx][cy] = 0
        return count


class TestUniquePathImplementation(unittest.TestCase):
    def test_1(self):
        obj = UniquePath()
        assert obj.unique_paths_iii([[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 2, -1]]) == 2

    def test_2(self):
        obj = UniquePath()
        assert obj.unique_paths_iii([[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 2]]) == 4

    def test_3(self):
        obj = UniquePath()
        assert obj.unique_paths_iii([[0, 1], [2, 0]]) == 0
