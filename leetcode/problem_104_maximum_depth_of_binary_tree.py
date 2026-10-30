"""
https://leetcode.com/problems/maximum-depth-of-binary-tree/description/

Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Example 1:
                    3
                   / \
                  9   20
                     /   \
                    15    7
Input: root = [3,9,20,null,null,15,7]
Output: 3

Example 2:
* Input: root = [1,null,2]
* Output: 2

Constraints:
* The number of nodes in the tree is in the range [0, 10^4].
* -100 <= Node.val <= 100
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from common_data_structure.binary_tree_node import TreeNode


class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        if root is None:
            return 0
        max_depth = 1
        stack = [(root, 1)]
        while len(stack) > 0:
            node_tuple = stack.pop()
            node = node_tuple[0]
            node_depth = node_tuple[1]
            max_depth = max(node_depth, max_depth)
            if node.left:
                stack.append((node.left, node_depth + 1))
            if node.right:
                stack.append((node.right, node_depth + 1))
        return max_depth
