from typing import Optional
import unittest
from common_data_structure.list_node import ListNode
import common_data_structure.list_node as list_node
import leetcode.problem_62_unique_paths as problem


class UnitTestData:
    def __init__(self, m: int, n: int, expected: int) -> None:
        self.m = m
        self.n = n
        self.expected = expected


unittest_data = [
    # UnitTestData(m=3, n=7, expected=28),
    # UnitTestData(m=3, n=2, expected=3),
    # UnitTestData(m=1, n=2, expected=1),
    UnitTestData(m=23, n=12, expected=193536720),
]


class TestSolution(unittest.TestCase):
    def test_leetcode_62_uniquePaths(self):
        s = problem.Solution()
        for item in unittest_data:
            retval = s.uniquePaths(item.m, item.n)
            self.assertEqual(retval, item.expected)
