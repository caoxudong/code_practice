#!/usr/bin/env python
#coding: utf-8

"""
树的广度优先遍历，从最底层开始输出，最后输出顶层节点

https://oj.leetcode.com/problems/binary-tree-level-order-traversal-ii/
"""


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
  root.data = 1
  left = node.Node
  left.data = 2
  root.children.insert(0, left)
  leftleft = node.Node
  leftleft.data = 3
  left.children.insert(0, leftleft)
  leftright = node.Node
  leftright.data = 4
  left.children.insert(0, leftright)
  right = node.Node
  right.data = 5
  root.children.insert(1, right)
  breadth_first_search(root)