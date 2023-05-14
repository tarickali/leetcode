"""
title : 2215_find_the_difference_of_two_arrays.py
create : @tarickali 23/05/14
update : @tarickali 23/05/14
"""


class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        s1, s2 = set(nums1), set(nums2)
        return [list(s1 - s2), list(s2 - s1)]
