"""
https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/description/

Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree and postorder is the postorder traversal of the same tree, construct and return the binary tree.

Example 1:
                    3
                   / \
                  9   20
                     /   \
                    15    7
* Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
* Output: [3,9,20,null,null,15,7]

Example 2:
* Input: inorder = [-1], postorder = [-1]
* Output: [-1]

Constraints:
* 1 <= inorder.length <= 3000
* postorder.length == inorder.length
* -3000 <= inorder[i], postorder[i] <= 3000
* inorder and postorder consist of unique values.
* Each value of postorder also appears in inorder.
* inorder is guaranteed to be the inorder traversal of the tree.
* postorder is guaranteed to be the postorder traversal of the tree.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from common_data_structure.binary_tree_node import TreeNode


class Solution:
    def buildTree(self, inorder: list[int], postorder: list[int]) -> TreeNode | None:
        n = len(inorder)
        return self.helper(inorder, postorder, 0, n - 1, 0, n - 1)

    def helper(self, inorder, postorder, inS, inE, postS, postE):
        if inS > inE:
            return None

        root = TreeNode(postorder[postE])

        i = inS
        while i <= inE:
            if inorder[i] == root.val:
                break
            i += 1

        leftSize = i - inS
        rightSize = inE - i

        root.left = self.helper(inorder, postorder, inS, i - 1, postS, postS + leftSize - 1)

        root.right = self.helper(inorder, postorder, i + 1, inE, postE - rightSize, postE - 1)

        return root
