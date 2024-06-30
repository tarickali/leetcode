"""
title : 0019_remove_nth_node_from_end_of_list.py
create : @tarickali 23/05/18
update : @tarickali 23/05/18
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        sz = 0
        curr = head
        while curr:
            sz += 1
            curr = curr.next

        if n == sz:
            head = head.next
        else:
            curr = head
            for _ in range(sz - n - 1):
                curr = curr.next
            curr.next = curr.next.next if curr.next else None

        return head
