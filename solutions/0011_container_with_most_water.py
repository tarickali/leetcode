"""
title : 0011_container_with_most_water.py
create : @tarickali 23/05/31
update : @tarickali 23/05/31
"""


class Solution:
    def maxArea(self, height: list[int]) -> int:
        i = 0
        j = len(height) - 1
        best = 0

        while i < j:
            area = min(height[i], height[j]) * (j - i)
            best = max(best, area)
            if height[i] > height[j]:
                j -= 1
            else:
                i += 1

        return best
