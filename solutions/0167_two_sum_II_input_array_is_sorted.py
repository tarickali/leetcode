"""
title : 0167_two_sum_II_input_array_is_sorted.py
create : @tarickali 23/05/31
update : @tarickali 23/05/31
"""


class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        i = 0
        j = len(numbers) - 1

        while i < j:
            if numbers[i] + numbers[j] == target:
                break
            elif numbers[i] + numbers[j] < target:
                i += 1
            else:  # numbers[i] + numbers[j] > target
                j -= 1

        return [i + 1, j + 1]
