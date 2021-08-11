import unittest
import logging
from typing import List

# from collections import Counter


LOG = logging.getLogger(__name__)


class PartitionEqualSum:
    """
    Given a non-empty array nums containing only positive integers, find if the array can be
    partitioned into two subsets such that the sum of elements in both subsets is equal.

    Constraints:

    1 <= nums.length <= 200
    1 <= nums[i] <= 100
    """

    def canPartition(self, nums: List[int]) -> bool:
        # if sum is odds -> False
        list_sum = sum(nums)
        if list_sum % 2 == 1:
            return False
        target_num = int(list_sum / 2)

        # if any > target_num -> return False, any = target_num -> True
        for i in nums:
            if i > target_num:
                return False
            elif i == target_num:
                return True
            else:
                break

        # now all the number in nums < target_num,
        # check remaining list can sum to target_num
        # backtesting, find out candidates sums to diff
        failure_target = set()
        # the trick this the failure_target cache
        # once seeing same target, it means what ever candidate it selected, it minus a same number
        # first time I think failure_target is not workable is due to
        # [2, 3, 5, 5, 1], goal 8
        # why you can say target 3 + [1, 2, 3, 5] (5) is equal to target 3, [1, 5, 5] (2, 3)?
        # print(target_num)
        return finding_candidates(target_num, nums, failure_target)


def finding_candidates(target_num, candidates, failure_target):
    if target_num in failure_target:
        return False
    for idx, i in enumerate(candidates):
        if i > target_num:
            continue
        elif i == target_num:
            return True
        else:
            print(target_num, i)
            if finding_candidates(target_num - i, candidates[idx + 1:], failure_target):
                return True
    # print(failure_target)
    failure_target.add(target_num)
    return False


class TestPartitionEqualSum(unittest.TestCase):
    def test_1(self):
        obj = PartitionEqualSum()
        self.assertTrue(obj.canPartition([1, 5, 11, 5]))

    def test_2(self):
        obj = PartitionEqualSum()
        self.assertTrue(obj.canPartition([1, 3, 3, 5]))

    def test_3(self):
        obj = PartitionEqualSum()
        self.assertFalse(obj.canPartition([1, 2, 3, 5]))

    def test_4(self):
        obj = PartitionEqualSum()
        self.assertTrue(obj.canPartition([1, 5, 5, 2, 3]))

    def test_5(self):
        obj = PartitionEqualSum()
        self.assertTrue(obj.canPartition([2, 3, 1, 5, 5]))

    # the test case time-exceeded
    def test_6(self):
        obj = PartitionEqualSum()
        self.assertTrue(
            obj.canPartition(
                [
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    99,
                    97,
                ]
            )
        )
