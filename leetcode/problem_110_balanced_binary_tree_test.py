import unittest
from common_data_structure.tree_node import TreeNode
import leetcode.problem_110_balanced_binary_tree as problem


class UnitTestData:
    def __init__(self, root: TreeNode | None, expected: bool):
        self.root = root
        self.expected = expected


unittest_data: list[UnitTestData] = [
    UnitTestData(root=TreeNode.from_list([3, 9, 20, None, None, 15, 7]), expected=True),
    UnitTestData(root=TreeNode.from_list([1, 2, 2, 3, 3, None, None, 4, 4]), expected=False),
    UnitTestData(root=TreeNode.from_list([]), expected=True),
]


class TestSolution(unittest.TestCase):
    def test_leetcode_110_isBalanced(self):
        for item in unittest_data:
            solution = problem.Solution()
            retval = solution.isBalanced(item.root)
            self.assertEqual(retval, item.expected)
