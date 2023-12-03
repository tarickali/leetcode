"""
title : 1980_find_unique_binary_string.py
create : @tarickali 23/11/15
update : @tarickali 23/11/15
"""


class Solution:
    def findDifferentBinaryString(self, nums: list[str]) -> str:
        nums.sort()
        b = 0

        for a in nums:
            if b != int(a, 2):
                break
            b += 1

        b = bin(b).split("0b")[1]
        return "0" * (len(nums) - len(b)) + b
