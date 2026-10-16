import unittest
import leetcode.problem_99_recover_binary_search_tree as problem


class UnitTestData:
    def __init__(self, root: problem.TreeNode | None, expected: problem.TreeNode | None):
        self.root = root
        self.expected = expected


unittest_data = [
    UnitTestData(
        root=problem.TreeNode.from_list([1, 3, None, None, 2]),
        expected=problem.TreeNode.from_list([3, 1, None, None, 2]),
    ),
    UnitTestData(
        root=problem.TreeNode.from_list([3, 1, 4, None, None, 2]),
        expected=problem.TreeNode.from_list([2, 1, 4, None, None, 3]),
    ),
]


class TestSolution(unittest.TestCase):
    def test_leetcode_99_recoverTree(self):
        for item in unittest_data:
            solution = problem.Solution()
            result = solution.recoverTree(item.root)
            self.assertEqual(item.root.to_list(), item.expected.to_list())
