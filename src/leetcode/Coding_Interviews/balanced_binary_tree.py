# -*- coding: utf-8 -*-


class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def is_balanced(self, root: TreeNode) -> bool:

        return self.recur(root) != -1

    def recur(self, root: TreeNode) -> int:
        if not root:
            return 0

        left = self.recur(root.left)
        if left == -1:
            return -1

        right = self.recur(root.right)
        if right == -1:
            return -1

        if abs(left - right) <= 1:
            return max(left, right) + 1
        else:
            return -1
