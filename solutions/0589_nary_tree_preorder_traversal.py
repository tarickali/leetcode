"""
title : 0589_nary_tree_preorder_traversal.py
create : @tarickali 23/03/28
update : @tarickali 23/03/28
"""


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root: Node) -> list[int]:
        def recurse(node: Node) -> list[int]:
            if not node:
                return []
            order = [node.val]
            for child in node.children:
                order += recurse(child)
            return order

        return recurse(root)
