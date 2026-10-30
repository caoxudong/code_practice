import unittest
from common_data_structure.binary_tree_node import TreeNode
import leetcode.problem_112_path_sum as problem


class UnitTestData:
    def __init__(self, root: TreeNode | None, targetSum: int, expected: bool):
        self.root = root
        self.targetSum = targetSum
        self.expected = expected


unittest_data: list[UnitTestData] = [
    UnitTestData(
        root=TreeNode.from_list([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1]), targetSum=22, expected=True
    ),
    UnitTestData(root=TreeNode.from_list([1, 2, 3]), targetSum=5, expected=False),
    UnitTestData(root=TreeNode.from_list([]), targetSum=0, expected=False),
]


class TestSolution(unittest.TestCase):
    def test_leetcode_112_hasPathSum(self):
        for item in unittest_data:
            solution = problem.Solution()
            retval = solution.hasPathSum(item.root, item.targetSum)
            self.assertEqual(retval, item.expected)
