import unittest
import leetcode.problem_20_valid_parentheses as problem


class UnitTestData:
    def __init__(self, s: str = "", expected: bool = False):
        self.s = s
        self.expected = expected


unittest_data = [
    UnitTestData(s="()", expected=True),
    UnitTestData(s="()[]{}", expected=True),
    UnitTestData(s="(]", expected=False),
    UnitTestData(s="([])", expected=True),
    UnitTestData(s="([)]", expected=False),
]


class TestSolution(unittest.TestCase):
    def test_isValid(self):
        s = problem.Solution()
        for item in unittest_data:
            result = s.isValid(item.s)
            print("item={},result={}".format(item.__dict__, result))
            self.assertEqual(result, item.expected)
