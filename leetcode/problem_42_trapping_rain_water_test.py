from typing import List
import unittest
import leetcode.problem_42_trapping_rain_water as problem


class UnitTestData:
    def __init__(self, height: List[int], expected: int) -> None:
        self.height = height
        self.expected = expected


unittest_data = [
    UnitTestData(height=[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], expected=6),
    UnitTestData(height=[4, 2, 0, 3, 2, 5], expected=9),
]


class TestSolution(unittest.TestCase):
    def test_leetcode_42_trap(self):
        s = problem.Solution()
        for item in unittest_data:
            retval = s.trap(item.height)
            self.assertEqual(retval, item.expected)
