"""
https://leetcode.com/problems/generate-parentheses/description/

Given `n` pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:
* Input: n = 3
* Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:
* Input: n = 1
* Output: ["()"]

Constraints:
* 1 <= n <= 8
"""


class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        stack = []
        res = []

        def backtrack(openN, closedN):
            if openN == closedN == n:
                res.append("".join(stack))
                return

            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN)
                stack.pop()

            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()

        backtrack(0, 0)
        return res
