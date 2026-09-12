from typing import List
import unittest
import leetcode.problem_78_subsets as problem


class UnitTestData:
    def __init__(self, nums: List[int], expected: list[list[int]]):
        self.nums = nums
        self.expected = expected
        self.expected = expected


unittest_data = [
    UnitTestData(nums=[1, 2, 3], expected=[[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]),
    UnitTestData(nums=[0], expected=[[], [0]]),
]


class TestSolution(unittest.TestCase):
    def test_leetcode_78_subsets(self):
        s = problem.Solution()
        for item in unittest_data:
            retval = s.subsets(item.nums)
            self.assertEqual(sorted(retval), sorted(item.expected))
