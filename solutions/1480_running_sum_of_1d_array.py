"""
title : 1480_running_sum_of_1d_array.py
create : @tarickali 23/03/24
update : @tarickali 23/03/24
"""


class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        total = 0
        running_sum = []
        for n in nums:
            total += n
            running_sum.append(total)
        return running_sum
