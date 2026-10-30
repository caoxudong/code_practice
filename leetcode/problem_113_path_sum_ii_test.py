import unittest
from common_data_structure.tree_node import TreeNode
import leetcode.problem_113_path_sum_ii as problem


class UnitTestData:
    def __init__(self, root: TreeNode | None, targetSum: int, expected: list[list[int]]):
        self.root = root
        self.targetSum = targetSum
        self.expected = expected


unittest_data: list[UnitTestData] = [
    UnitTestData(
        root=TreeNode.from_list([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1]),
        targetSum=22,
        expected=[[5, 4, 11, 2], [5, 8, 4, 5]],
    ),
    UnitTestData(root=TreeNode.from_list([1, 2, 3]), targetSum=5, expected=[]),
    UnitTestData(root=TreeNode.from_list([1, 2]), targetSum=0, expected=[]),
]


class TestSolution(unittest.TestCase):
    def test_leetcode_113_pathSum(self):
        for item in unittest_data:
            solution = problem.Solution()
            retval: list[list[int]] = solution.pathSum(item.root, item.targetSum)
            self.assertEqual(len(retval), len(item.expected), msg="list len not equal")
            len_list = len(retval)
            retval.sort()
            item.expected.sort()
            for i in range(len_list):
                retval_i = retval[i]
                expected_i = item.expected[i]
                self.assertEqual(retval_i, expected_i)
