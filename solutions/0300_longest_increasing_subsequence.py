"""
title : 0300_longest_increasing_subsequence.py
create : @tarickali 24/01/04
update : @tarickali 24/01/04
"""

import bisect


class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        memo = [nums[0]]
        for i in range(1, len(nums)):
            if memo[-1] < nums[i]:
                memo.append(nums[i])
            else:
                memo[bisect.bisect_left(memo, nums[i])] = nums[i]
        return len(memo)
