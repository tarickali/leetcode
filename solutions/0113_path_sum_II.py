"""
title: 0113_path_sum_II.py
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
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> list[list[int]]:
        paths = []

        def recurse(node: Optional[TreeNode], target: int) -> list[int]:
            if node == None:
                return []
            if node.left == None and node.right == None:
                if node.val == target:
                    paths.append([node.val])
                    return [len(paths) - 1]

            target -= node.val

            left_idxs = recurse(node.left, target)
            for idx in left_idxs:
                paths[idx] = [node.val] + paths[idx]

            right_idxs = recurse(node.right, target)
            for idx in right_idxs:
                paths[idx] = [node.val] + paths[idx]

            return left_idxs + right_idxs

        recurse(root, targetSum)

        return paths
