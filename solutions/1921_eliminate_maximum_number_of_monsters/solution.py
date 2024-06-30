"""
title : 1921_eliminate_maximum_number_of_monsters.py
create : @tarickali 23/11/06
update : @tarickali 23/11/06
"""


class Solution:
    def eliminateMaximum(self, dist: list[int], speed: list[int]) -> int:
        monsters = sorted([x / v for x, v in zip(dist, speed)])
        for t in range(len(monsters)):
            if t >= monsters[t]:
                break
        else:
            t += 1
        return t
