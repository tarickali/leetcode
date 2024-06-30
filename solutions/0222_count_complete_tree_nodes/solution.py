"""
title : 0222_count_complete_tree_nodes.py
create : @tarickali 23/06/13
update : @tarickali 23/06/13
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def search(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            left = search(node.left)
            right = search(node.right)
            return 1 + left + right

        return search(root)
