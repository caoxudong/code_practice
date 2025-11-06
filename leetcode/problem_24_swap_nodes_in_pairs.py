"""
https://leetcode.com/problems/swap-nodes-in-pairs/description/

Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

Example 1:
* Input: head = [1,2,3,4]
* Output: [2,1,4,3]

Example 2:
* Input: head = []
* Output: []

Example 3:
* Input: head = [1]
* Output: [1]

Example 4:
* Input: head = [1,2,3]
* Output: [2,1,3]

Constraints:
* The number of nodes in the list is in the range [0, 100].
* 0 <= Node.val <= 100
"""

# Definition for singly-linked list.
from multiprocessing import dummy
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None

        if head.next == None:
            return head

        dummy_node = ListNode(next=head)
        retval = head.next

        cur_p: ListNode = dummy_node.next
        pre_p: ListNode = dummy_node
        while cur_p != None and cur_p.next != None:
            pre_p.next = cur_p.next
            cur_p_next_next = cur_p.next.next
            cur_p.next = cur_p_next_next
            pre_p.next.next = cur_p
            cur_p = cur_p.next
            pre_p = pre_p.next.next

        return retval
