import unittest
import leetcode.problem_117_pascal_triangle as problem


class UnitTestData:
    def __init__(self, numRows: int, expected: list[list[int]]):
        self.numRows = numRows
        self.expected = expected


unittest_data: list[UnitTestData] = [
    UnitTestData(numRows=5, expected=[[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]),
    UnitTestData(numRows=1, expected=[[1]]),
]


class TestSolution(unittest.TestCase):
    def test_leetcode_117_generate(self):
        for data in unittest_data:
            with self.subTest(numRows=data.numRows):
                solution = problem.Solution()
                result = solution.generate(data.numRows)
                self.assertEqual(result, data.expected)
