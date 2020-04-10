"""
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:
Input: 121
Output: true

Example 2:
Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:
Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        s_len = len(s)
        s_len_half = int(s_len / 2)
        for i in range(s_len_half):
            if s[i] != s[s_len - i - 1]:
                return False
        return True

if __name__ == "__main__":
    s = Solution()
    tests = [121, -121, 10]
    for i in tests:
        print(str(i) + "\t->\t" + str(s.isPalindrome(i)))