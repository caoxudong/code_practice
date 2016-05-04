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
    result = []
    if root:
      queue = []
      queue.append(root)
      while len(queue):
        level_queue = []
        next_level_queue = []
        for node in queue:
          level_queue.append(node.val)
          if node.left:
            next_level_queue.append(node.left)
          if node.right:
            next_level_queue.append(node.right)
        result.append(level_queue)
        queue = next_level_queue
    return result
        