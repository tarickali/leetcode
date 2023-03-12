"""
title : 0543_diameter_of_binary_tree.py
create : @tarickali 23/03/11
update : @tarickali 23/03/11
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def recurse(node: Optional[TreeNode]) -> tuple[int, int]:
            if not node:
                return -1, 0
            if not (node.left or node.right):
                return 0, 0
            ldepth, lbest = recurse(node.left)
            rdepth, rbest = recurse(node.right)
            return max(ldepth, rdepth) + 1, max(ldepth + rdepth + 2, lbest, rbest)

        depth, diameter = recurse(root)
        return diameter
