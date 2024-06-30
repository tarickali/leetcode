"""
title : 2265_count_nodes_equal_to_average_of_subtree.py
create : @tarickali 23/11/02
update : @tarickali 23/11/02
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        def recurse(node: Optional[TreeNode]) -> tuple[int, int, int]:
            if node == None:
                return (0, 0, 0)
            if node.left == None and node.right == None:
                return (node.val, 1, 1)

            left_sum, left_cnt, left_valid = recurse(node.left)
            right_sum, right_cnt, right_valid = recurse(node.right)

            subtree_sum = left_sum + right_sum + node.val
            subtree_cnt = left_cnt + right_cnt + 1
            subtree_valid = left_valid + right_valid

            if subtree_sum // subtree_cnt == node.val:
                subtree_valid += 1

            return (subtree_sum, subtree_cnt, subtree_valid)

        root_sum, root_cnt, root_valid = recurse(root)
        return root_valid
