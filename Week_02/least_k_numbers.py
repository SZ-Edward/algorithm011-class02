# !/usr/bin/env python
# encoding: utf-8
"""
  https://leetcode-cn.com/problems/zui-xiao-de-kge-shu-lcof/
"""
class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
      if len(arr) < 2 or k > len(arr):
        return
      arr.sort()
      return arr[:k]
