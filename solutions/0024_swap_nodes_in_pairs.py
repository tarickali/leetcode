"""
title : 0024_swap_nodes_in_pairs.py
create : @tarickali 23/05/19
update : @tarickali 23/05/19
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return
        dummy = ListNode(0, head)

        prev = dummy
        curr = dummy.next
        while curr and curr.next:
            prev.next = curr.next
            temp = curr.next.next
            curr.next.next = curr
            curr.next = temp

            prev, curr = curr, curr.next

        return dummy.next
