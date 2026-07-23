from typing import List
import unittest
import leetcode.problem_40_combination_sum_ii as problem


class UnitTestData:
    def __init__(self, candidates: List[int], target: int, expected: List[List[int]]) -> None:
        self.candidates = candidates
        self.target = target
        self.expected = expected


unittest_data = [
    UnitTestData(candidates=[10, 1, 2, 7, 6, 1, 5], target=8, expected=[[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]),
    UnitTestData(candidates=[2, 5, 2, 1, 2], target=5, expected=[[1, 2, 2], [5]]),
]


class TestSolution(unittest.TestCase):
    def test_leetcode_40_combinationSum2(self):
        s = problem.Solution()
        for item in unittest_data:
            retval = s.combinationSum2(item.candidates, item.target)
            self.assertEqual(retval, item.expected)
