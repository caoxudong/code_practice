"""
题目：给定一个二叉搜索树(BST)，找到树中第 K 小的节点。

出题人：阿里巴巴出题专家：文景／阿里云 CDN 资深技术专家

参考答案：

* 考察点
基础数据结构的理解和编码能力
递归使用

* 示例
       5
      / \
     3   6
    / \
   2   4
  /
 1
 
说明：保证输入的 K 满足 1<=K<=(节点数目）
"""

class Node:
    def __init__(self, n):
        self.n = n
        self.parent = None
        self.left = None
        self.right = None

def find_kth(root, k):
    if root is None:
        return None
    
    node = root
    nodes = []
    current_index = 0

    while True:
        while node is not None:
            nodes.append(node)
            node = node.left

        if len(nodes) == 0:
            break

        current_node = nodes.pop()
        current_index = current_index + 1
        if current_index == k:
            return current_node

        if current_node.right is not None:
            nodes.append(current_node.right)

    raise Exception("you shouldn't be here")


if __name__ == "__main__":
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)

    node1.parent = node2
    node2.parent = node3
    node4.parent = node3
    node3.parent = node5
    node6.parent = node5
    root = node5

    node5.left = node3
    node5.right = node6
    node3.left = node2
    node3.right = node4
    node2.left = node1

    a = find_kth(root, 4)
    print(a.n)
