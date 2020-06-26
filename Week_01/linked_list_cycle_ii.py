# !/usr/bin/env python
# encoding: utf-8
"""
  https://leetcode-cn.com/problems/linked-list-cycle-ii/
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        try:
            slow = head.next
            fast = head.next.next
            while slow is not fast:
                slow = slow.next
                fast = fast.next.next
        except:
            return None
        slow = head
        while slow is not fast:
            slow = slow.next
            fast = fast.next
        return slow

