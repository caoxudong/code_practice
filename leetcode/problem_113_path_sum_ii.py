"""
https://leetcode.com/problems/path-sum-ii/description/


Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where the sum of the node values in the path equals targetSum. Each path should be returned as a list of the node values, not node references.

A root-to-leaf path is a path starting from the root and ending at any leaf node. A leaf is a node with no children.

Example 1:
                    5
                   / \
                  4   8
                 /   / \
                11  13  4
               /  \    / \
              7    2  5   1
* Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
* Output: [[5,4,11,2],[5,8,4,5]]
* Explanation: There are two paths whose sum equals targetSum:
    * 5 + 4 + 11 + 2 = 22
    * 5 + 8 + 4 + 5 = 22

Example 2:
            1
           / \
          2   3
* Input: root = [1,2,3], targetSum = 5
* Output: []

Example 3:
* Input: root = [1,2], targetSum = 0
* Output: []

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
from curses import newpad

from common_data_structure.tree_node import TreeNode


class Solution:
    def pathSum(self, root: TreeNode | None, targetSum: int) -> list[list[int]]:
        if root is None:
            return []

        retval = []
        stack: list[TreeNode] = [(root, targetSum - root.val, [root.val])]
        while len(stack) != 0:
            node_tuple = stack.pop()
            node: TreeNode = node_tuple[0]
            left_sum = node_tuple[1]
            current_path: list[int] = node_tuple[2]
            left_child_node: TreeNode = node.left
            right_child_node: TreeNode = node.right
            if left_child_node is not None:
                new_path = current_path.copy()
                new_path.append(left_child_node.val)
                stack.append((left_child_node, left_sum - left_child_node.val, new_path))
            if right_child_node is not None:
                new_path = current_path.copy()
                new_path.append(right_child_node.val)
                stack.append((right_child_node, left_sum - right_child_node.val, new_path))

            if left_child_node is None and right_child_node is None and left_sum == 0:
                retval.append(current_path)
        return retval
