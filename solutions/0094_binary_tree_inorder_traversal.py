'''
title : 0094_binary_tree_inorder_traversal.py
create : @tarickali 23/02/23
update : @tarickali 23/02/23
'''

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        order = []
        def recurse(node: Optional[TreeNode]) -> None:
            if node == None: return 
            recurse(node.left)
            order.append(node.val)
            recurse(node.right)
        recurse(root)
        return order
        