"""
title : 0199_binary_tree_right_side_view.py
create : @tarickali 23/01/26
update : @tarickali 23/01/26
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> list[int]:
        levels = []

        def traverse(node, i):
            if not node:
                return

            if i < len(levels):
                levels[i].append(node.val)
            else:
                levels.append([node.val])
            traverse(node.left, i + 1)
            traverse(node.right, i + 1)

        traverse(root, 0)
        return [level[-1] for level in levels]
