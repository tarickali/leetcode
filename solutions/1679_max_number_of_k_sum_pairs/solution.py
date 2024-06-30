"""
title : 1679_max_number_of_k_sum_pairs.py
create : 23/06/01
update : 23/06/01
"""


class Solution:
    def maxOperations(self, nums: list[int], k: int) -> int:
        nums.sort()
        i = 0
        j = len(nums) - 1
        cnt = 0

        while i < j:
            if nums[i] + nums[j] == k:
                i += 1
                j -= 1
                cnt += 1
            elif nums[i] + nums[j] < k:
                i += 1
            else:
                j -= 1
        return cnt
