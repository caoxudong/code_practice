import unittest
import leetcode.problem_29_divide_two_integers as problem


class UnitTestData:
    def __init__(self, dividend: int = 0, divisor: int = 0, expected: int = 0):
        self.dividend = dividend
        self.divisor = divisor
        self.expected = expected


unittest_data = [
    # UnitTestData(dividend=7, divisor=-3, expected=-2),
    # UnitTestData(dividend=10, divisor=3, expected=3),
    UnitTestData(dividend=-2147483648, divisor=-1, expected=2147483647),
]


class TestSolution(unittest.TestCase):
    def test_divide(self):
        s = problem.Solution()
        for item in unittest_data:
            result = s.divide(item.dividend, item.divisor)
            self.assertEqual(result, item.expected)
