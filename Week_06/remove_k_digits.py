# !/usr/bin/env python
# encoding: utf-8
"""
  https://leetcode-cn.com/problems/remove-k-digits/
"""
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
      stack = []
      remaining = len(num) - k
      for each in num:
        while stack and k and stack[-1] > each:
          stack.pop()
          k -= 1
        stack.append(each)
      return ''.join(stack[:remaining]).lstrip('0') or '0'
