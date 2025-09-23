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

import unittest
import leetcode.problem_17_letter_combinations_of_a_phone_number as problem


class TestSolution(unittest.TestCase):
    def test_letterCombinations(self):
        s = problem.Solution()

        result = s.letterCombinations("23")
        result.sort()
        expected = ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
        expected.sort()
        self.assertEqual(result, expected)

        result = s.letterCombinations("")
        result.sort()
        expected = []
        expected.sort()
        self.assertEqual(result, expected)

        result = s.letterCombinations("2")
        result.sort()
        expected = ["a", "b", "c"]
        expected.sort()
        self.assertEqual(result, expected)
