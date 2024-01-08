"""
title : 0572_subtree_of_another_tree.py
create : @tarickali 24/01/07
update : @tarickali 24/01/07
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def recurse(node: Optional[TreeNode], code: str = None) -> tuple[str, bool]:
            if node is None:
                return "", False

            left_code, left_contain = recurse(node.left, code)
            right_code, right_contain = recurse(node.right, code)

            curr_code = left_code + "," + right_code + "," + str(node.val)
            curr_contain = curr_code == code if code is not None else False

            return curr_code, left_contain or right_contain or curr_contain

        subcode, _ = recurse(subRoot)
        _, contain = recurse(root, subcode)
        return contain
