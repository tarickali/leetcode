"""
title : 108_convert_sorted_array_to_binary_search_tree.py
create : @tarickali 23/05/13
update : @tarickali 23/05/13
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> Optional[TreeNode]:
        def recurse(l: int, r: int) -> Optional[TreeNode]:
            if l >= r:
                return None
            m = l + (r - l) // 2
            left = recurse(l, m)
            right = recurse(m + 1, r)
            return TreeNode(nums[m], left, right)

        return recurse(0, len(nums))
