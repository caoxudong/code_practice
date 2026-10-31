# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val: int = 0, left: TreeNode = None, right: TreeNode = None):
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


def assertTreeNodeEqual(
    result: Optional[TreeNode] = None,
    expected: Optional[TreeNode] = None,
):
    if result == None and expected == None:
        return
    if result == None and expected != None:
        raise AssertionError("AssertionError, result is None, expected is {}".format(expected.to_string()))
    if result != None and expected == None:
        raise AssertionError("AssertionError, result is {}, expected is None".format(result.to_string()))

    result_stack: list[TreeNode] = [result]
    expected_stack: list[TreeNode] = [expected]
    while len(result_stack) > 0 and len(expected_stack) > 0:
        result_tmp_node = result_stack.pop()
        expected_tmp_node = expected_stack.pop()
        if result_tmp_node.val != expected_tmp_node.val:
            raise AssertionError(
                "AssertionError, result node value is {}, expected node value is {}".format(
                    result_tmp_node.val, expected_tmp_node.val
                )
            )

        result_tmp_node_left = result_tmp_node.left
        result_tmp_node_right = result_tmp_node.right
        expected_tmp_node_left = expected_tmp_node.left
        expected_tmp_node_right = expected_tmp_node.right
        if (
            (result_tmp_node_left is None and expected_tmp_node_left is not None)
            or (result_tmp_node_left is not None and expected_tmp_node_left is None)
            or (result_tmp_node_right is None and expected_tmp_node_right is not None)
            or (result_tmp_node_right is not None and expected_tmp_node_right is None)
        ):
            raise AssertionError("AssertionError, result and expected have different children")
        else:
            result_stack.append(result_tmp_node_right)
            result_stack.append(result_tmp_node_left)
            expected_stack.append(expected_tmp_node_right)
            expected_stack.append(expected_tmp_node_right)

    if len(result_stack) == len(expected_stack) == 0:
        pass
    else:
        raise AssertionError("AssertionError, result and expected have different nodes")
