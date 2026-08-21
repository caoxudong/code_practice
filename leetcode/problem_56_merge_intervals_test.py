from typing import List
import unittest
import leetcode.problem_56_merge_intervals as problem


class UnitTestData:
    def __init__(self, intervals: List[List[int]], expected: List[List[int]]) -> None:
        self.intervals = intervals
        self.expected = expected


unittest_data = [
    UnitTestData(intervals=[[1, 3], [2, 6], [8, 10], [15, 18]], expected=[[1, 5]]),
    UnitTestData(intervals=[[1, 3], [2, 6], [8, 10], [15, 18]], expected=[[1, 6], [8, 10], [15, 18]]),
    UnitTestData(intervals=[[4, 7], [1, 4]], expected=[[1, 7]]),
]


class TestSolution(unittest.TestCase):
    def test_leetcode_56_merge(self):
        s = problem.Solution()
        for item in unittest_data:
            retval = s.merge(item.intervals)
            self.assertEqual(item.expected, retval)
