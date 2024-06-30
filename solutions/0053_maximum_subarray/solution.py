"""
title : 0053_maximum_subarray.py
create : @tarickali 23/03/07
update : @tarickali 23/03/07
"""


class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        prev, curr = 0, nums[0]
        best = nums[0]
        for i in range(1, len(nums)):
            prev = curr
            curr = max(0, prev) + nums[i]
            best = max(best, curr)
        return best

    def maxSubArray(self, nums: list[int]) -> int:
        n = len(nums)
        memo = [0] * n
        best = memo[0] = nums[0]
        for i in range(1, n):
            memo[i] = max(nums[i], memo[i - 1] + nums[i])
            best = max(best, memo[i])
        return best
