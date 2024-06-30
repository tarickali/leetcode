"""
title : 0027_remove_element.py
create : @tarickali 23/05/30
update : @tarickali 23/05/30
"""


class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        i = 0
        j = len(nums) - 1
        k = 0
        while i <= j:
            if nums[i] != val:
                i += 1
                k += 1
            else:
                nums[i], nums[j] = nums[j], nums[i]
                j -= 1
        return k
