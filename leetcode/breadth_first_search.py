#!/usr/bin/env python

"""
广度优先遍历  https://oj.leetcode.com/problems/binary-tree-level-order-traversal/
"""

__author__ = 'caoxudong'


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
  # @param {TreeNode} root
  # @return {integer[][]}
  def levelOrder(self, root):
    if root:
      queue = []
      queue.append(root)
      while True:
        length = len(queue)
        if length:
          e = queue.pop(length - 1)
          if e.left:
            queue.append(e.left)
          if e.right:
            queue.append(e.right)
    return root
        