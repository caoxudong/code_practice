from typing import List
import unittest
import leetcode.problem_69_sqrt_x as problem


class UnitTestData:
    def __init__(self, x: int, expected: int):
        self.x = x
        self.expected = expected


unittest_data = [
    UnitTestData(x=4, expected=2),
    UnitTestData(x=8, expected=2),
]


class TestSolution(unittest.TestCase):
    def test_leetcode_69_sqrt_x(self):
        s = problem.Solution()
        for item in unittest_data:
            retval = s.mySqrt(item.x)
            self.assertEqual(retval, item.expected)
