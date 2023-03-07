"""
title : 0112_path_sum.py
create : @tarickali 23/03/06
update : @tarickali 23/03/06
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def recurse(node: Optional[TreeNode], target: int) -> bool:
            if node == None:
                return False
            if node.left == None and node.right == None:
                return node.val == target
            target -= node.val
            return recurse(node.left, target) or recurse(node.right, target)

        return recurse(root, targetSum)
