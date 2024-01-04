"""
title : 2640_find_the_score_of_all_prefixes_of_an_array.py
create : @tarickali 24/01/03
update : @tarickali 24/01/03
"""


class Solution:
    def findPrefixScore(self, nums: list[int]) -> list[int]:
        ans = [0] * len(nums)
        ans[0] = nums[0] * 2
        best = nums[0]
        for i in range(1, len(nums)):
            best = max(best, nums[i])
            ans[i] = ans[i - 1] + nums[i] + best
        return ans
