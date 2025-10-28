"""
https://leetcode.com/problems/swapping-nodes-in-a-linked-list/description/


You are given the head of a linked list, and an integer `k`.

Return the head of the linked list after swapping the values of the `kth` node from the beginning and the `kth` node from the end (the list is 1-indexed).

Example 1:
* Input: head = [1,2,3,4,5], k = 2
* Output: [1,4,3,2,5]

Example 2:
* Input: head = [7,9,6,6,7,8,3,0,9,5], k = 5
* Output: [7,9,6,6,8,7,3,0,9,5]

Constraints:
* The number of nodes in the list is n.
* 1 <= k <= n <= 105
* 0 <= Node.val <= 100
"""

from typing import Optional


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
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        fake_head = ListNode(next=head)

        jth_node: ListNode = fake_head
        kth_node: ListNode = jth_node.next
        for _ in range(k - 1):
            jth_node = jth_node.next
            kth_node = kth_node.next

        lth_r_node: ListNode = fake_head
        tmp_node: ListNode = kth_node
        while tmp_node.next != None:
            tmp_node = tmp_node.next
            lth_r_node = lth_r_node.next
        kth_r_node = lth_r_node.next

        jth_node.next, lth_r_node.next = kth_r_node, kth_node
        kth_node.next, kth_r_node.next = kth_r_node.next, kth_node.next

        return fake_head.next
