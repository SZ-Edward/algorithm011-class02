# !/usr/bin/env python
# encoding: utf-8
"""
  https://leetcode-cn.com/problems/reverse-linked-list/
"""
def reverseList(head):
    prev, curr = None, head
    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    return prev
