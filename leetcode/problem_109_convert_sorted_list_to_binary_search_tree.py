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
        if head is None:
            return None
        values = []
        cursor = head
        while cursor is not None:
            val = cursor.val
            values.append(val)
            cursor = cursor.next

        def build_bst(nums: list[int]) -> TreeNode | None:
            if len(nums) == 0:
                return None

            len_nums = len(nums)
            mid_index = len_nums >> 1
            left_child_values = nums[0:mid_index]
            right_child_values = nums[mid_index + 1 : len_nums]

            root = TreeNode(val=nums[mid_index], left=build_bst(left_child_values), right=build_bst(right_child_values))
            return root

        return build_bst(values)
