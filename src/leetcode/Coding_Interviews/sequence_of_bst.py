# -*- coding: utf-8 -*-


class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def verify_post_order(post_order: [int]) -> bool:
    return recur(0, len(post_order) - 1, post_order)


def recur(i, j, post_order):
    if i >= j:
        return True

    p = i
    while post_order[p] < post_order[j]:
        p += 1
    m = p
    while post_order[p] > post_order[j]:
        p += 1

    return p == j and recur(i, m - 1, post_order) and recur(m, j - 1, post_order)
