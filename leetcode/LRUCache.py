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

class LinkedList:
    head = None
    tail = None
    size = 0

    def __init__(self):
        pass

    def len(self):
        return self.size

    def remove(self, node=None):
        if node == None:
            return removeFirst()
        else:
            if node == self.head:
                self.head = node.next
                node.next = None
            elif node == self.tail:
                self.tail = node.prev
                node.prev = None
            else:
                node.prev.next = node.next
                node.next.prev = node.prev    
            node.next = None
            node.prev = None
            self.size = self.size - 1
            return node

    def removeFirst(self):
        if self.size == 0:
            return None
        else:            
            if self.size == 1:
                temp_node = self.head
                temp_node.next = None
                self.head = None
                self.tail = None
                self.size = self.size - 1
            else:
                temp_node = self.head
                self.head = temp_node.next
                self.head.prev = None
                temp_node.prev = None
                temp_node.next = None
                self.size = self.size - 1
            return temp_node

    def append(self, node):
        if self.size == 0:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        self.size = self.size + 1

class LRUCache:
 
    hash_table = {}
    __max_size = 0
    queue = LinkedList()
 
    def __init__(self, max_size):
        self.__max_size = max_size
 
    def get(self, key):
        value_node = self.hash_table.get(key)
        if value_node is None:
            return -1
        else:
            if self.queue.len() == 1:
                pass
            else:
                temp_node = self.queue.remove(value_node)                
                self.queue.append(temp_node)
            
            return value_node.value
 
    def set(self, key, value):
        value_node = self.hash_table.get(key)
        if value_node == None:
            if self.queue.len() == self.__max_size:
                node = self.queue.removeFirst()
                del self.hash_table[node.key]
            new_node = Node(key, value)
            self.queue.append(new_node)
            self.hash_table[key] = new_node            
        else:
            value_node.value = value
            value_node = self.queue.remove(value_node)
            self.queue.append(value_node)

cache = LRUCache(2)
print(cache.get(2))
cache.set(2,6)
print(cache.get(1))
cache.set(1,5)
cache.set(1,2)
print(cache.get(1))
print(cache.get(2))
