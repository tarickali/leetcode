"""
title : 0328_odd_even_linked_list.py
create : @tarickali 23/05/20
update : @tarickali 23/05/20
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd = ListNode()
        even = ListNode()

        curr = head
        curr_odd = odd
        curr_even = even
        i = 1
        while curr:
            if i % 2:
                curr_odd.next = curr
                curr_odd = curr_odd.next
            else:
                curr_even.next = curr
                curr_even = curr_even.next
            i += 1
            curr = curr.next

        curr_even.next = None
        curr_odd.next = even.next
        return odd.next
