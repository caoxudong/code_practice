from typing import List
import unittest
import leetcode.problem_44_wildcard_matching as problem


class UnitTestData:
    def __init__(self, s: str, p: str, expected: bool) -> None:
        self.s = s
        self.p = p
        self.expected = expected


unittest_data = [
    UnitTestData(s="aa", p="a", expected=False),
    UnitTestData(s="aa", p="*", expected=True),
    UnitTestData(s="cb", p="?a", expected=False),
    UnitTestData(s="acdcb", p="a*c?b", expected=False),
    UnitTestData(s="mississippi", p="m??*ss*?i*pi", expected=False),
]


class TestSolution(unittest.TestCase):
    def test_leetcode_44_isMatch(self):
        s = problem.Solution()
        for item in unittest_data:
            retval = s.isMatch(item.s, item.p)
            self.assertEqual(retval, item.expected)
