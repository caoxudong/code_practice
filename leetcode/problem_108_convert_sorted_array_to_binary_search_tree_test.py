import unittest
from common_data_structure.binary_tree_node import TreeNode
import leetcode.problem_108_convert_sorted_array_to_binary_search_tree as problem


class UnitTestData:
    def __init__(self, nums: list[int], expected: TreeNode):
        self.nums = nums
        self.expected = expected


unittest_data = [
    UnitTestData(nums=[-10, -3, 0, 5, 9], expected=TreeNode.from_list([0, -3, 9, -10, None, 5])),
    UnitTestData(nums=[1, 3], expected=TreeNode.from_list([3, 1])),
]


class TestSolution(unittest.TestCase):
    def test_leetcode_108_sortedArrayToBST(self):
        for item in unittest_data:
            solution = problem.Solution()
            retval = solution.sortedArrayToBST(item.nums)
            self.assertListEqual(retval.to_list(), item.expected.to_list())
