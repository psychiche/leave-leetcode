# -*- coding: utf-8 -*-
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # # 1、遍历一遍，获取链表长度，最终将 k % n
        # 虚拟头
        # n - k 个节点为新头
        n = 0
        dummmy_head, old_tail, old_head = ListNode(), head, head
        dummmy_head.next = head
        while dummmy_head.next:
            dummmy_head = dummmy_head.next
            old_tail = dummmy_head
            n += 1
        if n == 0:
            return head
        k = k % n
        if k == 0:
            return head
        
        # 记录 4 个节点：旧头、旧尾，新头，新尾
        dummmy_head.next = head
        new_tail, new_head = head, head.next
        i = 1
        while head.next:
            # while head and head.next:
            # 找到旋转点
            new_head = head.next
            if i == n - k:
                # 处理尾(yes)
                old_tail.next = dummmy_head.next
                new_tail.next = None
                
                return new_head
            else:
                i += 1
                new_tail = new_head
                head = head.next




