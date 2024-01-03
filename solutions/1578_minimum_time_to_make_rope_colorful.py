"""
title : 1578_minimum_time_to_make_rope_colorful.py
create : @tarickali 24/01/02
update : @tarickali 24/01/02
"""


class Solution:
    def minCost(self, colors: str, neededTime: list[int]) -> int:
        total_time = 0
        i = 0
        while i < len(colors):
            color_time = neededTime[i]
            worst_time = neededTime[i]
            j = i + 1
            while j < len(colors) and colors[i] == colors[j]:
                color_time += neededTime[j]
                worst_time = max(worst_time, neededTime[j])
                j += 1
            total_time += color_time - worst_time
            i = j

        return total_time
