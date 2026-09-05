from typing import List
import unittest
import leetcode.problem_70_climbing_stairs as problem


class UnitTestData:
    def __init__(self, n: int, expected: int):
        self.n = n
        self.expected = expected


unittest_data = [
    UnitTestData(n=2, expected=2),
    UnitTestData(n=3, expected=3),
]


class TestSolution(unittest.TestCase):
    def test_leetcode_70_climbing_stairs(self):
        s = problem.Solution()
        for item in unittest_data:
            retval = s.climbStairs(item.n)
            self.assertEqual(retval, item.expected)
