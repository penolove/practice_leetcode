import unittest
import logging
import timeit



LOG = logging.getLogger(__name__)


class TestZigZag(unittest.TestCase):
    """
    https://leetcode.com/problems/zigzag-conversion/
    Input: "PAYPALISHIRING", 4
    Output: "PINALSIGYAHRPI"
    """
    def convert(self, s: str, numRows: int) -> str:
        def serial_function(numRows):
            while True:
                for i in range(numRows):
                    yield i
                for i in reversed(range(1, numRows-1)):
                    yield i

        """naive implmentation
        """
        list_of_rows = [list() for i in range(numRows)]
        for idx, c in zip(serial_function(numRows), s):
            # print(idx)
            list_of_rows[idx].append(c)

        out = ""
        for i in range(numRows):
            out += "".join(list_of_rows[i])
        return out

    def convert_2(self, s: str, numRows: int) -> str:
        """string concat ver
        """
        def serial_function(numRows):
            while True:
                for i in range(numRows):
                    yield i
                for i in reversed(range(1, numRows-1)):
                    yield i


        list_of_rows = ["" for i in range(numRows)]
        for idx, c in zip(serial_function(numRows), s):
            list_of_rows[idx] += c

        out = ""
        for i in range(numRows):
            out += list_of_rows[i]
        return out

    def test_1(self):
        self.assertEqual(self.convert_2("PAYPALISHIRING", 3), "PAHNAPLSIIGYIR")

    def test_2(self):
        self.assertEqual(self.convert_2("PAYPALISHIRING", 4), "PINALSIGYAHRPI")

    def test_3(self):
        self.assertEqual(self.convert_2("A", 1), "A")


    def test_profiling(self):
        LOG.info("55. solution1: %s",
                 timeit.timeit(lambda: self.convert("PAYPALISHIRING", 4), number=1000))

        LOG.info("55. solution1: %s",
                 timeit.timeit(lambda: self.convert_2("PAYPALISHIRING", 4), number=1000))
