"""
title : 0213_house_robber_II.py
create : @tarickali 22/11/25
update : @tarickali 22/11/25
"""


class Solution:
    def rob(self, nums: list[int]) -> int:
        def walk(i: int, j: int) -> int:
            a, b, c = 0, nums[i], nums[i]
            for i in range(i + 1, j):
                c = max(nums[i] + a, b)
                a, b = b, c
            return c

        if len(nums) == 1:
            return nums[0]
        return max(walk(0, len(nums) - 1), walk(1, len(nums)))
