import unittest
from common_data_structure.binary_tree_node import TreeNode
import leetcode.problem_104_maximum_depth_of_binary_tree as problem


class UnitTestData:
    def __init__(self, root: TreeNode | None, expected: int):
        self.root = root
        self.expected = expected


unittest_data = [
    UnitTestData(root=TreeNode.from_list([3, 9, 20, None, None, 15, 7]), expected=3),
    UnitTestData(root=TreeNode.from_list([1, None, 2]), expected=2),
]


class TestSolution(unittest.TestCase):
    def test_leetcode_104_maxDepth(self):
        for item in unittest_data:
            solution = problem.Solution()
            retval = solution.maxDepth(item.root)
            self.assertEqual(retval, item.expected)
