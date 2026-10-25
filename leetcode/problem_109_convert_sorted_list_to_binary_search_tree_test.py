import unittest
from common_data_structure.list_node import ListNode
from common_data_structure.tree_node import TreeNode
import leetcode.problem_109_convert_sorted_list_to_binary_search_tree as problem


class UnitTestData:
    def __init__(self, head: ListNode | None, expected: TreeNode):
        self.head = head
        self.expected = expected


unittest_data = [
    UnitTestData(head=ListNode.from_list([-10, -3, 0, 5, 9]), expected=TreeNode.from_list([0, -3, 9, -10, None, 5])),
    UnitTestData(head=ListNode.from_list([]), expected=TreeNode.from_list([])),
]


class TestSolution(unittest.TestCase):
    def test_leetcode_109_sortedListToBST(self):
        for item in unittest_data:
            solution = problem.Solution()
            retval = solution.sortedListToBST(item.head)
            self.assertListEqual(retval.to_list(), item.expected.to_list())
