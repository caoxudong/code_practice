import unittest
import leetcode.problem_684_redundant_connection as problem


class UnitTestData:
    def __init__(
        self,
        edges: list[list[int]] = [],
        expected: list[int] = [],
    ):
        self.edges = edges
        self.expected = expected


unittest_data = [
    # UnitTestData(edges=[[1, 2], [1, 3], [2, 3]], expected=[2, 3]),
    # UnitTestData(edges=[[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]], expected=[1, 4]),
    # UnitTestData(edges=[[1, 3], [3, 4], [1, 5], [3, 5], [2, 3]], expected=[3, 5]),
    # UnitTestData(edges=[[1, 4], [3, 4], [1, 3], [1, 2], [4, 5]], expected=[1, 3]),
    UnitTestData(edges=[[3, 4], [1, 2], [2, 4], [3, 5], [2, 5]], expected=[2, 5]),
]


class TestSolution(unittest.TestCase):
    def test_findRedundantConnection(self):
        s = problem.Solution()
        for item in unittest_data:
            result = s.findRedundantConnection(item.edges)
            self.assertListEqual(result, item.expected)
