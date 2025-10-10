import unittest
import leetcode.problem_53_maximum_subarray as problem


class UnitTestData:
    def __init__(self, nums: list[int] = [], expected: int = []):
        self.nums = nums
        self.expected = expected


unittest_data = [
    UnitTestData(nums=[5, -3, 2, 7, -5, 3, 9, -3], expected=18),
]


class TestSolution(unittest.TestCase):
    def test_maxSubArray(self):
        s = problem.Solution()
        for item in unittest_data:
            result = s.maxSubArray(item.nums)
            self.assertEqual(result, item.expected)
