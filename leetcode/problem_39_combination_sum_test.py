from typing import List
import unittest
import leetcode.problem_39_combination_sum as problem


class UnitTestData:
    def __init__(self, candidates: List[int], target: int, expected: List[List[int]]) -> None:
        self.candidates = candidates
        self.target = target
        self.expected = expected


unittest_data = [
    UnitTestData(candidates=[2, 3, 6, 7], target=7, expected=[[2, 2, 3], [7]]),
    UnitTestData(candidates=[2, 3, 5], target=8, expected=[[2, 2, 2, 2], [2, 3, 3], [3, 5]]),
    UnitTestData(candidates=[2], target=1, expected=[]),
]


class TestSolution(unittest.TestCase):
    def test_leetcode_38_countAndSay(self):
        s = problem.Solution()
        for item in unittest_data:
            retval = s.countAndSay(item.n)
            self.assertEqual(retval, item.expected)
