"""
title : 1913_maximum_product_difference_between_two_pairs.py
create : @tarickali 23/12/20
update : @tarickali 23/12/20
"""


class Solution:
    def maxProductDifference(self, nums: list[int]) -> int:
        nums.sort()
        return (nums[-1] * nums[-2]) - (nums[0] * nums[1])
