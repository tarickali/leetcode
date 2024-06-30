"""
title : 0045_jump_game_II.py
create : @tarickali 23/05/26
update : @tarickali 23/05/26
"""


class Solution:
    def jump(self, nums: list[int]) -> int:
        best = term = hops = 0
        for i in range(len(nums) - 1):
            best = max(best, i + nums[i])
            if best >= len(nums) - 1:
                hops += 1
                break
            if i == term:
                term = best
                hops += 1
        return hops

    def jump(self, nums: list[int]) -> int:
        n = len(nums)
        inf = float("inf")
        memo = [inf] * n
        memo[n - 1] = 0
        for i in reversed(range(n - 1)):
            if i + nums[i] >= n - 1:
                memo[i] = 1
            else:
                memo[i] = 1 + min(
                    [memo[i + j] for j in range(1, nums[i] + 1) if i + j < n],
                    default=inf,
                )
        return memo[0]
