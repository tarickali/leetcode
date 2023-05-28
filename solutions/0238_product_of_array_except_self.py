"""
title : 0238_product_of_array_except_self.py
create : @tarickali 23/05/28
update : @tarickali 23/05/28
"""


class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)

        answer = [0] * n
        answer[0] = 1
        for i in range(1, n):
            answer[i] = nums[i - 1] * answer[i - 1]

        prod = 1
        for i in reversed(range(n - 1)):
            answer[i] = nums[i + 1] * prod * answer[i]
            prod *= nums[i + 1]

        return answer
