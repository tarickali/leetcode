"""
title : 0142_linked_list_cycle_II.py
create : @tarickali 23/03/26
update : @tarickali 23/03/26
"""

from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        indices = {}
        curr = head
        i = 0
        while curr and id(curr) not in indices:
            indices[id(curr)] = i
            curr = curr.next
            i += 1

        turtle = head
        hare = head
        while turtle and hare and hare.next:
            turtle = turtle.next
            hare = hare.next.next
            if hare == turtle:
                break
        else:
            return

        while indices[id(turtle)] < indices[id(turtle.next)]:
            turtle = turtle.next
        return turtle.next
