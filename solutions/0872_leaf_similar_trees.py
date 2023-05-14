"""
title : 0872_leaf_similar_trees.py
create : @tarickali 23/05/14
update : @tarickali 23/05/14
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def recurse(node: Optional[TreeNode], idx: int) -> None:
            if node == None:
                return
            if node.left == None and node.right == None:
                leaves[idx].append(node.val)
            recurse(node.left, idx)
            recurse(node.right, idx)

        leaves = [[], []]

        recurse(root1, 0)
        recurse(root2, 1)

        return leaves[0] == leaves[1]
