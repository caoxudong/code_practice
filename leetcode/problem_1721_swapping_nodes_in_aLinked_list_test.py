from typing import Optional
from venv import create
import leetcode.problem_1721_swapping_nodes_in_aLinked_list as problem
import unittest


class UnitTestData:
    def __init__(
        self,
        head: problem.ListNode = None,
        k: int = 0,
        expected: Optional[problem.ListNode] = None,
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
        expected=create_ListNode([1, 4, 3, 2, 5]),
    ),
    UnitTestData(
        head=create_ListNode([7, 9, 6, 6, 7, 8, 3, 0, 9, 5]),
        k=5,
        expected=create_ListNode([7, 9, 6, 6, 8, 7, 3, 0, 9, 5]),
    ),
    UnitTestData(head=create_ListNode([1, 2]), k=1, expected=create_ListNode([2, 1])),
]


def assertListNodeEqual(
    result: Optional[problem.ListNode] = None,
    expected: Optional[problem.ListNode] = None,
):
    if result == None and expected == None:
        return
    if result == None and expected != None:
        raise AssertionError(
            "AssertionError, result is None, expected is {}".format(
                expected.to_string()
            )
        )
    if result != None and expected == None:
        raise AssertionError(
            "AssertionError, result is {}, expected is None".format(result.to_string())
        )

    result_tmp_node = result
    expected_tmp_node = expected
    while True:
        if result_tmp_node.val != expected_tmp_node.val:
            raise AssertionError(
                "AssertionError, result is {}, expected is {}".format(
                    result.to_string(), expected.to_string()
                )
            )

        result_tmp_node = result_tmp_node.next
        expected_tmp_node = expected_tmp_node.next
        if result_tmp_node == None and expected_tmp_node == None:
            return
        elif result_tmp_node != None and expected_tmp_node != None:
            continue
        else:
            raise AssertionError(
                "AssertionError, result is {}, expected is {}".format(
                    result.to_string(), expected.to_string()
                )
            )


class TestSolution(unittest.TestCase):
    def test_swapNodes(self):
        s = problem.Solution()
        for item in unittest_data:
            result = s.swapNodes(item.head, item.k)
            assertListNodeEqual(result, item.expected)
