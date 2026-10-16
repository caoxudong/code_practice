import unittest
import leetcode.problem_102_binary_tree_level_order_traversal as problem


class UnitTestData:
    def __init__(self, root: problem.TreeNode | None, expected: list[list[int]]):
        self.root = root
        self.expected = expected


unittest_data = [
    UnitTestData(
        root=problem.TreeNode.from_list([3, 9, 20, None, None, 15, 7]),
        expected=[[3], [9, 20], [15, 7]],
    ),
    UnitTestData(
        root=problem.TreeNode.from_list([1]),
        expected=[[1]],
    ),
    UnitTestData(
        root=problem.TreeNode.from_list([]),
        expected=[],
    ),
]


class TestSolution(unittest.TestCase):
    def test_leetcode_102_levelOrder(self):
        for item in unittest_data:
            solution = problem.Solution()
            retval = solution.levelOrder(item.root)
            self.assertEqual(retval, item.expected)
