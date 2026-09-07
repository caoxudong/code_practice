from typing import List
import unittest
import leetcode.problem_72_edit_distance as problem


class UnitTestData:
    def __init__(self, word1: str, word2: str, expected: int):
        self.word1 = word1
        self.word2 = word2
        self.expected = expected


unittest_data = [
    UnitTestData(word1="horse", word2="ros", expected=3),
    UnitTestData(word1="intention", word2="execution", expected=5),
]


class TestSolution(unittest.TestCase):
    def test_leetcode_72_editDistance(self):
        s = problem.Solution()
        for item in unittest_data:
            retval = s.minDistance(item.word1, item.word2)
            self.assertEqual(retval, item.expected)
