"""
https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/

Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.


Example 1:
* Input: head = [1,1,2]
* Output: [1,2]

Example 2:
* Input: head = [1,1,2,3,3]
* Output: [1,2,3]

Constraints:
* The number of nodes in the list is in the range [0, 300].
* -100 <= Node.val <= 100
* The list is guaranteed to be sorted in ascending order.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional

from common_data_structure.list_node import ListNode


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(0)
        dummy_head.next = head
        prev_cursor = dummy_head
        curr_cursor = head
        values_set = set()

        while curr_cursor != None:
            if curr_cursor.val in values_set:
                prev_cursor.next = curr_cursor.next
            else:
                values_set.add(curr_cursor.val)
                prev_cursor = curr_cursor
            curr_cursor = curr_cursor.next

        return dummy_head.next
