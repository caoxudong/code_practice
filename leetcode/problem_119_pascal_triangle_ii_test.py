import unittest
import leetcode.problem_119_pascal_triangle_ii as problem


class UnitTestData:
    def __init__(self, rowIndex: int, expected: list[int]):
        self.rowIndex = rowIndex
        self.expected = expected


unittest_data: list[UnitTestData] = [
    UnitTestData(rowIndex=3, expected=[1, 3, 3, 1]),
    UnitTestData(rowIndex=0, expected=[1]),
    UnitTestData(rowIndex=1, expected=[1, 1]),
]


class TestSolution(unittest.TestCase):
    def test_leetcode_118_getRow(self):
        for data in unittest_data:
            with self.subTest(rowIndex=data.rowIndex):
                solution = problem.Solution()
                result = solution.getRow(data.rowIndex)
                self.assertEqual(result, data.expected)
