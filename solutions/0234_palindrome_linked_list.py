"""
title : 0234_palindrome_linked_list.py
create : @tarickali 23/05/13
update : @tarickali 23/05/13
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        seq = ""
        curr = head
        while curr != None:
            seq += str(curr.val)
            curr = curr.next

        n = len(seq)
        for i in range(n // 2):
            if seq[i] != seq[n - i - 1]:
                return False
        return True
