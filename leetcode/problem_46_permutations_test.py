from typing import List
import unittest
import leetcode.problem_46_permutations as problem


class UnitTestData:
    def __init__(self, nums: List[int], expected: List[List[int]]) -> None:
        self.nums = nums
        self.expected = expected


unittest_data = [
    UnitTestData(nums=[1, 2, 3], expected=[[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]),
    UnitTestData(nums=[0, 1], expected=[[0, 1], [1, 0]]),
    UnitTestData(nums=[1], expected=[[1]]),
    UnitTestData(nums=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], expected=[[1]]),
]


class TestSolution(unittest.TestCase):
    def test_leetcode_46_permute(self):
        s = problem.Solution()
        for item in unittest_data:
            retval = s.permute(item.nums)
            self.assertEqual(retval.sort(), item.expected.sort())
