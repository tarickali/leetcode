"""
title : 0446_arithmetic_slices_II_subsequence.py
create : @tarickali 24/01/06
update : @tarickali 24/01/06
"""


from collections import defaultdict


class Solution:
    def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        # memo[i][j] = # of arithemtic slices ending at i with difference j
        memo = [defaultdict(int) for _ in range(len(nums))]
        total = 0

        for i in range(1, len(nums)):
            for j in range(i):
                k = nums[i] - nums[j]
                memo[i][k] += 1
                if k in memo[j]:
                    memo[i][k] += memo[j][k]
                    total += memo[j][k]

        return total
