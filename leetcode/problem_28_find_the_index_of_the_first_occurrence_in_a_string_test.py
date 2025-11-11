import unittest
import leetcode.problem_28_find_the_index_of_the_first_occurrence_in_a_string as problem


class UnitTestData:
    def __init__(self, haystack: str = "", needle: str = "", expected: int = 0):
        self.haystack = haystack
        self.needle = needle
        self.expected = expected


unittest_data = [
    UnitTestData(haystack="sadbutsad", needle="sad", expected=0),
    UnitTestData(haystack="leetcode", needle="leeto", expected=-1),
    UnitTestData(haystack="aaa", needle="aaaa", expected=-1),
    UnitTestData(haystack="mississippi", needle="issip", expected=4),
    UnitTestData(haystack="mississippi", needle="issipi", expected=-1),
]


class TestSolution(unittest.TestCase):
    def test_strStr(self):
        s = problem.Solution()
        for item in unittest_data:
            result = s.strStr(item.haystack, item.needle)
            self.assertEqual(result, item.expected)
