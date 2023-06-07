"""
title : 0875_koko_eating_bananas.py
create : @tarickali 23/06/07
update : @tarickali 23/06/07
"""

import math


class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        def can_eat(k: int) -> bool:
            if k == 0:
                return False
            return sum(math.ceil(pile / k) for pile in piles) <= h

        i = 0
        j = max(piles)

        best = j
        while i <= j:
            k = i + (j - i) // 2
            if can_eat(k):
                best = k
                j = k - 1
            else:
                i = k + 1
        return best
