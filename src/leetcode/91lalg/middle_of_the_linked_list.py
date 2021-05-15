# -*- coding: utf-8 -*-

class ListNode:

    def __init__(self, val: int) -> None:
        self.val = val
        self.next = None


class Solution:

    def middle_node(self, head: ListNode) -> ListNode:
        l, r = head, head
        while r and r.next:
            l = l.next
            r = r.next.next
        
        return l
