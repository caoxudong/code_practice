import unittest
from common_data_structure.list_node import ListNode, assertListNodeEqual
import leetcode.problem_86_partition_list as problem


class UnitTestData:
    def __init__(self, head: ListNode | None, x: int, expected: ListNode | None):
        self.head = head
        self.x = x
        self.expected = expected


unittest_data = [
    UnitTestData(head=ListNode.from_list([1, 4, 3, 2, 5, 2]), x=3, expected=ListNode.from_list([1, 2, 2, 4, 3, 5])),
    UnitTestData(head=ListNode.from_list([2, 1]), x=2, expected=ListNode.from_list([1, 2])),
]


class TestSolution(unittest.TestCase):
    def test_leetcode_86_partition(self):
        for item in unittest_data:
            solution = problem.Solution()
            retval = solution.partition(item.head, item.x)
            assertListNodeEqual(retval, item.expected)
