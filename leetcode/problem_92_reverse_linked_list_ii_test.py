import unittest
from common_data_structure.list_node import ListNode
import leetcode.problem_92_reverse_linked_list_ii as problem


class UnitTestData:
    def __init__(self, head: ListNode, left: int, right: int, expected: ListNode):
        self.head = head
        self.left = left
        self.right = right
        self.expected = expected


unittest_data = [
    UnitTestData(
        head=ListNode.from_list([1, 2, 3, 4, 5]), left=2, right=4, expected=ListNode.from_list([1, 4, 3, 2, 5])
    ),
    UnitTestData(head=ListNode.from_list([5]), left=1, right=1, expected=ListNode.from_list([5])),
]


class TestSolution(unittest.TestCase):
    def test_leetcode_92_reverseBetween(self):
        for item in unittest_data:
            solution = problem.Solution()
            retval = solution.reverseBetween(item.head, item.left, item.right)
            self.assertEqual(retval.to_list(), item.expected.to_list())
