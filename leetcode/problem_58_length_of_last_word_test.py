from typing import List
import unittest
import leetcode.problem_58_length_of_last_word as problem


class UnitTestData:
    def __init__(self, s: str, expected: int) -> None:
        self.s = s
        self.expected = expected


unittest_data = [
    UnitTestData(s="Hello World", expected=5),
    UnitTestData(s="   fly me   to   the moon  ", expected=4),
    UnitTestData(s="luffy is still joyboy", expected=6),
    UnitTestData(s="Today is a nice day", expected=3),
]


class TestSolution(unittest.TestCase):
    def test_leetcode_58_lengthOfLastWord(self):
        s = problem.Solution()
        for item in unittest_data:
            retval = s.lengthOfLastWord(item.s)
            self.assertEqual(item.expected, retval)
