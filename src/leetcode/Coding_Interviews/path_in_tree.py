# -*- coding: utf-8 -*-


class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.result = []
        self.path = []

    def path_sum(self, root: TreeNode, sum: int) -> [[int]]:
        self.recur(root, sum)

        return self.result

    def recur(self, root, target):
        if not root:
            return []

        self.path.append(root.val)
        target -= root.val
        if target == 0 and not root.left and not root.right:
            self.result.append(list(self.path))
        self.recur(root.left, target)
        self.recur(root.right, target)
        self.path.pop()
