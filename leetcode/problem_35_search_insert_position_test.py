import unittest
import leetcode.problem_35_search_insert_position as problem


class UnitTestData:
    def __init__(self, nums: list[int] = [], target: int = 0, expected: int = 0) -> list[int]:
        self.nums = nums
        self.target = target
        self.expected = expected


unittest_data = [
    UnitTestData(nums=[1, 3, 5, 6], target=5, expected=2),
    UnitTestData(nums=[1, 3, 5, 6], target=2, expected=1),
    UnitTestData(nums=[1, 3, 5, 6], target=7, expected=4),
    UnitTestData(nums=[1, 3, 5, 6], target=0, expected=0),
]


class TestSolution(unittest.TestCase):
    def test_leetcode_35_searchInsert(self):
        s = problem.Solution()
        for item in unittest_data:
            result = s.searchInsert(item.nums, item.target)
            self.assertEqual(result, item.expected)
