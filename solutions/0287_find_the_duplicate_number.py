"""
title : 0287_find_the_duplicate_number.py
create : @tarickali 23/03/19
update : @tarickali 23/03/19
"""


class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        sorted_nums = sorted(nums)
        duplicate = None
        for i in range(len(sorted_nums) - 1):
            if sorted_nums[i] == sorted_nums[i + 1]:
                duplicate = sorted_nums[i]
                break
        return duplicate
