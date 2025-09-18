"""
https://leetcode.com/problems/longest-palindromic-substring/

Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example:

Input: "babad"

Output: "bab"

Note: "aba" is also a valid answer.
 

Example:

Input: "cbbd"

Output: "bb"
"""


class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s is None or len(s) < 1:
            return ''
        start = 0
        end = 0
        for i in range(len(s)):
            len1 = self.expandFromMiddle(s, i, i)
            len2 = self.expandFromMiddle(s, i, i+1)
            lens = max(len1, len2)
            if lens > end - start:
                start = i - (lens-1)//2
                end = i + lens//2
        return s[start:end+1]

    def expandFromMiddle(self, s, left, right):
        if s is None or left > right:
            return 0
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right-left - 1


if __name__ == "__main__":
    solution = Solution()
    str_a = '1234325'
    print(solution.longestPalindrome(str_a))
