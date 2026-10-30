import unittest
from common_data_structure.binary_tree_node import TreeNode, assertTreeNodeEqual
import leetcode.problem_114_flatten_binary_tree_to_linked_list as problem


class UnitTestData:
    def __init__(self, root: TreeNode | None, expected: TreeNode | None):
        self.root = root
        self.expected = expected


unittest_data: list[UnitTestData] = [
    UnitTestData(
        root=TreeNode.from_list([1, 2, 5, 3, 4, None, 6]),
        expected=TreeNode.from_list([1, None, 2, None, 3, None, 4, None, 5, None, 6]),
    ),
    UnitTestData(root=TreeNode.from_list([]), expected=TreeNode.from_list([])),
    UnitTestData(root=TreeNode.from_list([0]), expected=TreeNode.from_list([0])),
]


class TestSolution(unittest.TestCase):
    def test_leetcode_114_flatten(self):
        for item in unittest_data:
            solution = problem.Solution()
            solution.flatten(item.root)
            assertTreeNodeEqual(item.root, item.expected)
