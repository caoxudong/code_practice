#!/usr/bin/env python
#coding: utf-8

"""
树的广度优先遍历，从最底层开始输出，最后输出顶层节点

https://oj.leetcode.com/problems/binary-tree-level-order-traversal-ii/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[][]}
    def levelOrderBottom(self, root):
      result = self.levelOrder(root);
      return result[::-1]

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