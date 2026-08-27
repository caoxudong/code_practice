from typing import List
import unittest
import leetcode.problem_63_unique_paths_II as problem


class UnitTestData:
    def __init__(self, obstacleGrid: List[List[int]], expected: int) -> None:
        self.obstacleGrid = obstacleGrid
        self.expected = expected


unittest_data = [
    UnitTestData(obstacleGrid=[[0, 0, 0], [0, 1, 0], [0, 0, 0]], expected=2),
    UnitTestData(obstacleGrid=[[0, 1], [0, 0]], expected=1),
]


class TestSolution(unittest.TestCase):
    def test_leetcode_63_uniquePathsWithObstacles(self):
        s = problem.Solution()
        for item in unittest_data:
            retval = s.uniquePathsWithObstacles(item.obstacleGrid)
            self.assertEqual(retval, item.expected)
