"""
https://leetcode.com/problems/recover-binary-search-tree/description/

You are given the root of a binary search tree (BST), where the values of exactly two nodes of the tree were swapped by mistake. Recover the tree without changing its structure.

Example 1:
            1                      3
           / \                    /
          3   null    ->         1
         / \                      \
        null 2                     2
* Input: root = [1,3,null,null,2]
* Output: [3,1,null,null,2]
* Explanation: 3 cannot be a left child of 1 because 3 > 1. Swapping 1 and 3 makes the BST valid.


Example 2:
            3                      2
           / \                    / \
          1   4    ->            1   4
             /                      /
            2                      3
* Input: root = [3,1,4,null,null,2]
* Output: [2,1,4,null,null,3]
* Explanation: 2 cannot be in the right subtree of 3 because 2 < 3. Swapping 2 and 3 makes the BST valid.

Constraints:
* The number of nodes in the tree is in the range [2, 1000].
* -2^31 <= Node.val <= 2^31 - 1
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from gettext import find

from common_data_structure.binary_tree_node import TreeNode


class Solution:
    def recoverTree(self, root: TreeNode | None) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        inf = float("inf")
        tmp_root = root
        find_error = False
        while True:
            stack = [(tmp_root, -inf, inf)]
            find_error = False
            while len(stack) > 0:
                node_tuple = stack.pop()
                node = node_tuple[0]
                left_child = node.left
                right_child = node.right
                if left_child is not None:
                    if left_child.val >= node.val or left_child.val <= node_tuple[1]:
                        node.val, left_child.val = left_child.val, node.val
                        find_error = True
                        break
                    stack.append((left_child, node_tuple[1], node.val))
                if right_child is not None:
                    if right_child.val <= node.val or right_child.val >= node_tuple[2]:
                        node.val, right_child.val = right_child.val, node.val
                        find_error = True
                        break
                    stack.append((right_child, node.val, node_tuple[2]))
            if not find_error:
                break
        return None
