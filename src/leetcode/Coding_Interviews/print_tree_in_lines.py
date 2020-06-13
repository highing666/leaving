# -*- coding: utf-8 -*-

from collections import deque


class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def level_order(root: TreeNode) -> [[int]]:
    if not root:
        return []

    result, queue = [], deque()
    queue.append(root)
    while queue:
        tmp = []
        for _ in range(len(queue)):
            node = queue.popleft()
            tmp.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(tmp)

    return result
