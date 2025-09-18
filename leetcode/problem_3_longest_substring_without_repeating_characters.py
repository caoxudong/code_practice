"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/

Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

"""

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        chars_indexes = {}
        begin_index = 0
        max_length = 0
        for i, char in enumerate(s):
            if char in chars_indexes and begin_index <= chars_indexes[char] :
                begin_index = chars_indexes[char] + 1
            else :
                max_length = max(max_length, i - begin_index + 1)
            chars_indexes[char] = i
        return max_length

if __name__ == '__main__':
    obj = Solution()
    strings = ['abcdefd', 'abcabcbb', 'bbbb', 'pwwkew']
    for string in strings:
        print(obj.lengthOfLongestSubstring(string))