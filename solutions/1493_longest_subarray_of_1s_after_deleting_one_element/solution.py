"""
title : 1493_longest_subarray_of_1s_after_deleting_one_element.py
create : @tarickali 23/06/01
update : @tarickali 23/06/01
"""


class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        best = 0
        zero = -1
        start = 0

        for i in range(len(nums)):
            if nums[i] == 1:
                continue
            if zero == -1:
                zero = i
            else:
                best = max(best, i - start - 1)
                start = zero + 1
                zero = i

        return max(best, i - start)
