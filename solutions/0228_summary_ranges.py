"""
title : 0228_summary_ranges.py
create : @tarickali 23/05/18
update : @tarickali 23/05/18
"""


class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        ranges = []
        i = 0
        j = 0
        k = 1
        while k <= len(nums):
            if k < len(nums) and nums[k] == nums[j] + 1:
                j += 1
            else:
                if i == j:
                    ranges.append(str(nums[i]))
                else:
                    ranges.append(str(nums[i]) + "->" + str(nums[j]))
                i = j = k
            k += 1

        return ranges
