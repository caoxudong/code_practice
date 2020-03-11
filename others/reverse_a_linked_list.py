# 逆转单链表

class Node:
    def __init__(self, i, next):
        self.i = i
        self.next = next
    
    def printValue(self):
        print(self.i, end="\t")

def reverse(node):
    pass

def printList(node):
    if node == None:
        print("no nodes")
    else:
        tempNode = node
        while True:
            tempNode.printValue()
            tempNode = tempNode.next
            if tempNode is None:
                break

def createList(numberArray):
    numbersCount = len(numberArray)
    if numbersCount == 0:
        return None
    elif numbersCount == 1:
        return Node(numberArray[0], None)
    else:
        node = None
        for i in numberArray:
            node = Node(i, node)
        return node

def reverseList(node):
    if node is None:
        return node
    prevNode = None
    while node is not None:
        reserveNext = node.next
        node.next = prevNode
        prevNode = node
        node = reserveNext
    return prevNode


if __name__ == "__main__":
    numberArray = [1,2,3,4,5,6]
    nodeList = createList(numberArray)
    printList(nodeList)
    print()
    print("start reverse")
    reversedList = reverseList(nodeList)
    printList(reversedList)


