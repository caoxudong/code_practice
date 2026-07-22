"""
https://leetcode.com/problems/count-and-say/description/?utm_source=LCUS&utm_medium=ip_redirect&utm_campaign=transfer2china


The count-and-say sequence is a sequence of digit strings defined by the recursive formula:

* countAndSay(1) = "1"
* countAndSay(n) is the run-length encoding of countAndSay(n - 1).

Run-length encoding (RLE) is a string compression method that works by replacing each maximal group of consecutive identical characters with the concatenation of the length of the group followed by the character itself. For example, to compress the string "3322251" we replace "33" with "23", replace "222" with "32", replace "5" with "15", and replace "1" with "11". Thus the compressed string becomes "23321511".

Given a positive integer n, return the nth element of the count-and-say sequence.

Example 1:
* Input: n = 4
* Output: "1211"
* Explanation:
    * countAndSay(1) = "1"
    * countAndSay(2) = RLE of "1" = "11"
    * countAndSay(3) = RLE of "11" = "21"
    * countAndSay(4) = RLE of "21" = "1211"


Example 2:
* Input: n = 1
* Output: "1"
* Explanation:
    * This is the base case.

Constraints:
* 1 <= n <= 30
"""


class Solution:
    def countAndSay(self, n: int) -> str:
        def rle_str(n_str: str) -> str:
            retval = []
            last_c = n_str[0]
            last_c_count = 1
            for i in range(1, len(n_str)):
                c = n_str[i]
                if c == last_c:
                    last_c_count += 1
                else:
                    retval.append(str(last_c_count))
                    retval.append(last_c)
                    last_c = c
                    last_c_count = 1
            retval.append(str(last_c_count))
            retval.append(last_c)
            return "".join(retval)

        count_and_say_map = {1: "1"}
        for i in range(2, n + 1):
            last = count_and_say_map[i - 1]
            last_rle = rle_str(last)
            count_and_say_map[i] = last_rle

        return count_and_say_map[n]
