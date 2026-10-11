import unittest
import leetcode.problem_97_interleaving_string as problem


class UnitTestData:
    def __init__(self, s1: str, s2: str, s3: str, expected: bool):
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3
        self.expected = expected


unittest_data = [
    UnitTestData("aabcc", "dbbca", "aadbbcbcac", True),
    UnitTestData("aabcc", "dbbca", "aadbbbaccc", False),
    UnitTestData("", "", "", True),
]


class TestSolution(unittest.TestCase):
    def test_leetcode_97_isInterleave(self):
        solution = problem.Solution()
        for data in unittest_data:
            self.assertEqual(solution.isInterleave(data.s1, data.s2, data.s3), data.expected)
