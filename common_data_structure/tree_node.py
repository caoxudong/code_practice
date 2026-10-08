# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @staticmethod
    def from_list(values: list[int | None]) -> TreeNode | None:
        if len(values) == 0 or values[0] is None:
            return None

        root = TreeNode(values[0])
        from collections import deque

        queue = deque([root])

        index = 1
        while queue and index < len(values):
            current_node = queue.popleft()
            if values[index] is not None:
                current_node.left = TreeNode(values[index])
                queue.append(current_node.left)
            index += 1
            if index < len(values) and values[index] is not None:
                current_node.right = TreeNode(values[index])
                queue.append(current_node.right)
            index += 1
        return root

    def to_list(self) -> list[int]:
        if not self:
            return []

        result = []
        from collections import deque

        queue = deque([self])
        while queue:
            current_node = queue.popleft()
            if current_node is None:
                result.append(None)
            else:
                result.append(current_node.val)
                queue.append(current_node.left)
                queue.append(current_node.right)

        while result and result[-1] is None:
            result.pop()

        return result
