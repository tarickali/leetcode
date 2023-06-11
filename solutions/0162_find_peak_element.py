"""
title : 0162_find_peak_element.py
create : @tarickali 23/06/08
update : @tarickali 23/06/08
"""


class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        i = 0
        j = len(nums)

        while i < j:
            m = i + (j - i) // 2
            left = nums[m - 1] if m - 1 >= 0 else float("-inf")
            right = nums[m + 1] if m + 1 < len(nums) else float("-inf")

            if nums[m] > left and nums[m] > right:
                break
            else:
                if left < right:
                    i = m + 1
                else:
                    j = m

        return m
