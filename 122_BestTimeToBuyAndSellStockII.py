# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/
#
# Say you have an array for which the ith element is the price of a given stock on day i.
#
# Design an algorithm to find the maximum profit. You may complete as many transactions as you like
# (ie, buy one and sell one share of the stock multiple times). However, you may not engage in
# multiple transactions at the same time (ie, you must sell the stock before you buy again).

class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profits = 0
        for i in range(len(prices) - 1):
            if prices[i + 1] > prices[i]:
                profits += prices[i + 1] - prices[i]
        return profits

        # return sum(y - x for x, y in zip(prices[:-1], prices[1:]) if y > x)
