import unittest
import logging
from typing import List

LOG = logging.getLogger(__name__)


def check_number_valid(n: int) -> bool:
    return int(n) <= 255 and edge_case_check(n)


def edge_case_check(n):
    return len(n) == len(str(int(n)))


class TestRestoreIPAddress(unittest.TestCase):
    def restore_ip_addresses(self, x: str) -> List[str]:
        return self.restore_ip_addresses_sol1(x)

    def restore_ip_addresses_sol1(self, x: str, split_remain=3) -> List[str]:
        """
        for this question is to find all the splits that the string
        can be represent as ip address.
        Runtime: 24 ms, faster than 97.65% of Python3 online submissions for Restore IP Addresses

        """
        if len(x) > (split_remain + 1) * 3:  # string too long
            return []

        if len(x) < (split_remain + 1):  # string too sort
            return []

        all_candidates = []
        if split_remain >= 1 and len(x) > 1:
            max_range = min(len(x), 4)  # needn't check prefix length > 4
            for split in range(1, max_range):
                prefix = x[:split]
                if check_number_valid(prefix):
                    satisfied_result = self.restore_ip_addresses_sol1(
                        x[split:], split_remain=split_remain - 1
                    )
                    all_candidates += [
                        "%s.%s" % (prefix, suffix) for suffix in satisfied_result
                    ]

            return all_candidates
        elif split_remain == 0 and check_number_valid(x):
            return [x]
        else:
            return []

    def test_result1(self):
        self.assertListEqual(
            set(self.restore_ip_addresses("25525511135")),
            set(["255.255.11.135", "255.255.111.35"]),
        )

    def test_result2(self):
        self.assertSetEqual(
            set(self.restore_ip_addresses("010010")), set(["0.10.0.10", "0.100.1.0"])
        )
