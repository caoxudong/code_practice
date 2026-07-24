from typing import List
import unittest
import leetcode.problem_41_first_missing_positive as problem


class UnitTestData:
    def __init__(self, nums: List[int], expected: int) -> None:
        self.nums = nums
        self.expected = expected


unittest_data = [
    UnitTestData(nums=[1, 2, 0], expected=3),
    UnitTestData(nums=[3, 4, -1, 1], expected=2),
    UnitTestData(nums=[7, 8, 9, 11, 12], expected=1),
]


class TestSolution(unittest.TestCase):
    def test_leetcode_41_firstMissingPositive(self):
        s = problem.Solution()
        for item in unittest_data:
            retval = s.firstMissingPositive(item.nums)
            self.assertEqual(retval, item.expected)
