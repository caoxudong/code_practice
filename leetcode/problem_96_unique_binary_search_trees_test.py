import unittest
import leetcode.problem_96_unique_binary_search_trees as problem


class UnitTestData:
    def __init__(self, n: int, expected: int):
        self.n = n
        self.expected = expected


unittest_data = [
    UnitTestData(n=3, expected=5),
    UnitTestData(n=1, expected=1),
]


class TestSolution(unittest.TestCase):
    def test_leetcode_96_numTrees(self):
        for item in unittest_data:
            retval = problem.Solution().numTrees(item.n)
            self.assertEqual(retval, item.expected)
