"""
title : 0409_longest_palindrome.py
create : @tarickali 23/03/27
update : @tarickali 23/03/27
"""


class Solution:
    def longestPalindrome(self, s: str) -> int:
        counts = {}
        for c in s:
            counts[c] = counts.get(c, 0) + 1

        total = 0
        odd_seen = 0
        for _, count in counts.items():
            is_odd = count % 2
            total += count - is_odd
            odd_seen = max(odd_seen, is_odd)
        return total + odd_seen
