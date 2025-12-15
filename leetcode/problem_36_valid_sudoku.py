"""
https://leetcode.com/problems/valid-sudoku/description/?utm_source=LCUS&utm_medium=ip_redirect&utm_campaign=transfer2china

Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
* Each row must contain the digits 1-9 without repetition.
* Each column must contain the digits 1-9 without repetition.
* Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

Note:
* A Sudoku board (partially filled) could be valid but is not necessarily solvable.
* Only the filled cells need to be validated according to the mentioned rules.


Example 1:
Input: board =
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true


Example 2:
Input: board =
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.


Constraints:
* board.length == 9
* board[i].length == 9
* board[i][j] is a digit 1-9 or '.'.
"""


class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        v_numbers_sets: dict[int, list[int]] = {}
        h_numbers_sets: dict[int, list[int]] = {}
        sub_sodoku_numbers_sets: dict[str, list[int]] = {}

        for i in range(9):
            for j in range(9):
                c = board[i][j]
                if c == ".":
                    continue
                else:
                    if v_numbers_sets.get(i) is None:
                        v_numbers_sets[i] = []
                    if c in v_numbers_sets[i]:
                        return False
                    if h_numbers_sets.get(j) is None:
                        h_numbers_sets[j] = []
                    if c in h_numbers_sets[j]:
                        return False
                    sub_sudoku_index = "%s_%s" % (int(i / 3), int(j / 3))
                    if sub_sodoku_numbers_sets.get(sub_sudoku_index) is None:
                        sub_sodoku_numbers_sets[sub_sudoku_index] = []
                    if c in sub_sodoku_numbers_sets[sub_sudoku_index]:
                        return False
                    v_numbers_sets[i].append(c)
                    h_numbers_sets[j].append(c)
                    sub_sodoku_numbers_sets[sub_sudoku_index].append(c)
        return True
