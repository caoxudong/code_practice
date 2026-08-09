from typing import List
import unittest
import leetcode.problem_45_jump_game_II as problem


class UnitTestData:
    def __init__(self, nums: List[int], expected: int) -> None:
        self.nums = nums
        self.expected = expected


unittest_data = [
    UnitTestData(nums=[2, 3, 1, 1, 4], expected=2),
    UnitTestData(nums=[2, 3, 0, 1, 4], expected=2),
]


class TestSolution(unittest.TestCase):
    def test_leetcode_45_jump(self):
        s = problem.Solution()
        for item in unittest_data:
            retval = s.jump(item.nums)
            self.assertEqual(retval, item.expected)
