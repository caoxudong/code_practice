from typing import Optional
import leetcode.problem_19_remove_nth_node_from_nd_of_list as problem
import unittest


class UnitTestData:
    def __init__(
        self,
        head: problem.ListNode = None,
        n: int = 0,
        expected: Optional[problem.ListNode] = None,
    ):
        self.head = head
        self.n = n
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
        n=2,
        expected=create_ListNode([1, 2, 3, 5]),
    ),
    UnitTestData(head=create_ListNode([1]), n=1, expected=create_ListNode([])),
    UnitTestData(head=create_ListNode([1, 2]), n=1, expected=create_ListNode([1])),
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
    def test_removeNthFromEnd(self):
        s = problem.Solution()
        for item in unittest_data:
            result = s.removeNthFromEnd(item.head, item.n)
            assertListNodeEqual(result, item.expected)
