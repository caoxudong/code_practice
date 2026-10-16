import unittest
import leetcode.problem_100_same_tree as problem


class UnitTestData:
    def __init__(self, p: problem.TreeNode | None, q: problem.TreeNode | None, expected: bool):
        self.p = p
        self.q = q
        self.expected = expected


unittest_data = [
    UnitTestData(
        p=problem.TreeNode.from_list([1, 2, 3]),
        q=problem.TreeNode.from_list([1, 2, 3]),
        expected=True,
    ),
    UnitTestData(
        p=problem.TreeNode.from_list([1, 2]),
        q=problem.TreeNode.from_list([1, None, 2]),
        expected=False,
    ),
    UnitTestData(
        p=problem.TreeNode.from_list([1, 2, 1]),
        q=problem.TreeNode.from_list([1, 1, 2]),
        expected=False,
    ),
]


class TestSolution(unittest.TestCase):
    def test_leetcode_100_isSameTree(self):
        for item in unittest_data:
            solution = problem.Solution()
            result = solution.isSameTree(item.p, item.q)
            self.assertEqual(result, item.expected)
