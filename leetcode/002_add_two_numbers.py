#!/usr/bin/env python

"""
https://leetcode.com/problems/add-two-numbers/

You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = ListNode(-1)
        tail = result
        
        cf_flag = 0
        while l1 is not None and l2 is not None:
            value1 = l1.val
            value2 = l2.val
            if cf_flag == 0:
                value = value1 + value2 
            else:
                value = value1 + value2 + 1
            cf_flag = 0
            if value < 10:
                tail.next = ListNode(value)
            else:
                tail.next = ListNode(value % 10)
                cf_flag = 1
            tail = tail.next
            l1 = l1.next
            l2 = l2.next
        
        while l1 != None:
            value = l1.val
            if cf_flag != 0:
                value = value + 1
            cf_flag = 0
            if value < 10: 
                tail.next = ListNode(value)
            else:
                tail.next = ListNode(value % 10)
                cf_flag = 1
            tail = tail.next
            l1 = l1.next
        
        while l2 != None:
            value = l2.val
            if cf_flag != 0:
                value = value + 1
            cf_flag = 0
            if value < 10: 
                tail.next = ListNode(value)
            else:
                tail.next = ListNode(value % 10)
                cf_flag = 1
            tail = tail.next
            l2 = l2.next
        
        if cf_flag != 0:
            tail.next = ListNode(1)
            tail = tail.next
        
        return result.next