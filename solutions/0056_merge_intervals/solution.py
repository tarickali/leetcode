"""
title : 0056_merge_intervals.py
create : @tarickali 23/11/13
update : @tarickali 23/11/13
"""


class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key=lambda x: x[0])

        merged = [intervals[0]]
        for i in range(1, len(intervals)):
            interval = intervals[i]
            if interval[0] <= merged[-1][1]:
                merged[-1][1] = max(merged[-1][1], interval[1])
            else:
                merged.append(interval)
        return merged
