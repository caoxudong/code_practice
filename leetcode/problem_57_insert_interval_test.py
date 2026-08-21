from typing import List
import unittest
import leetcode.problem_57_insert_interval as problem


class UnitTestData:
    def __init__(self, intervals: List[List[int]], newInterval: List[int], expected: List[List[int]]) -> None:
        self.intervals = intervals
        self.newInterval = newInterval
        self.expected = expected


unittest_data = [
    UnitTestData(intervals=[[1, 3], [6, 9]], newInterval=[2, 5], expected=[[1, 5], [6, 9]]),
    UnitTestData(
        intervals=[[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], newInterval=[4, 8], expected=[[1, 2], [3, 10], [12, 16]]
    ),
]


class TestSolution(unittest.TestCase):
    def test_leetcode_57_insert(self):
        s = problem.Solution()
        for item in unittest_data:
            retval = s.insert(item.intervals, item.newInterval)
            self.assertEqual(item.expected, retval)
