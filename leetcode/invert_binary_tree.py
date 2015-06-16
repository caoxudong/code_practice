#!/usr/bin/env python
#coding: utf-8

"""
Invert a binary tree.  https://leetcode.com/problems/invert-binary-tree/

     4
   /   \
  2     7
 / \   / \
1   3 6   9

to
     4
   /   \
  7     2
 / \   / \
9   6 3   1

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
  # @param {TreeNode} root
  # @return {TreeNode}
  def invertTree(self, root):
    return self.invertNonRecursive(root)

  def invertRecursive(self, root):
    if root:
      root.left, root.right = root.right, root.left
      if root.left:
        self.invertRecursive(root.left)
      if root.right:
        self.invertRecursive(root.right)
    return root

  def invertNonRecursive(self, root):
    if root:
      queue = []
      queue.append(root)
      while True:
        length = len(queue)
        if length == 0:
          break;
        e = queue.pop(length - 1)
        e.left, e.right = e.right, e.left
        if e.left:
          queue.append(e.left)
        if e.right:
          queue.append(e.right)
    return root