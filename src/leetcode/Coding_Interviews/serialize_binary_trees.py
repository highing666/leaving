# -*- coding: utf-8 -*-

from collections import deque


class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    @staticmethod
    def serialize(root):
        """
        Encodes a tree to a single string.

        :param root: a binary tree
        :return: a string
        """
        if not root:
            return '[]'

        queue = deque()
        queue.append(root)
        result = []
        while queue:
            node = queue.popleft()
            if node:
                result.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append('null')

        return '[' + ','.join(result) + ']'

    @staticmethod
    def deserialize(data):
        """
        Decodes your encoded data to tree.

        :param data:
        :return:
        """
        if data == '[]':
            return

        values, i = data[1:-1].split(','), 1
        root = TreeNode(int(values[0]))
        queue = deque()
        queue.append(root)
        while queue:
            node = queue.popleft()

            if values[i] != 'null':
                node.left = TreeNode(int(values[i]))
                queue.append(node.left)
            i += 1

            if values[i] != 'null':
                node.right = TreeNode(int(values[i]))
                queue.append(node.right)
            i += 1

        return root
