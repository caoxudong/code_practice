#!/usr/bin/env python
#coding: utf-8

__author__ = 'caoxudong'

import random


class Node:
    def __init__(self, data, children):
        self.data = data
        self.children = children

    def __init__(self):
        self.data = 0
        self.children = []