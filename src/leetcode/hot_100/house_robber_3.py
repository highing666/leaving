# -*- coding: utf-8 -*-

from typing import Tuple


class TreeNode:

    def __init__(self, val: int = 0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def dfs(self, node: TreeNode) -> Tuple[int, int]:
        if not node:
            return 0, 0

        rob_l, skip_l = self.dfs(node.left)
        rob_r, skip_r = self.dfs(node.right)

        return node.val + skip_l + skip_r, max(rob_l, skip_l) + max(skip_r, rob_r)

    def rob(self, root: TreeNode) -> int:
        return max(self.dfs(root))
