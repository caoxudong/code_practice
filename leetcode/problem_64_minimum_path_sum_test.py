from typing import List
import unittest
import leetcode.problem_64_minimum_path_sum as problem


class UnitTestData:
    def __init__(self, grid: List[List[int]], expected: int) -> None:
        self.grid = grid
        self.expected = expected


unittest_data = [
    UnitTestData(grid=[[1, 3, 1], [1, 5, 1], [4, 2, 1]], expected=7),
    UnitTestData(grid=[[1, 2, 3], [4, 5, 6]], expected=12),
]


class TestSolution(unittest.TestCase):
    def test_leetcode_64_minPathSum(self):
        s = problem.Solution()
        for item in unittest_data:
            retval = s.minPathSum(item.grid)
            self.assertEqual(retval, item.expected)
