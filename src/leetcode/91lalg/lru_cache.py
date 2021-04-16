# -*- coding: utf-8 -*-

class DLinkedNode:

    def __init__(self, key=0, value=0) -> None:
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int) -> None:
        self.cache = dict()
        self.head = DLinkedNode()
        self.tail = DLinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity
        self.size = 0
    
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        self.move_to_head(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            node = DLinkedNode(key, value)
            self.cache[key] = node
            self.add_to_head(node)
            self.size += 1

            if self.size > self.capacity:
                removed = self.remove_tail()
                self.cache.pop(removed.key)
                self.size -= 1
        else:
            node = self.cache[key]
            node.value = value
            self.move_to_head(node)

    def add_to_head(self, node: DLinkedNode) -> None:
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def remove_node(self, node: DLinkedNode) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def move_to_head(self, node: DLinkedNode) -> None:
        self.remove_node(node)
        self.add_to_head(node)

    def remove_tail(self) -> DLinkedNode:
        node = self.tail.prev
        self.remove_node(node)
        return node

