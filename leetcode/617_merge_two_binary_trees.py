"""
Given two binary trees and imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not.

You need to merge them into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of new tree.

Example 1:
Input: 
	Tree 1                     Tree 2                  
          1                        2                             
         / \                      / \                            
        3   2                     1   3                        
       /                           \   \                      
      5                             4   7                  

Output: 
Merged tree:
	     3
	    / \
	   4   5
	  / \   \ 
	 5   4   7
 

Note: The merging process must start from the root nodes of both trees.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if t1 is None and t2 is None:
            return None
        else:
            result_root = TreeNode(0)
            stack = []

            if t1 is None:
                result_root.val = t2.val
                stack.append((None, t2.right, result_root, False))
                stack.append((None, t2.left, result_root, True))
            else:
                if t2 is None:
                    result_root.val = t1.val
                    stack.append((t1.right, None, result_root, False))
                    stack.append((t1.left, None, result_root, True))
                else:
                    result_root.val = t1.val + t2.val
                    stack.append((t1.right, t2.right, result_root, False))
                    stack.append((t1.left, t2.left, result_root, True))

            while len(stack) > 0:
                node_tuple = stack.pop()
                t1_node = node_tuple[0]
                t2_node = node_tuple[1]
                result_parent = node_tuple[2]
                is_left_child = node_tuple[3]

                if t1_node is None and t2_node is None:
                    continue
                else:
                    if t1_node is None:
                        result_node = TreeNode(t2_node.val)
                        stack.append((None, t2_node.right, result_node, False))
                        stack.append((None, t2_node.left, result_node, True))
                    else:
                        if t2_node is None:
                            result_node = TreeNode(t1_node.val)
                            stack.append(
                                (t1_node.right, None, result_node, False))
                            stack.append(
                                (t1_node.left, None, result_node, True))
                        else:
                            result_node = TreeNode(t1_node.val + t2_node.val)
                            stack.append(
                                (t1_node.right, t2_node.right, result_node, False))
                            stack.append(
                                (t1_node.left, t2_node.left, result_node, True))
                    if is_left_child:
                        result_parent.left = result_node
                    else:
                        result_parent.right = result_node
            return result_root


def create_tree(values):
    values_len = len(values)
    if values_len == 0:
        return None
    root = TreeNode(values[0])
    nodes = []
    nodes.append(root)
    i = 1
    while i < values_len:
        node_parent = nodes.pop(0)
        left_value = values[i]
        if left_value is None:
            node_parent.left = None
        else:
            left_node = TreeNode(left_value)
            node_parent.left = left_node
            nodes.append(left_node)
        i += 1

        if i < values_len:
            right_value = values[i]
            right_node = TreeNode(right_value)
            node_parent.right = right_node
            nodes.append(right_node)
            i += 1
    return root


if __name__ == "__main__":
    tests = [
        # ([[1, 3, 2, 5], [2, 1, 3, None, 4, None, 7]]),
        ([[], [1]])
    ]
    s = Solution()
    for t in tests:
        s.mergeTrees(create_tree(t[0]), create_tree(t[1]))
