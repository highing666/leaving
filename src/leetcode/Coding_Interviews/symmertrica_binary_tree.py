# -*- coding: utf-8 -*-


class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def isSymmertic(self, root: TreeNode) -> bool:
        return self.recur(root, root)

    def recur(self, root1, root2):
        if not (root1 or root2):
            return True

        if not (root1 and root2):
            return False

        if root1.val != root2.val:
            return False

        return self.recur(root1.left, root2.right) and self.recur(root1.right, root2.left)
