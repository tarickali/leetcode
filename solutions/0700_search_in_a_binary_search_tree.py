"""
title : 0700_search_in_a_binary_search_tree.py
create : @tarickali 23/05/22
update : @tarickali 23/05/22
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def traverse(node: Optional[TreeNode]) -> Optional[TreeNode]:
            if node == None:
                return None
            if node.val == val:
                return node
            elif node.val > val:
                return traverse(node.left)
            else:
                return traverse(node.right)

        return traverse(root)
