# !/usr/bin/env python
# encoding: utf-8
"""
  https://leetcode-cn.com/problems/subsets/
"""
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
      res = [[]]
      for num in nums:
        res += [[num] + each for each in res]
      return res
