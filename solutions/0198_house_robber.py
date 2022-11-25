class Solution:
    def rob(self, nums: list[int]) -> int:
        # Dynamic programming with no memoization
        a, b, c = 0, nums[0], nums[0]
        for i in range(1, len(nums)):
            c = max(nums[i] + a, b)
            a, b = b, c
        return c

    # def rob(self, nums: list[int]) -> int:
    #     # Dynamic programming with memoization
    #     n = len(nums)
    #     memo = [0] * (n + 1)
    #     memo[0], memo[1] = 0, nums[0]
    #     for i in range(2, n + 1):
    #         memo[i] = max(nums[i-1] + memo[i-2], memo[i-1])
    #     return memo[n]
