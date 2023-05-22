"""
title : 0374_guess_number_higher_or_lower.py
create : @tarickali 23/05/22
update : @tarickali 23/05/22
"""


def guess(num: int) -> int:
    # @param num, your guess
    # @return -1 if num is higher than the picked number
    #          1 if num is lower than the picked number
    #          otherwise return 0
    ...


class Solution:
    def guessNumber(self, n: int) -> int:
        i = 0
        j = n + 1

        while i <= j:
            m = i + (j - i) // 2
            g = guess(m)
            if g == 0:
                break
            elif g == 1:
                i = m + 1
            else:
                j = m
        return m
