"""
title : 0100_same_tree.py
create : @tarickali 23/05/18
update : @tarickali 23/05/18
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def search(s: Optional[TreeNode], t: Optional[TreeNode]) -> bool:
            if not s and not t:
                return True
            if (s and not t) or (not s and t) or (s.val != t.val):
                return False
            return search(s.left, t.left) and search(s.right, t.right)

        return search(p, q)

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def search(s: Optional[TreeNode], t: Optional[TreeNode]) -> None:
            if not s and not t:
                return
            if (s and not t) or (not s and t) or (s.val != t.val):
                raise
            search(s.left, t.left)
            search(s.right, t.right)

        try:
            search(p, q)
        except:
            return False
        return True
