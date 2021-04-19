# -*- coding: utf-8 -*-

class TreeNode:

    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.right = right
        self.left = left
        

class Solution:

    def is_same_tree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        elif not p or not q:
            return False
        elif p.val != q.val:
            return False
        else:
            return self.is_same_tree(p.left, q.left) and self.is_same_tree(p.right, q.right)
