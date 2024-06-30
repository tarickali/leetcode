"""
title : 0057_insert_interval.py
create : @tarickali 23/06/15
update : @tarickali 23/06/15
"""


class Solution:
    def insert(
        self, intervals: list[list[int]], newInterval: list[int]
    ) -> list[list[int]]:
        def overlap(a: list[int], b: list[int]) -> bool:
            return a[0] <= b[0] <= a[1] or b[0] <= a[0] <= b[1]

        def join(a: list[int], b: list[int]) -> list[int]:
            return [min(a[0], b[0]), max(a[1], b[1])]

        mergedIntervals = []
        union = [0, 0]
        overlapping = False
        merged = False
        for i, interval in enumerate(intervals):
            if not overlapping:
                if not overlap(interval, newInterval):
                    if newInterval[0] < interval[0]:
                        mergedIntervals.append(newInterval)
                        overlapping = True
                        merged = True
                    mergedIntervals.append(interval)
                else:
                    union = join(interval, newInterval)
                    overlapping = True
            elif not merged:
                if overlap(union, interval):
                    union = join(union, interval)
                else:
                    mergedIntervals += [union, interval]
                    merged = True
            else:
                mergedIntervals.append(interval)

        if not overlapping:
            mergedIntervals.append(newInterval)
        elif not merged:
            mergedIntervals.append(union)

        return mergedIntervals
