from typing import List

"""
PROBLEM

You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.

Find and return the maximum profit you can achieve.

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Total profit is 4 + 3 = 7.
Example 2:

Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Total profit is 4.
Example 3:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: There is no way to make a positive profit, so we never buy the stock to achieve the maximum profit of 0.
"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        profit = 0

        dp = []
        min_so_far = prices[0]

        for i, price in enumerate(prices):
            min_so_far = min(min_so_far, price)
            dp.insert(i, price - min_so_far)

            # if price on next day is lower - sell it
            if i + 1 < len(prices) and prices[i + 1] < price:
                transaction_profit = max(dp)
                # see if it makes sense to sell it
                if transaction_profit > 0:
                    profit += transaction_profit
                    min_so_far = prices[i + 1]
                    dp = []
            # last day, let's see if we can make profit
            elif i == len(prices) - 1:
                transaction_profit = max(dp)
                # see if it makes sense to sell it
                if transaction_profit > 0:
                    profit += transaction_profit
                    dp = []

        if profit == 0:
            profit = max(dp)

        return profit
