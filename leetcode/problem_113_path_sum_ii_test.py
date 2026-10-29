import unittest
from common_data_structure.tree_node import TreeNode
import leetcode.problem_113_path_sum_ii as problem


class UnitTestData:
    def __init__(self, root: TreeNode | None, targetSum: int, expected: list[list[int]]):
        self.root = root
        self.targetSum = targetSum
        self.expected = expected


unittest_data: list[UnitTestData] = []


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
