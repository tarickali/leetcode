"""
title : 0039_combination_sum.py
create : @tarickali 23/05/25
update : @tarickali 23/05/25
"""


class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        def backtrack(i: int) -> list[int]:
            def recurse(i: int, goal: int) -> list[list[int]]:
                if candidates[i] > goal:
                    return []
                if candidates[i] == goal:
                    return [[candidates[i]]]
                combos = []
                for j in range(i, len(candidates)):
                    partials = recurse(j, goal - candidates[i])
                    if len(partials) != 0:
                        combos += [[candidates[i]] + partial for partial in partials]
                return combos

            return recurse(i, target)

        combos = []
        for i in range(len(candidates)):
            combos += backtrack(i)
        return combos
