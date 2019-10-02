import unittest
from typing import List


class TestJumpGame(unittest.TestCase):
    """
    https://leetcode.com/problems/jump-game/
    Input: [2,3,1,1,4]
    Output: True
    Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
    """
    def can_jump(self, nums: List[int]) -> bool:
        return self.solution3(nums)

    def solution1(self, nums):
        """
        In my opinion, this task can be solved with recursive function,
        1. using depth first search to find solutions
        2. once first element can reach the len(num) return True
        3. once we meet 0 at first position return false

        this solution failure due to Time Limit Exceeded, this task can't pass test4
        """
        if nums[0] + 1 >= len(nums):
            return True
        else:
            for i in range(1, nums[0] + 1):
                out = self.solution1(nums[i:])
                if out is True:
                    return out
            return False

    def solution2(self, nums):
        """
        solution1 is too slow, alternative, this task should be slove with DP
        since for each position max distance you can reach is fixed, you needn't calculate it twice

        fuck, this solution will still cause Time Limit Exceeded.
        """
        if len(nums) <= 1:
            return True

        position_max_jump = {}

        def calculate_max_jump(index, nums, position_max_jump):
            if index >= len(nums):
                return 0

            if index in position_max_jump:
                return position_max_jump[index]
            else:
                best = 0
                for step in range(1, nums[index] + 1):
                    landing_distance = step + calculate_max_jump(
                        index + step, nums, position_max_jump)
                    if landing_distance > best:
                        best = landing_distance
                position_max_jump[index] = best
                return best

        return calculate_max_jump(0, nums, position_max_jump) >= len(nums) - 1

    def solution3(self, nums):
        """
        As google for some solution found that the critical point for this question is that:
        `don't concern the route path too much`
        you only need to care if the next step can jump farthest.

        this solution only better than 85% solutions,
        as check most fast solution were count down from the end of array.
        """
        if len(nums) <= 1:
            return True

        reach = nums[0]
        n_nums = len(nums)
        for idx in range(n_nums):
            if idx > reach:  # the farthest position is reach
                break
            if reach >= n_nums - 1:  # already reach the end of list
                break

            reach = max(idx + nums[idx], reach)
        return reach >= n_nums - 1

    def test_jump1(self):
        self.assertEqual(self.can_jump([2, 3, 1, 1, 4]), True)

    def test_jump2(self):
        self.assertEqual(self.can_jump([3, 2, 1, 0, 4]), False)

    def test_jump3(self):
        self.assertEqual(self.can_jump([1, 2, 3]), True)

    def test_jump4(self):
        self.assertEqual(self.can_jump(
            [2,  0,  6,  9,  8,  4,  5,  0,  8,  9,  1,  2,  9,  6,  8,  8,  0,  6,  3,  1,  2,  2,
             1,  2,  6,  5,  3,  1,  2,  2,  6,  4,  2,  4,  3,  0,  0,  0,  3,  8,  2,  4,  0,  1,
             2,  0,  1,  4,  6,  5,  8,  0,  7,  9,  3,  4,  6,  6,  5,  8,  9,  3,  4,  3,  7,  0,
             4,  9,  0,  9,  8,  4,  3,  0,  7,  7,  1,  9,  1,  9,  4,  9,  0,  1,  9,  5,  7,  7,
             1,  5,  8,  2,  8,  2,  6,  8,  2,  2,  7,  5,  1,  7,  9,  6]), False)

    def test_jump5(self):
        self.assertEqual(self.can_jump([0]), True)

    def test_jump6(self):
        self.assertEqual(self.can_jump([2, 0]), True)

    def test_jump7(self):
        self.assertEqual(self.can_jump([2, 0, 0]), True)
