"""
title : 0236_lowest_common_ancestor_of_a_binary_tree.py
create : @tarickali 23/06/03
update : @tarickali 23/06/03
"""

from typing import Optional


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        def search(node: Optional[TreeNode]) -> TreeNode:
            if not node:
                return None
            if node == p or node == q:
                return node

            left = search(node.left)
            right = search(node.right)

            if left and right:
                return node
            elif left:
                return left
            elif right:
                return right
            else:
                return None

        return search(root)
