#!/usr/bin/env python
#coding: utf-8

"""
LeetCode: https://leetcode.com/problems/copy-list-with-random-pointer/

A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.
"""

import os
import random

# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if None == head:
            return None
        
        # put the new copied node next to it's original node,
        step_node = head
        while step_node != None:
            new_node = RandomListNode(step_node.label * 10)
            new_node.next = step_node.next
            step_node.next = new_node
            step_node = new_node.next
        
        # copy random value
        step_node = head
        while step_node != None:
            target_node = step_node.next
            target_node.random = step_node.random and step_node.random.next
            step_node = target_node.next
        
        # delete origin node
        step_node, copied_node, result = head, head.next, head.next
        while step_node != None:
            step_node.next = copied_node.next
            step_node = copied_node.next
            copied_node.next = step_node and step_node.next
            copied_node = step_node and step_node.next 

        return result




def printList(head):
    step_node = head
    while step_node:
        temp_random_node = step_node.random
        if temp_random_node:
            print(step_node.label, " random -> ", step_node.random.label)
        else:
            print(step_node.label, " random -> ", None)
        step_node = step_node.next

head = RandomListNode(0)
node_list = []
step_node = head
<<<<<<< ccb1cdfd9e75bfd838ac4f23952695694bcee3fb
for i in range(1, 10):
=======
for i in range(1, 2):
>>>>>>> finish leetcode 138
    temp_node = RandomListNode(i)
    step_node.next = temp_node
    step_node = temp_node
    node_list.append(temp_node)

for temp_node in node_list:
    temp_node.random = node_list[random.randint(0, len(node_list)) - 1]

<<<<<<< ccb1cdfd9e75bfd838ac4f23952695694bcee3fb
printList(head)

print('================')

solution = Solution()
copied_list = solution.copyRandomList(head)
printList(copied_list)        


print('================')
printList(head)
=======
head = RandomListNode(-1)

printList(head)
print("=================")
solution = Solution()
copied_list = solution.copyRandomList(head)
printList(copied_list)        
print("=================")
printList(head)
>>>>>>> finish leetcode 138
