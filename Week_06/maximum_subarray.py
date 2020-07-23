# !/usr/bin/env python
# encoding: utf-8
"""
  https://leetcode-cn.com/problems/maximum-subarray/
"""
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
      for i in range(1, len(nums)):
        nums[i] += max(0, nums[i-1]) 
      return max(nums)
