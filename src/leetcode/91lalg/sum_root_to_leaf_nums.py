# -*- coding: utf-8 -*-

class TreeNode:

    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def sum_numbers(self, root: TreeNode) -> int:

        def dfs(root: TreeNode, pre_total: int) -> int:
            if not root:
                return 0

            total = pre_total * 10 + root.val
            if not root.left and not root.right:
                return total
            else:
                return dfs(root.left, total) + dfs(root.right, total)
        
        return dfs(root, 0)
