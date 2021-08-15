# Minimum Window Substring
import unittest
import logging
from collections import defaultdict, Counter

LOG = logging.getLogger(__name__)


class Solution:
    """
    https://leetcode.com/problems/minimum-window-substring/
    https://leetcode.com/explore/challenge/card/august-leetcoding-challenge-2021/615/week-3-august-15th-august-21st/3891/
    Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

    The testcases will be generated such that the answer is unique.

    A substring is a contiguous sequence of characters within the string.


    """  # noqa

    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        else:
            t_counter = Counter(t)
            window_counter = defaultdict(int)

            # stage 1: find first left right idx
            target_found = False
            for i in range(len(s)):
                window_counter[s[i]] += 1
                if all(c <= window_counter[k] for k, c in t_counter.items()):
                    target_found = True
                    right_idx = i + 1
                    break
            if not target_found:
                return ""

            # move left to the index make string shortest
            left_idx = 0
            for i in range(right_idx):
                window_counter[s[i]] -= 1
                if all(c <= window_counter[k] for k, c in t_counter.items()):
                    left_idx = i + 1
                else:
                    break

            # since we already have a answer left_idx: right_idx
            # lets find answer with shorten slices from left_idx +1: right_idx with slicing window
            # print(f"stage1 {right_idx}, {left_idx}")

            # stage 2: moving window to get the minimum length string
            search_r_idx = right_idx
            search_l_idx = left_idx + 1
            while search_r_idx < len(s):

                if search_r_idx - search_l_idx < len(t):
                    break

                left_charater = s[search_l_idx]
                window_counter[left_charater] -= 1
                search_l_idx += 1

                right_charater = s[search_r_idx]
                window_counter[right_charater] += 1
                search_r_idx += 1

                # if got answer check if we can shorten the len or not
                while all(c <= window_counter[i] for i, c in t_counter.items()):
                    right_idx = search_r_idx
                    left_idx = search_l_idx

                    left_charater = s[search_l_idx]
                    if window_counter[left_charater] - 1 >= t_counter[left_charater]:
                        search_l_idx += 1
                        window_counter[left_charater] -= 1
                    else:
                        break
            return s[left_idx:right_idx]

# I fail to finish within 30 minutes
# solution: https://leetcode.com/problems/minimum-window-substring/solution/
# the solution in the answer is much elegant than mine


class TestSolution(unittest.TestCase):
    def test_1(self):
        obj = Solution()
        s = "a"
        t = "aa"
        ans = ""
        assert obj.minWindow(s=s, t=t) == ans

    def test_2(self):
        obj = Solution()
        s = "a"
        t = "a"
        ans = "a"
        assert obj.minWindow(s=s, t=t) == ans

    def test_3(self):
        obj = Solution()
        s = "ADOBECODEBANC"
        t = "ABC"
        ans = "BANC"
        assert obj.minWindow(s=s, t=t) == ans

    def test_4(self):
        obj = Solution()
        s = "cabwefgewcwaefgcf"
        t = "cae"
        ans = "cwae"
        assert obj.minWindow(s=s, t=t) == ans

    def test_5(self):
        obj = Solution()
        s = "ab"
        t = "b"
        ans = "b"
        assert obj.minWindow(s=s, t=t) == ans
