"""
title : 0290_word_pattern.py
create : @tarickali 23/05/15
update : @tarickali 23/05/15
"""


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        table = {}
        seen = set()
        words = s.split()

        if len(pattern) != len(words):
            return False

        for i in range(len(words)):
            if pattern[i] not in table:
                if words[i] not in seen:
                    table[pattern[i]] = words[i]
                    seen.add(words[i])
                else:
                    return False
            elif table[pattern[i]] != words[i]:
                return False
        return True
