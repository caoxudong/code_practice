#!/usr/bin/env python
#coding: utf-8

"""
树的广度优先遍历，从最底层开始输出，最后输出顶层节点

https://oj.leetcode.com/problems/binary-tree-level-order-traversal-ii/
"""


from datastructure.common_datastructure import node

def visit_node(node):
  print(node.data)

def visit_list(list):
  for node in list:
    visit_node(node)

def breadth_first_search_ii(root=node.Node):
  if root:
    queue = []
    queue.append(root)
    levels_nodes_queue = []

    while len(queue):
      current_level_nodes_queue = []

      while len(queue):
        temp_node = queue.pop(0)
        current_level_nodes_queue.append(temp_node)

      levels_nodes_queue.insert(0, current_level_nodes_queue)

      for temp_node in current_level_nodes_queue:
        if temp_node.children and len(temp_node.children) > 0:
          for child_node in temp_node.children:
            queue.append(child_node)

    for temp_queue in levels_nodes_queue:
      visit_list(temp_queue)

if __name__ == '__main__':
  root = node.Node()
  root.data = 1

  left = node.Node()
  left.data = 2
  root.children.append(left)

  leftleft = node.Node()
  leftleft.data = 3
  left.children.append(leftleft)

  leftright = node.Node()
  leftright.data = 4
  left.children.append(leftright)

  right = node.Node()
  right.data = 5
  root.children.append(right)

  breadth_first_search_ii(root)