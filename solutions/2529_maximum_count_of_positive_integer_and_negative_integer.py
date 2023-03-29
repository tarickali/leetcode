"""
title : 2529_maximum_count_of_positive_integer_and_negative_integer.py
create : @tarickali 23/03/29
update : @tarickali 23/03/29
"""


class Solution:
    def maximumCount(self, nums: list[int]) -> int:
        n = len(nums)

        l = 0
        r = n - 1
        pos = n
        while l <= r:
            m = l + (r - l) // 2
            if nums[m] > 0:
                r = m - 1
                pos = min(pos, m)
            else:
                l = m + 1

        l = 0
        r = n - 1
        neg = 0
        while l <= r:
            m = l + (r - l) // 2
            if nums[m] < 0:
                l = m + 1
                neg = max(neg, m + 1)
            else:
                r = m - 1
        return max(neg, n - pos)
