from math import exp
import unittest
import leetcode.problem_122_best_time_to_buy_and_sell_stock_ii as problem


class UnitTestData:
    def __init__(self, prices: list[int] = [], expected: int = 0):
        self.prices = prices
        self.expected = expected


unittest_data = [
    UnitTestData(prices=[7, 1, 5, 3, 6, 4], expected=7),
    UnitTestData(prices=[1, 2, 3, 4, 5], expected=4),
]


class TestSolution(unittest.TestCase):
    def test_leetcode_122_maxProfit(self):
        s = problem.Solution()
        for item in unittest_data:
            result = s.maxProfit(item.prices)
            self.assertEqual(result, item.expected)
