# -*- coding: utf-8 -*-


class Node:

    def __init__(self, x: int, m_next: 'None' = None, random: 'None' = None):
        self.val = x
        self.m_next = m_next
        self.random = random


class Solution:

    def copy_random_list(self, head: 'Node') -> Node:
        self.clone_nodes(head)
        self.connect_sibling_nodes(head)
        return self.reconnect_nodes(head)

    @staticmethod
    def clone_nodes(head):
        p_node = head
        while p_node:
            p_cloned = Node(p_node.val)
            p_cloned.m_next = p_node.m_next
            p_cloned.random = None

            p_node.m_next = p_cloned

            p_node = p_cloned.m_next

    @staticmethod
    def connect_sibling_nodes(head):
        p_node = head
        while p_node:
            p_cloned = p_node.m_next
            if p_node.random:
                p_cloned.random = p_node.random.m_next

            p_node = p_cloned.m_next

    @staticmethod
    def reconnect_nodes(head):
        p_node = head
        p_cloned_head = None
        p_cloned_node = None

        if p_node:
            p_cloned_head = p_node.m_next
            p_cloned_node = p_node.m_next
            p_node.m_next = p_cloned_node.m_next
            p_node = p_node.m_next

        while p_node:
            p_cloned_node.m_next = p_node.m_next
            p_cloned_node = p_cloned_node.m_next
            p_node.m_next = p_cloned_node.m_next
            p_node = p_node.m_next

        return p_cloned_head
