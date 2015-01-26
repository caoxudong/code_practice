#!/usr/bin/env python

"""
广度优先遍历  https://oj.leetcode.com/problems/binary-tree-level-order-traversal/
"""

__author__ = 'caoxudong'

from datastructure.common_datastructure import node

def visit_node(node):
  print(node.data)

def breadth_first_search(root=node.Node):
  if root:
    queue = []
    queue.append(root)
    while len(queue):
      temp_node = queue.pop(0)
      visit_node(temp_node)
      if temp_node.children and len(temp_node.children) > 0:
        for e in temp_node.children:
          queue.append(e)

if __name__ == '__main__':
  root = node.Node
  breadth_first_search(root)