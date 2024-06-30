"""
title : 230_kth_smallest_element_in_a_bst.py
create : @tarickali 23/05/17
update : @tarickali 23/05/17
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        knode = None

        def search(node: Optional[TreeNode], h: int) -> int:
            nonlocal knode
            if node == None:
                return 0
            lsize = search(node.left, h)
            if lsize + 1 == h:
                knode = node
                raise
            rsize = search(node.right, h - lsize - 1)
            return lsize + rsize + 1

        try:
            search(root, k)
        except:
            pass
        return knode.val
