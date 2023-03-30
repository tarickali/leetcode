"""
title : 0098_validate_binary_search_tree.py
create : @tarickali 23/03/30
update : @tarickali 23/03/30
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def recurse(node: Optional[TreeNode]) -> tuple[int | None, bool]:
            if not node:
                return None, None, True

            left_min, left_max, left_valid = recurse(node.left)
            right_min, right_max, right_valid = recurse(node.right)

            curr_min = min({left_min, right_min, node.val} - {None})
            curr_max = max({left_max, right_max, node.val} - {None})
            curr_valid = (not left_max or left_max < node.val) and (
                not right_min or right_min > node.val
            )

            return curr_min, curr_max, curr_valid and left_valid and right_valid

        root_min, root_max, root_valid = recurse(root)
        return root_valid
