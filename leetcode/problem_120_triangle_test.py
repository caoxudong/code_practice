import unittest
import leetcode.problem_120_triangle as problem


class UnitTestData:
    def __init__(self, triangle: list[list[int]], expected: int):
        self.triangle = triangle
        self.expected = expected


unittest_data: list[UnitTestData] = [
    UnitTestData(triangle=[[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]], expected=11),
    UnitTestData(triangle=[[-10]], expected=-10),
]


class TestSolution(unittest.TestCase):
    def test_leetcode_120_minimumTotal(self):
        for data in unittest_data:
            with self.subTest(triangle=data.triangle):
                solution = problem.Solution()
                result = solution.minimumTotal(data.triangle)
                self.assertEqual(result, data.expected)
