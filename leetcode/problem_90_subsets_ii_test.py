import unittest
import leetcode.problem_90_subsets_ii as problem


class UnitTestData:
    def __init__(self, nums: list[int], expected: list[list[int]]):
        self.nums = nums
        self.expected = expected


unittest_data = [
    UnitTestData(nums=[1, 2, 2], expected=[[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]),
    UnitTestData(nums=[0], expected=[[], [0]]),
]


class TestSolution(unittest.TestCase):
    def test_leetcode_90_subsetsWithDup(self):
        for item in unittest_data:
            soluiton = problem.Solution()
            retval = soluiton.subsetsWithDup(item.nums)
            self.assertEqual(sorted(retval), sorted(item.expected))
