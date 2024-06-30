"""
title : 2641_cousins_in_binary_tree_II.py
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
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def get_levels(node: Optional[TreeNode], depth: int) -> None:
            if node == None:
                return

            if depth >= len(levels):
                levels.append(node.val)
            else:
                levels[depth] += node.val

            get_levels(node.left, depth + 1)
            get_levels(node.right, depth + 1)

        def sum_cousins(node: Optional[TreeNode], depth: int, siblings: int) -> None:
            if node == None:
                return

            node.val = levels[depth] - siblings
            siblings = (0 if node.left is None else node.left.val) + (
                0 if node.right is None else node.right.val
            )
            sum_cousins(node.left, depth + 1, siblings)
            sum_cousins(node.right, depth + 1, siblings)

        levels = []
        get_levels(root, 0)
        sum_cousins(root, 0, root.val)
        return root
