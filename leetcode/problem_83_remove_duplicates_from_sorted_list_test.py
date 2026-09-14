from typing import List, Optional
import unittest
from common_data_structure.list_node import ListNode
import leetcode.problem_83_remove_duplicates_from_sorted_list as problem


class UnitTestData:
    def __init__(self, head: Optional[ListNode], expected: List[int]):
        self.head = head
        self.expected = expected


unittest_data = [
    UnitTestData(head=ListNode.from_list([1, 1, 2]), expected=[1, 2]),
    UnitTestData(head=ListNode.from_list([1, 1, 2, 3, 3]), expected=[1, 2, 3]),
]


class TestSolution(unittest.TestCase):
    def test_leetcode_83_remove_duplicates_from_sorted_list(self):
        s = problem.Solution()
        for item in unittest_data:
            retval = s.deleteDuplicates(item.head)
            self.assertEqual(retval.to_list(), item.expected)
