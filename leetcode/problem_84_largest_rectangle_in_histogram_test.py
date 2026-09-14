import unittest
import leetcode.problem_84_largest_rectangle_in_histogram as problem


class UnitTestData:
    def __init__(self, heights: list[int], expected: int):
        self.heights = heights
        self.expected = expected


unittest_data = [
    UnitTestData(heights=[2, 1, 5, 6, 2, 3], expected=10),
    UnitTestData(heights=[2, 4], expected=4),
]


class TestSolution(unittest.TestCase):
    def test_leetcode_84_largest_rectangle_in_histogram(self):
        s = problem.Solution()
        for item in unittest_data:
            retval = s.largestRectangleArea(item.heights)
            self.assertEqual(retval, item.expected)
