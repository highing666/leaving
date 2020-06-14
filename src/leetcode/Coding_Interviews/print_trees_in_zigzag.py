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

    result, double_queue = [], deque([root])
    while double_queue:
        tmp = deque()
        for _ in range(len(double_queue)):
            node = double_queue.popleft()
            if len(result) % 2:
                tmp.appendleft(node.val)
            else:
                tmp.append(node.val)
            if node.left:
                double_queue.append(node.left)
            if node.right:
                double_queue.append(node.right)
        result.append(list(tmp))

    return result
