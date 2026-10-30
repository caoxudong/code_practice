"""
https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/

Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).

Example 1:
                3
               / \
              9   20
                 /  \
                15   7
* Input: root = [3,9,20,null,null,15,7]
* Output: [[3],[20,9],[15,7]]

Example 2:
* Input: root = [1]
* Output: [[1]]

Example 3:
* Input: root = []
* Output: []

Constraints:
* The number of nodes in the tree is in the range [0, 2000].
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
    def zigzagLevelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if root is None:
            return []

        stack = [(root, 1)]
        level_values_map = {}
        while len(stack) > 0:
            node_tuple = stack.pop(0)
            node = node_tuple[0]
            node_level = node_tuple[1]
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
        i = 1
        switch = False
        while True:
            level_values = level_values_map.get(i)
            if level_values:
                if switch:
                    level_values.reverse()
                retval.append(level_values)
                switch = not switch
                i += 1
            else:
                break

        return retval
