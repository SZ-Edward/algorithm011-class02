# !/usr/bin/env python
# encoding: utf-8
"""
  https://leetcode-cn.com/problems/longest-valid-parentheses/
"""
class Solution:
    def longestValidParentheses(self, s: str) -> int:
      max_length = 0
      stack = [-1]
      for i in range(len(s)):
        if s[i] == '(':
          stack.append(i)
        elif s[i] == ')':
          stack.pop()
          if len(stack) == 0:
            stack.append(i)
          else:
            max_length = max(max_length, i - stack[-1])
      return max_length
