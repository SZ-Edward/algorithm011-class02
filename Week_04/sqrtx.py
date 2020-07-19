# !/usr/bin/env python
# encoding: utf-8
"""
  https://leetcode-cn.com/problems/sqrtx/
"""
class Solution:
    def mySqrt(self, x: int) -> int:
      if x == 0:
        return x
      left, right = 1, x // 2
      while left < right:
        mid = (left + right + 1) >> 1
        square = mid * mid

        if square > x:
          right = mid - 1
        else:
          left = mid
      
      return left
