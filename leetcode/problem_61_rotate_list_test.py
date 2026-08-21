from typing import Optional
import unittest
import leetcode.problem_61_rotate_list as problem


class UnitTestData:
    def __init__(self, head: Optional[problem.ListNode], k: int, expected: str) -> None:
        self.head = head
        self.k = k
        self.expected = expected


unittest_data = [
    UnitTestData(head=[1, 2, 3, 4, 5], k=2, expected=[4, 5, 1, 2, 3]),
    UnitTestData(head=[0, 1, 2], k=4, expected=[2, 0, 1]),
]


class TestSolution(unittest.TestCase):
    def test_leetcode_61_rotateRight(self):
        s = problem.Solution()
        for item in unittest_data:
            retval = s.rotateRight(item.head, item.k)
            self.assertEqual(item.expected, retval)
