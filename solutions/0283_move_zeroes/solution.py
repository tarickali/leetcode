"""
title : 0283_move_zeroes.py
create : @tarickali 23/02/25
update : @tarickali 23/02/25
"""


class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        for k in range(len(nums)):
            if nums[k] != 0:
                nums[k], nums[i] = nums[i], nums[k]
                i += 1
