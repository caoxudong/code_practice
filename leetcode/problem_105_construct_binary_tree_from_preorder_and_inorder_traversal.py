"""
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/

Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

Example 1:
                    3
                   / \
                  9   20
                     /   \
                    15    7
* Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
* Output: [3,9,20,null,null,15,7]

Example 2:
* Input: preorder = [-1], inorder = [-1]
* Output: [-1]

Constraints:
* 1 <= preorder.length <= 3000
* inorder.length == preorder.length
* -3000 <= preorder[i], inorder[i] <= 3000
* preorder and inorder consist of unique values.
* Each value of inorder also appears in preorder.
* preorder is guaranteed to be the preorder traversal of the tree.
* inorder is guaranteed to be the inorder traversal of the tree.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

from common_data_structure.tree_node import TreeNode


class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        preorder = deque(preorder)

        def build(preorder, inorder):
            if inorder:
                idx = inorder.index(preorder.popleft())
                root = TreeNode(inorder[idx])

                root.left = build(preorder, inorder[:idx])
                root.right = build(preorder, inorder[idx + 1 :])

                return root

        return build(preorder, inorder)
