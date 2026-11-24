from typing import Optional
import unittest
import leetcode.problem_117_populating_next_right_pointers_in_each_node as problem


class UnitTestData:
    def __init__(self, root: Optional[problem.Node], expected: Optional[problem.Node]):
        self.root = root
        self.expected = expected


node1 = problem.Node(1)
node2 = problem.Node(2)
node3 = problem.Node(3)
node4 = problem.Node(4)
node5 = problem.Node(5)
node6 = problem.Node(6)
node7 = problem.Node(7)
node2.set_next(node3)
node4.set_next(node5)
node3.set_next(node7)
unittest_data: list[UnitTestData] = [
    UnitTestData(
        root=problem.Node.create_by_nodes(
            val=1,
            left=problem.Node.create_by_nodes(
                val=2, left=problem.Node.create_by_nodes(val=4), right=problem.Node.create_by_nodes(val=5)
            ),
            right=problem.Node.create_by_nodes(val=3, right=problem.Node.create_by_nodes(val=7)),
        ),
        expected=problem.Node.create_by_nodes(
            val=1,
            left=node2.set_left(node4).set_right(node5),
            right=node3.set_right(node7),
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
