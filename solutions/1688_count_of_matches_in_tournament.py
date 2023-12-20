"""
title : 1688_count_of_matches_in_tournament.py
create : @tarickali 23/12/20
update : @tarickali 23/12/20
"""


class Solution:
    def numberOfMatches(self, n: int) -> int:
        count = 0
        while n > 1:
            if n % 2 == 0:
                count += n // 2
                n = n // 2
            else:
                count += (n - 1) // 2 + 1
                n = (n - 1) // 2
        return count
