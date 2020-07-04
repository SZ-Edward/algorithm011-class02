# !/usr/bin/env python
# encoding: utf-8
"""
  https://leetcode-cn.com/problems/generate-parentheses/
"""
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
      def generate(p, left, right, res=[]):
        if left:         
          generate(p + '(', left - 1, right)
        if right > left: 
          generate(p + ')', left, right - 1)
        if not right:    
          res.append(p)
        return res

      return generate('', n, n)
