from typing import Optional
import unittest
import leetcode.problem_25_reverse_nodes_in_k_group as problem
import test_utils
import test_utils.assert_utils


class UnitTestData:
    def __init__(
        self,
        head: problem.ListNode = None,
        k: int = 0,
        expected: problem.ListNode = None,
    ):
        self.head = head
        self.k = k
        self.expected = expected


def create_ListNode(nums: list[int] = []) -> problem.ListNode:
    last_listnode = None
    while len(nums) > 0:
        tmp_val = nums.pop()
        tmp_listnode = problem.ListNode(tmp_val, last_listnode)
        last_listnode = tmp_listnode
    return last_listnode


unittest_data = [
    UnitTestData(
        head=create_ListNode([1, 2, 3, 4, 5]),
        k=2,
        expected=create_ListNode([2, 1, 4, 3, 5]),
    ),
    UnitTestData(
        head=create_ListNode([1, 2, 3, 4, 5]),
        k=3,
        expected=create_ListNode([3, 2, 1, 4, 5]),
    ),
]


class TestSolution(unittest.TestCase):
    def test_reverseKGroup(self):
        s = problem.Solution()
        for item in unittest_data:
            result = s.reverseKGroup(item.head, item.k)
            test_utils.assert_utils.assertListNodeEqual(result, item.expected)
