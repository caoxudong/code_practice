# 用Java/C/C++/Python语言之一定义栈的数据结构，
# 并在该类型中实现一个能够得到栈的最小元素的getMin和最大元素的getMax函数。
# 要求在该栈中，调用getMin、getMax, push及pop的时间复杂度都是O(1)。

class StackNode:
    def __init__(self, i, min, max):
        self.i = i
        self.min = min
        self.max = max

class Stack:

    def __init__(self):
        self.elements = []


    def min(self):
        if len(self.elements) == 0:
            return -1
        return self.elements[-1].min

    def max(self):
        if len(self.elements) == 0:
            return -1
        return self.elements[-1].max

    def push(self,i):
        if len(self.elements) == 0:
            min = i
            max = i
        else:
            min = self.elements[-1].min
            max = self.elements[-1].max
        if i < min:
            min = i
        if i > max:
            max = i
        node = StackNode(i, min, max)
        self.elements.append(node)

    def pop(self):
        if len(self.elements) == 0:
            return None
        node = self.elements[-1]
        self.elements = self.elements[:-1]
        return node.i


if __name__ == '__main__':
    stack = Stack()
    test_params = [1,3,6,2,5,7,4]
    for i in test_params:
        stack.push(i)
        print("stack.push("+str(i)+")", end="\t")
        print("min=" + str(stack.min()), end="\t")
        print("max=" + str(stack.max()), end="\t")
        print("")
    for i in test_params:
        stack.pop()
        print("stack.pop()", end="\t")
        print("min=" + str(stack.min()), end="\t")
        print("max=" + str(stack.max()), end="\t")
        print("")