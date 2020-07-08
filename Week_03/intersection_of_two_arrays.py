# !/usr/bin/env python
# encoding: utf-8
"""
  https://leetcode-cn.com/problems/intersection-of-two-arrays
"""
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
      return list(set([each for each in nums1 if each in nums2]))
