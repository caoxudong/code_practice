"""
https://leetcode.com/problems/rotate-list/description/


Given the head of a linked list, rotate the list to the right by k places.

Example 1:
* Input: head = [1,2,3,4,5], k = 2
* Output: [4,5,1,2,3]
* Explanation:
    * rotate 1: [1,2,3,4,5] -> [5,1,2,3,4]
    * rotate 2: [5,1,2,3,4] -> [4,5,1,2,3]


Example 2:
* Input: head = [0,1,2], k = 4
* Output: [2,0,1]
* Explanation:
    * rotate 1: [0,1,2] -> [2,0,1]
    * rotate 2: [2,0,1] -> [1,2,0]
    * rotate 3: [1,2,0] -> [0,1,2]
    * rotate 4: [0,1,2] -> [2,0,1]


Constraints:

* The number of nodes in the list is in the range [0, 500].
* -100 <= Node.val <= 100
* 0 <= k <= 2 * 10^9
"""

from typing import Optional

from common_data_structure.list_node import ListNode


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None:
            return None
        list_len = 0
        list_elements = {}
        cursor = head
        while cursor is not None:
            list_elements[list_len] = cursor
            cursor = cursor.next
            list_elements[list_len].next = None
            list_len += 1

        real_k = k % list_len
        cursor = ListNode()
        retval = cursor
        for i in range(list_len - real_k, list_len):
            cursor.next = list_elements[i]
            cursor = cursor.next
        for i in range(0, list_len - real_k):
            cursor.next = list_elements[i]
            cursor = cursor.next
        return retval.next
