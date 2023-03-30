"""
title : 0235_lowest_common_ancestor_of_a_binary_search_tree.py
create : @tarickali 23/03/30
update : @tarickali 23/03/30
"""

from typing import Optional


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: TreeNode, p: TreeNode, q: TreeNode
    ) -> TreeNode:
        mini = min(p.val, q.val)
        maxi = max(p.val, q.val)

        def recurse(node: Optional[TreeNode]) -> Optional[TreeNode]:
            if not node:
                return
            if (mini == node.val or maxi == node.val) or (
                mini < node.val and maxi > node.val
            ):
                return node
            elif mini < node.val and maxi < node.val:
                return recurse(node.left)
            elif mini > node.val and maxi > node.val:
                return recurse(node.right)
            else:  # mini > node.val and maxi < node.val
                return

        return recurse(root)
