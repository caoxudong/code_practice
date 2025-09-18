"""
https://leetcode.com/problems/letter-combinations-of-a-phone-number/

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

A mapping of digits to letters is given below.

1 -> None, meaning no letters
2 -> abc
3 -> def
4 -> ghi
5 -> jkl
6 -> mno
7 -> pqrs
8 -> tuv
9 -> xyz


Example 1:
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Example 2:
Input: digits = ""
Output: []

Example 3:
Input: digits = "2"
Output: ["a","b","c"]

Constraints:
* 0 <= digits.length <= 4
* digits[i] is a digit in the range ['2', '9'].
"""

from operator import le
from xml.dom import minidom


class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        mappings = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }

        if len(digits) == 0:
            return []
        elif len(digits) == 1:
            return mappings[digits[0]]

        result = mappings[digits[0]]

        for i in range(1, len(digits)):
            c = digits[i]
            mid_result = []
            for letter in mappings[c]:
                for item in result:
                    mid_result.append(item + letter)
            result = mid_result
        return result
