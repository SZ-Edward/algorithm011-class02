# !/usr/bin/env python
# encoding: utf-8
"""
  https://leetcode-cn.com/problems/cong-wei-dao-tou-da-yin-lian-biao-lcof/
"""
class Solution(object):
    def reversePrint(self, head):
        if not head:
          return []
        res, stack = [], []
        while head:
          stack.append(head.val)
          head = head.next
        while stack:
          res.append(stack.pop())
        return res
