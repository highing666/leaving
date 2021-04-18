# -*- coding: utf-8 -*-

class TreeNode:

    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def max_depth(self, root: TreeNode) -> int:
        if not root:
            return 0
        else:
            left_height = self.max_depth(root.left)
            right_height = self.max_depth(root.right)
            return max(left_height, right_height) + 1
        