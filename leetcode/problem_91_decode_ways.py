"""
https://leetcode.com/problems/decode-ways/description/


You have intercepted a secret message encoded as a string of numbers. The message is decoded via the following mapping:
* "1" -> 'A'
* "2" -> 'B'
* ...
* "25" -> 'Y'
* "26" -> 'Z'

However, while decoding the message, you realize that there are many different ways you can decode the message because some codes are contained in other codes ("2" and "5" vs "25").

For example, "11106" can be decoded into:
* "AAJF" with the grouping (1, 1, 10, 6)
* "KJF" with the grouping (11, 10, 6)
* The grouping (1, 11, 06) is invalid because "06" is not a valid code (only "6" is valid).

Note: there may be strings that are impossible to decode.

Given a string s containing only digits, return the number of ways to decode it. If the entire string cannot be decoded in any valid way, return 0.

The test cases are generated so that the answer fits in a 32-bit integer.

Example 1:
* Input: s = "12"
* Output: 2
* Explanation: "12" could be decoded as "AB" (1 2) or "L" (12).

Example 2:
* Input: s = "226"
* Output: 3
* Explanation: "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

Example 3:
* Input: s = "06"
* Output: 0
* Explanation: "06" cannot be mapped to "F" because of the leading zero ("6" is different from "06"). In this case, the string is not a valid encoding, so return 0.

Constraints:
* 1 <= s.length <= 100
* s contains only digits and may contain leading zero(s).
"""

from operator import index


class Solution:
    def numDecodings(self, s: str) -> int:
        class DataTuple:
            def __init__(self, index: int, subStr: str, endFlag: bool):
                self.index = index
                self.subStr = subStr
                self.endFlag = endFlag

        valid_number_set = set()
        for i in range(1, 27):
            valid_number_set.add(str(i))

        if len(s) == 1:
            if s[0] in valid_number_set:
                return 1
            else:
                return 0

        len_s = len(s)
        p_s = 0
        stack = [DataTuple(p_s + 1, s[0], False)]
        if len(s) == 2:
            stack.append(DataTuple(p_s + 2, s[0:2], True))
        else:
            stack.append(DataTuple(p_s + 2, s[0:2], False))

        retval = 0
        while len(stack) > 0:
            tmp_node_data = stack.pop()
            if tmp_node_data.endFlag == True:
                if tmp_node_data.subStr not in valid_number_set:
                    continue

                retval += 1
            else:
                if tmp_node_data.subStr not in valid_number_set:
                    continue

                if tmp_node_data.index >= len_s:
                    raise Exception("wrong index and endFlag combo")
                else:
                    if tmp_node_data.index + 2 <= len_s:
                        if tmp_node_data.index + 2 == len_s:
                            stack.append(
                                DataTuple(
                                    tmp_node_data.index + 2, s[tmp_node_data.index : tmp_node_data.index + 2], True
                                )
                            )
                        else:
                            stack.append(
                                DataTuple(
                                    tmp_node_data.index + 2, s[tmp_node_data.index : tmp_node_data.index + 2], False
                                )
                            )
                    if tmp_node_data.index + 1 <= len_s:
                        if tmp_node_data.index + 1 == len_s:
                            stack.append(
                                DataTuple(
                                    tmp_node_data.index + 1, s[tmp_node_data.index : tmp_node_data.index + 1], True
                                )
                            )
                        else:
                            stack.append(
                                DataTuple(
                                    tmp_node_data.index + 1, s[tmp_node_data.index : tmp_node_data.index + 1], False
                                )
                            )

        return retval
