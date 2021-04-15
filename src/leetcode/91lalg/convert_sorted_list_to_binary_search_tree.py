# -*- coding: utf-8 -*-


class ListNode:

    def __init__(self, val=0, right=None) -> None:
        self.val = val
        self.next = next
    

class TreeNode:

    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def sorted_list_to_bst(self, head: ListNode) -> TreeNode:

        def get_median(left: ListNode, right: ListNode) -> ListNode:
            fast = slow = left
            while fast != right and fast.next != right:
                fast = fast.next.next
                slow = slow.next
            return slow
        
        def build_tree(left: ListNode, right: ListNode) -> TreeNode:
            if left == right:
                return None
            
            mid = get_median(left, right)
            root = TreeNode(mid.val)
            root.left = build_tree(left, mid)
            root.right = build_tree(mid.next, right)
            return root
        
        return build_tree(head, None)
