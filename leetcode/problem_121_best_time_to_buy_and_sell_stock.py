"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/


You are given an array `prices` where `prices[i]` is the price of a given stock on the `ith` day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.



Example 1:
* Input: prices = [7,1,5,3,6,4]
* Output: 5
* Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
* Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2:
* Input: prices = [7,6,4,3,1]
* Output: 0
* Explanation: In this case, no transactions are done and the max profit = 0.


Constraints:
* 1 <= prices.length <= 105
* 0 <= prices[i] <= 104
"""

from turtle import right


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        prices_count = len(prices)
        if prices_count <= 1:
            return 0
        elif prices_count == 2:
            return max(0, prices[1] - prices[0])

        max_profit_buy_index = 0
        max_profit_sell_index = 1
        max_profit = max(
            0, prices[max_profit_sell_index] - prices[max_profit_buy_index]
        )

        buy_index = max_profit_buy_index
        sell_index = max_profit_sell_index

        for tmp_index in range(1, prices_count):
            if prices[tmp_index] < prices[buy_index]:
                if max_profit < prices[sell_index] - prices[buy_index]:
                    max_profit_buy_index = buy_index
                    max_profit_sell_index = sell_index
                    max_profit = (
                        prices[max_profit_sell_index] - prices[max_profit_buy_index]
                    )

                buy_index = tmp_index
                sell_index = tmp_index
                continue

            if prices[tmp_index] > prices[sell_index]:
                sell_index = tmp_index
                continue

        if max_profit < prices[sell_index] - prices[buy_index]:
            max_profit_buy_index = buy_index
            max_profit_sell_index = sell_index
            max_profit = prices[max_profit_sell_index] - prices[max_profit_buy_index]

        print(
            "sell_index={}, sell={}, buy_index={}, buy={}, profit={}".format(
                max_profit_sell_index,
                prices[max_profit_sell_index],
                max_profit_buy_index,
                prices[max_profit_buy_index],
                prices[max_profit_sell_index] - prices[max_profit_buy_index],
            )
        )

        return max_profit
