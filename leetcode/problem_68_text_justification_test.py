from typing import List
import unittest
import leetcode.problem_68_text_justification as problem


class UnitTestData:
    def __init__(self, words: List[str], maxWidth: int, expected: List[str]):
        self.words = words
        self.maxWidth = maxWidth
        self.expected = expected


unittest_data = [
    UnitTestData(
        words=["This", "is", "an", "example", "of", "text", "justification."],
        maxWidth=16,
        expected=["This    is    an", "example  of text", "justification.  "],
    ),
    UnitTestData(
        words=["What", "must", "be", "acknowledgment", "shall", "be"],
        maxWidth=16,
        expected=["What   must   be", "acknowledgment  ", "shall be        "],
    ),
    UnitTestData(
        [
            "Science",
            "is",
            "what",
            "we",
            "understand",
            "well",
            "enough",
            "to",
            "explain",
            "to",
            "a",
            "computer.",
            "Art",
            "is",
            "everything",
            "else",
            "we",
            "do",
        ],
        maxWidth=20,
        expected=[
            "Science  is  what we",
            "understand      well",
            "enough to explain to",
            "a  computer.  Art is",
            "everything  else  we",
            "do                  ",
        ],
    ),
]


class TestSolution(unittest.TestCase):
    def test_leetcode_68_text_justification(self):
        s = problem.Solution()
        for item in unittest_data:
            retval = s.fullJustify(item.words, item.maxWidth)
            self.assertListEqual(retval, item.expected)
