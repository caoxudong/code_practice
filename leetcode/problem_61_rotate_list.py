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
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        return None
