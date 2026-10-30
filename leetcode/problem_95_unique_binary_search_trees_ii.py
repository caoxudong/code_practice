"""
https://leetcode.com/problems/unique-binary-search-trees-ii/description/


Given an integer n, return all the structurally unique BST's (binary search trees), which has exactly n nodes of unique values from 1 to n. Return the answer in any order.


Example 1:
    1     1           2          3          3
     \     \         / \        /          /
      3     2       1   3      2          1
     /       \                /            \
    2         3              1              2
* Input: n = 3
* Output: [[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]

Example 2:
* Input: n = 1
* Output: [[1]]

Constraints:
* 1 <= n <= 8
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from common_data_structure.binary_tree_node import TreeNode


class Solution:
    def generateTrees(self, n: int) -> list[TreeNode | None]:
        if n == 0:
            return []

        def generate_bst_trees(
            left_values: list[int], root_value: int, right_values: list[int]
        ) -> list[TreeNode | None]:
            retval = []
            right_sub_trees = []
            for i in range(len(right_values)):
                right_sub_trees.extend(generate_bst_trees(right_values[:i], right_values[i], right_values[i + 1 :]))

            left_sub_trees = []
            for i in range(len(left_values)):
                left_sub_trees.extend(generate_bst_trees(left_values[:i], left_values[i], left_values[i + 1 :]))

            if len(left_sub_trees) == 0 and len(right_sub_trees) == 0:
                root = TreeNode(root_value)
                retval.append(root)
            elif len(left_sub_trees) == 0:
                for i in range(len(right_sub_trees)):
                    root = TreeNode(root_value)
                    root.right = right_sub_trees[i]
                    retval.append(root)
            elif len(right_sub_trees) == 0:
                for i in range(len(left_sub_trees)):
                    root = TreeNode(root_value)
                    root.left = left_sub_trees[i]
                    retval.append(root)
            else:
                for i in range(len(left_sub_trees)):
                    for j in range(len(right_sub_trees)):
                        root = TreeNode(root_value)
                        root.left = left_sub_trees[i]
                        root.right = right_sub_trees[j]
                        retval.append(root)
            return retval

        retval = []
        for i in range(n):
            retval.extend(generate_bst_trees(list(range(1, i + 1)), i + 1, list(range(i + 2, n + 1))))
        return retval
