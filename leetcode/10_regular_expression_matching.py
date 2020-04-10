"""
Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

Note:

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like . or *.

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
    def isMatch(self, s: str, p: str) -> bool:
        is_in_alter = False
        s_index = 0
        s_len = len(s)
        p_index = 0
        p_len = len(p)
        last_c_p = None

        while p_index < p_len:
            c_p = p[p_index]
            if s_index == s_len:
                return False
            if c_p == '.':
                s_index += 1
                last_c_p = c_p
                p_index += 1
            elif c_p == '*':
                if last_c_p is None:
                    return False
                else:
                    while s_index < s_len:
                        if s[s_index] != last_c_p:
                            break
                        s_index += 1
                    last_c_p = c_p
                    p_index += 1
            else:
                if p[p_index] != s[s_index]:
                    if p_index + 1 == p_len:
                        return False
                    else:
                        if p[p_index + 1] == '*':
                            last_c_p = None
                            p_index += 2
                        else:
                            return False
                else:
                    last_c_p = c_p
                    p_index += 1
                    s_index += 1

        if (s_index + 1) < s_len:
            return False

        return True


if __name__ == "__main__":
    s = Solution()
    tests = [
        ["aa", "a", False],
        ["aa", "a*", True],
        ["ab", ".*", True],
        ["aab", "c*a*b", True],
        ["mississippi", "mis*is*p*.", False]
    ]
    for t in tests:
        print("(" + t[0] + "," + t[1] + ") -> " +
              str(t[2]) + " -> " + str(s.isMatch(t[0], t[1])))
