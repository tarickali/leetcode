'''
title : 0001_two_sum.py
create : @tarickali 23/11/22
update : @tarickali 23/11/22
'''

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        T = {}
        for i, x in enumerate(nums):
            y = target - x
            if y in T:
                return [i, T[y]]
            T[x] = i
        return [None, None]
