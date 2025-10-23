import unittest
import leetcode.problem_152_maximum_product_subarray as problem


class UnitTestData:
    def __init__(self, nums: list[int] = [], expected: int = []):
        self.nums = nums
        self.expected = expected


unittest_data = [
    UnitTestData(nums=[5, -3, 2, 7, -5, 3, 9, -3], expected=28350),
    UnitTestData(nums=[2, 3, -2, 4], expected=6),
    UnitTestData(nums=[-2, 0, -1], expected=0),
]


class TestSolution(unittest.TestCase):
    def test_maxProduct(self):
        s = problem.Solution()
        for item in unittest_data:
            result = s.maxProduct(item.nums)
            self.assertEqual(result, item.expected)
