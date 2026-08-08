"""
https://leetcode.com/problems/multiply-strings/description/

Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

Example 1:
* Input: num1 = "2", num2 = "3"
* Output: "6"

Example 2:
* Input: num1 = "123", num2 = "456"
* Output: "56088"

Constraints:
* 1 <= num1.length, num2.length <= 200
* num1 and num2 consist of digits only.
* Both num1 and num2 do not contain any leading zero, except the number 0 itself.
"""


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        def big_numbers_plus(num1: str, num2: str) -> str:
            short_num = num1
            long_num = num2
            if len(num2) < len(num1):
                short_num = num2
                long_num = num1
            len_long_num = len(long_num)
            len_short_num = len(short_num)

            len_diff = len_long_num - len_short_num
            additional_one = 0
            result = []
            for index in range(len_short_num - 1, -1, -1):
                short_num_char = short_num[index]
                long_num_char = long_num[index + len_diff]
                sum_chars = int(short_num_char) + int(long_num_char) + additional_one
                additional_one = 0
                cur_char = ""
                if sum_chars >= 10:
                    additional_one = 1
                    cur_char = str(sum_chars - 10)
                else:
                    cur_char = str(sum_chars)
                result.append(cur_char)

            for index in range(len_diff - 1, -1, -1):
                sum_chars = int(long_num[index]) + additional_one
                additional_one = 0
                cur_char = ""
                if sum_chars >= 10:
                    additional_one = 1
                    cur_char = str(sum_chars - 10)
                else:
                    cur_char = str(sum_chars)
                result.append(cur_char)

            if additional_one == 1:
                result.append("1")
                additional_one = 0

            result.reverse()
            return "".join(result)

        multi_strings: list[str] = []
        for c1idx, c1 in enumerate(reversed(num1)):
            carry = 0
            if c1 == "0":
                continue
            for c2idx, c2 in enumerate(reversed(num2)):
                tmp_multi = int(c1) * int(c2) + carry
                if c2idx == len(num2) - 1:
                    tmp_result = str(tmp_multi) + "0" * (c1idx + c2idx)
                else:
                    carry = tmp_multi // 10
                    tmp_result = str(tmp_multi % 10) + "0" * (c1idx + c2idx)
                multi_strings.append(tmp_result)

        result = "0"
        for tmp in multi_strings:
            result = big_numbers_plus(result, tmp)

        return result
