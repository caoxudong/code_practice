"""
https://leetcode.com/problems/validate-binary-search-tree/description/


Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:
* The left subtree of a node contains only nodes with keys strictly less than the node's key.
* The right subtree of a node contains only nodes with keys strictly greater than the node's key.
* Both the left and right subtrees must also be binary search trees.

Example 1:
            2
           / \
          1   3
* Input: root = [2,1,3]
* Output: true


Example 2:
            5
           / \
          1   4
             / \
            3   6
* Input: root = [5,1,4,null,null,3,6]
* Output: false
* Explanation: The root node's value is 5 but its right child's value is 4.


Constraints:
* The number of nodes in the tree is in the range [1, 104].
* -2^31 <= Node.val <= 2^31 - 1
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from common_data_structure.tree_node import TreeNode


class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        return False
