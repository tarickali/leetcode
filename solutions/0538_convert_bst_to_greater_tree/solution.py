"""
title : 0538_convert_bst_to_greater_tree.py
create : @tarickali 23/11/13
update : @tarickali 23/11/13
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def recurse(node: Optional[TreeNode]) -> None:
            nonlocal tsum
            if node == None:
                return
            if node.left == None and node.right == None:
                tsum += node.val
                node.val = tsum
                return
            recurse(node.right)
            tsum += node.val
            node.val = tsum
            recurse(node.left)

        tsum = 0
        recurse(root)
        return root

    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def recurse(node: Optional[TreeNode], tsum: int) -> int:
            if node == None:
                return tsum
            if node.left == None and node.right == None:
                node.val += tsum
                return node.val
            rsum = recurse(node.right, tsum)
            node.val += rsum
            lsum = recurse(node.left, node.val)
            return lsum

        _ = recurse(root, 0)
        return root
