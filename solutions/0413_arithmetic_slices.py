"""
title : 0413_arithmetic_slices.py
create : @tarickali 24/01/06
update : @tarickali 24/01/06
"""


class Solution:
    def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        memo = [0] * len(nums)
        for i in range(2, len(nums)):
            if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
                memo[i] = memo[i - 1] + 1
        return sum(memo)

    def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        count = 0
        for i in range(len(nums) - 1):
            diff = nums[i + 1] - nums[i]
            size = 1
            for j in range(i + 1, len(nums)):
                if nums[j] - nums[j - 1] == diff:
                    size += 1
                else:
                    break
            count += max(size - 2, 0)
        return count
