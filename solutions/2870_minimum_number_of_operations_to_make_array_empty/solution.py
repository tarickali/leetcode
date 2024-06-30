"""
title : 2870_minimum_number_of_operations_to_make_array_empty.py
create : @tarickali 24/01/03
update : @tarickali 24/01/03
"""

from collections import Counter


class Solution:
    def minOperations(self, nums: list[int]) -> int:
        counts = list(Counter(nums).values())
        operations = 0

        i = 0
        while i < len(counts):
            if counts[i] < 0:
                return -1

            if counts[i] % 3 == 0:
                operations += counts[i] // 3
            else:
                div = counts[i] // 3
                rem = counts[i] - div * 3
                if rem % 2 == 0:
                    operations += div + rem // 2
                else:
                    counts[i] -= 2
                    operations += 1
                    continue
            i += 1

        return operations
