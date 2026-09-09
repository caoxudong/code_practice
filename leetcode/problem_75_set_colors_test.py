import unittest
import leetcode.problem_75_set_colors as problem


class UnitTestData:
    def __init__(self, nums: list[int], expected: list[int]):
        self.nums = nums
        self.expected = expected


unittest_data = [
    UnitTestData(nums=[2, 0, 2, 1, 1, 0], expected=[0, 0, 1, 1, 2, 2]),
    UnitTestData(nums=[2, 0, 1], expected=[0, 1, 2]),
]


class TestSolution(unittest.TestCase):
    def test_leetcode_75_sortColors(self):
        s = problem.Solution()
        for item in unittest_data:
            s.sortColors(item.nums)
            self.assertEqual(item.nums, item.expected)
