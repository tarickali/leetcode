"""
title : 0452_minimum_number_of_arrows_to_burst_balloons.py
create : @tarickali 23/06/15
update : @tarickali 23/06/15
"""


class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        points.sort(key=lambda x: x[0])

        groups = [points[0]]
        for i in range(1, len(points)):
            point = points[i]
            if groups[-1][0] <= point[0] <= groups[-1][1]:
                groups[-1][0] = max(groups[-1][0], point[0])
                groups[-1][1] = min(groups[-1][1], point[1])
            else:
                groups.append(point)

        return len(groups)
