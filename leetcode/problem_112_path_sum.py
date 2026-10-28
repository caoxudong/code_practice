"""
https://leetcode.com/problems/path-sum/description/

Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.



Example 1:
                        5
                       / \
                      4   8
                     /   / \
                    11  13  4
                   /  \      \
                  7    2      1
* Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
* Output: true
* Explanation: The root-to-leaf path with the target sum is shown.

Example 2:
                1
               / \
              2   3
* Input: root = [1,2,3], targetSum = 5
* Output: false
* Explanation: There are two root-to-leaf paths in the tree:
    * (1 --> 2): The sum is 3.
    * (1 --> 3): The sum is 4.
    * There is no root-to-leaf path with sum = 5.

Example 3:
* Input: root = [], targetSum = 0
* Output: false
* Explanation: Since the tree is empty, there are no root-to-leaf paths.

Constraints:
* The number of nodes in the tree is in the range [0, 5000].
* -1000 <= Node.val <= 1000
* -1000 <= targetSum <= 1000
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from ast import NodeVisitor
from typing import Tuple

from common_data_structure.tree_node import TreeNode


class Solution:
    def hasPathSum(self, root: TreeNode | None, targetSum: int) -> bool:
        if root is None:
            return False

        stack: list[Tuple[TreeNode, int]] = [(root, root.val)]
        while len(stack) != 0:
            node_tuple = stack.pop()
            node = node_tuple[0]
            node_sum = node_tuple[1]
            node_left_child = node.left
            node_right_child = node.right
            if node_left_child is None and node_right_child is None:
                if node_sum == targetSum:
                    return True
                continue

            if node_left_child is not None:
                stack.append((node_left_child, node_sum + node_left_child.val))

            if node_right_child is not None:
                stack.append((node_right_child, node_sum + node_right_child.val))

        return False
