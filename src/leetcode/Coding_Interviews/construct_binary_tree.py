# -*- coding: utf-8 -*-

class TreeNode:

    def __init__(self, x):
        super().__init__()
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def build_tree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        temp_dic = dict(enumerate(inorder))
        self.dic = {v: k for k, v in temp_dic.items()}
        self.po = preorder

        return self.recur(0, 0, len(inorder) - 1)

    def recur(self, pre_root, in_left, in_right):
        if in_left > in_right:
            return
        root = TreeNode(self.po[pre_root])
        i = self.dic[self.po[pre_root]]
        root.left = self.recur(pre_root + 1, in_left, i - 1)
        root.right = self.recur(i - in_left + pre_root + 1, i + 1, in_right)

        return root

