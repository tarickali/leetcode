"""
title : 0129_sum_root_to_leaf_numbers.py
create : @tarickali 23/03/06
update : @tarickali 23/03/06
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        total = 0

        def recurse(node: Optional[TreeNode]) -> list[int]:
            nonlocal total

            if node == None:
                return []
            if not node.left and not node.right:
                total += node.val
                return [1]

            depths = recurse(node.left) + recurse(node.right)
            for i in range(len(depths)):
                total += node.val * 10 ** depths[i]
                depths[i] += 1
            return depths

        recurse(root)
        return total
