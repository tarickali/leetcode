"""
title : 0637_average_of_levels_in_binary_tree.py
create : @tarickali 23/06/13
update : @tarickali 23/06/13
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> list[float]:
        levels = []

        def include(node: TreeNode, l: int):
            if l == len(levels):
                levels.append([node.val, 1])
            else:
                levels[l][0] += node.val
                levels[l][1] += 1

        def search(node: Optional[TreeNode], l: int) -> None:
            if not node:
                return
            include(node, l)
            search(node.left, l + 1)
            search(node.right, l + 1)

        search(root, 0)
        return [total / n for total, n in levels]
