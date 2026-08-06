from typing import List
import unittest
import leetcode.problem_43_multiply_strings as problem


class UnitTestData:
    def __init__(self, num1: str, num2: str, expected: str) -> None:
        self.num1 = num1
        self.num2 = num2
        self.expected = expected


unittest_data = [
    UnitTestData(num1="2", num2="3", expected="6"),
    UnitTestData(num1="123", num2="456", expected="56088"),
]


class TestSolution(unittest.TestCase):
    def test_leetcode_43_multiply(self):
        s = problem.Solution()
        for item in unittest_data:
            retval = s.multiply(item.num1, item.num2)
            self.assertEqual(retval, item.expected)
