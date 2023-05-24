"""
title : 0092_reverse_linked_list_II.py
create : @tarickali 23/05/24
update : @tarickali 23/05/24
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(
        self, head: Optional[ListNode], left: int, right: int
    ) -> Optional[ListNode]:
        if left == right:
            return head

        top = ListNode(0, head)
        curr = top
        i = 0
        while i < left - 1:
            curr = curr.next
            i += 1
        start = curr

        curr = curr.next
        succ = curr.next
        i += 1
        while i < right and succ:
            temp = succ.next
            succ.next = curr
            curr = succ
            succ = temp
            i += 1

        start.next.next = succ
        start.next = curr
        return top.next
