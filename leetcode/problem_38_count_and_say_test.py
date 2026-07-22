import unittest
import leetcode.problem_37_sudoku_solver as problem


class UnitTestData:
    def __init__(self, n: int = 1, expected: str = "") -> None:
        self.n
        self.expected = expected


unittest_data = [
    UnitTestData(
        n=1,
        expected="1",
    ),
    UnitTestData(n=4, expected="1211"),
]


class TestSolution(unittest.TestCase):
    def test_countAndSay(self):
        s = problem.Solution()
        for item in unittest_data:
            retval = s.countAndSay(item.n)
            self.assertEqual(retval, item.expected)
