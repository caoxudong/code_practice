"""
https://leetcode.com/problems/wildcard-matching/description/


Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*' where:

* '?' Matches any single character.
* '*' Matches any sequence of characters (including the empty sequence).

The matching should cover the entire input string (not partial).

Example 1:
* Input: s = "aa", p = "a"
* Output: false
* Explanation: "a" does not match the entire string "aa".

Example 2:
* Input: s = "aa", p = "*"
* Output: true
* Explanation: '*' matches any sequence.

Example 3:
* Input: s = "cb", p = "?a"
* Output: false
* Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.

Constraints:
* 0 <= s.length, p.length <= 2000
* s contains only lowercase English letters.
* p contains only lowercase English letters, '?' or '*'.
"""


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        si, pi, match, star = 0, 0, 0, -1
        sn, pn = len(s), len(p)
        while si < sn:
            if pi < pn and (p[pi] == "?" or p[pi] == s[si]):
                si += 1
                pi += 1
            elif pi < pn and p[pi] == "*":
                star = pi
                match = si
                pi += 1
            elif star != -1:
                pi = star + 1
                match += 1
                si = match
            else:
                return False
        while pi < pn and p[pi] == "*":
            pi += 1
        return pi == pn
