"""
title : 2264_largest_3_same_digit_number_in_string.py
create : @tarickali 23/12/20
update : @tarickali 23/12/20
"""

class Solution:
    def largestGoodInteger(self, num: str) -> str:
        best = ""
        i = 0
        while i < len(num):
            j = i + 1
            while j < len(num) and num[j] == num[i]:
                j += 1
            if j - i >= 3 and (not best or int(num[i]*3) >= int(best)):
                best = num[i] * 3
            i = j
        return best