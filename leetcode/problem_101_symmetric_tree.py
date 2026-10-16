"""
https://leetcode.com/problems/symmetric-tree/description/

Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

Example 1:
                            1
                           / \
                          2   2
                         / \ / \
                        3  4 4  3
* Input: root = [1,2,2,3,4,4,3]
* Output: true

Example 2:
                            1
                           / \
                          2   2
                           \   \
                            3    3
* Input: root = [1,2,2,null,3,null,3]
* Output: false

Constraints:
* The number of nodes in the tree is in the range [1, 1000].
* -100 <= Node.val <= 100
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from common_data_structure.tree_node import TreeNode


class Solution:
    def isSymmetric(self, root: TreeNode | None) -> bool:
        if root is None:
            return True

        if root.left is None and root.right is None:
            return True

        if root.left is None or root.right is None:
            return False

        p_stack = [root.left]
        q_stack = [root.right]

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

            q_stack.append(q_node.right)
            q_stack.append(q_node.left)

        if p_stack or q_stack:
            return False
        return True
