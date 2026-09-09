from typing import List
import unittest
import leetcode.problem_73_set_matrix_zeroes as problem


class UnitTestData:
    def __init__(self, matrix: List[List[int]], expected: List[List[int]]):
        self.matrix = matrix
        self.expected = expected
        self.expected = expected


unittest_data = [
    UnitTestData(matrix=[[1, 1, 1], [1, 0, 1], [1, 1, 1]], expected=[[1, 0, 1], [0, 0, 0], [1, 0, 1]]),
    UnitTestData(
        matrix=[[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]], expected=[[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]
    ),
]


class TestSolution(unittest.TestCase):
    def test_leetcode_73_setMatrixZeroes(self):
        s = problem.Solution()
        for item in unittest_data:
            # Create a copy of the matrix to avoid modifying the original
            matrix_copy = [row[:] for row in item.matrix]
            s.setZeroes(matrix_copy)
            self.assertEqual(matrix_copy, item.expected)
