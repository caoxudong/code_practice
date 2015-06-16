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
  	return self.invertRecursive(root)

  def invertRecursive(self, root):
  	if root:
  		temp = left
  		root.left = root.right
  		root.right = temp
  		if root.left:
  			invertRecursive(self, root.left)
  		if root.right:
  			invertRecursive(self, root.right)
  	return root

  def invertNonRecursive(self, root):
  	if root:
  		pass
  	return root