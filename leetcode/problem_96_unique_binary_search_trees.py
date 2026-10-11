"""
https://leetcode.com/problems/unique-binary-search-trees/description/

Given an integer n, return the number of structurally unique BST's (binary search trees) which has exactly n nodes of unique values from 1 to n.


Example 1:
    1     1           2          3          3
     \     \         / \        /          /
      3     2       1   3      2          1
     /       \                /            \
    2         3              1              2
* Input: n = 3
* Output: 5

Example 2:
* Input: n = 1
* Output: 1

Constraints:
* 1 <= n <= 19
"""


class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0] * (n+1)
        dp[0] = 1
        for i in range(1, n+1):
            for j in range(i):
                dp[i] += dp[j] * dp[i- 1 - j]
        return dp[n]
