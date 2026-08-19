from typing import List
import unittest
import leetcode.problem_55_jump_game as problem


class UnitTestData:
    def __init__(self, nums: List[int], expected: bool) -> None:
        self.nums = nums
        self.expected = expected


unittest_data = [
    UnitTestData(nums=[2, 3, 1, 1, 4], expected=True),
    UnitTestData(nums=[3, 2, 1, 0, 4], expected=False),
]


class TestSolution(unittest.TestCase):
    def test_leetcode_55_canJump(self):
        s = problem.Solution()
        for item in unittest_data:
            retval = s.canJump(item.nums)
            self.assertEqual(item.expected, retval)
