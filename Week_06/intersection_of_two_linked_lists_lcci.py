# !/usr/bin/env python
# encoding: utf-8
"""
  https://leetcode-cn.com/problems/intersection-of-two-linked-lists-lcci
"""
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
      if not headA or not headB:
        return None
      a, b = headA, headB
      while a != b:
        a = a.next if a else headB
        b = b.next if b else headA
      return a
