"""
title : 1004_max_consecutive_ones_III.py
create : @tarickali 23/05/31
update : @tarickali 23/05/31
"""

from collections import deque


class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        start = 0
        best = 0
        zeros = deque()

        for i in range(len(nums)):
            if nums[i] == 1:
                continue
            zeros.append(i)
            if len(zeros) == k + 1:
                best = max(best, i - start)
                start = zeros.popleft() + 1

        if len(zeros) < k:
            return len(nums)
        return max(best, i + 1 - start)
