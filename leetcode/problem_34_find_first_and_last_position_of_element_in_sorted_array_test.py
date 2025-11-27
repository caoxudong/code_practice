import unittest
import leetcode.problem_34_find_first_and_last_position_of_element_in_sorted_array as problem


class UnitTestData:
    def __init__(
        self, nums: list[int] = [], target: int = 0, expected: list[int] = []
    ) -> list[int]:
        self.nums = nums
        self.target = target
        self.expected = expected


unittest_data = [
    UnitTestData(nums=[5, 7, 7, 8, 8, 10], target=8, expected=[3, 4]),
    UnitTestData(nums=[5, 7, 7, 8, 8, 10], target=6, expected=[-1, -1]),
    UnitTestData(nums=[], target=0, expected=[-1, -1]),
]


class TestSolution(unittest.TestCase):
    def test_searchRange(self):
        s = problem.Solution()
        for item in unittest_data:
            result = s.searchRange(item.nums, item.target)
            self.assertListEqual(result, item.expected)
