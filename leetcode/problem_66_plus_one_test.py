from typing import List
import unittest
import leetcode.problem_66_plus_one as problem


class UnitTestData:
    def __init__(self, digits: List[int], expected: List[int]):
        self.digits = digits
        self.expected = expected


unittest_data = [
    UnitTestData(digits=[4, 3, 2, 1], expected=[4, 3, 2, 2]),
    UnitTestData(digits=[9], expected=[1, 0]),
]


class TestSolution(unittest.TestCase):
    def test_leetcode_66_plus_one(self):
        s = problem.Solution()
        for item in unittest_data:
            retval = s.plusOne(item.digits)
            self.assertEqual(retval, item.expected)
