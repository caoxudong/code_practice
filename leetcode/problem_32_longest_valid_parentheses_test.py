import unittest
import leetcode.problem_32_longest_valid_parentheses as problem


class UnitTestData:
    def __init__(self, s: str = "", expected: int = 0):
        self.s = s
        self.expected = expected


unittest_data = [
    UnitTestData(s="", expected=0),
    UnitTestData(s="(()", expected=2),
    UnitTestData(s="())", expected=2),
    UnitTestData(s=")()())", expected=4),
    UnitTestData(s="(((((((()()()()())))))))", expected=24),
    UnitTestData(s=")))())()((())", expected=4),
]


class TestSolution(unittest.TestCase):
    def test_longestValidParentheses(self):
        s = problem.Solution()
        for item in unittest_data:
            result = s.longestValidParentheses(item.s)
            self.assertEqual(result, item.expected)
