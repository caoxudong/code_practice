import unittest
import leetcode.problem_81_search_in_rotated_sorted_array_II as problem


class UnitTestData:
    def __init__(self, nums, target, expected):
        self.nums = nums
        self.target = target
        self.expected = expected


unittest_data = [
    UnitTestData(nums=[2, 5, 6, 0, 0, 1, 2], target=0, expected=True),
    UnitTestData(nums=[2, 5, 6, 0, 0, 1, 2], target=3, expected=False),
]


class TestSolution(unittest.TestCase):
    def test_leetcode_81_search_in_rotated_sorted_array_II(self):
        s = problem.Solution()
        for item in unittest_data:
            retval = s.search(item.nums, item.target)
            self.assertEqual(retval, item.expected)
