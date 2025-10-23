import unittest
import leetcode.problem_697_degree_of_an_array as problem


class UnitTestData:
    def __init__(self, nums: list[int] = [], expected: int = 0):
        self.nums = nums
        self.expected = expected


unittest_data = [
    UnitTestData(nums=[1, 2, 2, 3, 1], expected=2),
    UnitTestData(nums=[1, 2, 2, 3, 1, 4, 2], expected=6),
    UnitTestData(nums=[1], expected=1),
    UnitTestData(nums=[1, 1], expected=2),
]


class TestSolution(unittest.TestCase):
    def test_findShortestSubArray(self):
        s = problem.Solution()
        for item in unittest_data:
            result = s.findShortestSubArray(item.nums)
            self.assertEqual(result, item.expected)
