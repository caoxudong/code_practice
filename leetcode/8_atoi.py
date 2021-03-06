"""
Implement atoi which converts a string to an integer.

The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned.

Note:

Only the space character ' ' is considered as whitespace character.
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−2^31,  2^31 − 1]. If the numerical value is out of the range of representable values, INT_MAX (2^31 − 1) or INT_MIN (−2^31) is returned.

Example 1:
Input: "42"
Output: 42

Example 2:
Input: "   -42"
Output: -42
Explanation: The first non-whitespace character is '-', which is the minus sign. Then take as many numerical digits as possible, which gets 42.

Example 3:
Input: "4193 with words"
Output: 4193
Explanation: Conversion stops at digit '3' as the next character is not a numerical digit.

Example 4:
Input: "words and 987"
Output: 0
Explanation: The first non-whitespace character is 'w', which is not a numerical digit or a +/- sign. Therefore no valid conversion could be performed.

Example 5:
Input: "-91283472332"
Output: -2147483648
Explanation: The number "-91283472332" is out of the range of a 32-bit signed integer. Thefore INT_MIN (−231) is returned.
"""

class Solution:
    def myAtoi(self, s):
        all_signs = "+-"
        all_numbers = "0123456789"
        valid_chars = all_signs + all_numbers
        min_abs = 2 << 30
        min_abs_str = str(min_abs)
        max_abs = min_abs -1 
        max_abs_str = str(max_abs)

        s = s.strip(" ")
        if len(s) == 0:
            return 0

        sign = 0
        first_index = 0
        if s[0] == "-":
            sign = 1
            first_index = 1
        if s[0] == "+":
            sign = 0
            first_index = 1
        s = s[first_index:]

        first_index = 0
        last_index = 0
        for c in s:
            if c not in all_numbers:
                break
            last_index += 1
        if last_index == first_index:
            return 0
        s = s[first_index:last_index]
        s = s.strip(" ")
        if len(s) == 0:
            return 0
        
        result = 0
        index = 0
        len_s = len(s)
        for c in s:
            result = result * 10 + int(c)
        if sign > 0:
            if result > min_abs:
                result = -1 * min_abs
            else:
                result = -1 * result
        else:
            if result > max_abs:
                result = max_abs
        return result



if __name__ == "__main__":
    s = Solution()
    a = "3.15"
    print(s.myAtoi(a))
    a = "123123f"
    print(s.myAtoi(a))
    a = "-123123"
    print(s.myAtoi(a))
    a = "12312332fsfsa"
    print(s.myAtoi(a))
    a = "vsvs123123f"
    print(s.myAtoi(a))
    a = "   fs123123   sd"
    print(s.myAtoi(a))
    a = "123312312312312334123"
    print(s.myAtoi(a))

