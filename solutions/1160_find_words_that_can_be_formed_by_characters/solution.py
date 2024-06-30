"""
title : 1160_find_words_that_can_be_formed_by_characters.py
create : @tarickali 23/12/02
update : @tarickali 23/12/02
"""

from collections import Counter


class Solution:
    def countCharacters(self, words: list[str], chars: str) -> int:
        char_counts = Counter(chars)

        counts = 0
        for word in words:
            if Counter(word) <= char_counts:
                counts += len(word)

        return counts
