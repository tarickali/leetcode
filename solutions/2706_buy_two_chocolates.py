"""
title : 2706_buy_two_chocolates.py
create : @tarickali 23/12/20
update : @tarickali 23/12/20
"""


class Solution:
    def buyChoco(self, prices: list[int], money: int) -> int:
        first, second = min(prices[0], prices[1]), max(prices[0], prices[1])
        for i in range(2, len(prices)):
            if prices[i] < first:
                first, second = prices[i], first
            elif prices[i] < second:
                second = prices[i]
        cost = first + second
        return money if cost > money else money - cost
