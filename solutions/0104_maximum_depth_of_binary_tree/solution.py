"""
title : 0104_maximum_depth_of_binary_tree.py
create : @tarickali 23/02/23
update : @tarickali 23/02/23
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def recurse(node: Optional[TreeNode]) -> int:
            if node == None:
                return 0
            return max(recurse(node.left), recurse(node.right)) + 1

        return recurse(root)
