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
        v_numbers_sets: dict[int, set[str]] = {
            0: set([]),
            1: set([]),
            2: set([]),
            3: set([]),
            4: set([]),
            5: set([]),
            6: set([]),
            7: set([]),
            8: set([]),
        }
        h_numbers_sets: dict[int, set[str]] = {
            0: set([]),
            1: set([]),
            2: set([]),
            3: set([]),
            4: set([]),
            5: set([]),
            6: set([]),
            7: set([]),
            8: set([]),
        }
        sub_sudoku_numbers_sets: dict[str, set[str]] = {
            "0_0": set([]),
            "0_1": set([]),
            "0_2": set([]),
            "1_0": set([]),
            "1_1": set([]),
            "1_2": set([]),
            "2_0": set([]),
            "2_1": set([]),
            "2_2": set([]),
        }

        def make_key(i: int, j: int) -> str:
            return "%s_%s" % (int(i/3),int(j/3))

        def validate(board: list[list[str]], i: int, j: int, n: int) -> bool:
            nonlocal v_numbers_sets, h_numbers_sets, sub_sudoku_numbers_sets
            c = "%s"%(n)
            if c in v_numbers_sets[i] or c in h_numbers_sets[j]:
                return False
            sub_sudoku = sub_sudoku_numbers_sets.get(make_key(i,j))
            if sub_sudoku is not None and c in set(sub_sudoku):
                return False
            return True

        def solveSudokuInner(board: list[list[str]]) -> bool:
            nonlocal v_numbers_sets, h_numbers_sets, sub_sudoku_numbers_sets
            for i in range(0,9):
                for j in range(0,9):
                    c = board[i][j]
                    if c == ".":
                        for n in range (0, 9):
                            number = n+1
                            if validate(board, i, j, number):
                                number_str = "%s"%(number)
                                board[i][j] = number_str
                                v_numbers_sets[i].add(number_str)
                                h_numbers_sets[j].add(number_str)
                                sub_sudoku_numbers_sets[make_key(i,j)].add(number_str)
                                if solveSudokuInner(board):
                                    return True
                                board[i][j] = "."
                                v_numbers_sets[i].remove(number_str)
                                h_numbers_sets[j].remove(number_str)
                                sub_sudoku_numbers_sets[make_key(i,j)].remove(number_str)
                        return False
            return True
        
        for i in range(0,9):
            for j in range(0,9):
                c = board[i][j]
                if c != ".":
                    v_numbers_sets[i].add(c)
                    h_numbers_sets[j].add(c)
                    sub_sudoku_numbers_sets[make_key(i,j)].add(c)

        solveSudokuInner(board)
        

                
