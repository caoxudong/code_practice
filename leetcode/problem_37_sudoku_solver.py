"""
https://leetcode.com/problems/sudoku-solver/description/?utm_source=LCUS&utm_medium=ip_redirect&utm_campaign=transfer2china

Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:
* Each of the digits 1-9 must occur exactly once in each row.
* Each of the digits 1-9 must occur exactly once in each column.
* Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.

The '.' character indicates empty cells.

Example 1:
* Input: board =
[
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]
* Output:
[
    ["5","3","4","6","7","8","9","1","2"],
    ["6","7","2","1","9","5","3","4","8"],
    ["1","9","8","3","4","2","5","6","7"],
    ["8","5","9","7","6","1","4","2","3"],
    ["4","2","6","8","5","3","7","9","1"],
    ["7","1","3","9","2","4","8","5","6"],
    ["9","6","1","5","3","7","2","8","4"],
    ["2","8","7","4","1","9","6","3","5"],
    ["3","4","5","2","8","6","1","7","9"]
]


Constraints:
* board.length == 9
* board[i].length == 9
* board[i][j] is a digit or '.'.
* It is guaranteed that the input board has only one solution.
"""

from re import sub


class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        v_numbers_sets: dict[int, int] = {
            0: 0,
            1: 0,
            2: 0,
            3: 0,
            4: 0,
            5: 0,
            6: 0,
            7: 0,
            8: 0,
        }
        h_numbers_sets: dict[int, set[str]] = {
            0: 0,
            1: 0,
            2: 0,
            3: 0,
            4: 0,
            5: 0,
            6: 0,
            7: 0,
            8: 0,
        }
        sub_sudoku_numbers_sets: dict[str, set[str]] = {
            "0_0": 0,
            "0_1": 0,
            "0_2": 0,
            "1_0": 0,
            "1_1": 0,
            "1_2": 0,
            "2_0": 0,
            "2_1": 0,
            "2_2": 0,
        }

        def make_key(i: int, j: int) -> str:
            return "%s_%s" % (int(i / 3), int(j / 3))

        def validate(board: list[list[str]], i: int, j: int, n: int) -> bool:
            nonlocal v_numbers_sets, h_numbers_sets, sub_sudoku_numbers_sets
            tmp = 1 << n
            if v_numbers_sets[i] & tmp != 0 or h_numbers_sets[j] & tmp != 0:
                return False
            sub_sudoku = sub_sudoku_numbers_sets.get(make_key(i, j))
            if sub_sudoku is not None and int(sub_sudoku) & tmp != 0:
                return False
            return True

        def solveSudokuInner(board: list[list[str]], start_v: int, start_h: int) -> bool:
            nonlocal v_numbers_sets, h_numbers_sets, sub_sudoku_numbers_sets
            for i in range(start_v, 9):
                for j in range(0, 9):
                    if i == start_v and j < start_h:
                        continue
                    c = board[i][j]
                    if c == ".":
                        for n in range(0, 9):
                            number = n + 1
                            if validate(board, i, j, number):
                                number_str = "%s" % (number)
                                board[i][j] = number_str
                                v_numbers_sets[i] |= 1 << number
                                h_numbers_sets[j] |= 1 << number
                                sub_sudoku_numbers_sets[make_key(i, j)] |= 1 << number

                                if i < 8:
                                    if j < 8:
                                        if solveSudokuInner(board, i, j + 1):
                                            return True
                                    else:
                                        if solveSudokuInner(board, i + 1, 0):
                                            return True
                                else:
                                    if j < 8:
                                        if solveSudokuInner(board, i, j + 1):
                                            return True
                                    else:
                                        return True

                                board[i][j] = "."
                                v_numbers_sets[i] &= ~(1 << number)
                                h_numbers_sets[j] &= ~(1 << number)
                                sub_sudoku_numbers_sets[make_key(i, j)] &= ~(1 << number)
                        return False
            return True

        for i in range(0, 9):
            for j in range(0, 9):
                c = board[i][j]
                if c != ".":
                    v_numbers_sets[i] |= 1 << int(c)
                    h_numbers_sets[j] |= 1 << int(c)
                    sub_sudoku_numbers_sets[make_key(i, j)] |= 1 << int(c)

        solveSudokuInner(board, 0, 0)
