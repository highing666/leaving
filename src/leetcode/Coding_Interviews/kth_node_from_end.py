# -*- coding: utf-8 -*-


class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None


def get_kth_from_end(head: ListNode, k: int) -> ListNode:
    former, later = head, head
    for _ in range(k):
        former = former.next

    while former:
        former, later = former.next, later.next

    return later


if __name__ == '__main__':
    n1 = ListNode(2)
    print(get_kth_from_end(n1, 1))
