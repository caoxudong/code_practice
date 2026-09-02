"""
https://leetcode.com/problems/plus-one/description/


Given two binary strings a and b, return their sum as a binary string.



Example 1:
* Input: a = "11", b = "1"
* Output: "100"

Example 2:
* Input: a = "1010", b = "1011"
* Output: "10101"

Constraints:
* 1 <= a.length, b.length <= 10^4
* a and b consist only of '0' or '1' characters.
* Each string does not contain leading zeros except for the zero itself.
"""


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        min_length = min(len(a), len(b))
        result_list = []
        carry = 0
        for i in range(min_length):
            if a[-1 - i] == "1" and b[-1 - i] == "1":
                if carry == 1:
                    result_list.append("1")
                else:
                    result_list.append("0")
                carry = 1
            elif a[-1 - i] == "1" and b[-1 - i] == "0":
                if carry == 1:
                    result_list.append("0")
                    carry = 1
                else:
                    result_list.append("1")
                    carry = 0
            elif a[-1 - i] == "0" and b[-1 - i] == "1":
                if carry == 1:
                    result_list.append("0")
                    carry = 1
                else:
                    result_list.append("1")
                    carry = 0
            else:
                if carry == 1:
                    result_list.append("1")
                    carry = 0
                else:
                    result_list.append("0")
                    carry = 0
        if len(a) > min_length:
            for i in range(len(a) - min_length):
                if a[-1 - min_length - i] == "1":
                    if carry == 1:
                        result_list.append("0")
                        carry = 1
                    else:
                        result_list.append("1")
                        carry = 0
                else:
                    if carry == 1:
                        result_list.append("1")
                        carry = 0
                    else:
                        result_list.append("0")
                        carry = 0
        elif len(b) > min_length:
            for i in range(len(b) - min_length):
                if b[-1 - min_length - i] == "1":
                    if carry == 1:
                        result_list.append("0")
                        carry = 1
                    else:
                        result_list.append("1")
                        carry = 0
                else:
                    if carry == 1:
                        result_list.append("1")
                        carry = 0
                    else:
                        result_list.append("0")
                        carry = 0
        if carry == 1:
            result_list.append("1")
        result_list.reverse()
        retval = "".join(result_list)
        return retval
