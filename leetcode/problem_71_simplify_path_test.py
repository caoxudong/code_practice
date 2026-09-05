from typing import List
import unittest
import leetcode.problem_71_simplify_path as problem


class UnitTestData:
    def __init__(self, path: str, expected: str):
        self.path = path
        self.expected = expected


unittest_data = [
    UnitTestData(path="/home/", expected="/home"),
    UnitTestData(path="/home//foo/", expected="/home/foo"),
    UnitTestData(path="/home/user/Documents/../Pictures", expected="/home/user/Pictures"),
    UnitTestData(path="/../", expected="/"),
    UnitTestData(path="/.../a/../b/c/../d/./", expected="/.../b/d"),
]


class TestSolution(unittest.TestCase):
    def test_leetcode_71_simplifyPath(self):
        s = problem.Solution()
        for item in unittest_data:
            retval = s.simplifyPath(item.path)
            self.assertEqual(retval, item.expected)
