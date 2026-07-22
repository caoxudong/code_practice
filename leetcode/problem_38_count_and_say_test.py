import unittest
import leetcode.problem_38_count_and_say as problem


class UnitTestData:
    def __init__(self, n: int = 1, expected: str = "") -> None:
        self.n = n
        self.expected = expected


unittest_data = [
    UnitTestData(
        n=1,
        expected="1",
    ),
    UnitTestData(n=4, expected="1211"),
]


class TestSolution(unittest.TestCase):
    def test_leetcode_38_countAndSay(self):
        s = problem.Solution()
        for item in unittest_data:
            retval = s.countAndSay(item.n)
            self.assertEqual(retval, item.expected)
