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


class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def validate(board: list[list[str]], i: int, j: int, n: int) -> bool:
            c = "%s"%(n+1)
            for a in range(0,9):
                if c == board[i][a] or c == board[a][j]:
                    return False
            for a in range(0,3):
                for b in range(0,3):
                    if board[int(i/3)*3+a][int(j/3)*3+b] == c:
                        return False
            return True

        def solveSudokuInner(board: list[list[str]]) -> bool:
            for i in range(0,9):
                for j in range(0,9):
                    c = board[i][j]
                    if c == ".":
                        for n in range (0, 9):
                            if validate(board, i, j, n):
                                board[i][j] = "%s"%(n+1)
                                if solveSudokuInner(board):
                                    return True
                                board[i][j] = "."
                        return False
            return True
        
        solveSudokuInner(board)
        

                
