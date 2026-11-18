from typing import Optional
import unittest
import leetcode.problem_116_populating_next_right_pointers_in_each_node as problem


class UnitTestData:
    def __init__(self, root: Optional[problem.Node], expected: Optional[problem.Node]):
        self.root = root
        self.expected = expected


unittest_data: list[UnitTestData] = [
    UnitTestData(
        root=problem.Node(
            1,
            left=problem.Node(2, left=problem.Node(4), right=problem.Node(5)),
            right=problem.Node(3, left=problem.Node(6), right=problem.Node(7)),
        ),
        expected=problem.Node(
            1,
            left=problem.Node(
                2, left=problem.Node(4), right=problem.Node(5, next=problem.Node(6, next=problem.Node(7)))
            ),
            right=problem.Node(3, left=problem.Node(6, next=problem.Node(7)), right=problem.Node(7)),
        ),
    ),
    UnitTestData(
        root=None,
        expected=None,
    ),
]


def assert_trees_equal(node1: Optional[problem.Node], node2: Optional[problem.Node]):
    if node1 is None and node2 is None:
        return True
    if node1 is None or node2 is None:
        return False
    if node1.val != node2.val:
        return False
    if not assert_trees_equal(node1.left, node2.left):
        return False
    if not assert_trees_equal(node1.right, node2.right):
        return False
    if not assert_trees_equal(node1.next, node2.next):
        return False
    return True


class TestSolution(unittest.TestCase):
    def test_leetcode_116_connect(self):
        for item in unittest_data:
            solution = problem.Solution()
            retval = solution.connect(item.root)
            self.assertTrue(assert_trees_equal(retval, item.expected))
