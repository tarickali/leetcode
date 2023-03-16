"""
title : 0138_copy_list_with_random_pointer.py
create : @tarickali 23/03/15
update : @tarickali 23/03/15
"""

from __future__ import annotations
from typing import Optional


class Node:
    def __init__(self, x: int, next: Node = None, random: Node = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        table = {}
        nodes = {}

        curr = head
        while curr:
            table[id(curr)] = (id(curr.next), id(curr.random))
            nodes[id(curr)] = Node(curr.val)
            curr = curr.next

        curr = head
        while curr:
            nid, rid = table[id(curr)]
            nodes[id(curr)].next = nodes[nid] if nid != id(None) else None
            nodes[id(curr)].random = nodes[rid] if rid != id(None) else None
            curr = curr.next

        return nodes.get(id(head), None)
