# -*- coding: utf-8 -*-

from typing import List


class ListNode:

    def __init__(self, x):
        super().__init__()
        self.val = x
        self.next = None


class Solution:

    def get_intersection_node(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not (headA and headB):
            return None
        
        node1, node2 = headA, headB
        while node1 != node2:
            if node1:
                node1 = node1.next
            else:
                node1 = headB
            
            if node2:
                node2 = node2.next
            else:
                node2 = headA
        
        return node1
