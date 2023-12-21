"""
title : 1287_element_appearing_more_than_25_in_sorted_array.py
create : @tarickali 23/12/20
update : @tarickali 23/12/20
"""

from collections import Counter


class Solution:
    def findSpecialInteger(self, arr: list[int]) -> int:
        n = len(arr)
        counts = Counter(arr)
        for key, val in counts.items():
            if val > n // 4:
                break
        return key
