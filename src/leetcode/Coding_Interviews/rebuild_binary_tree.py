# -*- coding: utf-8 -*-

class TreeNode:

    def __init__(self, x):
        super().__init__()
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def build_tree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        
