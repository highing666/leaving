# -*- coding: utf-8 -*-


class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def mirrorTree(self, root: TreeNode):
        if not root:
            return

        root.left, root.right = self.mirrorTree(root.right), self.mirrorTree(root.left)

        return root
