"""
title : 0938_range_sum_of_bst.py
create : @tarickali 24/01/07
update : @tarickali 24/01/07
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def recurse(node: Optional[TreeNode]) -> int:
            if node is None:
                return 0

            curr = node.val if low <= node.val <= high else 0
            left = recurse(node.left)
            right = recurse(node.right)

            return curr + left + right

        return recurse(root)
