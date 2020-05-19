# -*- coding: utf-8 -*-

class ListNode:

    def __init__(self, x):
        super().__init__()
        self.val = x
        self.next = None

class Solution:

    def print_list_from_tail_to_head(self, list_node):
        if not list_node:
            return []
        return self.print_list_from_tail_to_head(list_node.next) + [list_node.val]
    

if __name__ == "__main__":
    node1 = ListNode(3)
    node2 = ListNode(2)
    node2.next = node1
    node3 = ListNode(1)
    node3.next = node2

    test_solution = Solution()
    print(test_solution.print_list_from_tail_to_head(node3))
