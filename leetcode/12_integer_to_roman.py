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

Given an integer, convert it to a roman numeral. Input is guaranteed to be within the range from 1 to 3999.

Example 1:
Input: 3
Output: "III"

Example 2:
Input: 4
Output: "IV"

Example 3:
Input: 9
Output: "IX"

Example 4:
Input: 58
Output: "LVIII"
Explanation: L = 50, V = 5, III = 3.

Example 5:
Input: 1994
Output: "MCMXCIV"
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
"""


class Solution:
    def intToRoman(self, num: int) -> str:
        roman_numerals = [
            (1000, 'M', None),
            (100,  'C', {9: 'CM', 8: 'DCCC',
                         7: 'DCC', 6: 'DC', 5: 'D', 4: 'CD'}),
            (10,   'X', {9: 'XC', 8: 'LXXX',
                         7: 'LXX', 6: 'LX', 5: 'L', 4: 'XL'}),
            (1,    'I', {9: 'IX', 8: 'VIII',
                         7: 'VII', 6: 'VI', 5: 'V', 4: 'IV'})
        ]
        roman_numerals_len = len(roman_numerals)

        result_numerals = []
        roman_numerals_index = 0
        remainder = num
        while True:
            if roman_numerals_index >= roman_numerals_len:
                break
            quotient = remainder // roman_numerals[roman_numerals_index][0]
            if quotient > 0:
                if roman_numerals[roman_numerals_index][2] is None:
                    result_numerals.append(
                        roman_numerals[roman_numerals_index][1] * quotient)
                else:
                    if roman_numerals[roman_numerals_index][2].get(quotient) is None:
                        result_numerals.append(
                            roman_numerals[roman_numerals_index][1] * quotient)
                    else:
                        result_numerals.append(
                            roman_numerals[roman_numerals_index][2][quotient])
            remainder = remainder % roman_numerals[roman_numerals_index][0]
            roman_numerals_index += 1

        result = "".join(result_numerals)
        return result


if __name__ == "__main__":
    test_params = [
        (3, "III"),
        (4, "IV"),
        (9, "IX"),
        (58, "LVIII"),
        (1994, "MCMXCIV"),
        (60, "LX")
    ]
    s = Solution()
    for test in test_params:
        result = s.intToRoman(test[0])
        print((test, result))
        assert test[1] == s.intToRoman(test[0])
