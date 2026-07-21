import unittest
import leetcode.problem_37_sudoku_solver as problem


class UnitTestData:
    def __init__(
        self, board: list[list[str]] = [], expected: list[list[int]] = []
    ) -> bool:
        self.board = board
        self.expected = expected


unittest_data = [
    UnitTestData(
        board=[
            [".",".",".",".",".",".",".",".","."],
            [".","9",".",".","1",".",".","3","."],
            [".",".","6",".","2",".","7",".","."],
            [".",".",".","3",".","4",".",".","."],
            ["2","1",".",".",".",".",".","9","8"],
            [".",".",".",".",".",".",".",".","."],
            [".",".","2","5",".","6","4",".","."],
            [".","8",".",".",".",".",".","1","."],
            [".",".",".",".",".",".",".",".","."]
        ],
        expected=[
            
        ],
    ),
]


class TestSolution(unittest.TestCase):
    def test_solveSudoku(self):
        s = problem.Solution()
        for item in unittest_data:
            s.solveSudoku(item.board)
            v_numbers_sets: dict[int, list[str]] = {
                0: [],
                1: [],
                2: [],
                3: [],
                4: [],
                5: [],
                6: [],
                7: [],
                8: [],
            }
            h_numbers_sets: dict[int, list[str]] = {
                0: [],
                1: [],
                2: [],
                3: [],
                4: [],
                5: [],
                6: [],
                7: [],
                8: [],
            }
            sub_sudoku_numbers_sets: dict[str, list[str]] = {
                0: [],
                1: [],
                2: [],
                3: [],
                4: [],
                5: [],
                6: [],
                7: [],
                8: [],
            }
            for i in range(9):
                for j in range(9):
                    c = item.board[i][j]
                    if c in v_numbers_sets[i]:
                        raise Exception("wrong answer")
                    v_numbers_sets[i].append(c)
                    if c in h_numbers_sets[j]:
                        raise Exception("wrong answer")
                    h_numbers_sets[j].append(c)
                    key = "%s_%s"%(int(i/3), int(j/3))
                    if sub_sudoku_numbers_sets.get(key) != None and c in list(sub_sudoku_numbers_sets.get(key)):
                        raise Exception("wrong answer")
                    sub_sudoku_numbers_sets[key] = c
