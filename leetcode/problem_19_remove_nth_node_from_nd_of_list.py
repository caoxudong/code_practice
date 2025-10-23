"""
https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/

Given the head of a linked list, remove the nth node from the end of the list and return its head.


Example 1:
* Input: head = [1,2,3,4,5], n = 2
* Output: [1,2,3,5]

Example 2:
* Input: head = [1], n = 1
* Output: []

Example 3:
* Input: head = [1,2], n = 1
* Output: [1]

Constraints:
* The number of nodes in the list is sz.
* 1 <= sz <= 30
* 0 <= Node.val <= 100
* 1 <= n <= sz
"""

from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next=None):
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
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def create_ListNode(nums: list[int] = []) -> ListNode:
            if nums is None:
                return None
            last_listnode = None
            while len(nums) > 0:
                tmp_val = nums.pop()
                tmp_listnode = ListNode(tmp_val, last_listnode)
                last_listnode = tmp_listnode
            return last_listnode

        list_values: list[int] = []
        node = head
        while True:
            list_values.append(node.val)
            node = node.next
            if node == None:
                break

        result_values = list_values[0 : -1 * n]
        if n != 1:
            result_values.extend(list_values[-1 * n + 1 :])

        return create_ListNode(result_values)
