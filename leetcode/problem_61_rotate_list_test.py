from typing import Optional
import unittest
from common_data_structure.list_node import ListNode
import common_data_structure.list_node as list_node
import leetcode.problem_61_rotate_list as problem


class UnitTestData:
    def __init__(self, head: Optional[ListNode], k: int, expected: str) -> None:
        self.head = head
        self.k = k
        self.expected = expected


unittest_data = [
    UnitTestData(
        head=list_node.create_ListNode([1, 2, 3, 4, 5]), k=2, expected=list_node.create_ListNode([4, 5, 1, 2, 3])
    ),
    UnitTestData(head=list_node.create_ListNode([0, 1, 2]), k=4, expected=list_node.create_ListNode([2, 0, 1])),
    UnitTestData(head=list_node.create_ListNode([]), k=0, expected=list_node.create_ListNode([])),
]


class TestSolution(unittest.TestCase):
    def test_leetcode_61_rotateRight(self):
        s = problem.Solution()
        for item in unittest_data:
            retval = s.rotateRight(item.head, item.k)
            list_node.assertListNodeEqual(item.expected, retval)
