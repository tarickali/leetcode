"""
title : 0015_3sum.py
create : @tarickali 23/03/08
update : @tarickali 23/03/08
"""

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        pairs = set()
        T = {x: i for i, x in enumerate(nums)}
        for i in range(n):
            for j in range(i+1, n):
                y = -(nums[i] + nums[j])
                if y in T and T[y] not in {i, j}:
                    pairs.add(tuple(sorted([nums[i], nums[j], y])))
        return pairs

