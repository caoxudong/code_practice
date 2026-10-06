import unittest
import leetcode.problem_93_restore_ip_addresses as problem


class UnitTestData:
    def __init__(self, s: str, expected: list[str]):
        self.s = s
        self.expected = expected


unittest_data = [
    UnitTestData(s="25525511135", expected=["255.255.11.135", "255.255.111.35"]),
    UnitTestData(s="0000", expected=["0.0.0.0"]),
    UnitTestData(s="101023", expected=["1.0.10.23", "1.0.102.3", "10.1.0.23", "10.10.2.3", "101.0.2.3"]),
]


class TestSolution(unittest.TestCase):
    def test_leetcode_93_restoreIpAddresses(self):
        for item in unittest_data:
            solution = problem.Solution()
            retval = solution.restoreIpAddresses(item.s)
            self.assertEqual(sorted(retval), sorted(item.expected))
