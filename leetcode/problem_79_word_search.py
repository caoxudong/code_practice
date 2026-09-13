"""
https://leetcode.com/problems/word-search/description/


Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.


Example 1:
* Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
* Output: true

Example 2:
* Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
* Output: true

Example 3:
* Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
* Output: false

Constraints:
* m == board.length
* n = board[i].length
* 1 <= m, n <= 6
* 1 <= word.length <= 15
* board and word consists of only lowercase and uppercase English letters.


Follow up: Could you use search pruning to make your solution faster with a larger board?
"""

from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        rows, cols = len(board), len(board[0])
        visited = set()

        def dfs(r, c, k):
            if k == len(word):
                return True

            if not (0 <= r < rows) or not (0 <= c < cols) or (r, c) in visited or board[r][c] != word[k]:
                return False

            visited.add((r, c))
            res = dfs(r + 1, c, k + 1) or dfs(r - 1, c, k + 1) or dfs(r, c + 1, k + 1) or dfs(r, c - 1, k + 1)
            visited.remove((r, c))
            return res

        count = {}
        for c in word:
            count[c] = 1 + count.get(c, 0)

        if count[word[0]] > count[word[-1]]:
            word = word[::-1]

        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True

        return False
