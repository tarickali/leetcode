"""
title : 0082_remove_duplicates_from_sorted_list_II.py
create : @tarickali 23/05/25
update : @tarickali 23/05/25
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodes = {}
        dupes = set()

        curr = head
        while curr:
            if curr.val in nodes:
                nodes.pop(curr.val)
                dupes.add(curr.val)
            if curr.val not in dupes:
                nodes[curr.val] = curr
            curr = curr.next

        top = ListNode()
        curr = top
        for key in nodes:
            curr.next = nodes[key]
            curr = curr.next
        curr.next = None

        return top.next
