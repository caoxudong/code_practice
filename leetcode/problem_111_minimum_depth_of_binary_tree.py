"""
https://leetcode.com/problems/minimum-depth-of-binary-tree/description/


Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.


Example 1:
            3
           / \
          9   20
             /  \
            15   7
* Input: root = [3,9,20,null,null,15,7]
* Output: 2

Example 2:
* Input: root = [2,null,3,null,4,null,5,null,6]
* Output: 5
 

Constraints:
* The number of nodes in the tree is in the range [0, 10^5].
* -1000 <= Node.val <= 1000
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from ast import Tuple

from common_data_structure.binary_tree_node import TreeNode


class Solution:
    def minDepth(self, root: TreeNode | None) -> int:
        if root is None:
            return 0

        min_level = 10000000
        stack: list[Tuple[TreeNode, int]] = [(root, 1)]
        while len(stack) != 0:
            node_tuple = stack.pop()
            node = node_tuple[0]
            node_level = node_tuple[1]
            node_left_child = node.left
            node_right_child = node.right
            if node_left_child is None and node_right_child is None:
                min_level = min(min_level, node_level)
                continue

            if node_left_child is not None:
                stack.append((node_left_child, node_level + 1))

            if node_right_child is not None:
                stack.append((node_right_child, node_level + 1))

        return min_level
