"""
title : 0345_reverse_vowels_of_a_string.py
create : @tarickali 23/05/22
update : @tarickali 23/05/22
"""


class Solution:
    def reverseVowels(self, s: str) -> str:
        V = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
        vowels = []
        for i in range(len(s)):
            if s[i] in V:
                vowels.append(i)

        t = ""
        j = 1
        for i in range(len(s)):
            if s[i] in V:
                t += s[vowels[-j]]
                j += 1
            else:
                t += s[i]
        return t
