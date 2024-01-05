"""
title : 0993_cousins_in_binary_tree.py
create : @tarickali 24/01/04
update : @tarickali 24/01/04
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        def recurse(node: Optional[TreeNode], depth: int) -> bool:
            if node == None:
                return False

            if depth >= len(levels):
                levels.append({node.val})
            else:
                levels[depth].add(node.val)

            left = recurse(node.left, depth + 1)
            right = recurse(node.right, depth + 1)

            return (
                left
                or right
                or not (
                    node.left is None
                    or node.right is None
                    or {node.left.val, node.right.val} != {x, y}
                )
            )

        levels = []
        siblings = recurse(root, 0)

        if siblings:
            return False

        for level in levels:
            if x in level and y in level:
                return True
        return False
