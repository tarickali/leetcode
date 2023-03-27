"""
title : 0121_best_time_to_buy_and_sell_stock.py
create : @tarickali 23/03/27
update : @tarickali 23/03/27
"""


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        minimum_price = float("inf")
        maximum_profit = 0
        for price in prices:
            minimum_price = min(minimum_price, price)
            maximum_profit = max(maximum_profit, price - minimum_price)
        return maximum_profit
