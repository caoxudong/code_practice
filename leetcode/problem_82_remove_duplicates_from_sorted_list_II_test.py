from typing import List, Optional
import unittest
from common_data_structure.list_node import ListNode
import leetcode.problem_82_remove_duplicates_from_sorted_list_II as problem


class UnitTestData:
    def __init__(self, head: Optional[ListNode], expected: List[int]):
        self.head = head
        self.expected = expected


unittest_data = [
    UnitTestData(head=ListNode.from_list([1, 2, 3, 3, 4, 4, 5]), expected=[1, 2, 5]),
    UnitTestData(head=ListNode.from_list([1, 1, 1, 2, 3]), expected=[2, 3]),
]


class TestSolution(unittest.TestCase):
    def test_leetcode_82_remove_duplicates_from_sorted_list_II(self):
        s = problem.Solution()
        for item in unittest_data:
            head = problem.ListNode.from_list(item.head)
            retval = s.deleteDuplicates(head)
            self.assertEqual(retval.to_list(), item.expected)
