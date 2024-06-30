"""
title : 0724_find_pivot_index.py
create : @tarickali 23/03/24
update : @tarickali 23/03/24
"""


class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        n = len(nums)
        prefix = [0]
        for i in range(n):
            prefix.append(prefix[i] + nums[i])

        for i in range(1, n + 1):
            if prefix[i - 1] == prefix[n] - prefix[i]:
                return i - 1
        return -1
