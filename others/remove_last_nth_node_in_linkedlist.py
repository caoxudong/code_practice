"""
题目：给定一个链表，删除链表的倒数第 N 个节点，并且返回链表的头结点。
◼ 示例： 给定一个链表: 1->2->3->4->5, 和 n = 2. 当删除了倒数第二个节点后，链表变为 1->2->3->5. 说明： 给定的 n 保证是有效的。 要求： 只允许对链表进行一次遍历。

出题人：阿里巴巴出题专家：屹平／阿里云视频云边缘计算高级技术专家
"""

class Node:
    def __init__(self, n, next = None):
        self.n = n
        self.next = next

def print_nodes(tail):
    while tail is not None:
        print(tail.n, end="\t")
        tail = tail.next

def remove_last_nth(tail, n):
    m_node = tail
    n_node = tail

    i = 0
    while i <= n:
        m_node = m_node.next
        i = i + 1
    
    while m_node.next is not None:
        m_node = m_node.next
        n_node= n_node.next

    temp_node = n_node.next
    n_node.next = n_node.next.next
    temp_node.next = None
    return tail

if __name__ == "__main__":
    node1 = Node(1)
    next_node = node1
    for i in range(2,10):
        temp_node = Node(i,next_node)
        next_node = temp_node

    print_nodes(next_node)
    print("")

    remove_last_nth(next_node, 3)
    print_nodes(next_node)
    print("")
    