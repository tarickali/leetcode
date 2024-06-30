"""
title : 2300_successful_pairs_of_spells_and_potions.py
create : @tarickali 23/06/08
update : @tarickali 23/06/08
"""


class Solution:
    def successfulPairs(
        self, spells: list[int], potions: list[int], success: int
    ) -> list[int]:
        def search(k: int) -> int:
            i = 0
            j = len(potions)

            combos = 0
            while i < j:
                m = i + (j - i) // 2
                if potions[m] * spells[k] >= success:
                    combos += j - m
                    j = m
                else:
                    i = m + 1
            return combos

        potions.sort()

        pairs = []
        for k in range(len(spells)):
            pairs.append(search(k))
        return pairs
