# -*- coding: utf-8 -*-


class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def __init__(self, k=None, target=None):
        self.k = k
        self.target = target

    def kth_largest(self, root: TreeNode, k: int) -> int:
        self.k, self.target = k, 0
        self.dfs(root)

        return self.target

    def dfs(self, root: TreeNode) -> None:
        if not root:
            return
        self.dfs(root.right)
        if self.k == 0:
            return
        self.k -= 1
        if self.k == 0:
            self.target = root.val
        self.dfs(root.left)

        return
