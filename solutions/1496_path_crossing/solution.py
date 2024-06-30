"""
title : 1496_path_crossing.py
create : @tarickali 23/12/23
update : @tarickali 23/12/23
"""


class Solution:
    def isPathCrossing(self, path: str) -> bool:
        def move(point: tuple[int, int], arrow: str) -> tuple[int, int]:
            match arrow:
                case "N":
                    return (point[0], point[1] + 1)
                case "E":
                    return (point[0] + 1, point[1])
                case "S":
                    return (point[0], point[1] - 1)
                case "W":
                    return (point[0] - 1, point[1])
                case _:
                    return point

        point = (0, 0)
        points = {point}
        for arrow in path:
            point = move(point, arrow)
            if point in points:
                return True
            points.add(point)
        return False
