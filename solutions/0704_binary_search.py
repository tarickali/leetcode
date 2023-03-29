"""
title : 0704_binary_search.py
create : @tarickali 23/03/29
update : @tarickali 23/03/29
"""


class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l = 0
        r = len(nums)

        while l < r:
            m = l + (r - l) // 2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m
        return -1
