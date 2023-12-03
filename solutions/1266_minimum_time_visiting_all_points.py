"""
title : 1266_minimum_time_visiting_all_points.py
create : @tarickali 23/12/02
update : @tarickali 23/12/02
"""


class Solution:
    def minTimeToVisitAllPoints(self, points: list[list[int]]) -> int:
        time = 0
        for i in range(len(points) - 1):
            time += max(
                abs(points[i][0] - points[i + 1][0]),
                abs(points[i][1] - points[i + 1][1]),
            )
        return time
