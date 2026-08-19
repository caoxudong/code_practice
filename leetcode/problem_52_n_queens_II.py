"""
https://leetcode.com/problems/n-queens-ii/description/


The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return the number of distinct solutions to the n-queens puzzle.

Example 1:
* Input: n = 4
* Output: 2
* Explanation: There are two distinct solutions to the 4-queens puzzle as shown.

Example 2:
* Input: n = 1
* Output: 1


Constraints:
* 1 <= n <= 9
"""

from typing import List


class Solution:
    def totalNQueens(self, n: int) -> int:
        # Helper function that implements backtracking algorithm
        def backtrack(r):
            # Base case: if we've placed queens in all rows successfully
            if r == n:
                # Create a deep copy of current board state
                copy = board[:]
                sol = []
                # Convert each row to string representation
                for c in copy:
                    sol.append("".join(c[:]))
                # Add valid solution to final answer list
                ans.append(sol)
                return

            # Try placing queen in each column of current row
            for c in range(n):
                # Skip if column is attacked by another queen:
                # - placedCol: same column
                # - placedPos: same positive diagonal (r + c)
                # - placedNeg: same negative diagonal (r - c)
                if c in placedCol or r + c in placedPos or r - c in placedNeg:
                    continue

                # Place queen and mark attacked positions
                board[r][c] = "Q"
                placedCol.add(c)
                placedPos.add(r + c)
                placedNeg.add(r - c)

                # Recursively try to place queens in next rows
                backtrack(r + 1)

                # Backtrack: remove queen and unmark attacked positions
                board[r][c] = "."
                placedCol.remove(c)
                placedPos.remove(r + c)
                placedNeg.remove(r - c)

        # Initialize empty chess board
        board = [["."] * n for _ in range(n)]

        # Sets to track attacked positions:
        placedCol = set()  # Columns with queens
        placedPos = set()  # Positive diagonals (r + c)
        placedNeg = set()  # Negative diagonals (r - c)
        ans = []  # Store all valid solutions

        # Start backtracking from row 0
        backtrack(0)

        ans_set = set()
        for tmp in ans:
            ans_set.add(tuple(tmp))

        return len(ans_set)
