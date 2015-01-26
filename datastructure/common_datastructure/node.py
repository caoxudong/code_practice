#!/usr/bin/env python

__author__ = 'caoxudong'

import random


class Node:
    data = None
    children = None

    def __init__(self, data, children):
        self.data = data
        self.children = children

    def __init__(self):
        self.data = random.randint(1, 100)
        self.children = []