"""
title : 0814_binary_tree_pruning.py
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
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def recurse(node: Optional[TreeNode]) -> bool:
            if node is None:
                return False

            curr = node.val == 1
            left = recurse(node.left)
            right = recurse(node.right)

            if not left:
                node.left = None
            if not right:
                node.right = None

            return curr or left or right

        contains = recurse(root)
        if not contains:
            root = None

        return root
