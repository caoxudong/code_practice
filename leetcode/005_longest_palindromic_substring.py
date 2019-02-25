"""
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
        new_s = '#' + '#'.join(s) + '#'
        print(new_s)
        radio_length_array = [1] * len(new_s)
        max_right_pos = 0
        pos = 0
        max_radio_length = 0
        print("i\tpos\tmax_radio_length\tmax_right_pos\tradio_length_array[i]")
        for i in range(1, len(new_s)):
            if i < max_right_pos:
                radio_length_array[i] = min(
                    radio_length_array[2 * pos - 1], max_right_pos - 1)
            while i - radio_length_array[i] >= 0 and i + radio_length_array[i] < len(new_s) and new_s[i - radio_length_array[i]] == new_s[i + radio_length_array[i]]:
                radio_length_array[i] += 1
            if radio_length_array[i] + i > max_right_pos:
                max_right_pos = radio_length_array[i] + i - 1
                pos = i
            max_radio_length = max(max_radio_length, radio_length_array[i])
            print(str(i) + "\t" + str(pos) + "\t" + str(max_radio_length) + "\t\t\t" + str(max_right_pos) + "\t\t" + str(radio_length_array[i]))
        print(new_s[pos - max_radio_length - 1: pos + 1], new_s[pos], new_s[pos + 1: pos + max_radio_length - 1])
        return (new_s[pos - max_radio_length - 1: pos + 1] + new_s[pos] + new_s[pos + 1: pos + max_radio_length - 1]).replace('#', '')


if __name__ == "__main__":
    solution = Solution()
    str_a = '1234325'
    print(solution.longestPalindrome(str_a))
