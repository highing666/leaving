# -*- coding: utf-8


class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None


def reverse_list(head):
    p_reverse_head = None
    p_node = head
    p_prev = None

    while p_node:
        p_next = p_node.next

        if not p_next:
            p_reverse_head = p_node

        p_node.next = p_prev

        p_prev = p_node
        p_node = p_next

    return p_reverse_head
