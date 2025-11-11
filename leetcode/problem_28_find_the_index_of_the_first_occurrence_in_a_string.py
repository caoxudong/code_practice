"""
https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/

Given two strings `needle` and `haystack`, return the index of the first occurrence of `needle` in `haystack`, or `-1` if `needle` is not part of `haystack`.


Example 1:
* Input: haystack = "sadbutsad", needle = "sad"
* Output: 0
* Explanation: "sad" occurs at index 0 and 6.The first occurrence is at index 0, so we return 0.

Example 2:
* Input: haystack = "leetcode", needle = "leeto"
* Output: -1
* Explanation: "leeto" did not occur in "leetcode", so we return -1.

Constraints:
* 1 <= haystack.length, needle.length <= 104
* haystack and needle consist of only lowercase English characters.
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i_haystack: int = 0
        len_haystack = len(haystack)
        len_needle = len(needle)
        if len_needle > len_haystack:
            return -1
        while i_haystack < len_haystack:
            i_needle = 0
            tmp_i_haystack = i_haystack
            while (
                i_needle < len_needle
                and i_needle < len_haystack
                and tmp_i_haystack < len_haystack
            ):
                if needle[i_needle] == haystack[tmp_i_haystack]:
                    i_needle += 1
                    tmp_i_haystack += 1
                    continue
                else:
                    break
            if i_needle == len_needle:
                return i_haystack
            i_haystack += 1
        return -1
