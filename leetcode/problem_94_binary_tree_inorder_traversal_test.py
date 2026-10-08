import unittest
from common_data_structure.tree_node import TreeNode
import leetcode.problem_94_binary_tree_inorder_traversal as problem


class UnitTestData:
    def __init__(self, root: TreeNode | None, expected: list[int]):
        self.root = root
        self.expected = expected


unittest_data = [
    UnitTestData(root=TreeNode.from_list([1, None, 2, 3]), expected=[1, 3, 2]),
    UnitTestData(
        root=TreeNode.from_list([1, 2, 3, 4, 5, None, 8, None, None, 6, 7, 9]), expected=[4, 2, 6, 5, 7, 1, 3, 9, 8]
    ),
    UnitTestData(root=TreeNode.from_list([]), expected=[]),
    UnitTestData(root=TreeNode.from_list([1]), expected=[1]),
]


class TestSolution(unittest.TestCase):
    def test_leetcode_94_inorderTraversal(self):
        for item in unittest_data:
            self.assertEqual(problem.Solution().inorderTraversal(item.root), item.expected)
