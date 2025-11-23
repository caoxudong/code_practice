"""
https://leetcode.com/problems/longest-valid-parentheses/?utm_source=LCUS&utm_medium=ip_redirect&utm_campaign=transfer2china


Given a string containing just the characters '(' and ')', return the length of the longest valid (well-formed) parentheses substring.


Example 1:
* Input: s = "(()"
* Output: 2
* Explanation: The longest valid parentheses substring is "()".

Example 2:
* Input: s = ")()())"
* Output: 4
* Explanation: The longest valid parentheses substring is "()()".

Example 3:
* Input: s = ""
* Output: 0

Constraints:
* 0 <= s.length <= 3 * 104
* s[i] is '(', or ')'.

"""


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack: list[int] = []
        len_s = len(s)
        left_parenthese = "("
        right_parenthese = ")"

        for i in range(len_s):
            if s[i] == left_parenthese:
                stack.append(i)
            elif s[i] == right_parenthese:
                if len(stack) == 0:
                    stack.append(i)
                    continue
                if s[stack[-1]] == left_parenthese:
                    stack.pop()
                else:
                    stack.append(i)
            else:
                # illegal character
                return 0

        if len(stack) == 0:
            return len_s

        len_max = 0
        last_index = -1
        for index in stack:
            len_max = max(len_max, index - last_index - 1)
            last_index = index
        len_max = max(len_max, len_s - 1 - last_index)
        return len_max
