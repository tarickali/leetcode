"""
title : 0876_middle_of_the_linked_list.py
create : @tarickali 23/03/26
update : @tarickali 23/03/26
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        size = 0
        curr = head
        while curr:
            size += 1
            curr = curr.next

        curr = head
        for _ in range(size // 2):
            curr = curr.next

        return curr
