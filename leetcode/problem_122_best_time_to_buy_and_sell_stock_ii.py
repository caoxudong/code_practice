"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/

You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can sell and buy the stock multiple times on the same day, ensuring you never hold more than one share of the stock.

Find and return the maximum profit you can achieve.


Example 1:
* Input: prices = [7,1,5,3,6,4]
* Output: 7
* Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4. Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3. Total profit is 4 + 3 = 7.

Example 2:
* Input: prices = [1,2,3,4,5]
* Output: 4
* Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4. Total profit is 4.

Example 3:
* Input: prices = [7,6,4,3,1]
* Output: 0
* Explanation: There is no way to make a positive profit, so we never buy the stock to achieve the maximum profit of 0.

Constraints:
* 1 <= prices.length <= 3 * 10^4
* 0 <= prices[i] <= 104
"""


class Solution:
    def maxProfit(self, prices: list[int]) -> int:

        prices_count = len(prices)
        if prices_count <= 1:
            return 0
        elif prices_count == 2:
            return max(0, prices[1] - prices[0])

        max_profit_buy_index = 0
        max_profit_sell_index = 1
        max_profit = max(0, prices[max_profit_sell_index] - prices[max_profit_buy_index])

        buy_index = max_profit_buy_index
        sell_index = max_profit_sell_index

        for tmp_index in range(1, prices_count):
            if prices[tmp_index] < prices[buy_index]:
                if max_profit < prices[sell_index] - prices[buy_index]:
                    max_profit_buy_index = buy_index
                    max_profit_sell_index = sell_index
                    max_profit = prices[max_profit_sell_index] - prices[max_profit_buy_index]

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
