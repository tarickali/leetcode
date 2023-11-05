"""
title : 0501_find_mode_in_binary_search_tree.py
create : @tarickali 23/11/01
update : @tarickali 23/11/01
"""

from typing import Optional
from collections import defaultdict


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findMode(self, root: Optional[TreeNode]) -> list[int]:
        table = defaultdict(int)

        def recurse(node: Optional[TreeNode]) -> None:
            if node == None:
                return
            table[node.val] += 1
            recurse(node.left)
            recurse(node.right)

        recurse(root)
        mode = max(table.values())
        return [x for x in table if table[x] == mode]
