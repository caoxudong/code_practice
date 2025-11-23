import unittest
import leetcode.problem_33_search_in_rotated_sorted_array as problem


class UnitTestData:
    def __init__(self, nums: list[int] = [], target: int = 0, expected: int = 0):
        self.nums = nums
        self.target = target
        self.expected = expected


unittest_data = [
    UnitTestData(nums=[4, 5, 6, 7, 0, 1, 2], target=0, expected=4),
    UnitTestData([4, 5, 6, 7, 0, 1, 2], target=3, expected=-1),
    UnitTestData([1], target=0, expected=-1),
]


class TestSolution(unittest.TestCase):
    def test_search(self):
        s = problem.Solution()
        for item in unittest_data:
            result = s.search(item.nums, item.target)
            self.assertEqual(result, item.expected)
