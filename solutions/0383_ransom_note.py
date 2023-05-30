"""
title : 0383_ransom_note.py
create : @tarickali 23/05/30
update : @tarickali 23/05/30
"""

from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_counts = Counter(ransomNote)
        magazine_counts = Counter(magazine)
        for c in ransom_counts:
            if ransom_counts.get(c, 0) > magazine_counts.get(c, 0):
                return False
        return True
