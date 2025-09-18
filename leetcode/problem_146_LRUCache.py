#!/usr/bin/env python
#coding: utf-8

"""
LeetCode: https://oj.leetcode.com/problems/lru-cache/

Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and set.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
set(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.
"""

from collections import OrderedDict
 
class LRUCache:

    # @param capacity, an integer
    def __init__(self, capacity):
        self.cache = OrderedDict()
        self.capacity = capacity
        self.size = 0

    # @return an integer
    def get(self, key):
        if key in self.cache:
            value = self.cache[key]
            del self.cache[key]
            self.cache[key] = value
            return value
        else:
            return -1
        
    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if key in self.cache:
            del self.cache[key]
            self.size = self.size - 1
        self.cache[key] = value
        self.size = self.size + 1
        if self.size > self.capacity:
            self.cache.popitem(False)
            self.size = self.size - 1
