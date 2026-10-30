import unittest
from common_data_structure.binary_tree_node import TreeNode
import leetcode.problem_106_construct_binary_tree_from_inorder_and_postorder_traversal as problem


class UnitTestData:
    def __init__(self, inorder: list[int], postorder: list[int], expected=TreeNode):
        self.inorder = inorder
        self.postorder = postorder
        self.expected = expected


unittest_data = [
    UnitTestData(
        inorder=[9, 3, 15, 20, 7],
        postorder=[9, 15, 7, 20, 3],
        expected=TreeNode.from_list([3, 9, 20, None, None, 15, 7]),
    ),
    UnitTestData(inorder=[-1], postorder=[-1], expected=TreeNode.from_list([-1])),
]


class TestSolution(unittest.TestCase):
    def test_leetcode_106_buildTree(self):
        for item in unittest_data:
            solution = problem.Solution()
            retval = solution.buildTree(item.inorder, item.postorder)
            self.assertListEqual(retval.to_list(), item.expected.to_list())
