__author__ = 'caoxudong'

"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.

https://oj.leetcode.com/problems/min-stack/
"""

from collections import OrderedDict

class MinStack:
    # initialize your data structure here.
    def __init__(self):
        self.stack = list()

    # @param x, an integer
    # @return nothing
    def push(self, x):
        curMin = self.getMin()
        if curMin is None or curMin > x:
            curMin = x        
        self.stack.append((x, curMin))


    # @return nothing
    def pop(self):        
        x, curMin = self.stack.pop()
        return x

    # @return an integer
    def top(self):
        return self.stack[-1][0]

    # @return an integer
    def getMin(self):        
        if self.stack:
            return self.stack[-1][1]
        else:
            return None