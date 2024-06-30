"""
title : 0219_contains_duplicate_II.py
create : @tarickali 23/05/18
update : @tarickali 23/05/18
"""


class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        table = {}
        for i, x in enumerate(nums):
            if x in table and abs(table[x] - i) <= k:
                return True
            table[x] = i
        return False
