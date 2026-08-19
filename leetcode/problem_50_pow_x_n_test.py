from typing import List
import unittest
import leetcode.problem_50_pow_x_n as problem


class UnitTestData:
    def __init__(self, x: float, n: int, expected: float) -> None:
        self.x = x
        self.n = n
        self.expected = expected


unittest_data = [
    UnitTestData(2.00000, n=10, expected=1024.00000),
    UnitTestData(x=2.10000, n=3, expected=9.26100),
    UnitTestData(x=2.00000, n=-2, expected=0.25000),
    UnitTestData(x=0.00001, n=2147483647, expected=0.00000),
]


class TestSolution(unittest.TestCase):
    def test_leetcode_50_myPow(self):
        s = problem.Solution()
        for item in unittest_data:
            retval = s.myPow(item.x, item.n)
            self.assertAlmostEqual(item.expected, retval)
