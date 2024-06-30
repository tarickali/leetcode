"""
title : 2785_sort_vowels_in_a_string.py
create : @tarickali 23/11/12
update : @tarickali 23/11/12
"""


class Solution:
    def sortVowels(self, s: str) -> str:
        VOWELS = set("aeiouAEIOU")
        vowels = [i for i in range(len(s)) if s[i] in VOWELS]
        vowels.sort(key=lambda x: s[x], reverse=True)
        t = "".join([c if c not in VOWELS else s[vowels.pop()] for c in s])
        return t
