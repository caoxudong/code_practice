import random


class SkipListNode:
    def __init__(self, key: int = 0, data: object = None, level: int = 0):
        self.key = key
        self.data = data
        self.next_nodes: list[SkipListNode] = [None] * level


class Skiplist:

    def __init__(self, max_level: int = 1):
        self.random_obj = random.Random()
        self.random_obj.seed(None)
        self.max_level = max_level
        self.head = SkipListNode(key=int.max, data=None, level=max_level)

    def find(self, target_key: int = 0) -> object:
        retval = None
        max_level = self.max_level

        tmp_cursor_node = self.head
        for tmp_level in range(max_level):
            while tmp_cursor_node.next_nodes[tmp_level].key < target_key:
                tmp_cursor_node = tmp_cursor_node.next_nodes[tmp_level]
        
        if tmp_cursor_node.key == target_key:
            return tmp_cursor_node.data
        else:

        return retval

    def insert_data(self, key: int = 0, data: object = None):
        level = self.random_obj.randint(1, self.max_level)
