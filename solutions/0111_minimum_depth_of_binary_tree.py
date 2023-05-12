"""
title : 0111_minimum_depth_of_binary_tree.py
create : @tarickali 23/05/12
update : @tarickali 23/05/12
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def recurse(node: Optional[TreeNode]) -> int:
            if node == None:
                return 0
            if not node.left and not node.right:
                return 1
            left = recurse(node.left) if node.left else float("inf")
            right = recurse(node.right) if node.right else float("inf")
            return min(left, right) + 1

        return recurse(root)
