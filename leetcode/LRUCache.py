#!/usr/bin/env python
#coding: utf-8

"""
LeetCode: https://oj.leetcode.com/problems/lru-cache/
"""

 
#一个简单的LRUCache

class Node:
    key = ""
    value = ""
    prev = None
    next = None

    def __init__(self, key, value, prev=None, next=None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next

class LRUCache:
 
    __hash_table = {}
    __max_size = 0
    __queue = []
 
    def __init__(self, max_size):
        self.__max_size = max_size
 
    def get(self, key):
        value_node = self.__hash_table.get(key)
        if value_node is None:
            return None
        else:
            if self.__queue.size == 1:
                pass
            else:
                value_node.prev.next = value_node.next
                value_node.next.prev = value_node.prev
                self.__queue.enqueue(value_node)
            
            return value_node.value
 
    def set(self, key, value):
        if len(self.__queue) == self.__max_size:
            node = self.__queue.pop()
            del self.__hash_table[node.key]
        new_node = Node(key, value, len(self.__queue))
        self.__queue.insert(0, new_node)
        self.__hash_table[key] = new_node



cache = LRUCache(3)
cache.set(2, 1)
print(cache.get(2))
cache.set(3, 1)
cache.set(4, 1)
cache.set(5, 1)
cache.set(6, 1)
print(cache.get(3))
print(cache.get(4))
print(cache.get(5))
print(cache.get(6))
