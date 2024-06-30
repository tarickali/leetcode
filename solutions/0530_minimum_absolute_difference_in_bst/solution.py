"""
title : 0530_minimum_absolute_difference_in_bst.py
create : @tarickali 23/05/17
update : @tarickali 23/05/17
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        inf = float("inf")

        def search(node: Optional[TreeNode]) -> tuple[int, int, int]:
            if node == None:
                return inf, -inf, inf
            lmin, lmax, lbest = search(node.left)
            rmin, rmax, rbest = search(node.right)

            return (
                min(lmin, node.val),
                max(rmax, node.val),
                min(lbest, rbest, abs(node.val - lmax), abs(node.val - rmin)),
            )

        _, _, best = search(root)
        return best
