"""
title : 0046_permutations.py
create : @tarickali 23/03/13
update : @tarickali 23/03/13
"""


class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        def recurse(i: int, seen: set[int]) -> list[list[int]]:
            if len(seen) == len(nums):
                return [[nums[i]]]
            permutations = []
            for j in range(len(nums)):
                if j not in seen:
                    permutations += [
                        [nums[i]] + perm for perm in recurse(j, seen | {j})
                    ]
            return permutations

        permutations = []
        for i in range(len(nums)):
            permutations += recurse(i, {i})
        return permutations
