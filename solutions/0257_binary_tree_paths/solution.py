"""
title : 0257_binary_tree_paths.py
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
    def binaryTreePaths(self, root: Optional[TreeNode]) -> list[str]:
        paths = []

        def recurse(node: Optional[TreeNode]) -> list[int]:
            if not node:
                return []
            if not node.left and not node.right:
                paths.append(str(node.val))
                return [len(paths) - 1]

            idxs = recurse(node.left) + recurse(node.right)
            for idx in idxs:
                paths[idx] = str(node.val) + "->" + paths[idx]
            return idxs

        recurse(root)
        return paths
