import unittest
from common_data_structure.binary_tree_node import TreeNode
import leetcode.problem_111_minimum_depth_of_binary_tree as problem


class UnitTestData:
    def __init__(self, root: TreeNode | None, expected: int):
        self.root = root
        self.expected = expected


unittest_data: list[UnitTestData] = [
    UnitTestData(root=TreeNode.from_list([3, 9, 20, None, None, 15, 7]), expected=2),
    UnitTestData(root=TreeNode.from_list([2, None, 3, None, 4, None, 5, None, 6]), expected=5),
]


class TestSolution(unittest.TestCase):
    def test_leetcode_111_minDepth(self):
        for item in unittest_data:
            solution = problem.Solution()
            retval = solution.minDepth(item.root)
            self.assertEqual(retval, item.expected)
