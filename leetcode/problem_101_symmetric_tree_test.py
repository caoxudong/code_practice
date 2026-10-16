import unittest
import leetcode.problem_101_symmetric_tree as problem


class UnitTestData:
    def __init__(self, root: problem.TreeNode | None, expected: bool):
        self.root = root
        self.expected = expected


unittest_data = [
    UnitTestData(
        root=problem.TreeNode.from_list([1, 2, 2, 3, 4, 4, 3]),
        expected=True,
    ),
    UnitTestData(
        root=problem.TreeNode.from_list([1, 2, 2, None, 3, None, 3]),
        expected=False,
    ),
]


class TestSolution(unittest.TestCase):
    def test_leetcode_101_isSymmetric(self):
        for item in unittest_data:
            solution = problem.Solution()
            retval = solution.isSymmetric(item.root)
            self.assertEqual(retval, item.expected)
