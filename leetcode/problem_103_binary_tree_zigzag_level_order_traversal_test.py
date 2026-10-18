import unittest
import leetcode.problem_103_binary_tree_zigzag_level_order_traversal as problem


class UnitTestData:
    def __init__(self, root: problem.TreeNode | None, expected: list[list[int]]):
        self.root = root
        self.expected = expected


unittest_data = [
    UnitTestData(
        root=problem.TreeNode.from_list([3, 9, 20, None, None, 15, 7]),
        expected=[[3], [20, 9], [15, 7]],
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
    def test_leetcode_103_zigzagLevelOrder(self):
        for item in unittest_data:
            solution = problem.Solution()
            retval = solution.zigzagLevelOrder(item.root)
            self.assertEqual(retval, item.expected)
