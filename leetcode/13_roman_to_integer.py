"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.

Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.

Example 1:
Input: "III"
Output: 3

Example 2:
Input: "IV"
Output: 4

Example 3:
Input: "IX"
Output: 9

Example 4:
Input: "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.

Example 5:
Input: "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
"""


class Solution:
    def romanToInt(self, s: str) -> int:
        roman_numerals = {
            'I': (1, ('V', 'X')),
            'V': (5, None),
            'X': (10, ('L', 'C')),
            'L': (50, None),
            'C': (100, ('D', 'M')),
            'D': (500, None),
            'M': (1000, None)
        }
        result_nums = []
        prefix_nums = []
        s_len = len(s)
        for s_index in range(s_len):
            c = s[s_index]
            temp_tuple = roman_numerals[c]
            temp_number = temp_tuple[0]
            if temp_tuple[1] is None:
                result_nums.append(temp_number)
            else:
                if s_index + 1 == s_len:
                    result_nums.append(temp_number)
                elif s[s_index + 1] == temp_tuple[1][0] or s[s_index + 1] == temp_tuple[1][1]:
                    result_nums.append(-1 * temp_number)
                else:
                    result_nums.append(temp_number)
            s_index += 1
        
        result = 0
        for num in result_nums:
            result += num
        
        return result

if __name__ == "__main__":
    test_params = [
        ('III', 3),
        ('IV', 4),
        ('IX', 9),
        ('LVIII', 58),
        ('MCMXCIV', 1994)
    ]

    s = Solution()
    for t in test_params:
        number = s.romanToInt(t[0])
        print(t[0] + "\t" + str(t[1]) + " -> " + str(number))
        assert t[1] == number
