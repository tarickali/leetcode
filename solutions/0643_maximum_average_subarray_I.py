"""
title : 0643_maximum_average_subarray_I.py
create : @tarickali 23/05/28
update : @tarickali 23/05/28
"""


class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        curr = best = sum(nums[:k])
        for i in range(len(nums) - k):
            curr = curr - nums[i] + nums[i + k]
            best = max(best, curr)
        return best / k
