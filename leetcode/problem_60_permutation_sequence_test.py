from typing import List
import unittest
import leetcode.problem_60_permutation_sequence as problem


class UnitTestData:
    def __init__(self, n: int, k: int, expected: str) -> None:
        self.n = n
        self.k = k
        self.expected = expected


unittest_data = [
    UnitTestData(n=3, k=3, expected="213"),
    UnitTestData(n=4, k=9, expected="2314"),
    UnitTestData(n=3, k=1, expected="123"),
]


class TestSolution(unittest.TestCase):
    def test_leetcode_60_getPermutation(self):
        s = problem.Solution()
        for item in unittest_data:
            retval = s.getPermutation(item.n, item.k)
            self.assertEqual(item.expected, retval)
