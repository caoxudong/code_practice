"""
https://leetcode.com/problems/same-tree/description/

Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.


Example 1:
            1                     1
           / \                   / \
          2   3    ->           2   3
* Input: p = [1,2,3], q = [1,2,3]
* Output: true

Example 2:
            1                     1
           / \                   / \
          2   null    ->        null 2
* Input: p = [1,2], q = [1,null,2]
* Output: false

Example 3:
            1                     1
           / \                   / \
          2   1    ->           1   2
* Input: p = [1,2,1], q = [1,1,2]
* Output: false

Constraints:
* The number of nodes in both trees is in the range [0, 100].
* -10^4 <= Node.val <= 10^4
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from common_data_structure.tree_node import TreeNode


class Solution:
    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        p_stack = [p]
        q_stack = [q]

        while p_stack and q_stack:
            p_node = p_stack.pop()
            q_node = q_stack.pop()

            if not p_node and not q_node:
                continue

            if not p_node or not q_node:
                return False

            if p_node.val != q_node.val:
                return False

            p_stack.append(p_node.left)
            p_stack.append(p_node.right)

            q_stack.append(q_node.left)
            q_stack.append(q_node.right)

        if p_stack or q_stack:
            return False
        return True
