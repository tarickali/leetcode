"""
title : 0141_linked_list_cycle.py
create : @tarickali 23/03/11
update : @tarickali 23/03/11
"""

from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        turtle = head
        hare = head
        while turtle and hare:
            turtle = turtle.next
            if not hare.next:
                return False
            hare = hare.next.next
            if turtle and hare and turtle == hare:
                return True
        return False
