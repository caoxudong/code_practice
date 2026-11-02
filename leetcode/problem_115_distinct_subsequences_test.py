import unittest
import leetcode.problem_115_distinct_subsequences as problem


class UnitTestData:
    def __init__(self, s: str, t: str, expected: int):
        self.s = s
        self.t = t
        self.expected = expected


unittest_data: list[UnitTestData] = [
    UnitTestData(s="rabbbit", t="rabbit", expected=3),
    UnitTestData(s="babgbag", t="bag", expected=5),
]


class TestSolution(unittest.TestCase):
    def test_leetcode_115_numDistinct(self):
        for item in unittest_data:
            solution = problem.Solution()
            retval = solution.numDistinct(item.s, item.t)
            self.assertEqual(retval, item.expected)
