"""
title : 0061_rotate_list.py
create : @tarickali 23/05/23
update : @tarickali 23/05/23
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        n = 0
        curr = head
        while curr:
            n += 1
            curr = curr.next

        if n == 0:
            return None

        m = k % n

        curr = head
        for _ in range(n - m - 1):
            curr = curr.next
        tail = curr
        for _ in range(n - m, n):
            curr = curr.next

        curr.next = head
        head = tail.next
        tail.next = None

        return head
