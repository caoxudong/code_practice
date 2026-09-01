from typing import List
import unittest
import leetcode.problem_67_add_binary as problem


class UnitTestData:
    def __init__(self, a: str, b: str, expected: str):
        self.a = a
        self.b = b
        self.expected = expected


unittest_data = [
    UnitTestData(a="11", b="1", expected="100"),
    UnitTestData(a="1010", b="1011", expected="10101"),
]


class TestSolution(unittest.TestCase):
    def test_leetcode_67_add_binary(self):
        s = problem.Solution()
        for item in unittest_data:
            retval = s.plusOne(item.a, item.b)
            self.assertEqual(retval, item.expected)
