"""
https://leetcode.com/problems/merge-two-sorted-lists/description/


You are given the heads of two sorted linked lists `list1` and `list2`.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Example:
* Input: list1 = [1,2,4], list2 = [1,3,4]
* Output: [1,1,2,3,4,4]

Example 2:
* Input: list1 = [], list2 = []
* Output: []

Example 3:
* Input: list1 = [], list2 = [0]
* Output: [0]

Constraints:
* The number of nodes in both lists is in the range [0, 50].
* -100 <= Node.val <= 100
* Both list1 and list2 are sorted in non-decreasing order.
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def to_string(self) -> str:
        list_values: list[int] = []

        node = self
        while True:
            list_values.append(node.val)
            node = node.next
            if node == None:
                break

        return "[{}]".format(",".join(map(str, list_values)))


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1

        p_list1: ListNode = list1
        p_list2: ListNode = list2

        result_nums = []
        while p_list1 != None and p_list2 != None:
            n_list1 = p_list1.val
            n_list2 = p_list2.val

            if n_list1 > n_list2:
                result_nums.append(n_list2)
                p_list2 = p_list2.next
            else:
                result_nums.append(n_list1)
                p_list1 = p_list1.next

        if p_list1 == None:
            while p_list2 != None:
                result_nums.append(p_list2.val)
                p_list2 = p_list2.next
        if p_list2 == None:
            while p_list1 != None:
                result_nums.append(p_list1.val)
                p_list1 = p_list1.next

        def create_ListNode(nums: list[int] = []) -> ListNode:
            last_listnode = None
            while len(nums) > 0:
                tmp_val = nums.pop()
                tmp_listnode = ListNode(tmp_val, last_listnode)
                last_listnode = tmp_listnode
            return last_listnode

        result = create_ListNode(result_nums)
        return result
