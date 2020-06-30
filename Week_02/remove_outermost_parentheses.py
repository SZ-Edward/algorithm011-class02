# !/usr/bin/env python
# encoding: utf-8
"""
  https://leetcode-cn.com/problems/remove-outermost-parentheses/
"""
class Solution:
    def removeOuterParentheses(self, S: str) -> str:
      stack = []
      result = ""
      for c in S:
        if c == "(":
          stack.append(c)
          if len(stack) > 1:
            result += "("
        else:
          stack.pop()
          if len(stack) > 0:
            result += ")"
      return result
