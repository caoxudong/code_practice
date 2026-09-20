import unittest
import leetcode.problem_87_scramble_string as problem


class UnitTestData:
    def __init__(self, s1: str, s2: str, expected: bool):
        self.s1 = s1
        self.s2 = s2
        self.expected = expected


unittest_data = [
    UnitTestData(s1="great", s2="rgeat", expected=True),
    UnitTestData(s1="abcde", s2="caebd", expected=False),
    UnitTestData(s1="a", s2="a", expected=True),
]


class TestSolution(unittest.TestCase):
    def test_leetcode_87_scramble_string(self):
        for item in unittest_data:
            solution = problem.Solution()
            retval = solution.isScramble(item.s1, item.s2)
            self.assertEqual(retval, item.expected)
