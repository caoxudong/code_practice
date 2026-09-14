"""
https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/description/


You are given the head of a sorted linked list.

Delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

Return the linked list sorted as well.

Example 1:
* Input: head = [1,2,3,3,4,4,5]
* Output: [1,2,5]

Example 2:
* Input: head = [1,1,1,2,3]
* Output: [2,3]

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
        tmp_cursor = head
        values_count = {}

        while tmp_cursor != None:
            values_count[tmp_cursor.val] = values_count.get(tmp_cursor.val, 0) + 1
            tmp_cursor = tmp_cursor.next

        dummy_node = ListNode(val=0, next=head)
        new_cursor = dummy_node
        while new_cursor.next != None:
            if values_count[new_cursor.next.val] > 1:
                new_cursor.next = new_cursor.next.next
            else:
                new_cursor = new_cursor.next
                
        return dummy_node.next
