"""
title : 1759_count_number_of_homogenous_substrings.py
create : @tarickali 23/11/08
update : @tarickali 23/11/08
"""


class Solution:
    def countHomogenous(self, s: str) -> int:
        cnt = 0
        i, j = 0, 0

        n = len(s)
        while i < n:
            c = s[i]
            while j < n:
                if s[j] == c:
                    j += 1
                else:
                    break
            k = j - i
            cnt += k * (k + 1) // 2
            i = j
        return cnt % (10**9 + 7)
