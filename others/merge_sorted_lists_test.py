import unittest
import others.merge_sorted_lists as problem


class UnitTestData:
    def __init__(
        self,
        nums: list[list[int]] = [],
        expected: list[int] = [],
    ):
        self.nums = nums
        self.expected = expected


unittest_data = [
    UnitTestData(
        nums=[
            [1, 2, 3, 4],
            [-3, -2, -1, 0],
            [2, 3, 5, 7],
            [-5, -4, -3, 0],
            [3, 4, 5, 6],
            [9],
        ],
        expected=[-5, -4, -3, -3, -2, -1, 0, 0, 1, 2, 2, 3, 3, 3, 4, 4, 5, 5, 6, 7, 9],
    ),
]


class TestMergeSortedLists(unittest.TestCase):
    def test_merge_sorted_lists(self):
        s = problem.Solution()
        for item in unittest_data:
            result = s.merge_sorted_lists(item.nums)
            self.assertListEqual(result, item.expected)
            result = s.merge_sorted_lists_2(item.nums)
            self.assertListEqual(result, item.expected)
