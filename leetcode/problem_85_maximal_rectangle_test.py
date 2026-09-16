import unittest
import leetcode.problem_85_maximal_rectangle as problem


class UnitTestData:
    def __init__(self, matrix: list[list[str]], expected: int):
        self.matrix = matrix
        self.expected = expected


unittest_data = [
    UnitTestData(
        matrix=[
            ["1", "0", "1", "0", "0"],
            ["1", "0", "1", "1", "1"],
            ["1", "1", "1", "1", "1"],
            ["1", "0", "0", "1", "0"],
        ],
        expected=6,
    ),
    UnitTestData(matrix=[["0"]], expected=0),
    UnitTestData(matrix=[["1"]], expected=1),
]


class TestSolution(unittest.TestCase):
    def test_leetcode_85_maximal_rectangle(self):
        s = problem.Solution()
        for item in unittest_data:
            retval = s.maximalRectangle(item.matrix)
            self.assertEqual(retval, item.expected)
