"""
title : 2095_delete_the_middle_node_of_a_linked_list.py
create : @tarickali 23/05/20
update : @tarickali 23/05/20
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n = 0
        curr = head
        while curr:
            n += 1
            curr = curr.next

        m = n // 2
        i = 0
        curr = head
        while i < m - 1:
            i += 1
            curr = curr.next

        if curr.next:
            curr.next = curr.next.next
        else:  # curr.next == None iff n == 1 iff m == 0 => delete head
            head = None
        return head
