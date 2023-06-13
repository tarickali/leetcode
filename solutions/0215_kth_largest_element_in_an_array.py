"""
title : 0215_kth_largest_element_in_an_array.py
create : @tarickali 23/06/13
update : @tarickali 23/06/13
"""

import random


class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        def partition(i: int, j: int) -> int:
            p = random.randrange(i, j)
            key = nums[p]

            nums[i], nums[p] = nums[p], nums[i]
            r = i
            for l in range(i + 1, j):
                if nums[l] > key:
                    r += 1
                    nums[l], nums[r] = nums[r], nums[l]
            nums[i], nums[r] = nums[r], nums[i]
            return r

        def quickselect(i: int, j: int) -> int:
            if j - i <= 0:
                return nums[i - 1]

            p = partition(i, j)
            if p + 1 == k:
                return nums[p]
            elif p + 1 < k:
                return quickselect(p + 1, j)
            else:
                return quickselect(i, p)

        return quickselect(0, len(nums))
