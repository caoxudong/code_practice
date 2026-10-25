"""
https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/description/


Given the head of a singly linked list where elements are sorted in ascending order, convert it to a height-balanced binary search tree.

Example 1:
                0
               /  \
              -3   9
             /    /
            -10  5
* Input: head = [-10,-3,0,5,9]
* Output: [0,-3,9,-10,null,5]
* Explanation: [0,-10,5,null,-3,null,9] is also accepted:
                0
               / \
            -10   5
              \    \
               -3   9

Example 2:
* Input: nums = []
* Output: []

Constraints:
* The number of nodes in head is in the range [0, 2 * 10^4].
* -10^5 <= Node.val <= 10^5
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from common_data_structure.list_node import ListNode
from common_data_structure.tree_node import TreeNode


class Solution:
    def sortedListToBST(self, head: ListNode | None) -> TreeNode | None:
        return None
