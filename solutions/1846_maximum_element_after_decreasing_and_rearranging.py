"""
title : 1846_maximum_element_after_decreasing_and_rearranging.py
create : @tarickali 23/11/14
update : @tarickali 23/11/14
"""


class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: list[int]) -> int:
        arr.sort()
        arr[0] = 1
        for i in range(1, len(arr)):
            if abs(arr[i] - arr[i - 1]) > 1:
                arr[i] = arr[i - 1] + 1
        return arr[-1]
