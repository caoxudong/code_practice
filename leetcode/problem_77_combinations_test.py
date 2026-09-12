import unittest
import leetcode.problem_77_combinations as problem


class UnitTestData:
    def __init__(self, n: int, k: int, expected: list[list[int]]):
        self.n = n
        self.k = k
        self.expected = expected

unittest_data = [
    UnitTestData(n=4, k=2, expected=[[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]),
    UnitTestData(n=1, k=1, expected=[[1]]),
]

class TestSolution(unittest.TestCase):
    def test_leetcode_77_combine(self):
        s = problem.Solution()
        for item in unittest_data:
            retval = s.combine(item.n, item.k)
            self.assertEqual(retval, item.expected)