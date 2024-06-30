"""
title : 0605_can_place_flowers.py
create : @tarickali 23/06/12
update : @tarickali 23/06/12
"""


class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        c = 0
        l = -2
        for i in range(len(flowerbed)):
            if flowerbed[i] == 1:
                c += max((i - l) // 2 - 1, 0)
                l = i
        c += (i - l) // 2
        return c >= n
