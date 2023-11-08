"""
title : 1080_insufficient_nodes_in_root_to_leaf_paths.py
create : @tarickali 23/11/07
update : @tarickali 23/11/07
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sufficientSubset(
        self, root: Optional[TreeNode], limit: int
    ) -> Optional[TreeNode]:
        def recurse(node: Optional[TreeNode], psum: int) -> bool:
            if node is None:
                return True
            if node.left is None and node.right is None:
                return node.val + psum < limit

            left_insuff = recurse(node.left, node.val + psum)
            right_insuff = recurse(node.right, node.val + psum)

            if left_insuff:
                node.left = None
            if right_insuff:
                node.right = None

            return left_insuff and right_insuff

        root_insuff = recurse(root, 0)

        return None if root_insuff else root
