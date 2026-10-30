import unittest
from common_data_structure.binary_tree_node import TreeNode
import leetcode.problem_98_validate_binary_search_tree as problem


class UnitTestData:
    def __init__(self, root: TreeNode | None, expected: bool):
        self.root = root
        self.expected = expected


unittest_data = [
    # UnitTestData(root=TreeNode.from_list([2, 1, 3]), expected=True),
    # UnitTestData(root=TreeNode.from_list([5, 1, 4, None, None, 3, 6]), expected=False),
    # UnitTestData(root=TreeNode.from_list([5, 4, 6, None, None, 3, 7]), expected=False),
    # UnitTestData(root=TreeNode.from_list([32, 26, 47, 19, None, None, 56, None, 27]), expected=False),
    UnitTestData(root=TreeNode.from_list([45, 42, None, None, 44, 43, None, 41]), expected=False),
]


class TestSolution(unittest.TestCase):
    def test_leetcode98_isValidBST(self):
        for item in unittest_data:
            solution = problem.Solution()
            result = solution.isValidBST(item.root)
            self.assertEqual(result, item.expected)
