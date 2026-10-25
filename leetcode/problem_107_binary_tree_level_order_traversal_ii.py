"""
https://leetcode.com/problems/binary-tree-level-order-traversal-ii/description/


Given the root of a binary tree, return the bottom-up level order traversal of its nodes' values. (i.e., from left to right, level by level from leaf to root).


Example 1:
            3
           / \
          9  20
            /  \
           15   7
* Input: root = [3,9,20,null,null,15,7]
* Output: [[15,7],[9,20],[3]]

Example 2:
* Input: root = [1]
* Output: [[1]]

Example 3:
* Input: root = []
* Output: []

Constraints:
* The number of nodes in the tree is in the range [0, 2000].
* -1000 <= Node.val <= 1000
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from common_data_structure.tree_node import TreeNode


class Solution:
    def levelOrderBottom(self, root: TreeNode | None) -> list[list[int]]:
        if root is None:
            return []

        max_level = 1
        stack = [(root, 1)]
        level_values_map = {}
        while len(stack) > 0:
            node_tuple = stack.pop(0)
            node = node_tuple[0]
            node_level = node_tuple[1]
            max_level = max(max_level, node_level)
            left_child = node.left
            right_child = node.right
            level_values = level_values_map.get(node_level, [])
            level_values.append(node.val)
            level_values_map[node_level] = level_values

            if left_child:
                stack.append((left_child, node_level + 1))
            if right_child:
                stack.append((right_child, node_level + 1))

        retval = []
        i = max_level
        while i > 0:
            level_values = level_values_map.get(i)
            if level_values:
                retval.append(level_values)
                i -= 1
            else:
                break

        return retval
