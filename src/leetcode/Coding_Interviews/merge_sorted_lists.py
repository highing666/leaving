# -*- coding: utf-8 -*-


class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None


def merge_two_lists(l1: ListNode, l2: ListNode):
    if not l1:
        return l2
    elif not l2:
        return l1

    if l1.val < l2.val:
        merged_head = l1
        merged_head.next = merge_two_lists(l1.next, l2)
    else:
        merged_head = l2
        merged_head.next = merge_two_lists(l1, l2.next)

    return merged_head
