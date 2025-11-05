import unittest
import leetcode.problem_22_generate_parentheses as problem


class UnitTestData:
    def __init__(self, n: int = 0, expected: list[str] = []):
        self.n = n
        self.expected = expected


unittest_data = [
    UnitTestData(n=3, expected=["((()))", "(()())", "(())()", "()(())", "()()()"]),
    UnitTestData(n=1, expected=["()"]),
]


def assertGeneratedParenthesesEqual(result: list[str] = [], expected: list[str] = []):
    assertError = AssertionError(
        "AssertionError, result is {}, expected is {}".format(result, expected)
    )

    if len(result) != len(expected):
        raise assertError

    for s in result:
        if s not in expected:
            raise assertError


class TestSolution(unittest.TestCase):
    def test_generateParenthesis(self):
        s = problem.Solution()
        for item in unittest_data:
            result = s.generateParenthesis(item.n)
            assertGeneratedParenthesesEqual(result, item.expected)
