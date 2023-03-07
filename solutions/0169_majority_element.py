"""
title : 0169_majority_element.py
create : @tarickali 23/02/25
update : @tarickali 23/02/25
"""


class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        n = len(nums)
        table = {}
        for k in nums:
            table[k] = table.get(k, 0) + 1
            if table[k] > n // 2:
                return k
