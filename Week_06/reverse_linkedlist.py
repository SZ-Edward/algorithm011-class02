# !/usr/bin/env python
# encoding: utf-8
"""
  https://leetcode-cn.com/problems/fan-zhuan-lian-biao-lcof/
"""
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
      prev, curr = None, head
      while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
      return prev
