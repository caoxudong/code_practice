import unittest
from leetcode.problem_76_minimum_window_substring import problem


class UnitTestData:
    def __init__(self, s: str, t: str, expected: str):
        self.s = s
        self.t = t
        self.expected = expected


unittest_data = [
    UnitTestData(s="ADOBECODEBANC", t="ABC", expected="BANC"),
    UnitTestData(s="a", t="a", expected="a"),
    UnitTestData(s="a", t="aa", expected=""),
]


class TestSolution(unittest.TestCase):
    def test_leetcode_76_minWindow(self):
        s = problem.Solution()
        for item in unittest_data:
            retval = s.minWindow(item.s, item.t)
            self.assertEqual(retval, item.expected)
