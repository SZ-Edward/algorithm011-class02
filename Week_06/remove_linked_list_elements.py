# !/usr/bin/env python
# encoding: utf-8
"""
  https://leetcode-cn.com/problems/remove-linked-list-elements
"""
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
      guard = ListNode(0)
      guard.next = head;
      prev, curr = guard, head;
      while curr:
        if curr.val == val:
          prev.next = curr.next
        else:
          prev = curr
        curr = curr.next
      return guard.next
