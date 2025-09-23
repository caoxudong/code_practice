import unittest
import others.big_numbers_compute as problem


class UnitTestData:
    def __init__(self, num1: str = "", num2: str = "", expected: str = ""):
        self.num1 = num1
        self.num2 = num2
        self.expected = expected


unittest_data = [
    UnitTestData(num1="1", num2="99", expected="100"),
    UnitTestData(num1="1", num2="9", expected="10"),
    UnitTestData(num1="199", num2="12342423", expected="12342622"),
    UnitTestData(
        num1="19999999999999999999999999999999",
        num2="12342423",
        expected="20000000000000000000000012342422",
    ),
    UnitTestData(
        num1="1999999999999999999999999999999919999999999999999999999999999999",
        num2="9999999999999999999999999999999919999999999999999999999999999999",
        expected="11999999999999999999999999999999839999999999999999999999999999998",
    ),
]


class TestSolution(unittest.TestCase):
    def test_big_numbers_plus(self):
        s = problem.Solution()
        for item in unittest_data:
            result = s.big_numbers_plus(item.num1, item.num2)
            self.assertEqual(result, item.expected)
