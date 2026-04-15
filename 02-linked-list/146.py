# -*- coding: utf-8 -*-
class DBLinkNode:
    def __init__(self, key=0, val=0, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next


class LRUCache:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache_data = {}
        self.size = 0
        self.head = DBLinkNode()
        self.tail = DBLinkNode()
        
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def get(self, key: int) -> int:
        if key not in self.cache_data:
            return -1
        node = self.cache_data[key]
        self.move_to_head(node)
        return node.val
    
    def put(self, key: int, value: int) -> None:
        
        if key not in self.cache_data:
            node = DBLinkNode(key=key, val=value)
            self.cache_data[key] = node
            self.size += 1
            self.add_to_head(node)
            if self.size > self.capacity:
                node = self.remove_tail()
                self.cache_data.pop(node.key)
                self.size -= 1
        else:
            node = self.cache_data[key]
            node.val = value
            self.move_to_head(node)
    
    def add_to_head(self, node):
        self.head.next.prev = node
        node.next = self.head.next
        self.head.next = node
        node.prev = self.head
    
    def remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def move_to_head(self, node):
        self.remove_node(node)
        self.add_to_head(node)
    
    def remove_tail(self):
        node = self.tail.prev
        self.remove_node(node)
        return node

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)