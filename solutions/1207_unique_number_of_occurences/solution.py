"""
title : 1207_unique_number_of_occurences.py
create : @tarickali 23/05/16
update : @tarickali 23/05/16
"""


class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        table = {}
        for a in arr:
            table[a] = table.get(a, 0) + 1
        return len(set(table.values())) == len(table)
