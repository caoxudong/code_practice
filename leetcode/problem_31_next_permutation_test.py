import unittest
import leetcode.problem_31_next_permutation as problem


class UnitTestData:
    def __init__(self, nums: list[int] = [], expected: list[int] = []):
        self.nums = nums
        self.expected = expected


unittest_data = [
    UnitTestData(nums=[1, 2, 3], expected=[1, 3, 2]),
    UnitTestData(nums=[3, 2, 1], expected=[1, 2, 3]),
    UnitTestData(nums=[1, 1, 5], expected=[1, 5, 1]),
    UnitTestData(nums=[1, 3, 2], expected=[2, 1, 3]),
]


class TestSolution(unittest.TestCase):
    def test_nextPermutation(self):
        s = problem.Solution()
        for item in unittest_data:
            s.nextPermutation(item.nums)
            self.assertListEqual(item.nums, item.expected)
