# -*- coding: utf-8 -*-


class Node:

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def __init__(self):
        self.head = None
        self.pre = None

    def tree_to_doubly_list(self, root: 'Node'):
        if not root:
            return None

        self.pre = None
        self.dfs(root)
        self.head.left, self.pre.right = self.pre, self.head

        return self.head

    def dfs(self, cur):
        if not cur:
            return

        self.dfs(cur.left)
        if self.pre:
            self.pre.right, cur.left = cur, self.pre
        else:
            self.head = cur
        self.pre = cur
        self.dfs(cur.right)
