"""
title : 0322_coin_change.py
create : @tarickali 23/05/13
update : @tarickali 23/05/13
"""


class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        memo = {}  # num -> amount of coins to num
        memo[0] = 0
        for num in range(1, amount + 1):
            best = min(memo.get(num - coin, float("inf")) for coin in coins)
            if best != float("inf"):
                memo[num] = best + 1
        return memo.get(amount, -1)
