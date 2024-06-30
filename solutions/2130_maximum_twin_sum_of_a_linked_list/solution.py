"""
title : 2130_maximum_twin_sum_of_a_linked_list.py
create : @tarickali 23/05/23
update : @tarickali 23/05/23
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        n = 0
        curr = head
        while curr:
            n += 1
            curr = curr.next

        vals = []
        curr = head
        for i in range(n // 2):
            vals.append(curr.val)
            curr = curr.next

        for i in range(n // 2):
            vals[-i - 1] += curr.val
            curr = curr.next

        return max(vals)
