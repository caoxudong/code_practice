from math import exp
import unittest
from common_data_structure.tree_node import TreeNode
import leetcode.problem_105_construct_binary_tree_from_preorder_and_inorder_traversal as problem


class UnitTestData:
    def __init__(self, preorder: list[int], inorder: list[int], expected=TreeNode):
        self.preorder = preorder
        self.inorder = inorder
        self.expected = expected


unittest_data = [
    UnitTestData(
        preorder=[3, 9, 20, 15, 7],
        inorder=[9, 3, 15, 20, 7],
        expected=TreeNode.from_list([3, 9, 20, None, None, 15, 7]),
    ),
    UnitTestData(preorder=[-1], inorder=[-1], expected=TreeNode.from_list([-1])),
]


class TestSolution(unittest.TestCase):
    def test_leetcode_105_buildTree(self):
        for item in unittest_data:
            solution = problem.Solution()
            retval = solution.buildTree(item.preorder, item.inorder)
            self.assertListEqual(retval.to_list(), item.expected.to_list())
