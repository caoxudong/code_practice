from typing import Optional
import unittest
import leetcode.problem_21_merge_two_sorted_lists as problem


class UnitTestData:
    def __init__(
        self,
        list1: Optional[problem.ListNode] = [],
        list2: Optional[problem.ListNode] = [],
        expected: Optional[problem.ListNode] = [],
    ):
        self.list1 = list1
        self.list2 = list2
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
        list1=create_ListNode([1, 2, 4]),
        list2=create_ListNode([1, 3, 4]),
        expected=create_ListNode([1, 1, 2, 3, 4, 4]),
    ),
    UnitTestData(
        list1=create_ListNode([]),
        list2=create_ListNode([]),
        expected=create_ListNode([]),
    ),
    UnitTestData(
        list1=create_ListNode([]),
        list2=create_ListNode([0]),
        expected=create_ListNode([0]),
    ),
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
    def test_mergeTwoLists(self):
        s = problem.Solution()
        for item in unittest_data:
            result = s.mergeTwoLists(item.list1, item.list2)
            assertListNodeEqual(result, item.expected)
