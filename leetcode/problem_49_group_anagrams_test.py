from typing import List
import unittest
import leetcode.problem_49_group_anagrams as problem


class UnitTestData:
    def __init__(self, strs: List[str], expected: List[List[str]]) -> None:
        self.strs = strs
        self.expected = expected


unittest_data = [
    UnitTestData(
        strs=["eat", "tea", "tan", "ate", "nat", "bat"], expected=[["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
    ),
    UnitTestData(
        strs=[""],
        expected=[[""]],
    ),
    UnitTestData(
        strs=["a"],
        expected=[["a"]],
    ),
]


class TestSolution(unittest.TestCase):
    def test_leetcode_49_groupAnagrams(self):
        s = problem.Solution()
        for item in unittest_data:
            retval = s.groupAnagrams(item.strs)
            self.assertEqual(item.expected.sort(), retval.sort())
