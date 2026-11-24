"""
https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/

Given a binary tree

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}

Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.


Example 1:
                    1                           1   -> NULL
                  /   \                       /   \
                2       3                   2   ->  3 -> NULL
              /  \        \                /  \       \
             4    5        7              4 -> 5    -> 7 -> NULL
* Input: root = [1,2,3,4,5,null,7]
* Output: [1,#,2,3,#,4,5,7,#]
* Explanation: Given the above binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.

Example 2:
* Input: root = []
* Output: []

Constraints:
* The number of nodes in the tree is in the range [0, 6000].
* -100 <= Node.val <= 100

Follow-up:
* You may only use constant extra space.
* The recursive approach is fine. You may assume implicit stack space does not count as extra space for this problem.
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Node:
    def __init__(self, val: int = 0, left: "Node" = None, right: "Node" = None, next: "Node" = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

    @staticmethod
    def create_by_nodes(val: int = 0, left: Node = None, right: Node = None, next: Node = None) -> Node:
        return Node(val=val, left=left, right=right, next=next)

    def set_next(self, next_node: "Node") -> Node:
        self.next = next_node
        return self

    def set_left(self, left_node: "Node") -> Node:
        self.left = left_node
        return self

    def set_right(self, right_node: "Node") -> Node:
        self.right = right_node
        return self


from typing import Optional


class Solution:
    def connect(self, root: Optional[Node]) -> Optional[Node]:
        if not root:
            return root

        from collections import deque

        q = deque([root])

        while q:
            size = len(q)
            for i in range(size):
                node = q.popleft()
                if i < size - 1:
                    node.next = q[0]
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        return root
