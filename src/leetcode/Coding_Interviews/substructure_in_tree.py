# -*- coding: utf-8 -*-


class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def isSubStructure(self, a: TreeNode, b: TreeNode) -> bool:
        result = False

        if a and b:
            if a.val == b.val:
                result = self.does_tree1_have_tree2(a, b)
            if not result:
                result = self.isSubStructure(a.left, b)
            if not result:
                result = self.isSubStructure(a.right, b)

        return result

    def does_tree1_have_tree2(self, a, b):
        if not b:
            return True
        if not a or a.val != b.val:
            return False

        return self.does_tree1_have_tree2(a.left, b.left) and self.does_tree1_have_tree2(a.right, b.right)
