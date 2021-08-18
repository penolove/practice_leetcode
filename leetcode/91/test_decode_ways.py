import unittest
import logging

LOG = logging.getLogger(__name__)
string_mapping = set(str(i) for i in range(1, 27))
cache = {}


class Solution_1:
    """
    https://leetcode.com/problems/decode-ways/
    """

    cache = {}

    def numDecodings(self, s: str) -> int:
        if s in cache:
            return cache[s]

        if len(s) == 0:
            return 1
        elif s[0] == "0":
            return 0
        out = 0
        if len(s) >= 1 and s[0] in string_mapping:
            res = self.numDecodings(s[1:])
            cache[s[1:]] = res
            out += res

        if len(s) >= 2 and s[:2] in string_mapping:
            res = self.numDecodings(s[2:])
            cache[s[2:]] = res
            out += res

        cache[s] = out
        return out


class TestSolution(unittest.TestCase):
    def test_1(self):
        input_ = "12"
        assert Solution_1().numDecodings(input_) == 2

    def test_2(self):
        input_ = "226"
        assert Solution_1().numDecodings(input_) == 3

    def test_3(self):
        input_ = "0"
        assert Solution_1().numDecodings(input_) == 0

    def test_4(self):
        input_ = "06"
        assert Solution_1().numDecodings(input_) == 0
