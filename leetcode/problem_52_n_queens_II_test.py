from typing import List
import unittest
import leetcode.problem_51_n_queens as problem


class UnitTestData:
    def __init__(self, n: int, expected: List[List[str]]) -> None:
        self.n = n
        self.expected = expected


unittest_data = [
    UnitTestData(n=4, expected=[[".Q..", "...Q", "Q...", "..Q."], ["..Q.", "Q...", "...Q", ".Q.."]]),
    UnitTestData(n=1, expected=[["Q"]]),
]


class TestSolution(unittest.TestCase):
    def test_leetcode_51_solveNQueens(self):
        s = problem.Solution()
        for item in unittest_data:
            retval = s.solveNQueens(item.n)
            self.assertAlmostEqual(item.expected, retval)
