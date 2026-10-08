"""
https://leetcode.com/problems/binary-tree-inorder-traversal/description/

Given the root of a binary tree, return the inorder traversal of its nodes' values.

Example 1:
* Input: root = [1,null,2,3]
* Output: [1,3,2]
* Explanation:
    1
     \
      2
     /
    3


Example 2:
* Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]
* Output: [4,2,6,5,7,1,3,9,8]
* Explanation:
            1
           /  \
          2    3
         / \    \
        4   5    8
           / \   /
          6   7 9


Example 3:
* Input: root = []
* Output: []

Example 4:
* Input: root = [1]
* Output: [1]

Constraints:
* The number of nodes in the tree is in the range [0, 100].
* -100 <= Node.val <= 100

Follow up: Recursive solution is trivial, could you do it iteratively?
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from common_data_structure.tree_node import TreeNode


class Solution:
    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
        result = []
        self._inorder_helper(root, result)
        return result

    def _inorder_helper(self, node: TreeNode | None, result: list[int]) -> None:
        if not node:
            return
        self._inorder_helper(node.left, result)
        result.append(node.val)
        self._inorder_helper(node.right, result)
