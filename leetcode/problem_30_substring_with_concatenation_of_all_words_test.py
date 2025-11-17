import unittest
import leetcode.problem_30_substring_with_concatenation_of_all_words as problem


class UnitTestData:
    def __init__(self, s: str = "", words: list[str] = [], expected: list[int] = []):
        self.s = s
        self.words = words
        self.expected = expected


unittest_data = [
    UnitTestData(s="barfoothefoobarman", words=["foo", "bar"], expected=[0, 9]),
    UnitTestData(
        s="wordgoodgoodgoodbestword",
        words=["word", "good", "best", "word"],
        expected=[],
    ),
    UnitTestData(
        s="barfoofoobarthefoobarman", words=["bar", "foo", "the"], expected=[6, 9, 12]
    ),
    UnitTestData(s="foobarfoobar", words=["foo", "bar"], expected=[0, 3, 6]),
    UnitTestData(
        s="fffffffffffffffffffffffffffffffff",
        words=[
            "a",
            "a",
            "a",
            "a",
            "a",
            "a",
            "a",
            "a",
            "a",
            "a",
            "a",
            "a",
            "a",
            "a",
            "a",
            "a",
            "a",
            "a",
            "a",
            "a",
        ],
        expected=[],
    ),
]


class TestSolution(unittest.TestCase):
    def test_findSubstring(self):
        s = problem.Solution()
        for item in unittest_data:
            result = s.findSubstring(item.s, item.words)
            result.sort()
            item.expected.sort()
            self.assertListEqual(result, item.expected)
