"""
title : 0026_remove_duplicates_from_sorted_array.py
create : @tarickali 23/05/18
update : @tarickali 23/05/18
"""


class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        k = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[k - 1]:
                nums[k], nums[i] = nums[i], nums[k]
                k += 1
            elif nums[i] < nums[k - 1]:
                break
        return k
