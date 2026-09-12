import unittest
import leetcode.problem_79_word_search as problem


class UnitTestData:
    def __init__(self, board: list[list[str]], word: str, expected: bool):
        self.board = board
        self.word = word
        self.expected = expected


unittest_data = [
    UnitTestData(
        board=[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], word="ABCCED", expected=True
    ),
    UnitTestData(board=[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], word="SEE", expected=True),
    UnitTestData(board=[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], word="ABCB", expected=False),
]


class TestSolution(unittest.TestCase):
    def test_leetcode_79_word_search(self):
        s = problem.Solution()
        for item in unittest_data:
            retval = s.exist(item.board, item.word)
            self.assertEqual(retval, item.expected)
