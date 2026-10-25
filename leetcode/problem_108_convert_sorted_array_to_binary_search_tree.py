"""
https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/


Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.

Example 1:
                0
               /  \
              -3   9
             /    /
            -10  5
* Input: nums = [-10,-3,0,5,9]
* Output: [0,-3,9,-10,null,5]
* Explanation: [0,-10,5,null,-3,null,9] is also accepted:
                0
               / \
            -10   5
              \    \
               -3   9

Example 2:
            3       1 
           /         \   
          1           3
* Input: nums = [1,3]
* Output: [3,1]
* Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.

Constraints:
* 1 <= nums.length <= 10^4
* -10^4 <= nums[i] <= 10^4
* nums is sorted in a strictly increasing order.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from common_data_structure.tree_node import TreeNode


class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> TreeNode | None:
        def build_bst(nums: list[int]) -> TreeNode | None:
            if len(nums) == 0:
                return None

            len_nums = len(nums)
            mid_index = len_nums >> 1
            left_child_values = nums[0:mid_index]
            right_child_values = nums[mid_index + 1 : len_nums]

            root = TreeNode(val=nums[mid_index], left=build_bst(left_child_values), right=build_bst(right_child_values))
            return root

        return build_bst(nums)
