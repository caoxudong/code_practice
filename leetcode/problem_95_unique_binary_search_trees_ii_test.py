import unittest
import leetcode.problem_95_unique_binary_search_trees_ii as problem


class UnitTestData:
    def __init__(self, n: int, expected: list[list[int | None]]):
        self.n = n
        self.expected = expected


unittest_data = [
    UnitTestData(
        n=3, expected=[[1, None, 2, None, 3], [1, None, 3, 2], [2, 1, 3], [3, 1, None, None, 2], [3, 2, None, 1]]
    ),
    UnitTestData(n=1, expected=[[1]]),
]


class TestSolution(unittest.TestCase):
    def test_leetcode_95_generateTrees(self):
        for item in unittest_data:
            retval = problem.Solution().generateTrees(item.n)
            tree_list = []
            for tree in retval:
                tree_list.append(tree.to_list())
            self.assertEqual(sorted(tree_list), sorted(item.expected))
