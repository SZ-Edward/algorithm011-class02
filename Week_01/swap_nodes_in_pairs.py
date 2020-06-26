# !/usr/bin/env python
# encoding: utf-8
"""
  https://leetcode-cn.com/problems/swap-nodes-in-pairs/
"""
def swapPairs(head: ListNode) -> ListNode:
    if not head or not head.next:
        return head
    node = head.next
    head.next = swapPairs(head.next.next)
    node.next = head
    return node
