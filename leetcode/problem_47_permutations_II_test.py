from typing import List
import unittest
import leetcode.problem_47_permutations_II as problem


class UnitTestData:
    def __init__(self, nums: List[int], expected: List[List[int]]) -> None:
        self.nums = nums
        self.expected = expected


unittest_data = [
    UnitTestData(nums=[1, 2, 3], expected=[[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]),
    UnitTestData(nums=[1, 1, 2], expected=[[1, 1, 2], [1, 2, 1], [2, 1, 1]]),
]


class TestSolution(unittest.TestCase):
    def test_leetcode_47_permuteUnique(self):
        s = problem.Solution()
        for item in unittest_data:
            retval = s.permuteUnique(item.nums)
            self.assertEqual(retval.sort(), item.expected.sort())
