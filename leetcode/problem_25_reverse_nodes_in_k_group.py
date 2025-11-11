"""
https://leetcode.com/problems/reverse-nodes-in-k-group/description/


Given the `head` of a linked list, reverse the nodes of the list `k` at a time, and return the modified list.

`k` is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of `k` then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.


Example 1:
* Input: head = [1,2,3,4,5], k = 2
* Output: [2,1,4,3,5]

Example 2:
* Input: head = [1,2,3,4,5], k = 3
* Output: [3,2,1,4,5]

Constraints:
* The number of nodes in the list is n.
* 1 <= k <= n <= 5000
* 0 <= Node.val <= 1000
"""

from typing import Optional
from common_data_structure.list_node import ListNode


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None:
            return None

        values = []
        p_cur = head
        while p_cur != None:
            values.append(p_cur.val)
            p_cur = p_cur.next

        i = 0
        values_count = len(values)
        while True:
            if i + k > values_count:
                break

            for j in range(int(k / 2)):
                values[i + j], values[i + k - 1 - j] = (
                    values[i + k - 1 - j],
                    values[i + j],
                )

            i += k

        def create_ListNode(nums: list[int] = []) -> ListNode:
            last_listnode = None
            while len(nums) > 0:
                tmp_val = nums.pop()
                tmp_listnode = ListNode(tmp_val, last_listnode)
                last_listnode = tmp_listnode
            return last_listnode

        retval = create_ListNode(values)
        return retval
