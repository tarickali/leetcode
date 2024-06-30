"""
title : 0136_single_number.py
create : @tarickali 23/03/19
update : @tarickali 23/03/19
"""


class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        digit = 0
        for num in nums:
            digit ^= num
        return digit
