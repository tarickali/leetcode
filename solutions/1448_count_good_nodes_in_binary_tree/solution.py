"""
title : 1448_count_good_nodes_in_binary_tree.py
create : @tarickali 23/06/02
update : @tarickali 23/06/02
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def search(node: Optional[TreeNode], maxi: int) -> int:
            if not node:
                return 0
            lcount = search(node.left, max(maxi, node.val))
            rcount = search(node.right, max(maxi, node.val))
            mcount = int(node.val >= maxi)

            return lcount + rcount + mcount

        return search(root, root.val)
