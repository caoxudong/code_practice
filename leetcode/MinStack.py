__author__ = 'caoxudong'

"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.


https://oj.leetcode.com/problems/min-stack/
"""


class MinStack:
    __data_queue = []
    __min_queue = None

    class Node:
        value = None
        next = None
        prev = None

    # @param x, an integer
    # @return an integer
    def push(self, x):
        node = self.Node()
        node.value = x
        if self.__min_queue:
            root = self.__min_queue

            # fast path
            if x <= root.value:
                node.next = root
                root.prev = node
                self.__min_queue = node
                self.__data_queue.append(node)
                return x

            temp_node = root
            while temp_node.next:
                if x <= temp_node.value:
                    node.next = temp_node
                    if temp_node.prev:
                        node.prev = temp_node.prev
                        temp_node.prev.next = node
                    temp_node.prev = node
                    self.__data_queue.append(node)
                    return x
                temp_node = temp_node.next
            if x <= temp_node.value:
                temp_node.prev.next = node
                node.prev = temp_node.prev
                temp_node.prev = node
                node.next = temp_node
            else:
                temp_node.next = node
                node.prev = temp_node

        else:
            self.__min_queue = node
        self.__data_queue.append(node)
        return x

    # @return nothing
    def pop(self):
        if self.__data_queue:
            node_count = len(self.__data_queue)
            temp_node = self.__data_queue.pop()
            if node_count == 1:
                self.__min_queue = None
            else:
                if temp_node.prev and temp_node.next is None:
                    temp_node.prev.next = None
                    temp_node.prev = None
                elif temp_node.next and temp_node.prev is None:
                    temp_node.next.prev = None
                    temp_node.next = None
                else:
                    temp_node.prev.next = temp_node.next
                    temp_node.next.prev = temp_node.prev

    # @return an integer
    def top(self):
        if self.__data_queue:
            return self.__data_queue[-1].value
        else:
            return None

    # @return an integer
    def getMin(self):
        if self.__data_queue:
            return self.__min_queue.value
        else:
            return None

    def print_data_queue(self):
        count = len(self.__data_queue)
        if count > 0:
            print('data_quque:', end="")
            for index in range(len(self.__data_queue) - 1, -1, -1):
                print(str(self.__data_queue[index].value) + "\t", end="")
            print()

    def print_min_queue(self):
        if len(self.__data_queue):
            temp_node = self.__min_queue
            print('min_quque:', end="")
            while temp_node:
                print(str(temp_node.value) + "\t", end="")
                temp_node = temp_node.next
            print()

if __name__ == "__main__":
    stack = MinStack()

    stack.push(2147483646)
    stack.push(2147483646)
    stack.push(2147483647)
    print(stack.top())
    stack.pop()
    print(stack.getMin())
    stack.pop()
    print(stack.getMin())
    stack.pop()
    stack.push(2147483647)
    print(stack.top())
    print(stack.getMin())
    stack.push(-2147483648)
    print(stack.top())
    print(stack.getMin())
    stack.pop()
    print(stack.getMin())

    stack.print_data_queue()
    stack.print_min_queue()