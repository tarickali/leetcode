"""
title : 2610_convert_an_array_into_a_2d_array_with_conditions.py
create : @tarickali 24/01/01
update : @tarickali 24/01/01
"""

from collections import Counter


class Solution:
    def findMatrix(self, nums: list[int]) -> list[list[int]]:
        counts = Counter(nums).most_common()
        table = [[] for _ in range(counts[0][1])]

        for num, cnt in counts:
            for i in range(cnt):
                table[i].append(num)

        return table
