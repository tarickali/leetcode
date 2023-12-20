"""
title : 1436_destination_city.py
create : @tarickali 23/12/20
update : @tarickali 23/12/20
"""


class Solution:
    def destCity(self, paths: list[list[str]]) -> str:
        cities = set()
        starts = set()
        for path in paths:
            cities |= {path[0], path[1]}
            starts.add(path[0])
        return (cities - starts).pop()
