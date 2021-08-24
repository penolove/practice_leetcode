import unittest
import logging

LOG = logging.getLogger(__name__)


def parse_num(num1):
    real, complex_ = num1.split("+")
    real = int(real)
    complex_ = int(complex_[:-1])
    return real, complex_


class Solution:
    """
    537. Complex Number Multiplication
    https://leetcode.com/problems/complex-number-multiplication/

    faster than 92% solution
    """

    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        real1, complex1 = parse_num(num1)
        real2, complex2 = parse_num(num2)
        real_ans = real1 * real2 - complex1 * complex2
        complex_ans = real1 * complex2 + real2 * complex1
        return f"{real_ans}+{complex_ans}i"


class TestSolution(unittest.TestCase):
    def test_1(self):
        num1 = "1+1i"
        num2 = "1+1i"
        assert Solution().complexNumberMultiply(num1, num2) == "0+2i"

    def test_2(self):
        num1 = "1+-1i"
        num2 = "1+-1i"
        assert Solution().complexNumberMultiply(num1, num2) == "0+-2i"
