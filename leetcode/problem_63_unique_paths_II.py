"""
https://leetcode.com/problems/unique-paths-ii/description/


You are given an m x n integer array grid. There is a robot initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

An obstacle and space are marked as 1 or 0 respectively in grid. A path that the robot takes cannot include any square that is an obstacle.

Return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The testcases are generated so that the answer will be less than or equal to 2 * 10^9.


Example 1:
* Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
* Output: 2
* Explanation: There is one obstacle in the middle of the 3x3 grid above.
    * There are two ways to reach the bottom-right corner:
    * 1. Right -> Right -> Down -> Down
    * 2. Down -> Down -> Right -> Right

Example 2:
* Input: obstacleGrid = [[0,1],[0,0]]
* Output: 1

Constraints:
* m == obstacleGrid.length
* n == obstacleGrid[i].length
* 1 <= m, n <= 100
* obstacleGrid[i][j] is 0 or 1.
"""

from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[-1] * n for _ in range(m)]

        def solve(i, j):

            # Outside the grid
            if i < 0 or j < 0:
                return 0

            # Obstacle
            if obstacleGrid[i][j] == 1:
                return 0

            # Starting cell
            if i == 0 and j == 0:
                return 1

            # Already calculated
            if dp[i][j] != -1:
                return dp[i][j]

            up = solve(i - 1, j)
            left = solve(i, j - 1)

            dp[i][j] = up + left

            return dp[i][j]

        return solve(m - 1, n - 1)
