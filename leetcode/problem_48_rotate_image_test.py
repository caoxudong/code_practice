from typing import List
import unittest
import leetcode.problem_48_rotate_image as problem


class UnitTestData:
    def __init__(self, matrix: List[List[int]], expected: List[List[int]]) -> None:
        self.matrix = matrix
        self.expected = expected


unittest_data = [
    UnitTestData(matrix=[[1, 2, 3], [4, 5, 6], [7, 8, 9]], expected=[[7, 4, 1], [8, 5, 2], [9, 6, 3]]),
    UnitTestData(
        matrix=[[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]],
        expected=[[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]],
    ),
]


class TestSolution(unittest.TestCase):
    def test_leetcode_48_rotate(self):
        s = problem.Solution()
        for item in unittest_data:
            s.rotate(item.matrix)
            self.assertEqual(item.matrix, item.expected)
