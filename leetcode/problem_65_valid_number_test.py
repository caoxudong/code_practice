import unittest
import problem_65_valid_number as problem


class UnitTestData:
    def __init__(self, s: str, expected: str):
        self.s = s
        self.expected = expected


unittest_data = [
    UnitTestData(s="0", expected=True),
    UnitTestData(s="e", expected=False),
    UnitTestData(s=".", expected=False),
]


class TestSolution(unittest.TestCase):
    def test_leetcode_65_isNumber(self):
        s = problem.Solution()
        for item in unittest_data:
            retval = s.isNumber(item.s)
            self.assertEqual(retval, item.expected)
