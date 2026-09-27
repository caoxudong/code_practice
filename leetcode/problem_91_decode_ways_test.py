import unittest
import leetcode.problem_91_decode_ways as problem


class UnitTestData:
    def __init__(self, s: str, expected: int):
        self.s = s
        self.expected = expected


unittest_data = [
    UnitTestData(s="12", expected=2),
    UnitTestData(s="226", expected=3),
    UnitTestData(s="06", expected=0),
]


class TestSoluiton(unittest.TestCase):
    def test_leetcode_91_numDecodings(self):
        for item in unittest_data:
            solution = problem.Solution()
            retval = solution.numDecodings(item.s)
            self.assertEqual(retval, item.expected)
