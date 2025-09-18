"""
problem url, https://leetcode.com/problems/regular-expression-matching/description/

Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

Example 1:
Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".

Example 2:
Input:
s = "aa"
p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".

Example 3:
Input:
s = "ab"
p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".

Example 4:
Input:
s = "aab"
p = "c*a*b"
Output: true
Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore, it matches "aab".

Example 5:
Input:
s = "mississippi"
p = "mis*is*p*."
Output: false
"""


class Solution:
    def isMatch(self, text: str, pattern: str) -> bool:
        memo = {}

        def dp(i: int, j: int) -> bool:
            if (i, j) not in memo:
                if j == len(pattern):
                    ans = i == len(text)
                else:
                    first_match = i < len(text) and pattern[j] in {text[i], "."}
                    if j + 1 < len(pattern) and pattern[j + 1] == "*":
                        ans = dp(i, j + 2) or first_match and dp(i + 1, j)
                    else:
                        ans = first_match and dp(i + 1, j + 1)

                memo[i, j] = ans
            return memo[i, j]

        return dp(0, 0)


if __name__ == "__main__":
    s = Solution()
    tests = [
        ["aa", "a", False],
        ["aa", "a*", True],
        ["ab", ".*", True],
        ["aab", "c*a*b", True],
        ["mississippi", "mis*is*p*.", False],
    ]
    for t in tests:
        print(
            "("
            + t[0]
            + ","
            + t[1]
            + ") -> "
            + str(t[2])
            + " -> "
            + str(s.isMatch(t[0], t[1]))
        )
