# !/usr/bin/env python
# encoding: utf-8
"""
  https://leetcode-cn.com/problems/rotate-list/
"""
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
      if not head:
        return
      last = head
      length = 1
      while last.next:
        last = last.next
        length += 1
      k = k % length
      last.next = head
      temp = head
      for _ in range(length - k - 1):
        temp = temp.next
      new_head = temp.next
      temp.next = None
      return new_head
