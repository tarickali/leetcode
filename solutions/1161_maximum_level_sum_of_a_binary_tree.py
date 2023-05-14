"""
title : 1161_maximum_level_sum_of_a_binary_tree.py
create : @tarickali 23/05/14
update : @tarickali 23/05/14
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        levels = []

        def recurse(node: Optional[TreeNode], lvl: int) -> None:
            if node == None:
                return

            if lvl >= len(levels):
                levels.append(0)
            levels[lvl] += node.val

            recurse(node.left, lvl + 1)
            recurse(node.right, lvl + 1)

        recurse(root, 0)

        return levels.index(max(levels)) + 1
