"""
title : 0101_symmetric_tree.py
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
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def traverse(u: Optional[TreeNode], v: Optional[TreeNode]) -> bool:
            if not u and not v:
                return True
            if (u and not v) or (not u and v):
                return False
            if not (u.left or u.right) and not (v.left or v.right):
                return u.val == v.val

            left = traverse(u.left, v.right)
            right = traverse(u.right, v.left)
            return left and u.val == v.val and right

        return traverse(root.left, root.right)
