from typing import List
import unittest
import leetcode.problem_74_search_a_2d_matrix as problem


class UnitTestData:
    def __init__(self, matrix: List[List[int]], target: int, expected: bool):
        self.matrix = matrix
        self.target = target
        self.expected = expected


unittest_data = [
    UnitTestData(matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target=3, expected=True),
    UnitTestData(matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target=13, expected=False),
]


class TestSolution(unittest.TestCase):
    def test_leetcode_74_searchMatrix(self):
        s = problem.Solution()
        for item in unittest_data:
            retval = s.searchMatrix(item.matrix, item.target)
            self.assertEqual(retval, item.expected)
