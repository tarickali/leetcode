"""
title : 0114_flatten_binary_tree_to_linked_list.py
create : @tarickali 23/05/12
update : @tarickali 23/05/12
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        def recurse(node: Optional[TreeNode]) -> None:
            nonlocal root
            if node == None:
                return
            root.right = TreeNode(node.val)
            root = root.right
            recurse(node.left)
            recurse(node.right)

        if root == None:
            return

        left_root = root.left
        right_root = root.right

        root.left = None
        root.right = None

        recurse(left_root)
        recurse(right_root)
