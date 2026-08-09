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
        class isMatchWithoutStarMarkRetval:
            def __init__(self, matched: bool, need_backtrace: bool, pointer_s: int, pointer_p: int, step: int):
                self.matched = matched
                self.need_backtrace = need_backtrace
                self.pointer_s = pointer_s
                self.pointer_p = pointer_p
                self.step = step

        def isMatchWithoutStarMark(
            s: str, pointer_s: int, limit_s_exclude: int, p: str, pointer_p: int, limit_p_exclude: int, step: int
        ) -> isMatchWithoutStarMarkRetval:
            question_mark = "?"
            star_mark = "*"

            while pointer_s != limit_s_exclude and pointer_p != limit_p_exclude:
                c = s[pointer_s]
                w = p[pointer_p]
                if w == star_mark:
                    return isMatchWithoutStarMarkRetval(
                        matched=False, need_backtrace=True, pointer_s=pointer_s, pointer_p=pointer_p, step=step
                    )
                if w == question_mark:
                    pointer_p += step
                    pointer_s += step
                    continue
                if w != question_mark and w != star_mark and w != c:
                    return isMatchWithoutStarMarkRetval(
                        matched=False, need_backtrace=False, pointer_s=pointer_s, pointer_p=pointer_p, step=step
                    )
                pointer_p += 1
                pointer_s += 1

            if pointer_s == limit_s_exclude == pointer_p == limit_p_exclude:
                return isMatchWithoutStarMarkRetval(
                    matched=True, need_backtrace=False, pointer_s=pointer_s, pointer_p=pointer_p, step=step
                )
            return isMatchWithoutStarMarkRetval(
                matched=False, need_backtrace=False, pointer_s=pointer_s, pointer_p=pointer_p, step=step
            )

        len_s = len(s)
        len_p = len(p)

        pointer_s = 0
        pointer_p = 0
        limit_s_exclude = len_s
        limit_p_exclude = len_p
        step = 1

        while True:
            matchRetval = isMatchWithoutStarMark(s, pointer_s, limit_s_exclude, p, pointer_p, limit_p_exclude, step)
            if matchRetval.matched:
                return True
            else:
                if not matchRetval.need_backtrace:
                    return False
                pointer_s = limit_s_exclude - step
                pointer_p = limit_p_exclude - step
                limit_s_exclude = matchRetval.pointer_s
                limit_p_exclude = matchRetval.pointer_p
                step *= -1
                continue
