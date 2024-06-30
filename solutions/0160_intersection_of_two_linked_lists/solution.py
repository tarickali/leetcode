"""
title : 0160_intersection_of_two_linked_lists.py
create : @tarickali 23/05/13
update : @tarickali 23/05/13
"""

from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # Time: O(n + m), Space: O(n)
    def getIntersectionNode(
        self, headA: ListNode, headB: ListNode
    ) -> Optional[ListNode]:
        a_nodes = set()
        curr = headA
        while curr:
            a_nodes.add(curr)
            curr = curr.next

        curr = headB
        while curr:
            if curr in a_nodes:
                return curr
            curr = curr.next

        return None

    # Time: O(n + m), Space: O(1)
    def getIntersectionNode(
        self, headA: ListNode, headB: ListNode
    ) -> Optional[ListNode]:
        x, y = headA, headB
        while x != y:
            x = x.next if x != None else headB
            y = y.next if y != None else headA
        return x
